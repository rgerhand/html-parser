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
            - insert_into_table()       - responsible for insert data into table 
"""


class MySQL(DatabaseMain):
    """ MySQL Class"""
    def login(self, host: str, user: str, passwd: str, database: str = ''):
        """ Login to database"""
        self._connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
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

    def create_database(self, database_name: str):
        """ Create the database"""
        self.cursor.execute(f"CREATE DATABASE {database_name}")
        return self

    def create_table(self, table_name: str, **kwargs: dict):
        """ Create a table with unlimited number of  columns"""
        columns_with_type = ','.join(f'{column} {column_type}' for column, column_type in kwargs.items())
        sql_formula = f'CREATE TABLE {table_name} ({columns_with_type})'
        self.cursor.execute(sql_formula)
        return self

    def insert_into_table(self, table_name, *args):
        """ Insert data into table"""
        data_to_insert = list(input("Insert data: ").split(','))
        string_with_data = ''
        for element in data_to_insert:
            string_with_data += "\'" + element + "\'" + ','
        without_last_char = string_with_data[:-1]
        columns = ', '.join(args)
        sql_formula = f'INSERT INTO {table_name} ({columns}) VALUES ({without_last_char})'
        self.cursor.execute(sql_formula)
        self.connection.commit()
        return self


mysql1 = MySQL()
mysql1.login(host='localhost', user='root', passwd='1234Pass', database='input').insert_into_table('table1', 'name',
                                                                                                   'surname')
