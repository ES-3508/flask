
from ..db_settings.mysql_database_orm import Session
from ...domain.features.customer_portal.repositories.i_customerportal_command_repository import ICustomerportalCommandRepository
from ..orm_mapper.pinned_items_mapper import CustomerPinnedItems
from ...domain.features.customer_portal.aggregates.pinnedItems import PinnedItems

from ..orm_mapper.saved_filters_mapper import CustomerSavedFilters
from ...domain.features.customer_portal.aggregates.savedfilters import SavedFilters
from ..db_settings.mysql_database_orm import db_context_orm, Session
from ...domain.features.customer_portal.aggregates.chat import Chat
from ..orm_mapper.chat_mapper import ChatOrm


class CustomerportalCommandRepository(ICustomerportalCommandRepository):
    def __init__(self):
        self.db = db_context_orm

    def save_pinned_item(self, pinned_item: PinnedItems) -> None:
        session = Session() 
        customer_pinned_item = CustomerPinnedItems(
            customer_id=pinned_item.customer_id,
            add_id=pinned_item.add_id
        )
        session.add(customer_pinned_item)
        session.commit()


    def save_saved_filter(self, saved_filter: SavedFilters) -> None:
        session = Session()
        customer_saved_filter = CustomerSavedFilters(
            customer_id=saved_filter.customer_id,
            filter_id=saved_filter.filter_id,
            value=saved_filter.value
        )
        session.add(customer_saved_filter)
        session.commit()
        
    def save_chat_message(self, chat: Chat) -> None:
        session = Session()
        chat_message = ChatOrm(
            sender_id=chat.sender_id,
            receiver_id=chat.receiver_id,
            message=chat.message
        )
        session.add(chat_message)
        session.commit()
      

    # def save_customer_details(self, customer_details: CustomerDetails) -> None:
    #     try:
    #         customer_orm = Customer_Orm(
    #             customer_id=customer_details.customer_id,
    #             name=customer_details.name,
    #             sys_user_id=customer_details.sys_user_id
    #         )
    #         self.session.add(customer_orm)
    #         self.session.commit()
    #     except Exception as e:
    #         raise CustomerDetailsError(f"Error saving customer details: {str(e)}")
