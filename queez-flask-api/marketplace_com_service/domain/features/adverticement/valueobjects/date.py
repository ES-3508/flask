from datetime import date
from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Date:
    value: date

    def __post_init__(self):
        if not isinstance(self.value, date):
            raise ValueError(AdverticementErrors.DATE_MSG)

        # You can add additional validation logic for the date if needed
