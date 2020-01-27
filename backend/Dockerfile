# FROM python:3.6-alpine
FROM alpine:latest

LABEL Author="Anh DH"
LABEL Version="1.0"

COPY requirements.txt ./

RUN apk --update add python3 py3-pip openssl ca-certificates py-openssl wget bash mariadb-dev
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python3-dev py3-pip build-base \
  && pip3 install --upgrade pip \
  && pip3 install --no-cache-dir -r requirements.txt \
  && apk del build-dependencies

ADD . .

RUN chmod 755 wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh ${MYSQL_HOST}:${MYSQL_FORWARD_PORT} -t 0 -- flask db upgrade heads && flask run --host=0.0.0.0 --port=5000"]