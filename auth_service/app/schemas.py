from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    """Schema để nhận dữ liệu khi đăng ký người dùng."""
    username: str
    password: str

class UserResponse(BaseModel):
    """Schema để trả về thông tin người dùng sau khi đăng ký thành công."""
    # model_config cho phép Pydantic đọc dữ liệu từ một đối tượng ORM
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    username: str

class UserLogin(BaseModel):
    """Schema để nhận dữ liệu khi người dùng đăng nhập."""
    username: str
    password: str

class Token(BaseModel):
    """Schema để trả về token JWT sau khi xác thực thành công."""
    access_token: str
    # token_type mặc định là "bearer"
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Schema cho dữ liệu bên trong JWT (Payload)."""
    # Username được dùng để xác định người dùng hiện tại
    username: Optional[str] = None