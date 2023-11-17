from ..exceptions.landing_errors import LandingErrors
from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    Value: str

    def __post_init__(self):
        if not isinstance(self.Value, str) or not self.Value.isalpha():
            raise ValueError(LandingErrors.CATEGORY_MSG)
