from dataclasses import dataclass
from typing import Any
from authentication_service.domain.features.user.enums.user_message import   UserMessages

@dataclass(frozen=True)
class FullName:
    Value: str

    def __post_init__(self):
        if not self.Value.strip():
            raise ValueError(UserMessages.INVALID_FULL_NAME_MSG)

        return True