"""
# @File    : utils.py

# @Author  : lhy
# @Time    : 2018/8/10 22:54
"""
import datetime
import decimal
import functools
from json import JSONEncoder

from flask_babel import LazyString
from flask_login import current_user, login_required

from app.errors import errno, AuthError


class UserType:
    ADMIN = 0
    USER = 1


def admin_or_user(id):
    if isinstance(id, str):
        id = int(id)

    if 0 < id < 5000:
        return UserType.ADMIN
    else:
        return UserType.USER


def admin_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if admin_or_user(current_user.id) != UserType.ADMIN:
            raise AuthError(errno.CUSTOMER_IS_NOT_ALLOWED)

        return func(*args, **kwargs)

    return login_required(decorator)


def user_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if admin_or_user(current_user.id) != UserType.USER:
            raise AuthError(errno.BOSS_IS_NOT_ALLOWED)

        return func(*args, **kwargs)

    return login_required(decorator)


class EnhancedJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, LazyString):
            return str(o)
        elif isinstance(o, decimal.Decimal):
            return int(o)
        try:
            it = iter(o)
        except TypeError:
            pass
        else:
            return list(it)

        return super().default(o)