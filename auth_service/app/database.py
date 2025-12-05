import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Xây dựng DATABASE_URL để kết nối
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    # Bắt buộc phải có chuỗi kết nối. Báo lỗi ngay nếu không tìm thấy.
    raise ValueError("DATABASE_URL environment variable is not set.")

# Tạo engine kết nối cơ sở dữ liệu
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency để lấy Session của database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()