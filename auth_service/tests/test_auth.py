import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base
from app.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
import sys
import os

# Thêm thư mục gốc của dự án vào đường dẫn tìm kiếm của Python
# Điều này cho phép Pytest tìm thấy các mô-đun trong thư mục backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Khởi tạo TestClient để thực hiện các yêu cầu giả lập tới ứng dụng FastAPI
client = TestClient(app)

# Fixture để tạo và thả bảng cho môi trường thử nghiệm sạch sẽ
@pytest.fixture(name="db", scope="function")
def database_fixture():
    """
    Creates test database tables before each test and
    deletes them after the test is finished.
    """
    db = SessionLocal()
    # Bước quan trọng: Xóa tất cả các bảng để đảm bảo trạng thái sạch
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Ghi đè dependency get_db của FastAPI để sử dụng session database test
        app.dependency_overrides[get_db] = lambda: db
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        # Xóa ghi đè để không ảnh hưởng đến các bài kiểm tra khác
        del app.dependency_overrides[get_db]

def test_register_user_success(db: Session):
    """Test successful user registration."""
    response = client.post("/register", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["username"] == "testuser"

def test_register_user_already_exists(db: Session):
    """Test registration failure when username already exists."""
    # Đăng ký lần đầu
    client.post("/register", json={"username": "existinguser", "password": "testpassword"})
    
    # Đăng ký lần thứ hai với cùng tên người dùng
    response = client.post("/register", json={"username": "existinguser", "password": "testpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

def test_login_for_access_token_success(db: Session):
    """Test successful login and token retrieval."""
    # Đăng ký người dùng để đăng nhập
    client.post("/register", json={"username": "loginuser", "password": "loginpassword"})
    
    # Đăng ký
    form_data = {"username": "loginuser", "password": "loginpassword"}
    response = client.post("/token", data=form_data)
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_for_access_token_failure(db: Session):
    """Test failed login with incorrect credentials."""
    form_data = {"username": "wronguser", "password": "wrongpassword"}
    response = client.post("/token", data=form_data)
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

def test_protected_route_with_valid_token(db: Session):
    """Test accessing a protected route with a valid token."""
    # Đăng ký và đăng nhập để nhận mã thông báo
    client.post("/register", json={"username": "protecteduser", "password": "protectedpassword"})
    token_response = client.post("/token", data={"username": "protecteduser", "password": "protectedpassword"})
    token = token_response.json()["access_token"]
    
    # Gửi yêu cầu đến tuyến đường được bảo vệ
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/protected", headers=headers)
    
    assert response.status_code == 200
    assert "Welcome protecteduser" in response.json()["message"]

def test_protected_route_without_token():
    """Test accessing a protected route without a token."""
    response = client.get("/protected")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"