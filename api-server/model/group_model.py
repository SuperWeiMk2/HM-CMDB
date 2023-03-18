from bean.pojo.group import Group
from core.server import Server


class GroupModel:

    @staticmethod
    def get_group_by_name(name):
        result = Server.datasource["default"].db["group"].find({'_id': {"$regex": name}})

        groups = []
        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        return groups
        # return Group(name=result["_id"],
        #              usage=result["usage"],
        #              create_time=result["create_time"],
        #              update_time=result["update_time"])

    @staticmethod
    def all_group():
        result = Server.datasource["default"].db["group"].find()

        groups = []

        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        return groups

    @staticmethod
    def get_group_by_usage(usage: str):
        result = Server.datasource["default"].db["group"].find({"usage": usage})

        return result

    @staticmethod
    def create_group(name, usage, create_time, update_time):
        Server.datasource["default"].db["group"] \
            .insert_one({"_id": name, "usage": usage, "create_time": create_time,
                         "update_time": update_time, "is_delete": False})

        return True

    @staticmethod
    def delete_group_by_name(delete_name) -> bool:
        Server.datasource["default"].db["group"].delete_one({"_id": delete_name})

        return True

    @staticmethod
    def update_group(name, usage) -> bool:
        Server.datasource["default"].db["group"].update_one({"_id": name}, {"$set": {"usage": usage}})

        return True
