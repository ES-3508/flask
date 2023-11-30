from dataclasses import dataclass
from typing import Any
from authentication_service.domain.features.user.enums.user_message import   UserMessages
import re

@dataclass(frozen=True)
class Password:
    Value: str

    def __post_init__(self):
        
        # Check minimum length requirement
        if len(self.Value) < 8:
            raise ValueError(UserMessages.MIN_LENGTH_MSG)

        # Check if password contains at least one uppercase letter
        if not any(char.isupper() for char in self.Value):
            raise ValueError(UserMessages.UPPERCASE_MSG)

        # Check if password contains at least one lowercase letter
        if not any(char.islower() for char in self.Value):
            raise ValueError(UserMessages.LOWERCASE_MSG)

        # Check if password contains at least one digit
        if not any(char.isdigit() for char in self.Value):
            raise ValueError(UserMessages.DIGIT_MSG)

        # Check if password contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.Value):
            raise ValueError(UserMessages.SPECIAL_CHAR_MSG)

        # Password meets the common standards
        return True