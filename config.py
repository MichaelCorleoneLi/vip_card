"""
# @File    : config.py

# @Author  : lhy
# @Time    : 2018/6/26 22:49
"""
import re


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = None

    @property
    def SQLALCHEMY_BINDS(self):
        bind_re = re.compile(r'SQLALCHEMY_(\w+)_DATABASE_URI')
        binds = {}
        for key in dir(self):
            match = bind_re.search(key)
            if match:
                binds[match.group(1).lower()] = getattr(self, key)

        if binds:
            return binds
        else:
            return None

    def init_app(self, app):
        app.config.from_object(self)


class DevConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@127.0.0.1/order_food'


class TestConfig():
    pass


class ProductionConfig(Config):
    pass


config = {
    'dev': DevConfig(),
    'test': TestConfig,
    'production': ProductionConfig
}