from ..valueobjects.customer_id import CustomerId
from ..valueobjects.name import Name
from ..valueobjects.sys_user_id import SysUserId


class CustomerDetails:
    def __init__(self, customer_id: CustomerId, name: Name, sys_user_id: SysUserId):
        self.customer_id = customer_id
        self.name = name
        self.sys_user_id = sys_user_id
