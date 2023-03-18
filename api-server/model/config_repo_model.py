from core.server import Server
from bean.pojo.config_repo import ConfigRepo


class ConfigRepoModel:

    @staticmethod
    def create_config_repo(name, _type, address, usage, create_time, update_time):
        result = Server.datasource["default"].db["config_repo"] \
            .insert_one({"name": name, "connect_type": _type, "address": address, "usage": usage,
                         "create_time": create_time, "update_time": update_time, "is_delete": False})

        return result

    @staticmethod
    def get_all_config_repo():
        result = Server.datasource["default"].db["config_repo"].find()

        repos = []

        for item in result:
            repos.append(ConfigRepo(name=item["name"],
                                    connect_type=item["connect_type"],
                                    address=item["address"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]
                                    ),
                         )
        print(repos)
        return repos
