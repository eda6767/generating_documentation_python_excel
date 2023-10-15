# -*- coding: utf-8 -*-

class Connector:
    def __init__(self, dsn, user, data=None ):
        self.dsn = dsn
        self.user = user
        self.data = data
        

    def __str__(self):
        return "dsn {}, data{}".format(self.dsn, self.data)

    def connect_database(self):
        import getpass
        import pandas as pd
        import cx_Oracle
        
        def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
            if defaultType == cx_Oracle.CLOB:
                return cursor.var(cx_Oracle.LONG_STRING, arraysize=cursor.arraysize)
            if defaultType == cx_Oracle.BLOB:
                return cursor.var(cx_Oracle.LONG_BINARY, arraysize=cursor.arraysize)
        
        print("Connecting to Oracle Database")
        userpwd = getpass.getpass('Password:')
        connection = cx_Oracle.connect(self.user, password=userpwd, dsn=self.dsn)
        connection.outputtypehandler = OutputTypeHandler
        query = connection.cursor()
        rs=query.execute("select metric, area_name, target_table, metric_id, description, metric_type, \
                         simple_metric, metric_version_id, function, grouping_key, source_table, \
                         custom_sql_file, expression, where_condition, \
                         status from agr_44.metric_definition_list")


        global METRICS
        METRICS=pd.DataFrame(rs.fetchall())
        col_names=[]
        for i in range(0, len(query.description)):
            col_names.append(query.description[i][0])
        METRICS.columns=col_names

        self.data = METRICS
        print(METRICS)
        connection.close()
        print("Connection with database - closed")
        

if __name__ == "__connect_database__":
    pass



