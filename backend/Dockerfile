FROM python:3.8-alpine3.10

LABEL Author="Anh DH"
LABEL Version="1.0"
WORKDIR /app

COPY requirements.txt ./

RUN apk --update add bash

RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev build-base \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del build-dependencies

ADD . /app

RUN chmod 755 wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh ${MYSQL_HOST}:${MYSQL_FORWARD_PORT} -t 0 -- flask db upgrade heads && flask run --host=0.0.0.0 --port=5000"]