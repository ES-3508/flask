from abc import ABC, abstractmethod
from typing import List, Optional
from ...adverticement.aggregates.adverticement import AdvertisementHeader

class IAdvertisementQueryRepository(ABC):
    @abstractmethod
    def get_advertisement_by_id(self, advertisement_id: int) -> Optional[AdvertisementHeader]:
        """Get an advertisement by ID."""
        pass
    @abstractmethod
    def get_advertisement_by_filter_id_and_value(self, filter_id, value):
        pass
        # Construct MongoDB query
    # @abstractmethod
    # def get_all_advertisements(self) -> List[AdvertisementHeader]:
    #     """Get all advertisements."""
    #     pass

    # @abstractmethod
    # def filter_by_category(self, category: str) -> List[AdvertisementHeader]:
    #     """Filter advertisements by category."""
    #     pass

    # Add more query methods as needed for your application
