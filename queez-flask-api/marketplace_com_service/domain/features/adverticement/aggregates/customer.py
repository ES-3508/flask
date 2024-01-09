from ..valueobjects.id import Id
from ..valueobjects.name import Name
from ..valueobjects.sys_user_id import SysUserId


class Customer:
    def __init__(self, customer_id: Id, name: Name, sys_user_id: SysUserId):
        self.customer_id = customer_id
        self.name = name
        self.sys_user_id = sys_user_id
        # Add other properties related to Customer
        
        
        
        
        



