"""
# @File    : config.py

# @Author  : lhy
# @Time    : 2018/6/26 22:49
"""

class Config():
    def init_app(self, app):
        app.config.from_object(self)


class DevConfig(Config):
    pass


class TestConfig():
    pass


class ProductionConfig(Config):
    pass


config = {
    'dev': DevConfig(),
    'test': TestConfig,
    'production': ProductionConfig
}