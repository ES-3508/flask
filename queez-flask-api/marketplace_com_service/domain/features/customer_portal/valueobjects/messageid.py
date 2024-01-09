from ..exceptions.customerportal_errors import CustomerportalErrors
from dataclasses import dataclass

@dataclass(frozen=True)
class MessageID:
    value: int

    def __post_init__(self):
        if not isinstance(self.Value, int) or self.Value <= 0:
            raise ValueError(CustomerportalErrors.MESSAGE_MSG)