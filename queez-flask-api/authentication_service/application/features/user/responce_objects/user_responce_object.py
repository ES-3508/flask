class UserResponceObjct:
    def __init__(self, id, username,user_fullname=None,user_address=None,
                 user_contact=None,user_email=None,password=None,
                 token=None,user_role=None):
        self.id = id
        self.username = username
        self.password = password
        self.token = token
        self.user_fullname = user_fullname
        self.user_address = user_address
        self.user_email = user_email
        self.user_contact = user_contact
        self.user_role = user_role