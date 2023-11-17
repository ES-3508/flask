from dataclasses import dataclass
from ...landing.exceptions.landing_errors import LandingErrors


@dataclass(frozen=True)
class Ref_id:
    Value: int

    def __post_init__(self):
        if self.Value <= 0:
            raise ValueError(LandingErrors.ID_MSG)
        
        return True