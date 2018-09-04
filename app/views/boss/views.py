"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/4 21:56
"""

from app.views.boss import boss


@boss.route('/self')
def boss_info():
    pass