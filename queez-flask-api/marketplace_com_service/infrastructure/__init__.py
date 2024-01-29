
from .orm_mapper.hierarchicaldata_mapper import Base as HierarchicalDataOrm
from .orm_mapper.filter_mapper import Base as FilterOrm

from .orm_mapper.sys_keys_mapper import Base as Sys_keyOrm


from .orm_mapper.add_pkg_mapper import Base as AdvertisementPackage_Orm
from .orm_mapper.customer_mapper import Base as Customer_Orm

from .orm_mapper.add_header_mapper import Base as AdvertisementHeader_Orm
from .orm_mapper.add_detail_mapper import Base as AdvertisementDetails_Orm
from .orm_mapper.image_mapper import Base as ImageDetails_Orm
from .orm_mapper.workflow_mapper import Base as WorkflowHistory_Orm
from .orm_mapper.pinned_items_mapper import Base
from .orm_mapper.saved_filters_mapper import Base
# from .orm_mapper.chat_mapper import Base

# from .db_settings.mysql_database_orm import Base
from .db_settings.mysql_database_orm import  engine

from sqlalchemy.orm import sessionmaker


HierarchicalDataOrm.metadata.create_all(bind=engine)
# header_mapper.metadata.create_all(bind=engine)
# detail_mapper.metadata.create_all(bind=engine)
# image_mapper.metadata.create_all(bind=engine)
# sys_keys_mapper.metadata.create_all(bind=engine)
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine) 
session = Session() 



# HierarchicalDataMapper.create_table()
# FilterMapper.create_table()
# Sys_key_Mapper.create_table()
# HeaderTableMapper.create_table()
# DetailTableMapper.create_table()
# ImageTableMapper.create_table()

# Import necessary classes and methods


# Create tables in the correct order to avoid dependency issues



