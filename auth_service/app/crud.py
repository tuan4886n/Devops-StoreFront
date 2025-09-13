from sqlalchemy.orm import Session
from . import models, schemas
from .auth_utils import get_password_hash # Import hàm băm mật khẩu

# Hàm để lấy người dùng từ database bằng tên đăng nhập
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Hàm để tạo người dùng mới và lưu vào database
def create_user(db: Session, user: schemas.UserCreate):
    # Sử dụng hàm băm mật khẩu để lưu mật khẩu đã mã hóa
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
