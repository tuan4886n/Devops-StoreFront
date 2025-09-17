# Nhật ký Lỗi và Khắc phục

## [31/08/2025] Lỗi: Lỗi ban đầu khi bắt đầu dự án

Mô tả: Lỗi kết nối database trong file database.py.

Nguyên nhân: Lỗi cú pháp trong file cấu hình.

Giải pháp: Cấu hình lại file database.py để đảm bảo kết nối đến PostgreSQL.

Kết quả: Đã khắc phục thành công.

## [02/09/2025] Lỗi: Lỗi trong pipeline Jenkins

Mô tả: Lỗi sudo: not found, sau đó là docker: Permission denied, và cuối cùng là no such file or directory khi build Docker image.

Nguyên nhân: \* Thiếu các công cụ sudo và docker trong container Jenkins.

Lỗi quyền truy cập vào Docker daemon.

Đường dẫn Dockerfile trong Jenkinsfile không chính xác.

Giải pháp:

Tạo Dockerfile tùy chỉnh cho Jenkins để cài đặt sudo và docker.

Sửa lại lệnh build trong Jenkinsfile để trỏ đúng đến đường dẫn của Dockerfile.

Kết quả: Đã khắc phục thành công, pipeline đã chạy mà không có lỗi.

## [16/09/2025] Lỗi: Jenkins container thoát và lỗi plugin

Mô tả: Jenkins không khởi động được do các plugin không tương thích và có vẻ như một số plugin đã bị hỏng.

Nguyên nhân: Phiên bản Jenkins đang sử dụng (2.525-jdk17) không tương thích hoàn toàn với các plugin mới nhất.

Giải pháp: Cập nhật Dockerfile để sử dụng phiên bản Jenkins LTS ổn định nhất (jenkins/jenkins:lts-slim-jdk17) và cài đặt trực tiếp các plugin cần thiết bằng lệnh jenkins-plugin-cli trong Dockerfile.

Kết quả: Sau khi cập nhật Dockerfile và cài đặt lại plugin, Jenkins đã khởi động thành công và hoạt động ổn định.
