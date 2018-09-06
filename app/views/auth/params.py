"""
# @File    : params.py

# @Author  : lhy
# @Time    : 2018/9/6 12:57
"""

LOGIN = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 1},
        'password': {'type': 'string', 'minLength': 1},
        'verify_code': {
            'type': 'string',
            'length': 4
        }
    },
    'required': ['username', 'password']
}