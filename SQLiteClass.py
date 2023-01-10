import sqlite3
from DataBaseHandler import DatabaseMain


class SqliteClass(DatabaseMain):
    """ SQLITE Class"""
    def __init__(self, database_name=None):
        """Sending parameters to create a base and table"""
        self._con = None
        if database_name != None:
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

#TODO: **kwargs
    def create_table(self, table_name, **kwargs):
        """ Create table with two rows"""
        self.cursor.execute(f"CREATE TABLE {table_name}(country text, population text)")

#TODO: **kwargs
    def insert_into_table(self, table_name):
        """ Insert data into table"""
        table_name = SqliteClass.create_table
        sql_formula = f'''
                INSERT INTO {table_name} (country, population) VALUES (?,?)'''
        test1 = ('test1', '12321')
        self.cursor.execute(sql_formula, test1)
        self.con.commit()

#TODO: switch database
#TODO: fluent pattern


sqlite1 = SqliteClass()
sqlite1.create_database = 'testSET.db'
#sqlite1.create_table("test2")
#sqlite1.create_table("test2")
#sqlite1.insert_into_table("test2")
#sqlite1.create_database("test1")
#sqlite1.create_table("world")
