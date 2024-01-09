from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Value:
    Content: str

    def __post_init__(self):
        if not isinstance(self.Content, str):
            raise ValueError(AdverticementErrors.VALUE_MSG)
