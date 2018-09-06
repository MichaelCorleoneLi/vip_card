"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/4 21:56
"""
from flask_login import current_user

from app.utils import boss_required
from app.views.boss import boss


@boss.route('/restaurant_list')
@boss_required
def restaurant_list():
    return {'restaurant_list': [restaurant.to_dict() for restaurant in current_user.restaurants]}