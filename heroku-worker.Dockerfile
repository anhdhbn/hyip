FROM python:3.8-alpine3.10

LABEL Author="Anh DH"
LABEL Version="1.0"

WORKDIR /app

RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

RUN apk update
RUN apk add libxslt-dev g++ gcc bash libressl-dev musl-dev libffi-dev nodejs npm nodejs-npm ca-certificates
COPY ./worker/requirements.txt ./

RUN pip install -r requirements.txt
ADD ./worker /app