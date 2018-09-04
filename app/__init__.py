"""
# @File    : __init__.py

# @Author  : lhy
# @Time    : 2018/6/26 12:46
"""
import logging

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry
from werkzeug.contrib.fixers import ProxyFix

from app.hashids import Hashids
from config import config

log = logging.getLogger(__name__)

db = SQLAlchemy(session_options={'expire_on_commit': False})
sentry = Sentry()
login_manager = LoginManager()
hashids = Hashids(min_length=5)


def init_views(app):
    from app.views.boss import boss

    app.register_blueprint(boss)

def init_extensions(app):
    login_manager.init_app(app)
    db.init_app(app)

    db.app = app
    app.wsgi_app = ProxyFix(app.wsgi_app)


class MyFlask(Flask):
    pass


def create_app(config_name):
    app = MyFlask(__name__, instance_relative_config=True)

    config[config_name].init_app(app)
    init_extensions(app)
    init_views(app)

    log.info('Initalized app')
    return app