from ...landing.exceptions.landing_errors import LandingErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Description:
    Value: str

    def __post_init__(self):
        if not isinstance(self.Value, str):
            raise ValueError(LandingErrors.DESCRIPTION_MSG)
        
        return True
        
        









