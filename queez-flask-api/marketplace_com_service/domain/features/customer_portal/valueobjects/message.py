from dataclasses import dataclass

@dataclass(frozen=True)
class MessageText:
    value: str