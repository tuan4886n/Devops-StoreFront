FROM jenkins/jenkins:2.525-jdk17

USER root

# Cài đặt sudo và các công cụ cần thiết
RUN apt-get update && \
    apt-get install -y sudo docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Thêm người dùng jenkins vào nhóm docker để có quyền truy cập
RUN usermod -aG docker jenkins

# Trở lại user jenkins mặc định
USER jenkins