from sqlalchemy import text
from ..infrastructure.db_settings.mysql_database_orm  import db_context_orm
from ..infra.logger import log_exceptions
from ..domain.sql_quary import SqlQuary


class SelectQuaryRunner:
    def __init__(self):
        self.db = db_context_orm  # Database context

    @log_exceptions
    def run_sql_select_query_string(sql_object,values_array):
        query = text(sql_object.sql_string)
        param_value_dict = dict(zip(sql_object.filter_para, values_array))
        result = db_context_orm.execute(query, param_value_dict)
        data = result.fetchone()
        if data:
            return data

        return None
    
    @log_exceptions
    def fetch_run_sql_select_query_string(query_code,values_array):
        sql_object=SelectQuaryRunner.get_query_by_code(query_code)
        query = text(sql_object.sql_string)
        param_value_dict = dict(zip(sql_object.filter_para, values_array))
        result = db_context_orm.execute(query, param_value_dict)
        data = result.fetchone()
        if data:
            return data

        return None
    
    @log_exceptions
    def get_query_by_code(query_code):
        query = text("SELECT sql_string,display_field,query_filter,filter_para FROM sys_query_string WHERE query_code = :query_code ")
        result = db_context_orm.execute(query, {"query_code": query_code })
        data = result.fetchone()

        if data:
            sql_string,display_field,query_filter,filter_para = data
            sql_string = sql_string.replace("@", display_field)
            sql = f"{sql_string}  {query_filter}"
            parameters = filter_para.split(",")
            filtered_array = list(filter(None, parameters))
            sqlQuary = SqlQuary(
                sql_string=sql,
                filter_para=filtered_array
            )
            return sqlQuary

        return None