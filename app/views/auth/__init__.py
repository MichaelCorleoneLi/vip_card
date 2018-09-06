"""
# @File    : __init__.py.py

# @Author  : lhy
# @Time    : 2018/9/4 21:53
"""

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from app.views.auth import views