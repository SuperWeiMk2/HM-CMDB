from bean.pojo.group import Group
from bean.pojo.logon import Logon
from core.server import Server


class LogonModel:

    @staticmethod
    def check_username_and_password(name, password):
        result = Server.datasource["default"].db["root"].find({"name": name, "password": password})

        check_empty = []

        for empty in result:
            check_empty.append(Logon(name=empty["name"],
                                     password=empty["password"],
                                     ))
        return check_empty
