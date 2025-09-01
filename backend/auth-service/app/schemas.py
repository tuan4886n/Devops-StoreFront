from pydantic import BaseModel
from typing import Optional

# Schema để nhận dữ liệu khi đăng ký người dùng
class UserCreate(BaseModel):
    username: str
    password: str

# Schema để trả về thông tin người dùng sau khi đăng ký thành công
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

# Schema để nhận dữ liệu khi người dùng đăng nhập
class UserLogin(BaseModel):
    username: str
    password: str

# Schema để trả về token JWT
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Schema cho dữ liệu bên trong JWT
class TokenData(BaseModel):
    username: Optional[str] = None
