from ..valueobjects.is_active import IsActive
from..valueobjects.advertisement_id import AdvertisementPackageId
from ..valueobjects.description import Description
from ..valueobjects.numofadd import NumberOfAdd
from ..valueobjects.numofdays import NumDays
from ..valueobjects.price import Price

class AdvertisementPackage:
    def __init__(self, package_id: AdvertisementPackageId, description: Description, number_of_add: NumberOfAdd,
                 num_days: NumDays, is_active: IsActive, price: Price):
        self.package_id = package_id
        self.description = description
        self.number_of_add = number_of_add
        self.num_days = num_days
        self.is_active = is_active
        self.price = price