FROM python:3.8-alpine3.10

LABEL Author="Anh DH"
LABEL Version="1.0"

WORKDIR /app

# update apk repo
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver libxslt-dev g++ gcc bash libressl-dev musl-dev libffi-dev

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . /app

RUN chmod 755 wait-for-it.sh
