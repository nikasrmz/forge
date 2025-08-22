from enum import Enum

class ParamSource(Enum):
    PATH = "PATH"
    INJECT = "INJECT"
    QUERY = "QUERY"