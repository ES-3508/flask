from dataclasses import dataclass
from typing import Any
from authentication_service.domain.features.user.enums.user_message import   UserMessages

@dataclass(frozen=True)
class UserRole:
    Value: str

    def __post_init__(self):
        if not self.Value.strip():
            raise ValueError(UserMessages.INVALID_USER_ROLE_MSG)
        
        return True
