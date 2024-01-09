from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    X: float
    Y: float

    def __post_init__(self):
        if not isinstance(self.X, float) or not isinstance(self.Y, float):
            raise ValueError(AdverticementErrors.COORDINATES_MSG)
