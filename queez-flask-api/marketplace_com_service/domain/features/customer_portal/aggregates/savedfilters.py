from ..valueobjects.filter_id import FilterId
from ..valueobjects.value import Value

class SavedFilters:
    def __init__(self, customer_id: int, filter_id: FilterId, value: Value):
        self.customer_id = customer_id
        self.filter_id = filter_id
        self.value = value
