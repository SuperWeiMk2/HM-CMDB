from model.config_repo_model import ConfigRepoModel


class ConfigRepoService:

    @staticmethod
    def get_config_repo_by_name(name):
        pass

    @staticmethod
    def all_config_repo():
        return ConfigRepoModel.get_all_config_repo()

    @staticmethod
    def create_config_repo(name, _type, address, usage, create_time, update_time):
        empty_ok = [name, _type, address, usage]

        for OK in empty_ok:
            if OK is None:
                return False

        return ConfigRepoModel.create_config_repo(name, _type, address, usage, create_time, update_time)

    @staticmethod
    def update_config_repo_by_name(_type, address, usage, update_time):
        pass

    @staticmethod
    def delete_config_repo_by_name(name):
        pass

    @staticmethod
    def delete_config_repo(name_list):
        pass
