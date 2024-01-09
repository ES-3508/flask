from abc import ABC, abstractmethod
from typing import List, Optional
from ...adverticement.aggregates.adverticement import AdvertisementHeader

class IAdvertisementCommandRepository(ABC):
    @abstractmethod
    def create_advertisement(self, advertisement: AdvertisementHeader) -> None:
        """Create a new advertisement."""
        pass

    # @abstractmethod
    # def update_advertisement(self, advertisement: AdvertisementHeader) -> None:
    #     """Update an existing advertisement."""
    #     pass

    # @abstractmethod
    # def delete_advertisement(self, advertisement_id: int) -> None:
    #     """Delete an advertisement by ID."""
    #     pass

