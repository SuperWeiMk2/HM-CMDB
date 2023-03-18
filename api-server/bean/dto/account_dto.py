#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from datetime import datetime
from flask_restful import fields


class AccountDTO:

    fields = {
        "uid": fields.String,
        "name": fields.String,
        "job_number": fields.String,
        "group": fields.String,
        "phone": fields.String,
        "email": fields.String,
        "sex": fields.String,
        "arch_group": fields.String,
        "create_time": fields.DateTime(attribute="create_time"),
        "update_time": fields.DateTime(attribute="update_time")
    }

    def __init__(self, uid: str = None,
                 name: str = None,
                 job_number: str = None,
                 group: str = None,
                 phone: str = None,
                 email: str = None,
                 sex: str = None,
                 arch_group: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 ):
        self.uid = uid
        self.name = name
        self.job_number = job_number
        self.group = group
        self.phone = phone
        self.email = email
        self.sex = sex
        self.arch_group = arch_group
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
    def get_job_number(self) -> str:
        return self.job_number

    def set_job_number(self, job_number: str):
        self.job_number = job_number

    # ============================
    def get_group(self) -> str:
        return self.group

    def set_group(self, group: str):
        self.group = group

    # ============================
    def get_phone(self) -> str:
        return self.group

    def set_phone(self, phone: str):
        self.phone = phone

    # ============================
    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    # ============================
    def get_sex(self) -> str:
        return self.sex

    def set_sex(self, sex: str):
        self.sex = sex

    # ============================
    def get_arch_group(self) -> str:
        return self.arch_group

    def set_arch_group(self, arch_group: str):
        self.arch_group = arch_group

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
