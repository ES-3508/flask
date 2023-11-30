from .....application.features.landing.responce_objects.filter_responce_object import FilterResponseObject
from .....application.features.landing.responce_objects.hierarchicaldata_responce_object import HierarchicalDataResponseObject


        
        
class FilterandhierarcHicaldataResponceObject(FilterResponseObject, HierarchicalDataResponseObject):
    def __init__(self, filter_id, filter_name, filter_description, filter_ref_id, filter_type,
                 filter_is_active, filter_sql_statement, hierarchical_id, hierarchical_name,
                 hierarchical_level, hierarchical_parent, hierarchical_is_active, hierarchical_category):
        super().__init__(filter_id, filter_name, filter_description, filter_ref_id, filter_type,
                         filter_is_active, filter_sql_statement)
        self.hierarchical_id = hierarchical_id
        self.hierarchical_name = hierarchical_name
        self.hierarchical_level = hierarchical_level
        self.hierarchical_parent = hierarchical_parent
        self.hierarchical_is_active = hierarchical_is_active
        self.hierarchical_category = hierarchical_category

# Modify the get_all_filters_and_data function to use the CombinedResponseObject





