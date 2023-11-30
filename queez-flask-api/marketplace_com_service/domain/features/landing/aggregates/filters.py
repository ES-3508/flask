from ..valueobjects.name import Name
from ..valueobjects.id import Id
from ..valueobjects.description import Description
from ..valueobjects.ref_id import Ref_id
from ..valueobjects.is_active import IsActive
from ..valueobjects.type import Type
from ..valueobjects.sql_statement import SQLStatement



class Filter:
    def __init__(self, id:Id, name:Name, description:Description, ref_id:Ref_id, type:Type, is_active:IsActive, sql_statement:SQLStatement):
        self.id = id
        self.name = name
        self.description = description
        self.ref_id = ref_id
        self.type = type
        self.is_active = is_active
        self.sql_statement = sql_statement

    
