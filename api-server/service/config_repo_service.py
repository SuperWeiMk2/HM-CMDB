from model.config_repo_model import ConfigRepoModel


class ConfigRepoService:

    @staticmethod
    def get_config_repo_by_name(name):
        pass

    @staticmethod
    def conditional_search_config_repo(name, connect_type, usage):

        check_empty = {"name": name, "connect_type": connect_type, "usage": usage}

        for key, value in list(check_empty.items()):
            print(key)
            print(value)
            if value is None:
                check_empty.pop(key)

        repo_search = check_empty
        print(repo_search)
        print(type(repo_search))
        return ConfigRepoModel.conditional_search_config_repo(repo_search)

    @staticmethod
    def all_config_repo():
        return ConfigRepoModel.get_all_config_repo()

    @staticmethod
    def create_config_repo(uid, name, connect_type, address, usage, create_time, update_time):
        empty_ok = [name, connect_type, address, usage]

        for OK in empty_ok:
            if OK is None:
                return False

        return ConfigRepoModel.create_config_repo(uid, name, connect_type, address, usage, create_time, update_time)

    @staticmethod
    def update_config_repo_by_uid(uid, name, connect_type, address, usage, update_time):
        check_empty = [uid, name, connect_type, address, usage, update_time]
        for OK in check_empty:
            if OK is None:
                return False
        return ConfigRepoModel.update_config_repo_by_uid(uid, name, connect_type, address, usage, update_time)

    @staticmethod
    def delete_config_repo_by_name(name):
        pass

    @staticmethod
    def delete_config_repo(name_list):
        pass
