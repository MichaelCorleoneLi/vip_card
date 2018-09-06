"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/5 22:23
"""

from app.views.customer import  customer


@customer.route('/order_list')
def order_list():
    pass