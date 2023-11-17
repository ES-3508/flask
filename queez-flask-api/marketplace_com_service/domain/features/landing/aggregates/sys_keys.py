from ..valueobjects.id import Id
from ..valueobjects.key import Key
from ..valueobjects.description import Description

class Sys_keys :
    def __init__(self, id:Id, key:Key, description:Description):
        self.id = id
        self.key = key
        self.description = description
        
