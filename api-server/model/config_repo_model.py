from core.server import Server
from bean.pojo.config_repo import ConfigRepo


class ConfigRepoModel:

    @staticmethod
    def create_config_repo(uid, name, connect_type, address, usage, create_time, update_time):
        result = Server.datasource["default"].db["config_repo"] \
            .insert_one({"uid": uid, "name": name, "connect_type": connect_type, "address": address, "usage": usage,
                         "create_time": create_time, "update_time": update_time, "is_delete": False})

        return result

    @staticmethod
    def get_all_config_repo():
        result = Server.datasource["default"].db["config_repo"].find()

        repos = []

        for item in result:
            repos.append(ConfigRepo(uid=item["uid"],
                                    name=item["name"],
                                    connect_type=item["connect_type"],
                                    address=item["address"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"],
                                    ))

        return repos

    @staticmethod
    def conditional_search_config_repo(repo_search):

        result = Server.datasource["default"].db["config_repo"].find(repo_search)

        repo_search = []

        for item in result:
            repo_search.append(ConfigRepo(uid=item["uid"],
                                          name=item["name"],
                                          connect_type=item["connect_type"],
                                          address=item["address"],
                                          usage=item["usage"],
                                          create_time=item["create_time"],
                                          update_time=item["update_time"]
                                          ),
                               )

        return repo_search

    @staticmethod
    def update_config_repo_by_uid(uid, name, connect_type, address, usage, update_time):
        result = Server.datasource["default"].db["config_repo"] \
            .update_one({"uid": uid}, {"$set": {"name": name, "connect_type": connect_type, "address": address,
                                                "usage": usage, "update_time": update_time}})
        return result
