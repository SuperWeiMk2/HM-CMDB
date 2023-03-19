from datetime import datetime
import uuid
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
    @api.route("/search", methods=('PUT',))
    def conditional_search_config_repo():
        print("收到post请求")
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_type = RequestUtil.get_param_from_body_raw_json(request, "connect_type")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        connect_type = StringUtil.smart_trim(p_type)
        usage = StringUtil.smart_trim(p_usage)

        repo_search = ConfigRepoService.conditional_search_config_repo(name, connect_type, usage)

        for search in repo_search:
            repo_search.append(ConfigRepoDTO(search.get_uid(),
                                             search.get_name(),
                                             search.get_connect_type(),
                                             search.get_address(),
                                             search.get_usage(),
                                             search.get_create_time(),
                                             search.get_update_time(),
                                             ))
        print("check4")
        print(repo_search)
        return GenericJSONResponse(data=marshal(repo_search, fields=ConfigRepoDTO.fields)).build()

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
            dto_list.append(ConfigRepoDTO(ConfigRepo.get_uid(),
                                          ConfigRepo.get_name(),
                                          ConfigRepo.get_connect_type(),
                                          ConfigRepo.get_address(),
                                          ConfigRepo.get_usage(),
                                          ConfigRepo.get_create_time(),
                                          ConfigRepo.get_update_time(),
                                          ))

        return GenericJSONResponse(data=marshal(dto_list, fields=ConfigRepoDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('PUT',))
    def create_config_repo():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_type = RequestUtil.get_param_from_body_raw_json(request, "connect_type")
        p_address = RequestUtil.get_param_from_body_raw_json(request, "address")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        uid = str(uuid.uuid4())
        name = StringUtil.smart_trim(p_name)
        connect_type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        ConfigRepoService.create_config_repo(uid, name, connect_type, address, usage, create_time, update_time)

        return {}

    @staticmethod
    @api.route("/<uid>", methods=('PUT',))
    def update_config_repo_by_name(uid):
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_type = RequestUtil.get_param_from_body_raw_json(request, "connect_type")
        p_address = RequestUtil.get_param_from_body_raw_json(request, "address")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        connect_type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)
        update_time = datetime.utcnow()

        ConfigRepoService.update_config_repo_by_uid(uid, name, connect_type, address, usage, update_time)

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
