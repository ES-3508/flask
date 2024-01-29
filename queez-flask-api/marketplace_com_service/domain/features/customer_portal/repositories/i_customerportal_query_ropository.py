from abc import ABC, abstractmethod
from typing import List, Optional
from ..aggregates.pinnedItems import PinnedItems
from ..aggregates.savedfilters import SavedFilters
from ..aggregates.customerdetails import CustomerDetails
from ..aggregates.chat import Chat

class ICustomerportalQueryRepository(ABC):
    @abstractmethod
    def get_pinned_items_by_customer_id(self, customer_id: int) -> List[PinnedItems]:
        """Get pinned items by customer ID."""
        pass

    @abstractmethod
    def get_saved_filters_by_customer_id(self, customer_id: int) -> List[SavedFilters]:
        """Get saved filters by customer ID."""
        pass

    # @abstractmethod
    # def retrieve_chat_messages(self, sender_id: int, receiver_id: int) -> List[Chat]:
    #     """Retrieve chat messages between sender and receiver."""
    #     pass
    # @abstractmethod
    # def get_customer_details_by_id(self, customer_id: int) -> Optional[CustomerDetails]:
    #     """Get customer details by ID."""
    #     pass
