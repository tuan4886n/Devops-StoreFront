# Nhật ký Lỗi và Khắc phục

## [31/08/2025] Lỗi 1: Lỗi ban đầu khi bắt đầu dự án

Mô tả: Lỗi kết nối database trong file database.py.

Nguyên nhân: Lỗi cú pháp trong file cấu hình.

Giải pháp: Cấu hình lại file database.py để đảm bảo kết nối đến PostgreSQL.

Kết quả: Đã khắc phục thành công.

## [02/09/2025] Lỗi 2: Lỗi trong pipeline Jenkins

Mô tả: Lỗi sudo: not found, sau đó là docker: Permission denied, và cuối cùng là no such file or directory khi build Docker image.

Nguyên nhân: \* Thiếu các công cụ sudo và docker trong container Jenkins.

Lỗi quyền truy cập vào Docker daemon.

Đường dẫn Dockerfile trong Jenkinsfile không chính xác.

Giải pháp:

Tạo Dockerfile tùy chỉnh cho Jenkins để cài đặt sudo và docker.

Sửa lại lệnh build trong Jenkinsfile để trỏ đúng đến đường dẫn của Dockerfile.

Kết quả: Đã khắc phục thành công, pipeline đã chạy mà không có lỗi.
