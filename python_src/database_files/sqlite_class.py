""" This file is responsible for operations executed on sqlite3 database"""
from __future__ import annotations

import sqlite3

from python_src.database_files.data_base_handler import DatabaseMain


class SqliteClass(DatabaseMain):
    """A class used to manage sqlite3 database.

    The class contains all the necessary methods to manage a simple database.
    """

    def login(self, **kwargs) -> True:
        """Login to database.

        :param kwargs:
        :return: True
        """

        pass

    @property
    def connection(self) -> sqlite3.Connection:
        """Connection method.

        :return: sqlite3.Connection
        """

        return self._con

    @property
    def cursor(self) -> sqlite3.Cursor:
        """Cursor to database.

        Cursor function allows to execute sql commands

        :return: sqlite3.Cursor
        """

        return self.connection.cursor()

    def create_database(self, database_name: str) -> SqliteClass:
        """Create a new database.

        :param database_name: name of database
        :return: SqliteClass object
        """

        self._con = sqlite3.connect(database_name)
        return self

    def create_table(self, table_name: str, *args) -> SqliteClass:
        """Create a table with unlimited number of columns.

        :param table_name: name of table
        :param args: name of columns
        :return: SqliteClass object
        """

        columns = ",".join(args)
        self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        return self

    def insert_into_table(self, table_name: str, **kwargs) -> SqliteClass:
        """Insert data into table.

        :param table_name: name of table
        :param kwargs: column names with values
        :return: SqliteClass object
        """

        numbers_of_value = len(kwargs.values())
        marks = "?" * numbers_of_value
        sql_formula = f"INSERT INTO {table_name} ({', '.join(kwargs.keys())}) VALUES ({', '.join(marks)})"
        date_to_insert = ",".join(kwargs.values()).split(",")
        self.cursor.execute(sql_formula, date_to_insert)
        self.connection.commit()
        return self


if __name__ == '__main__':
    sqlite1 = SqliteClass()
    sqlite1.create_database('new_db.db').insert_into_table('table_1', col_1='test_55', col_2='test_55')
