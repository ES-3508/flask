from .orm_mapper.filter_mapper import FilterMapper
from .orm_mapper.hierarchicaldata_mapper import HierarchicalDataMapper
from .orm_mapper.sys_keys_mapper import Sys_key_Mapper

Sys_key_Mapper.create_table()
HierarchicalDataMapper.create_table()
FilterMapper.create_table()

