# Nhật ký Triển khai

## [31/08/2025] Triển khai 1: Dịch vụ Xác thực (auth-service)

Mô tả: Triển khai auth-service và database (db) bằng Docker Compose.

Kết quả:

Container db và auth-service hoạt động.

Có thể đăng ký người dùng mới và lấy JWT token thành công.

Route được bảo vệ đã hoạt động như mong đợi.

## [02/09/2025] Triển khai 2: Triển khai tự động bằng Jenkins (auth-service)

Mô tả: Triển khai auth-service tự động thông qua pipeline CI/CD của Jenkins.

Kết quả:

Pipeline đã build, test và deploy container auth-service thành công.

Container mới được khởi động và hoạt động đúng với các thay đổi.
