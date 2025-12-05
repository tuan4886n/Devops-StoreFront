import os
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, crud, schemas
from .database import SessionLocal, engine
from .auth_utils import verify_password, create_access_token, get_current_user

# Tạo tất cả các bảng trong database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Authentication Service",
    description="Dịch vụ quản lý người dùng, đăng ký, đăng nhập và xác thực (Microservice)",
)

# Dependency để lấy Session của database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint để kiểm tra sức khỏe của dịch vụ
@app.get("/healthz")
def read_health():
    return {"status": "ok"}

# Endpoint để đăng ký người dùng
@app.post("/register", response_model=schemas.UserResponse)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    return crud.create_user(db=db, user=user)

# Endpoint để đăng nhập và lấy JWT token
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint được bảo vệ, chỉ có thể truy cập bằng JWT token hợp lệ
@app.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Welcome {current_user}, you have access to this protected route."}
