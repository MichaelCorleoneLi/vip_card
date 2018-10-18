# Created by LiHuaiyuan at 2018/9/24 11:41
from app import db
from app.models import Boss, Restaurant
from . import api


@api.route('/boss_all')
def boss_all():
    return {'boss_all': [boss.to_dict() for boss in db.session.query(Boss).all()]}


@api.route('/restaurant_all')
def restaurant_all():
    return {'restaurant_all': [restaurant.to_dict() for restaurant in db.session.query(Restaurant).all()]}