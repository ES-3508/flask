from ..valueobjects.publisher_id import PublisherId
from ..valueobjects.time_period import TimePeriod
from ..valueobjects.is_active import IsActive
from ..valueobjects.cordinates import Coordinates
from ..valueobjects.id import Id
from ..valueobjects.date import Date

class AdvertisementHeader:
    def __init__(self, header_id: Id, publisher_id: PublisherId,
                 time_period: TimePeriod, is_active: IsActive, coordinates: Coordinates,
                 wf_state_id: Id, date: Date, user_id: Id, package_id: Id):
        self.header_id = header_id
        self.publisher_id = publisher_id
        self.time_period = time_period
        self.is_active = is_active
        self.coordinates = coordinates
        self.wf_state_id = wf_state_id
        self.date = date
        self.user_id = user_id
        self.package_id = package_id
