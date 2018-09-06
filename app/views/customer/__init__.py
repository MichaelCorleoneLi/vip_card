"""
# @File    : __init__.py.py

# @Author  : lhy
# @Time    : 2018/9/4 21:54
"""

from flask import Blueprint

customer = Blueprint('customer', __name__, url_prefix='/customer')

from app.views.customer import customer