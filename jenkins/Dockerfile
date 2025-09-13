FROM jenkins/jenkins:lts-jdk17

USER root

# Cài đặt sudo và các công cụ cần thiết
RUN apt-get update && \
    apt-get install -y --no-install-recommends sudo docker.io curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Thêm người dùng jenkins vào nhóm docker để có quyền truy cập
RUN usermod -aG docker jenkins

# Cài đặt các plugin bằng CLI chính thức.
# Bao gồm cả các plugin bị lỗi và các plugin thường dùng.
RUN jenkins-plugin-cli --plugins \
    docker-workflow \
    authentication-tokens \
    docker-commons \
    matrix-auth \
    workflow-aggregator \
    pipeline-github-lib \
    credentials \
    plain-credentials \
    ssh-credentials

# Trở lại user jenkins mặc định
USER jenkins