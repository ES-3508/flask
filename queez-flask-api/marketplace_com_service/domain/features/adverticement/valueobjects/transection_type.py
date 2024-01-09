

from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class TransectionType:
    value: str

    def __post_init__(self):
        # Add validation logic for the 'TransectionType' attribute
        pass