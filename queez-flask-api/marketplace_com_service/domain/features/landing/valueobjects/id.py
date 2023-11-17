from ...landing.exceptions.landing_errors import LandingErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Id:
    Value: int

    def __post_init__(self):
        if self.Value <= 0:
            raise ValueError(LandingErrors.ID_MSG)
        
        return True

