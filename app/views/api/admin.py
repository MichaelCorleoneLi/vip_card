# Created by LiHuaiyuan at 2018/9/24 11:41
from flask_login import current_user

from app import db
from app.utils import admin_required
from app.models import Shop
from . import api


@api.route('/admin/shop_card_list/<int:shop_id>')
@admin_required
def shop_card_list(shop_id):
    shop = db.session.query(Shop).get(shop_id)
    return {
        'success': True,
        'data': {
            'shop_card_list': [card.to_dict() for card in shop.cards]
        }
    }


@api.route('/admin/shop_list')
@admin_required
def admin_shop_list():
    return {
        'success': True,
        'data': {
            'shop_list': [shop.to_dict() for shop in current_user.shops]
        }
    }


@api.route('/admin/shop_detail/<int:shop_id>')
@admin_required
def shop_detail(shop_id):
    shop = db.session.query(Shop).get(shop_id)
    return {
        'success': True,
        'data': {
            'shop': shop.to_dict()
        }
    }