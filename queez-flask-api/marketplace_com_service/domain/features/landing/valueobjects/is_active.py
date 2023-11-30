
from ...landing.exceptions.landing_errors import LandingErrors
from dataclasses import dataclass


@dataclass(frozen=True)
class IsActive:
    Value: bool

    def __post_init__(self):
        if not isinstance(self.Value, bool):
            raise ValueError(LandingErrors.IS_ACTIVE_MSG)
        return True