from datetime import datetime

from flask import Blueprint, request
from flask_restful import marshal

from core.response.generic_json_response import GenericJSONResponse
from bean.dto.config_repo_dto import ConfigRepoDTO
from service.config_repo_service import ConfigRepoService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class ConfigRepoAPI:
    api = Blueprint("config_repo", __name__, url_prefix="/config_repo")

    @staticmethod
    @api.route("/<name>", methods=('GET',))
    def get_config_repo_by_name(name):
        ConfigRepoService.get_config_repo_by_name(StringUtil.smart_trim(name))
        return {}

    @staticmethod
    @api.route("/", methods=('GET',))
    def all_config_repo():
        p_type = RequestUtil.get_param_from_url_query_param(request, "connect_type")
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        connect_type = StringUtil.smart_trim(p_type)
        usage = StringUtil.smart_trim(p_usage)

        config_repos = ConfigRepoService.all_config_repo()

        dto_list = []

        for ConfigRepo in config_repos:
            dto_list.append(ConfigRepoDTO(ConfigRepo.get_name(),
                                          ConfigRepo.get_type(),
                                          ConfigRepo.get_address(),
                                          ConfigRepo.get_usage(),
                                          ConfigRepo.get_create_time(),
                                          ConfigRepo.get_update_time(),
                                          ))
        print(dto_list)
        return GenericJSONResponse(data=marshal(dto_list, fields=ConfigRepoDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('PUT',))
    def create_config_repo():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_type = RequestUtil.get_param_from_body_raw_json(request, "connect_type")
        p_address = RequestUtil.get_param_from_body_raw_json(request, "address")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        connect_type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        ConfigRepoService.create_config_repo(name, connect_type, address, usage, create_time, update_time)

        return {}

    @staticmethod
    @api.route("/<name>", methods=('PUT',))
    def update_config_repo_by_name(name):
        p_type = RequestUtil.get_param_from_body_raw_json(request, "connect_type")
        p_address = RequestUtil.get_param_from_body_raw_json(request, "address")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        connect_type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)
        update_time = datetime.utcnow()

        ConfigRepoService.update_config_repo_by_name(connect_type, address, usage, update_time)

        return {}

    @staticmethod
    @api.route("/<name>", methods=('DELETE',))
    def delete_config_repo_by_name(name):
        ConfigRepoService.delete_config_repo_by_name(StringUtil.smart_trim(name))
        return {}

    @staticmethod
    @api.route("/", methods=('DELETE',))
    def delete_config_repo():
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            ConfigRepoService.delete_config_repo(name_list)

        return {}
