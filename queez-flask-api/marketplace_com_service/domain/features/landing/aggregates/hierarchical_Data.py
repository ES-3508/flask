from ..valueobjects.name import Name
from ..valueobjects.id import Id
from ..valueobjects.level import Level
from ..valueobjects.parent import Parent
from ..valueobjects.is_active import IsActive
from ..valueobjects.category import Category

class HierarchicalData :
    def __init__(self, id:Id, name:Name, level:Level,parent:Parent,is_active:IsActive,category:Category):
        self.id = id
        self.name = name
        self.level = level
        self.parent = parent
        self.is_active = is_active
        self.category = category
        


# class HierarchicalData:
#     def __init__(self, id: Id, name: Name, level: Level, parent: Parent):
#         self.id = id
#         self.name = name
#         self.level = level
#         self.parent = parent
#         self.filters = []  # List to hold Filter instances
#         self.sys_keys = []  # List to hold Sys_keys instances

#     def add_filter(self, filter_instance: Filter):
#         # Add validation logic if needed
#         self.filters.append(filter_instance)

#     def remove_filter(self, filter_instance: Filter):
#         self.filters.remove(filter_instance)

#     def update_sys_key(self, sys_key_instance: Sys_keys):
#         # Add validation logic if needed
#         self.sys_keys.append(sys_key_instance)

#     # Other operations specific to HierarchicalData

# # Example Usage:
# hierarchical_data = HierarchicalData(id=1, name="Sample", level=2, parent=None)
# filter_instance = Filter(code="123", name="Filter1", level=1, parent=None, Type="Type1")
# sys_key_instance = Sys_keys(id=1, key="sample_key", description="Sample description")

# hierarchical_data.add_filter(filter_instance)
# hierarchical_data.update_sys_key(sys_key_instance)
