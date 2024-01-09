from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Time:
    value: datetime

    def __post_init__(self):
        # Your custom initialization logic here, if needed
        pass
