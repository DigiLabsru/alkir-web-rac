FROM python:3.12.9-slim-bookworm 

ARG PROJECT_USER
ARG PROJECT_FOLDER
WORKDIR /${PROJECT_FOLDER}

RUN set -ex \
&& apt-get update -yqq \
&& ACCEPT_EULA=Y apt-get install --no-install-recommends gnupg wget curl -yqq \
&& useradd --create-home --shell /bin/bash --uid 1000 ${PROJECT_USER} \
&& chown -R ${PROJECT_USER}:${PROJECT_USER} /${PROJECT_FOLDER}

# Добавляем GPG-ключ Temurin
RUN set -ex && \
    wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public > /tmp/key.asc && \
    gpg --dearmor -o /etc/apt/trusted.gpg.d/adoptium.gpg /tmp/key.asc && \
    rm /tmp/key.asc 

# Добавляем репозиторий Temurin для Debian Bookworm
RUN echo "deb https://packages.adoptium.net/artifactory/deb bookworm main" | tee /etc/apt/sources.list.d/adoptium.list

# Устанавливаем OpenJDK 21 из Temurin
RUN apt-get update && \
    apt-get install -y --no-install-recommends temurin-21-jdk

# Опционально: задаем переменные окружения (путь может отличаться)
ENV PATH="/home/${PROJECT_USER}/.local/bin:/usr/lib/jvm/temurin-21-jdk-amd64/bin:${PATH}"

USER ${PROJECT_USER}

COPY --chown=${PROJECT_USER}:${PROJECT_USER} app /${PROJECT_FOLDER}/app

RUN pip install --user --no-cache -r /${PROJECT_FOLDER}/app/requirements.txt 

EXPOSE 8080

#HEALTHCHECK --interval=600s --timeout=5s --start-period=60s --retries=3 \
#  CMD curl -f http://localhost:8000/v1/heals_check || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
