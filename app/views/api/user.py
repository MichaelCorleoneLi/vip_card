"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/5 22:23
"""
from flask_login import current_user

from app import db
from app.models import Card
from app.utils import user_required
from . import  api


@api.route('/record_list')
@user_required
def order_list():
    return {
        'success': True,
        'data': [order.to_dict() for order in current_user.orders]
    }


@api.route('/card_list')
@user_required
def card_list():
    return {
        'success': True,
        'data': [card.to_dict() for card in current_user.cards]
    }


@api.route('/card_detail/<int:card_id>')
@user_required
def card_detail(card_id):
    card = db.session.query(Card).get(card_id)
    return {
        'success': True,
        'data': {
            'card': card.to_dict()
        }
    }