FROM node as build-deps
WORKDIR /app
COPY ./frontend/package.json ./
RUN yarn install
COPY ./frontend ./
RUN yarn build

FROM python:3.8-alpine3.10

LABEL Author="Anh DH"
LABEL Version="1.0"
WORKDIR /app
COPY --from=build-deps /app/build /app/build
COPY --from=build-deps /app/build/index.html /app/hyip/templates/index.html
COPY ./backend/requirements.txt ./

RUN apk --update add --virtual build-dependencies bash libffi-dev openssl-dev build-base \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del build-dependencies

RUN apk --update add bash

ADD ./backend /app

RUN chmod 755 wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh ${PROD_MYSQL_HOST}:${PROD_MYSQL_PORT} -t 0 -- gunicorn -c etc/gunicorn.conf.py  --workers 8  wsgi:app  --log-level info"]
