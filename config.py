"""
# @File    : config.py

# @Author  : lhy
# @Time    : 2018/6/26 22:49
"""

class Config():
    pass


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