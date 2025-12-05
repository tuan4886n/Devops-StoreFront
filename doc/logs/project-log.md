# Nhật ký Dự án Cửa Hàng Trực tuyến DevOps

## [31/08/2025] Giai đoạn 1: Xây dựng Microservice Xác thực (Auth-Service)

Mục tiêu: Tạo dịch vụ quản lý người dùng, đăng ký, đăng nhập và bảo vệ các route bằng JWT.

Tiến độ: Hoàn thành 100%. Dịch vụ đã hoạt động ổn định và đã được kiểm tra thành công.

Kết quả: Đã có một microservice xác thực hoạt động, là nền tảng cho các dịch vụ khác.

## [01/09/2025] Chuẩn bị cho CI/CD với Jenkins

Quyết định: Thống nhất lộ trình mới: tích hợp CI/CD cho từng microservice sau khi hoàn thành.

Công cụ: Lựa chọn Jenkins thay vì GitHub Actions để đa dạng hóa công nghệ.

Kế hoạch: Bắt đầu với việc thiết lập môi trường Git và Jenkins.

## [02/09/2025] Giai đoạn 2: Hoàn thành CI/CD cho Auth-Service

Mục tiêu: Khắc phục các lỗi trong pipeline Jenkins để hoàn thành quy trình CI/CD tự động cho auth-service.

Tiến độ: Đã khắc phục thành công các lỗi sudo: not found, Permission denied và no such file or directory.

Kết quả: Pipeline CI/CD cho auth-service đã hoạt động hoàn toàn tự động, từ build, test cho đến deploy.

## [28/11/2025] Trở lại dự án sau 3 tháng

Lý do: Tạm dừng vì đi làm thêm.  
Hoạt động: Quay lại cải tiến auth_service, sửa Dockerfile, tối ưu Jenkinsfile, chạy lại test.  
Kết quả: Test pass, pipeline ổn định.  
Kế hoạch: Chuẩn bị triển khai lên K3s.
