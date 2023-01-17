import sqlite3
from DataBaseHandler import DatabaseMain

"""
    SqliteClass class
        
        Methods:
            - __init__()            - responsible for SqliteClass class initialization
            - login()               - responsible for login to database
            - con()                 - responsible for connecting with database
            - cursor()              - responsible for creating cursor with database
            - create_database()     - responsible for creating database
            - create_table()        - responsible for creating table in database
            - insert_into_table()   - responsible for insert data into table
"""


class SqliteClass(DatabaseMain):
    """ SQLITE Class"""
    def __init__(self, database_name=None):
        """Sending parameters to create a database"""
        self._con = None
        if database_name is not None:
            self.create_database(database_name)

    def login(self, **kwargs):
        """ Login to database"""
        pass

    @property
    def con(self):
        """ Connection method"""
        return self._con

    @property
    def cursor(self):
        """ Cursor to database"""
        return self.con.cursor()

    def create_database(self, database_name_set):
        """Set database name"""
        self._con = sqlite3.connect(database_name_set)
        return self

    def create_table(self, table_name, *args):
        """ Create a table with unlimited number of  columns"""
        columns = ','.join(args)
        self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        return self

    def insert_into_table(self, table_name, *args):
        """ Insert data into table"""
        data_to_insert = input('Podaj dane: ').split(',')
        numbers_of_data = len(data_to_insert)
        without_first_char = numbers_of_data - 1
        data = '?' + ' ' + without_first_char * ',?'
        columns = ','.join(args)
        sql_formula = f'''
                INSERT INTO {table_name} ({columns}) VALUES ({data})'''
        self.cursor.execute(sql_formula, data_to_insert)
        self.con.commit()
        return self


sqlite1 = SqliteClass()
sqlite1.create_database('testDB1.db').insert_into_table('table4', 'test1', 'test2')
