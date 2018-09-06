"""
# @File    : models.py

# @Author  : lhy
# @Time    : 2018/8/10 23:00
"""
import datetime

from flask_login import UserMixin
from sqlalchemy.dialects.mysql import INTEGER

from app import db, hashids


def text(flag):
    return db.text(str(flag))


class UNSIGNED_INT(INTEGER):
    def __init__(self, display_width=None, **kwargs):
        kwargs.pop('unsigned', None)
        super().__init__(display_width, unsigned=True, **kwargs)

    def __repr__(self):
        return INTEGER.__repr__(self)


class ToDictMixin:
    auto_load_attrs = ()

    def to_dict(self):
        ret = {}
        for attr in self.auto_load_attrs:
            ret[attr] = getattr(self, attr)

        # 对id做混淆
        if 'id' in ret and isinstance(ret['id'], int):
            ret['id'] = hashids.encode(ret['id'])

        return ret


# region Models
class Boss(db.Model, UserMixin, ToDictMixin):
    """老板"""
    __tablename__ = 'Boss'
    auto_load_attrs = ('id', 'name')

    id = db.Column(UNSIGNED_INT, primary_key=True, autoincrement=True)
    # 微信昵称
    nick_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(40), nullable=True)
    province = db.Column(db.String(40), nullable=True)
    country = db.Column(db.String(40), nullable=True)
    avatarUrl = db.Column(db.String(200), nullable=True)
    cashbox = db.Column(db.Numeric(8,2), default=0.0)
    # 银行卡
    band_card_number = db.Column(db.String(32), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    restaurants = db.relationship('Restaurant', back_populates='boss')


class Restaurant():
    """餐馆"""
    __tablename = 'Restaurant'
    auto_load_attrs = ('id', 'ref_boss_id')

    id = db.Column(UNSIGNED_INT, primary_key=True, autoincrement=True)
    # 店名
    name = db.Column(db.String(64), nullable=False)
    # 老板id
    ref_boss_id = db.Column(UNSIGNED_INT, db.ForeignKey(Boss.id), nullable=False)
    # 介绍
    introduction = db.Column(db.Text, nullable=True)
    # 地址
    address = db.Column(db.String(64), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    boss = db.relationship('Boss', back_populates='restaurants')
    foods = db.relationship('Food', back_populates='restaurant')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'introduction': self.introduction
        }


class Food():
    """菜品"""
    __tablename = 'Food'
    auto_load_attrs = ('id', 'name')

    id = db.Column(UNSIGNED_INT, primary_key=True, autoincrement=True)
    # 菜名
    name = db.Column(db.String(64), nullable=False)
    # 价格
    price = db.Column(UNSIGNED_INT, nullable=False)
    # 餐馆id
    ref_restaurant_id = db.Column(UNSIGNED_INT, db.ForeignKey(Restaurant.id), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    restaurant = db.relationship('Restaurant', back_populaters='foods')


class Order():
    """订单"""
    __tablename = 'order'
    auto_load_attrs = ('id')

    id = db.Column(UNSIGNED_INT, primary_key=True, autoincrement=True)
    # 总价
    total_price = db.Column(UNSIGNED_INT, nullable=False)
    # 顾客id
    ref_customer_id = db.Column(UNSIGNED_INT, db.ForeignKey(Customer.id), nullable=False)
    # 消费时间
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 折扣
    discount = db.Column(db.Float, default=1)
    is_deleted = db.Column(db.Boolean, default=False)

    customer = db.relationship('Customer', back_populates='orders')


class Customer(db.Model, UserMixin, ToDictMixin):
    """顾客"""
    __tablename = 'customer'
    auto_load_attrs = ('id')

    id = db.Column(UNSIGNED_INT, primary_key=True, autoincrement=True)
    # 昵称
    nick_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(40), nullable=True)
    province = db.Column(db.String(40), nullable=True)
    country = db.Column(db.String(40), nullable=True)
    avatarUrl = db.Column(db.String(200), nullable=True)
    cashbox = db.Column(db.Numeric(8,2), default=0.0)

    is_deleted = db.Column(db.Boolean, default=False)

    orders = db.relationship('Order', back_populates='customer')

    def to_dict(self):
        return {
            'id': self.id,
            'nick_name': self.nick_name
        }

# endregion