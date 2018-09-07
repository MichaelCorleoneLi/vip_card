"""
# @File    : __init__.py.py

# @Author  : lhy
# @Time    : 2018/9/4 21:54
"""

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import boss, customer, restaurant