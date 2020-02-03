FROM python:3.8-alpine3.10

LABEL Author="Anh DH"
LABEL Version="1.0"
WORKDIR /app

COPY requirements.txt ./

RUN apk --update add --virtual build-dependencies bash libffi-dev openssl-dev build-base \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del build-dependencies

RUN apk --update add bash

ADD . /app

RUN flask db init

RUN chmod 755 wait-for-it.sh

# CMD ["sh", "-c", "./wait-for-it.sh ${PROD_MYSQL_HOST}:${PROD_MYSQL_PORT} -t 0 -- flask db upgrade heads && gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info"]
CMD ["sh", "-c", "./wait-for-it.sh ${PROD_MYSQL_HOST}:${PROD_MYSQL_PORT} -t 0 -- flask db upgrade heads && flask run -h 0.0.0.0 -p 5000"]