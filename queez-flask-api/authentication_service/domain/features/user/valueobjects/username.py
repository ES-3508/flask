from dataclasses import dataclass
from typing import Any
import re
from authentication_service.domain.features.user.enums.user_message import   UserMessages

@dataclass(frozen=True)
class Username:
    Value: str

    def __post_init__(self):
        
        allowed_characters = r'^[a-zA-Z0-9_@.-]+$'
        if not (4 <= len(self.Value) <= 20):
            raise ValueError(UserMessages.VALID_LENGTH_MSG)

        # Check if the username contains only allowed characters
        if not re.match(allowed_characters, self.Value):
            raise ValueError(UserMessages.INVALID_CHARACTERS_MSG)

        return True
       
       