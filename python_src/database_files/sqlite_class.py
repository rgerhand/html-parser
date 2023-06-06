""" This file is responsible for operations executed on sqlite3 database"""
from __future__ import annotations

import sqlite3

from python_src.database_files.data_base_handler import DatabaseMain

"""
    SqliteClass class
        
        Methods:
            - login()               - responsible for login to database
            - connection()          - responsible for connecting with database
            - cursor()              - responsible for creating cursor to database
            - create_database()     - responsible for creating database
            - create_table()        - responsible for creating table in database
            - insert_into_table()   - responsible for insert data into table
"""


class SqliteClass(DatabaseMain):
    """SqliteClass class #TODO
    Methods:
        - login()               - responsible for login to database
        - connection()          - responsible for connecting with database
        - cursor()              - responsible for creating cursor to database
        - create_database()     - responsible for creating database
        - create_table()        - responsible for creating table in database
        - insert_into_table()   - responsible for insert data into table
    """

    def login(self, **kwargs) -> True:
        """Login to database"""
        pass

    @property
    def connection(self) -> sqlite3.Connection:
        """Connection method"""
        return self._con

    @property
    def cursor(self) -> sqlite3.Cursor:
        """Cursor to database"""
        return self.connection.cursor()

    def create_database(self, database_name: str) -> SqliteClass:
        """

        :param database_name:
        :return:
        """
        self._con = sqlite3.connect(database_name)
        return self

    def create_table(self, table_name: str, *args) -> SqliteClass:
        """Create a table with unlimited number of  columns"""
        columns = ",".join(args)
        self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        return self

    def insert_into_table(self, table_name: str, **kwargs) -> SqliteClass:
        """Insert data into table"""
        numbers_of_value = len(kwargs.values())
        marks = "?" * numbers_of_value
        sql_formula = f"INSERT INTO {table_name} ({', '.join(kwargs.keys())}) VALUES ({', '.join(marks)})"
        date_to_insert = ",".join(kwargs.values()).split(",")
        self.cursor.execute(sql_formula, date_to_insert)
        self.connection.commit()
        return self


# sqlite1 = SqliteClass()
# sqlite1.create_database('new_db.db').insert_into_table('table_1', col_1='test_55', col_2='test_55')
