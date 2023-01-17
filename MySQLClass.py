import mysql.connector
from DataBaseHandler import DatabaseMain

"""
    MySQL class
    
        Methods:
            - login()                   - responsible for login to database
            - connection()              - responsible for creating connection
            - cursor()                  - responsible for creating cursor to database
            - create_database()         - responsible for creating database
            - create_table()            - responsible for creating table in database 
"""


class MySQL(DatabaseMain):
    """ MySQL Class"""
    def login(self, **kwargs):
        """ Login to database"""
        self._connection = mysql.connector.connect(
            host=kwargs['host'],
            user=kwargs['user'],
            passwd=kwargs['passwd'],
            database=kwargs['database']
            )
        return self

    @property
    def connection(self):
        """ Connection method"""
        return self._connection

    @property
    def cursor(self):
        """ Cursor to database"""
        return self.connection.cursor()

    def create_database(self, database_name):
        """ Create the database"""
        self.cursor.execute(f"CREATE DATABASE {database_name}")
        return self

    def create_table(self, table_name, **kwargs):
        """ Create a table with unlimited number of  columns"""
        empty_string = ''
        for key, value in kwargs.items():
            columns_with_type = '%s %s' % (key, value)
            empty_string += columns_with_type + ','
        columns_with_type_without_last_char = empty_string[:-1]
        sql_formula = f'''CREATE TABLE {table_name} ({columns_with_type_without_last_char})'''
        self.cursor.execute(sql_formula)


mysql1 = MySQL()
mysql1.login(host='localhost', user='root', passwd='1234Pass', database='test1').create_table('table3',
                                                                                              name='VARCHAR(255)',
                                                                                              surname='VARCHAR(255)',
                                                                                              population='VARCHAR(255)')
