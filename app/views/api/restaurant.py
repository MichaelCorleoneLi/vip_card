"""
# @File    : restaurant.py

# @Author  : lhy
# @Time    : 2018/9/6 18:37
"""
from app.models import Restaurant
from . import api


@api.route('/menu/<int:restaurant_id>')
def get_menu(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    return {'menu': [food.to_dict() for food in restaurant.foods]}