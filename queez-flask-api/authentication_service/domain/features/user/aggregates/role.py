class Role:
    def __init__(self, id: int=None, role_name: str=None, 
                 role_description: str=None):
        self.id = id
        self.role_privileges = []
    
    @property
    def privileges(self):
        return self.role_privileges

    @privileges.setter
    def privileges(self, privileges_list):
        self.role_privileges = privileges_list