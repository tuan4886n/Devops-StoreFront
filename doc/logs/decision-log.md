# Nhật ký Quyết định

## [2025-09-01] Quyết định 1: Lộ trình phát triển dự án

Mô tả: Thay đổi lộ trình phát triển từ "Hoàn thành tất cả các microservice và front-end, sau đó mới tích hợp DevOps" sang một luồng linh hoạt hơn.

Lý do: Kế hoạch ban đầu không phản ánh đúng quy trình làm việc thực tế trong môi trường DevOps chuyên nghiệp. Việc tích hợp CI/CD sớm cho từng microservice giúp đảm bảo tính độc lập, khả năng mở rộng và dễ dàng gỡ lỗi.

Quyết định:

Tiếp tục phát triển từng microservice một.

Sau khi hoàn thành mỗi microservice, sẽ ngay lập tức viết và tích hợp CI/CD pipeline cho nó.

## [2025-09-01] Quyết định 2: Công cụ CI/CD

Mô tả: Lựa chọn công cụ CI/CD để đa dạng hóa kinh nghiệm.

Lý do: Người dùng muốn sử dụng Jenkins thay vì GitHub Actions để làm phong phú thêm kiến thức và kinh nghiệm, điều này rất có lợi cho CV.

Quyết định: Sử dụng Jenkins để xây dựng CI/CD pipeline cho các microservice backend.

## [2025-09-01] Quyết định 3: Triển khai Front-end

Mô tả: Lựa chọn nền tảng triển khai cho front-end.

Lý do: Để tập trung vào kiến thức DevOps cốt lõi (CI/CD, Docker, Kubernetes) cho phần backend, chúng ta sẽ tận dụng các dịch vụ tự động hóa có sẵn cho front-end.

Quyết định: Sử dụng Vercel hoặc Netlify để triển khai front-end, tận dụng tính năng CI/CD tích hợp sẵn của họ.

## [2025-09-01] Quyết định 4: Quy trình làm việc Git

Mô tả: Thống nhất quy trình làm việc với Git cho dự án cá nhân.

Lý do: Với quy mô dự án và số người tham gia, việc sử dụng các mô hình phức tạp (như Git Flow) là không cần thiết.

Quyết định: Tiếp tục sử dụng branch main cho xuyên suốt dự án để đơn giản hóa quy trình và tập trung vào các công nghệ DevOps.
