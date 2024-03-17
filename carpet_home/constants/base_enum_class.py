from builtins import object

__author__ = 'shashank'


class BaseEnumClass(object):
    @classmethod
    def get_list_of_values(cls):
        """
        from enum import Enum
        from constants.base_enum_class import BaseEnumClass
        class MyEnum(BaseEnumClass, Enum)
            YELLOW = "YELLOW"
            PINK = "PINK"

        MyEnum.get_list_of_values()
        >> ["YELLOW", "PINK"]
        Get list of enum values as list
        :return:
            ["YELLOW", "PINK"]
        """
        return [item.value for item in cls]

    @classmethod
    def get_list_of_names(cls):
        return [item.name for item in cls]

    @classmethod
    def get_list_of_tuple(cls):
        return [(item.value, item.value) for item in cls]
