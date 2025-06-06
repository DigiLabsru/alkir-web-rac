FROM python:3.12.9-bookworm as builder

COPY app/requirements.txt .

RUN set -ex \
&& apt-get update -yqq \
&& ACCEPT_EULA=Y apt-get install --no-install-recommends -yqq git net-tools iputils-ping telnet mc \
&& pip3 install -r requirements.txt


# Добавляем GPG-ключ Temurin
RUN wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public > /tmp/key.asc && \
    gpg --dearmor -o /etc/apt/trusted.gpg.d/adoptium.gpg /tmp/key.asc && \
    rm /tmp/key.asc


# Добавляем репозиторий Temurin для Debian Bookworm
RUN echo "deb https://packages.adoptium.net/artifactory/deb bookworm main" | tee /etc/apt/sources.list.d/adoptium.list

# Устанавливаем OpenJDK 21 из Temurin
RUN apt-get update && \
    apt-get install -y --no-install-recommends temurin-21-jdk

# Опционально: задаем переменные окружения (путь может отличаться)
ENV JAVA_HOME=/usr/lib/jvm/temurin-21-jdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"
