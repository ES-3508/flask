class HierarchicalDataResponseObject:    
    def __init__(self, id, name, level=None,parent=None,is_active=None,category=None):
        self.id = id
        self.name = name
        self.level = level
        self.parent = parent
        self.is_active = is_active
        self.category = category