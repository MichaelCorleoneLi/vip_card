"""
# @File    : views.py

# @Author  : lhy
# @Time    : 2018/9/5 22:23
"""
from flask_login import current_user

from app import db
from app.utils import user_required
from app.models import Card, Shop
from . import api


@api.route('/user/record_list')
@user_required
def order_list():
    return {
        'success': True,
        'data': [order.to_dict() for order in current_user.orders]
    }


@api.route('/user/card_list')
@user_required
def card_list():
    return {
        'success': True,
        'data': [card.to_dict() for card in current_user.cards]
    }


@api.route('/user/card_detail/<int:card_id>')
@user_required
def card_detail(card_id):
    card = db.session.query(Card).get(card_id)
    return {
        'success': True,
        'data': {
            'card': card.to_dict() if card else None
        }
    }


@api.route('/user/shop_detail/<int:shop_id>')
@user_required
def user_shop_detail(shop_id):
    shop = db.session.query(Shop).get(shop_id)
    return {
        'success': True,
        'data': {
            'shop': shop.to_dict() if shop else None
        }
    }