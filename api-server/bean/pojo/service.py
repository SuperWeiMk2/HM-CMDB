from datetime import datetime


class Service:
    def __init__(self, name: str = None,
                 level: str = None,
                 parent: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 usage: str = None,
                 is_delete: bool = None):
        self.__name = name
        self.__level = level
        self.__parent = parent
        self.__create_time = create_time
        self.__update_time = update_time
        self.__usage = usage
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    # ============================

    def get_level(self) -> str:
        return self.__level

    def set_level(self, level: str):
        self.__level = level

    # ============================

    def get_parent(self) -> str:
        return self.__parent

    def set_parent(self, parent: str):
        self.__parent = parent

    # ============================

    def get_create_time(self) -> datetime:
        return self.__create_time

    def set_create_time(self, create_time: datetime):
        self.__create_time = create_time

    # ============================

    def get_update_time(self) -> datetime:
        return self.__update_time

    def set_update_time(self, update_time: datetime):
        self.__update_time = update_time

    # ============================

    def get_usage(self) -> str:
        return self.__usage

    def set_usage(self, usage: str):
        self.__usage = usage

    # ============================

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete
