
from..valueobjects.full_name import FullName

from ..valueobjects.address import Address
from ..valueobjects.contact import Contact
from ..valueobjects.email import Email
from ..valueobjects.password import Password
from ..valueobjects.token import Token
from ..valueobjects.user_role import UserRole
from ..valueobjects.username import Username
class User:
    def __init__(self, id, username:Username,user_fullname:FullName=None,user_address:Address=None,
                 user_contact:Contact=None,user_email:Email=None,password:Password=None,
                 token:Token=None,user_role:UserRole=None):
        self.id = id
        self.username = username
        self.password = password
        self.token = token
        self.user_fullname = user_fullname
        self.user_address = user_address
        self.user_email = user_email
        self.user_contact = user_contact
        self.user_role = user_role



 