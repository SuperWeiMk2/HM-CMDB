from flask import Blueprint


class DefaultInterface:
    api = Blueprint("defaultInterface", __name__, "/")

    @staticmethod
    @api.route("/", methods=('GET',))
    def defaultInterface() -> str:
        return "Welcome Use HM CMDB API Server !"
