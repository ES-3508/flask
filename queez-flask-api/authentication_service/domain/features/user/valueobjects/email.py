from dataclasses import dataclass
from typing import Any
from authentication_service.domain.features.user.enums.user_message import   UserMessages
import re

@dataclass(frozen=True)
class Email:
    Value: str

    def __post_init__(self):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.Value):
            raise ValueError(UserMessages.INVALID_EMAIL_FORMAT_MSG)

        # Check for '@' symbol
        if '@' not in self.Value:
            raise ValueError(UserMessages.MISSING_AT_MSG)

        _, domain = self.Value.split('@')
        if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
            raise ValueError(UserMessages.INVALID_DOMAIN_MSG)

        return True