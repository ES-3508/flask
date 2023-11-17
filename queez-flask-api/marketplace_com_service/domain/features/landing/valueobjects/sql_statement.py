from ...landing.exceptions.landing_errors import LandingErrors
from dataclasses import dataclass
import re




@dataclass(frozen=True)
class SQLStatement:
    Value: str

    def __post_init__(self):
        if not isinstance(self.Value, str):
            raise ValueError(LandingErrors.SQL_STATEMENT_MSG)

        # Additional validation based on your requirements
        if not re.match(r'^[a-zA-Z0-9_]+$', self.Value):
            raise ValueError(LandingErrors.INVALID_SQL_STATEMENT_MSG)
        
        return True
