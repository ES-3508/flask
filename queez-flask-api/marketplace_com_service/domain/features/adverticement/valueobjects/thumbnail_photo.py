from ..exceptions.adverticement_errors import AdverticementErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class ThumbnailPhoto:
    URL: str

    def __post_init__(self):
        if not isinstance(self.URL, str):
            raise ValueError(AdverticementErrors.THUMBNAIL_PHOTO_MSG)
