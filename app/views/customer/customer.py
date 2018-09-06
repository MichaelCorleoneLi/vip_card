"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/5 22:23
"""
from flask_login import current_user

from app.utils import customer_required
from app.views.customer import  customer


@customer.route('/order_list')
@customer_required
def order_list():
    return {'order_list': [order.to_dict() for order in current_user.orders]}