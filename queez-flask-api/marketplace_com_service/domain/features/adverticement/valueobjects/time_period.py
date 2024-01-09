from datetime import datetime
from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class TimePeriod:
    Value: datetime

    def __post_init__(self):
        if not isinstance(self.Value, datetime):
            raise ValueError(AdverticementErrors.TIME_PERIOD_MSG)
