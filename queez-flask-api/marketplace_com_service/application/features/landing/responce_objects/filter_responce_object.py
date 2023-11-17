class FilterResponseObject:
    def __init__(self, id, name, description,ref_id,type,is_active,sql_statement):
        self.id = id
        self.name = name
        self.description = description
        self.ref_id = ref_id
        self.type = type
        self.is_active = is_active
        self.sql_statement = sql_statement
    
  