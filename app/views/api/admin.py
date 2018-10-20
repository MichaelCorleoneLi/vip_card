# Created by LiHuaiyuan at 2018/9/24 11:41
from flask_login import current_user

from app import db
from app.models import Shop
from . import api


@api.route('/shop_card_list/<int:shop_id>')
def shop_card_list(shop_id):
    shop = db.session.query(Shop).get(shop_id)
    return {'shop_card_list': [card.to_dict() for card in shop.cards]}


@api.route('/shop_list')
def shop_list():
    return {'shop_list': [shop.to_dict() for shop in current_user.shops]}


@api.route('/shop_detail/<int:shop_id>')
def shop_detail(shop_id):
    shop = db.session.query(Shop).get(shop_id)
    return shop.to_dict()