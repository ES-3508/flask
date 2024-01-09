
from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass


@dataclass(frozen=True)
class IsActive:
    Value: bool

    def __post_init__(self):
        if not isinstance(self.Value, bool):
            raise ValueError(AdverticementErrors.IS_ACTIVE_MSG)
        return True