from dataclasses import dataclass
from ..exceptions.customerportal_errors import CustomerportalErrors

@dataclass(frozen=True)
class ReceiverID:
    Value: int

    def __post_init__(self):
        if not isinstance(self.Value, int) or self.Value <= 0:
            raise ValueError(CustomerportalErrors.RECEIVER_MSG)