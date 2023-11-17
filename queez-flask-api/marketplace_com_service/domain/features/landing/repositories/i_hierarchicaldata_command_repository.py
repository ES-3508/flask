from abc import ABC, abstractmethod
from ..valueobjects.id import Id
from ..aggregates.hierarchical_Data import HierarchicalData



class IHierarchicalDataCommandRepository(ABC):
    
    @abstractmethod
    def create_data(self, data: HierarchicalData) -> None:
        pass

    @abstractmethod
    def update_data(self, data_id: Id, updated_data: HierarchicalData) -> None:
        pass
    
    @abstractmethod
    def delete_data(self, data_id: Id) -> None:
        pass

  
