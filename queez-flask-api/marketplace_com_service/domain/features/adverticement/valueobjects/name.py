from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or not self.value:
            raise ValueError(AdverticementErrors.NAME_MSG)