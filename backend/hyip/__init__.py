# coding=utf-8
import logging

import flask
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from hyip.extensions.exceptions import NotFoundException, \
    UnAuthorizedException, BadRequestException, ForbiddenException
from hyip.extensions.custom_exception import  UserExistsException, DomainExistsException
from hyip.extensions.sentry import before_send

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def create_app():
    import config
    import logging.config
    import os
    from flask_jwt_extended import JWTManager
    
    from . import api, models, services

    def load_app_config(app):
        """
        Load app's configurations
        :param flask.Flask app:
        :return:
        """
        app.config.from_object(config)
        app.config.from_pyfile('config.py', silent=True)

    app = flask.Flask(
        __name__,
        instance_relative_config=True,
        instance_path=os.path.join(config.ROOT_DIR, 'instance'),
        static_url_path='',
        static_folder=os.path.join(config.ROOT_DIR, 'build'),
    )
    load_app_config(app)

    # Register new flask project here and get new dsn: https://sentry.io

    

    app.config['SENTRY_CONFIG'] = {
        'ignore_exceptions':    [NotFoundException, UnAuthorizedException,
                              BadRequestException, ForbiddenException, 
                              UserExistsException, DomainExistsException],
        'level': logging.ERROR,
    }

    if app.config["APP_ENV"] == "PROD":
        dsn = app.config['SENTRY_DSN']
        sentry_sdk.init(
            dsn=dsn,
            integrations=[FlaskIntegration()],
            environment=os.getenv('APP_ENV'),
            in_app_exclude=['app.extensions.exceptions'],
            before_send=before_send
        )
    
    if os.path.isdir("build"):
        @app.route('/')
        def index():
            return flask.render_template("index.html")

        @app.route('/<path:path>')
        def send_file(path):
            return flask.send_from_directory('', path)
            
    if os.getenv("SQLALCHEMY_POOL_RECYCLE"):
        try:
            timeout = int(os.getenv("SQLALCHEMY_POOL_RECYCLE"))
            app.config['SQLALCHEMY_POOL_RECYCLE'] = timeout
        except:
            pass
    # setup jwt extended
    # app.config.setdefault('RESTPLUS_MASK_HEADER', 'X-Fields')
    # app.config.setdefault('RESTPLUS_MASK_SWAGGER', True)
    # app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY", "MY_SECRET_KEY")
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    # How long an access token should live before it expires. Set by minutes (int)
    # app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('TOKEN_UPTIME', 24)) * 60
    # app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'

    # should not, but i will use it in this app.
    # app.config['JWT_COOKIE_CSRF_PROTECT'] = False

    jwt = JWTManager(app)

    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'

    # setup logging
    logging.config.fileConfig(app.config['LOGGING_CONFIG_FILE'], disable_existing_loggers=False)

    app.secret_key = config.FLASK_APP_SECRET_KEY
    models.init_app(app)
    api.init_app(app)
    services.init_app(app)
    CORS(app)
    return app


app = create_app()