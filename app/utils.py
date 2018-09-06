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
	
	
def init_loggers(app):
    # 在创建 app 之后调用

    level = logging.DEBUG if app.debug else logging.INFO
    logging.basicConfig(level=level,
                        format=LOG_FORMAT,
                        stream=sys.stdout)

    # 显示 urllib3 和 requests 的请求日志
    logging.getLogger('requests').setLevel(logging.DEBUG)
    if 'urllib3' not in logging.root.manager.loggerDict:
        logging.getLogger('requests.packages.urllib3').setLevel(logging.DEBUG)
        logging.getLogger('requests.packages.urllib3.util.retry').disabled = True
    else:
        logging.getLogger('urllib3').setLevel(logging.DEBUG)
        logging.getLogger('urllib3.util.retry').disabled = True

    # todo remove as to flask1.0
    flask_production_handler = app.logger.handlers[1]  # type:logging.Handler
    flask_production_handler.setLevel(level)
    flask_production_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # logging.getLogger('sqlalchemy').setLevel(level)
    sql_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
    sql_logger.propagate = False
	
	
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(MyResponse, cls).force_type(response, environ)


class MyFlask(Flask):
    response_class = MyResponse
	
	
    json_encoder = EnhancedJsonEncoder

    def handle_http_exception(self, e):
        if e.code is None:
            return e

        handler = self._find_error_handler(e)
        if handler is None:
            # 自己定义的 HTTPException 可以直接返回 e 作为响应
            if isinstance(e, APIError):
                return e
            # 未处理的部分 HTTPException，简单的组成 JSON 返回
            return jsonify(success=False, msg=e.description, code=e.code), e.code
        # 明确定义了 handler 的 HTTPException, 则使用 handler 处理
        return handler(e)