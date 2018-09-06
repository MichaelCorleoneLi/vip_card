"""
# @File    : utils.py

# @Author  : lhy
# @Time    : 2018/8/10 22:54
"""


class UserType:
	BOSS = 0
	CUSTOMER = 1
	
	
def boss_or_customer(id):
	if 0 < id < 5000:
		return UserType.BOSS
	else:
		return UserType.CUSTOMER



def boss_required(func):
	@functools.wraps(func)
	def decorator(*args, **kwargs):
		if boss_or_customer(current_user.id) != UserType.BOSS:
			raise AuthError(errno.CUSTOMER_IS_NOT_ALLOWED)
			
		return func(*args, **kwargs)
		
	return login_required(decorator)
	
	
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(MyResponse, cls).force_type(response, environ)


class MyFlask(Flask):
    response_class = MyResponse