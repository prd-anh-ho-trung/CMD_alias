from enum import Enum


class TypeCMD(str, Enum):
    OLIVIA = "olivia"


class optionsFactory():
    def __init__(self, type):
        self.type = type
    def get_options

