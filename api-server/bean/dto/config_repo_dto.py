from datetime import datetime
from flask_restful import fields


class ConfigRepoDTO:
    fields = {
        "uid": fields.String,
        "name": fields.String,
        "connect_type": fields.String,
        "address": fields.String,
        "usage": fields.String,
        "create_time": fields.DateTime(attribute="create_time"),
        "update_time": fields.DateTime(attribute="update_time")
    }

    def __init__(self, uid: str = None,
                 name: str = None,
                 connect_type: str = None,
                 address: str = None,
                 usage: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow()
                 ):
        self.uid = uid
        self.name = name
        self.connect_type = connect_type
        self.address = address
        self.usage = usage
        self.create_time = create_time
        self.update_time = update_time

    def get_uid(self) -> str:
        return self.uid

    def set_uid(self, uid: str):
        self.uid = uid

    # ============================

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    # ============================

    def get_connect_type(self) -> str:
        return self.connect_type

    def set__type(self, connect_type: str):
        self.connect_type = connect_type

    # ============================

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    # ============================

    def get_usage(self) -> str:
        return self.usage

    def set_usage(self, usage: str):
        self.usage = usage

    # ============================

    def get_create_time(self) -> datetime:
        return self.create_time

    def set_create_time(self, create_time: datetime):
        self.create_time = create_time

    # ============================

    def get_update_time(self) -> datetime:
        return self.update_time

    def set_update_time(self, update_time: datetime):
        self.create_time = update_time

    # ============================
