
from dataclasses import dataclass

@dataclass(frozen=True)
class State:
    value: str

    def __post_init__(self):
        # Add validation logic for the 'State' attribute
        pass