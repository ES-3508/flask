from dataclasses import dataclass
from ...landing.exceptions.landing_errors import LandingErrors


@dataclass(frozen=True)
class Type:
    Value: str

    def __post_init__(self):
        if not isinstance(self.Value, str) or not self.Value.isalpha() or not self.Value.isupper():
            raise ValueError(LandingErrors.PARENT_TYPE_MSG)

    
    