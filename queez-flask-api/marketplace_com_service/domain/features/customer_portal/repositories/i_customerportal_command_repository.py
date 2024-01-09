from abc import ABC, abstractmethod
from ..aggregates.pinnedItems import PinnedItems
from ..aggregates.savedfilters import SavedFilters
from ..aggregates.customerdetails import CustomerDetails
from ..aggregates.chat import Chat

class ICustomerportalCommandRepository(ABC):
    @abstractmethod
    def save_pinned_item(self, pinned_item: PinnedItems) -> None:
        """Save a pinned item."""
        pass

    @abstractmethod
    def save_saved_filter(self, saved_filter: SavedFilters) -> None:
        """Save a saved filter."""
        pass
    
    @abstractmethod
    def save_chat_message(self, message: Chat) -> None:
        """Save a chat message."""
        pass

    

    # @abstractmethod
    # def save_customer_details(self, customer_details: CustomerDetails) -> None:
    #     """Save customer details."""
    
    
