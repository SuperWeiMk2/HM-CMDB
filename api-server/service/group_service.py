from model.group_model import GroupModel


class GroupService:

    @staticmethod
    def get_group_by_name(name: str):
        return GroupModel.get_group_by_name(name)

    @staticmethod
    def get_group(usage: str | None):
        if usage is None:
            return GroupModel.all_group()
        else:
            return GroupModel.get_group_by_usage(usage)

    @staticmethod
    def create_group(name, usage, create_time, update_time):
        group_name_list = GroupModel.get_group_by_name(name)
        if name in group_name_list:
            return False
        else:
            GroupModel.create_group(name, usage, create_time, update_time)

    @staticmethod
    def update_group(name, usage):
        return GroupModel.update_group(name, usage)

    @staticmethod
    def delete_group_by_name(delete_name):
        return GroupModel.delete_group_by_name(delete_name)

    @staticmethod
    def delete_group(name_list):
        pass
