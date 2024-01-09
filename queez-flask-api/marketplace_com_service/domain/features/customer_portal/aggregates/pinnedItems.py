from ..valueobjects.add_id import AddId
from ..valueobjects.id import Id
from ..valueobjects.customer_id import CustomerId

class PinnedItems:
    def __init__(self, id:Id, customer_id: CustomerId, add_id: AddId):
        self.id = id
        self.customer_id = customer_id
        self.add_id = add_id
