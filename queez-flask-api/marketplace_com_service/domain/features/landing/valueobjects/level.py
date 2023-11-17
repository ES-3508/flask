from ...landing.exceptions.landing_errors import LandingErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Level:
    Value: int

    def __post_init__(self):
        if not isinstance(self.Value, int) or not (1 <= self.Value <= 100):
            raise ValueError(LandingErrors.LEVEL_MSG)
        
        return True