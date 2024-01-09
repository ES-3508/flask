from ..valueobjects.add_detail_id import AdvertisementDetailsId
from ..valueobjects.add_id import AddId
from ..valueobjects.filter_id import FilterId
from ..valueobjects.value import Value


class AdvertisementDetails:
    def __init__(self, advertisement_details_id: AdvertisementDetailsId, add_id: AddId, filter_id: FilterId, value: Value):
        self.advertisement_details_id = advertisement_details_id
        self.add_id = add_id
        self.filter_id = filter_id
        self.value = value


