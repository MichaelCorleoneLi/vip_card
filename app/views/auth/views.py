"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/5 22:30
"""
import functools
from http.client import HTTPException

from flask import request, current_app
from flask_login import login_user
from jsonschema import Draft4Validator
from werkzeug.routing import ValidationError

from app import login_manager
from app.errors import AuthError, errno
from app.models import Boss, Customer
from app.utils import boss_or_customer, UserType
from app.views.auth import auth
from app.views.auth.params import LOGIN


def validate_input(schema):
    """
    验证请求参数 JSON 格式, 将验证后的数据作为视图函数的第一个参数

    Args:
        schema 验证 data 是否符合此 schema

    Returns:
        验证成功返回 json data, 否则抛出 AuthError

    Raises:
        验证失败抛出 AuthError(errno.INVALID_PARAMETERS)
    """

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if request.method == 'GET':
                data = request.args
            elif request.is_json:
                try:
                    data = request.get_json(force=True)
                except HTTPException:
                    raise AuthError(errno.INVALID_PARAMETERS)
            else:
                data = request.form

            try:
                if current_app.debug:
                    Draft4Validator.check_schema(schema)

                Draft4Validator(schema).validate(data)
            except ValidationError as e:
                desc = str(e) if current_app.debug else None
                raise AuthError(errno.INVALID_PARAMETERS, description=desc)

            return func(data, *args, **kwargs)

        return inner

    return decorator


@login_manager.user_loader
def load_user(user_id):
    user_type = boss_or_customer(user_id)
    if user_type == UserType.BOSS:
        user = Boss.query.get(user_id)
    else:
        user = Customer.query.get(user_id)
    return user


@auth.route('/login', methods=['POST'])
@validate_input(LOGIN)
def login(data):
    # 微信验证登陆
    # 获取用户
    user = Boss.query.get(1)
    login_user(user)
    return {'success': True}