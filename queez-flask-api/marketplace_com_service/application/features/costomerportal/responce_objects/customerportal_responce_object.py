# class CustomerportalResponseObject:
#     def __init__(self, customer_id, add_id=None,filter_id=None,value =None,  name=None, sys_user_id=None, pinned_items=None, saved_filters=None):
#         self.customer_id = customer_id
#         self.add_id = add_id
#         self.filter_id =filter_id
#         self.value = value
#         self.name = name
#         self.sys_user_id = sys_user_id
        
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class CustomerportalResponseObject:
    customer_id: int
    add_id: Optional[int] = None
    filter_id: Optional[int] = None
    value: Optional[str] = None
    name: Optional[str] = None
    sys_user_id: Optional[int] = None
 


      
