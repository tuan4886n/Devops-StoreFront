import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Lấy các biến môi trường
JWT_SECRET_KEY = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Khởi tạo context để băm mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Khởi tạo OAuth2PasswordBearer để xử lý việc xác thực token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Các hàm xử lý mật khẩu ---
def verify_password(plain_password, hashed_password):
    """Xác minh mật khẩu thường với mật khẩu đã băm."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Băm mật khẩu thường."""
    return pwd_context.hash(password)

# --- Các hàm xử lý JWT ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Tạo JWT access token."""
    to_encode = data.copy()
    # Sửa lỗi: Thay đổi datetime.utcnow() thành datetime.now(timezone.utc)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """Giải mã và xác minh JWT access token."""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

# --- Hàm dependency để lấy người dùng hiện tại từ JWT ---
def get_current_user(token: str = Depends(oauth2_scheme)):
    """Lấy người dùng hiện tại từ token JWT."""
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username