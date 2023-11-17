from abc import ABC, abstractmethod
from ..valueobjects.id import Id
from ..aggregates.filters import Filter
from typing import List

class IFilterQueryRepository(ABC):
    @abstractmethod
    def get_filter_by_code(self, id: Id) -> Filter:
        pass
    
    @abstractmethod
    def get_all_filter(self) -> List[Filter]:
        pass