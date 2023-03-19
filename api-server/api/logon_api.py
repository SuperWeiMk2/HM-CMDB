from flask import request, Blueprint

from service.logon_server import LogonServer
from util.request_util import RequestUtil
from util.string_util import StringUtil
from core.server import Server


class LogonAPI:
    api = Blueprint("logon", __name__, url_prefix="/logon")

    @staticmethod
    @api.route("/", methods=("PUT",))
    def log_on_system():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_password = RequestUtil.get_param_from_body_raw_json(request, "password")

        name = StringUtil.smart_trim(p_name)
        password = StringUtil.smart_trim(p_password)

        result = LogonServer.logon(name, password)
        print(result)
        if len(result) == 0:
            return "1"
        else:
            return "0"
