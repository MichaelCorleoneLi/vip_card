# Created by John Jiang at 2018/3/5 16:39

# noinspection PyUnresolvedReferences
from json import JSONDecodeError

from flask import json
from flask_babel import lazy_gettext as _
# noinspection PyUnresolvedReferences
from requests import RequestException
from werkzeug.exceptions import HTTPException


class Error(HTTPException):
    pass


class DescritionFormatError(Exception):
    pass


class APIError(Error):
    code = 200

    def __init__(self, error, description=None, **kwargs):
        """
        error 一般是 errno 的属性，如 raise APIError(errno.UNAUTHORIZED)
        description 为空时使用 error_code 默认的错误描述，也可以使用自定义的字符串。字符串中可以包含 "{name}" 这样可以被替换的部分。
        args 可以是任何关键字参数，会被格式化到 description 中。
        """
        if isinstance(error, tuple):
            error_code, desc = error
            # 如果没有提供 description, 使用默认的
            if description is None:
                description = desc
        else:
            # 自定义的 error_code, 必须要提供 description
            error_code = error
            if description is None:
                raise ValueError('Custom error code but does not specify description')

        super().__init__(str(description))
        self.error_code = error_code
        self.kwargs = kwargs

    def get_description(self, environ=None):
        desc = self.description

        if self.kwargs:
            try:
                desc = desc.format_map(self.kwargs)
            except KeyError:
                raise DescritionFormatError('Error when formatting error description: {!r}'.format(desc))

        return desc

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    def get_body(self, environ=None):
        return json.dumps({
            'success': False,
            'msg': self.get_description(environ),
            'code': self.error_code,
        })


class AuthError(APIError):
    pass


class ServerError(APIError):
    code = 500


class errno:
    CUSTOMER_IS_NOT_ALLOWED = 1, _('This interface is not for customer')
    BOSS_IS_NOT_ALLOWED = 1, _('This interface is not for boss')
    # 这些代码不是在一个有效的 request context 中执行的，所以必须用 lazy_gettext
    UNKNOWN = 100, _('Unknown error')
    INVALID_PARAMETERS = 101, _('Invalid parameters')
    USERNAME_OR_PASSWORD_ERROR = 102, _('Username or password is not correct')
    EXCEED_MAX_LOGIN_FAILS = 104, _('You have failed too many times, please try later')
    ACCOUNT_DISABLED = 105, _('Account disabled')
    ACCOUNT_EXPIRED = 106, _('Account has expired')
    VISITOR_IS_NOT_ALLOWD = 107, _('Visitor is not allowed')
    NEED_LOGIN = 108, 'need_login'
    NOT_ENTITLED_FOR_TRIAL = 109, _('You are not entitled for a trial')
    NEED_MOA_NONCE = 110, _('Send moa nonce first')
    MOA_NONCE_NOT_MATCH = 111, _('Moa nonce not match')
    MOA_NONCE_EXPIRED = 112, _('Moa nonce has expired')
    MOA_NONCE_TOO_OFTEN = 113, _('Send moa message too often')
    MOA_NONCE_NEED_CAPTCHA = 114, _('Need verify captcha to send moa')
    SSO_ERROR = 115, _('SSO server complianed about something')
    REPORT_NOT_FOUND = 116, _('The report file does not found')
    RESOURCE_NOT_EXIST = 117, _('The resource you requested does not exist')
    RESOURCE_ALREADY_EXIST = 118, _('The resource already exists')
    NO_RIGHT_TO_ACCESS = 119, _('You have no right to access the resource')
    EXCEED_MAX_ASSET_NUM = 120, _('The assets you added exceed max asset num')
    FILE_TYPE_NOT_ALLOWED = 121, _('The file type is not allowed')
    FILE_CONTENT_ERROR = 122, _('Error when parse the file')
    EXCEED_MAX_CONCURRENT_TASK = 123, _('You have exceed max concurrent tasks')
    BUSINESS_ALREADY_EXIST = 124, _('Business name({business_name}) already exist')
    ASSET_ALREADY_EXIST = 125, _('Asset name({asset_name}) already exist')
    INTERVAL_TOO_LARGE = 126, _('Interval too large')
    EXECUTING_TASKS_TOO_MUCH = 127, _('Executing tasks too much')
    IP_INVALID = 128, _('IP invalid, {error_msg}')
    PUSH_ON_TOO_MUCH = 129, _('One task can only be pushed {max_times} times')
    LICENSE_INVALID = 130, _('License invalid')
    SCANNER_OFFLINE = 131, _('Scanner offline')
    EXIST_EXECUTING_TASK = 132, _('You have executing task, please try later')
    IMAGE_VERIFY_CODE_ERROR = 133, _('Image verify code error')
    OLD_PASSWORD_NOT_CORRECT = 134, _('Old password is not correct')
    ASSET_NAME_INVALID = 135, _('Asset name({asset_name}) contains invalid char({invalid_char})')
    PARSE_DEVICE_INFO_ERROR = 136, _('Parse local device_info.txt error')
    INCONSISTENT_DEVICE_INFO = 137, _('Device info in local and license are inconsistent')
    LICENSE_REPEATED = 138, _('License is repeated')
    LICENSE_EXPIRED = 139, _('License is expired')
    INTERVAL_TOO_SMALL = 140, _('Interval too small')
    UPGRADE_WAS_ABORTED = 141, _('The upgrade was aborted')
    UPGRADE_FAIL = 142, _('Upgrade fail({error})')
    UPGRADE_START_FAILED = 143, _('Start upgrade failed')
    ACTIVATED_SCANNER_FAILED = 144, _('Activated scanner failed')
    # todo 开发完成后统一编译

    NO_MORE_PAGE = 300, _('No more pages')

    SERVER_BUSY = 500, _('Server is very busy now, please try some time later')
    DB_INFO_ERROR = 501, _('Database information has some errors')
