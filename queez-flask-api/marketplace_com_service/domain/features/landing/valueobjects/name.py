from dataclasses import dataclass
from ...landing.exceptions.landing_errors import LandingErrors

@dataclass(frozen=True)
class Name:
    Value: str

    def __post_init__(self):
        if not isinstance(self.Value, str) or not self.Value.isalpha():
            raise ValueError(LandingErrors.NAME_MSG)
        
        return True