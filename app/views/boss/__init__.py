"""
# @File    : __init__.py.py

# @Author  : lhy
# @Time    : 2018/9/4 21:54
"""

from flask import Blueprint

boss = Blueprint('boss', __name__, url_prefix='/boss')

from app.views.boss import views