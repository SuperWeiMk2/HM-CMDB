import uuid

from flask import request, Blueprint
from datetime import datetime

from flask_restful import marshal

from bean.dto.account_dto import AccountDTO
from core.response.generic_json_response import GenericJSONResponse
from service.account_service import AccountService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AccountAPI:
    api = Blueprint("account", __name__, url_prefix="/account")

    @staticmethod
    @api.route("/", methods=("GET",))
    def get_all_account():
        """
        索引全库
        :return: all_account
        """
        accounts = AccountService.get_all_account()
        account_dto_list = []

        for account in accounts:
            account_dto_list.append(AccountDTO(account.get_uid(),
                                               account.get_name(),
                                               account.get_job_number(),
                                               account.get_group(),
                                               account.get_phone(),
                                               account.get_email(),
                                               account.get_sex(),
                                               account.get_arch_group(),
                                               account.get_create_time(),
                                               account.get_update_time()))

        return GenericJSONResponse(data=marshal(account_dto_list, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/<uid>", methods=("GET",))
    def get_account_by_uid(uid):
        """
        根据工号，精确搜索
        :param uid:
        :return:
        """
        AccountService.get_account_by_uid(StringUtil.smart_trim(uid))

        return {}

    @staticmethod
    @api.route("/", methods=("GET",))
    def list_account():
        """
        根据条件进行匹配
        :return:
        """
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_phone = RequestUtil.get_param_from_url_query_param(request, "phone")
        p_email = RequestUtil.get_param_from_url_query_param(request, "email")
        p_sex = RequestUtil.get_param_from_url_query_param(request, "sex")
        p_arch_group = RequestUtil.get_param_from_url_query_param(request, "arch-group")

        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        AccountService.list_account(name, phone, email, sex, arch_group)

        return {}

    @staticmethod
    @api.route("/create", methods=("PUT",))
    def create_account():
        """
        向数据库增加用户。
        :return: {}
        """
        p_name = RequestUtil.get_param_from_body_raw_json(request, "create_name")
        p_job_number = RequestUtil.get_param_from_body_raw_json(request, "create_job_number")
        p_group = RequestUtil.get_param_from_body_raw_json(request, "create_group")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "create_phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "create_email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "create_sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "create_arch_group")

        uid = str(uuid.uuid4())
        name = StringUtil.smart_trim(p_name)
        job_number = StringUtil.smart_trim(p_job_number)
        group = StringUtil.smart_trim(p_group)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)
        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        AccountService.create_account(uid, name, job_number, group, phone, email, sex, arch_group, create_time, update_time)
        return {}

    # @staticmethod
    # @api.route("/<uid>", methods=("DELETE",))
    # def delete_account_by_uid(uid):
    #     """
    #     通过 uid 删除某个用户。
    #     :param uid:
    #     :return: bool
    #     """
    #     AccountService.delete_account_by_uid(StringUtil.smart_trim(uid))
    #     pass

    @staticmethod
    @api.route("/", methods=("DELETE",))
    def delete_account():
        """

        :return: bool
        """
        p_uid_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(p_uid_list) > 0:
            AccountService.delete_account(p_uid_list)

        return {}

    @staticmethod
    @api.route("/<uid>", methods=("PUT",))
    def update_account_by_uid(uid):
        """
        通过 uid 更新用户。
        :param uid:
        :return:
        """
        # p_uid = RequestUtil.get_param_from_body_raw_json(request, "uid")
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_job_number = RequestUtil.get_param_from_body_raw_json(request, "job_number")
        p_group = RequestUtil.get_param_from_body_raw_json(request, "group")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch_group")

        # uid = StringUtil.smart_trim(uid)
        name = StringUtil.smart_trim(p_name)
        job_number = StringUtil.smart_trim(p_job_number)
        group = StringUtil.smart_trim(p_group)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)
        update_time = datetime.utcnow()
        print(uid, name, job_number, group, phone, email, sex, arch_group, update_time)

        AccountService.update_account(uid, name, job_number, group, phone, email, sex, arch_group, update_time)

        return {}

    @staticmethod
    @api.route("/useJobNumberDelete", methods=("DELETE",))
    def delete_by_job_number():
        job_number = RequestUtil.get_param_from_url_query_param(request, "job_number")

        if AccountService.delete_account_by_job_number(job_number):
            return {}
        else:
            return {}

