from abc import ABC, abstractmethod
from ..valueobjects.id import Id
from ..aggregates.filters import Filter

class IFilterCommandRepository(ABC):
    
    @abstractmethod
    def create_filter(self, filter_data: Filter) -> None:
        pass

    @abstractmethod
    def update_filter(self, filter_id: Id, updated_filter_data: Filter) -> None:
        pass
    
    @abstractmethod
    def delete_filter(self, filter_id: Id) -> None:
        pass
