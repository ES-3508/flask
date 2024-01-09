from sqlalchemy.orm import Session
from typing import List, Optional
from ...domain.features.customer_portal.repositories.i_customerportal_query_ropository import ICustomerportalQueryRepository
from ..orm_mapper.pinned_items_mapper import CustomerPinnedItems
from ...domain.features.customer_portal.aggregates.pinnedItems import PinnedItems
from ..orm_mapper.saved_filters_mapper import CustomerSavedFilters
from ...domain.features.customer_portal.aggregates.savedfilters import SavedFilters
from ..db_settings.mysql_database_orm import db_context_orm
from ..db_settings.mysql_database_orm import Session

class CustomerportalQueryRepository(ICustomerportalQueryRepository):
    def __init__(self):
        self.db = db_context_orm

    def get_pinned_items_by_customer_id(self, customer_id: int) -> List[PinnedItems]:
        session = Session()
        customer_pinned_items = (
            session.query(CustomerPinnedItems)
            .filter_by(customer_id=customer_id)
            .all()
        )
        return customer_pinned_items

    def get_saved_filters_by_customer_id(self, customer_id: int) -> List[SavedFilters]:
        session = Session()
        customer_saved_filters = (
            session.query(CustomerSavedFilters)
            .filter_by(customer_id=customer_id)
            .all()
        )
        return [
            SavedFilters(customer_id=item.customer_id, filter_id=item.filter_id, value=item.value)
            for item in customer_saved_filters
        ]

    # def get_customer_details_by_id(self, customer_id: int) -> Optional[CustomerDetails]:
    #     customer_orm = (
    #         self.session.query(Customer_Orm)
    #         .filter_by(customer_id=customer_id)
    #         .first()
    #     )
    #     if customer_orm:
    #         return CustomerDetails(
    #             customer_id=customer_orm.customer_id,
    #             name=customer_orm.name,
    #             sys_user_id=customer_orm.sys_user_id
    #         )
    #     return None
