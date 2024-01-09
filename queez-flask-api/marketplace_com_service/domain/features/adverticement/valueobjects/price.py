from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Price:
    value: float

    def __post_init__(self):
        if not isinstance(self.value, (int, float)) or self.value <= 0:
            raise ValueError(AdverticementErrors.PRICE_MSG)