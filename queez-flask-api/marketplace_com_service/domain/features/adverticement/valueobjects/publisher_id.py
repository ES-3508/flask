from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class PublisherId:
    Value: int

    def __post_init__(self):
        if not isinstance(self.Value, int) or self.Value <= 0:
            raise ValueError(AdverticementErrors.PUBLISHER_ID_MSG)

