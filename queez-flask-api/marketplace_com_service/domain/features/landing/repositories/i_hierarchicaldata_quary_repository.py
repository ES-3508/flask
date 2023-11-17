from abc import ABC, abstractmethod
from ..valueobjects.id import Id
from ..aggregates.hierarchical_Data import HierarchicalData
from typing import List


class IHierarchicalDataQueryRepository(ABC):
    @abstractmethod
    def get_data_by_id(self, id: Id) -> HierarchicalData:
        pass

    @abstractmethod
    def get_all_data(self) -> List[HierarchicalData]:
        pass