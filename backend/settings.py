import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


class BaseConfig():
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False

    ROOT_DIR = os.path.abspath(os.path.join(
        os.path.dirname(__file__)
    ))

    LOGGING_CONFIG_FILE = os.path.join(ROOT_DIR, 'etc', 'logging.ini')

    FLASK_APP_SECRET_KEY = os.getenv('SECRET_KEY', 'MY_SECRET_KEY')

    MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_PORT = os.environ['MYSQL_PORT']

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
    REDIS_PORT = os.environ['REDIS_PORT']


    REDIS_URL = 'redis://:{0}@{1}:{2}/0'.format(
        REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
    )

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    

class DEVConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://db_user:db_password@db-postgres:5432/flask-deploy'
    # CELERY_BROKER = 'redis://h:12345678@localhost:6379'
    # CELERY_RESULT_BACKEND = 'redis://h:12345678@localhost:6379'

    

class PRODConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = True
    dsn = os.environ.get('SENTRY_DSN')
    sentry_sdk.init(
        dsn=dsn,
        integrations=[FlaskIntegration()],
        environment=os.getenv('APP_ENV'),
        in_app_exclude=['app.extensions.exceptions'],
    )
    # SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
    # CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
    # CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'

# class TempConfig(BaseConfig):
#     FLASK_ENV = 'production'
#     SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
#     CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
#     CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'

class TESTConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    # make celery execute tasks synchronously in the same process
    CELERY_ALWAYS_EAGER = True