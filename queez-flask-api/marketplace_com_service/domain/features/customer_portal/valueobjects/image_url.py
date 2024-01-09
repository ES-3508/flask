from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class ImageURL:
    URL: str

    def __post_init__(self):
        if not isinstance(self.URL, str):
            raise ValueError(AdverticementErrors.IMAGE_URL_MSG)
