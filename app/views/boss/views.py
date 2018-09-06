"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/4 21:56
"""
from app.utils import boss_required
from app.views.boss import boss


@boss.route('/restaurant_list')
@boss_required
def restaurant_list():
    pass