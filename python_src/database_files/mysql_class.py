"""This file is responsible for operations executed on MySQL database."""
from __future__ import annotations

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from python_src.database_files.data_base_handler import DatabaseMain


class MySQL(DatabaseMain):
    """A class used to manage MySQL database.

    The class contains all the necessary methods to manage a simple database.
    """

    def __init__(self):
        """Initializes a 'MySQL' instance."""

        self._connection: MySQLConnection | None = None

    def login(self, host: str, user: str, passwd: str, database: str = "") -> MySQL:
        """Login to database with specific credential.

        :param host: database hostname
        :param user: database username
        :param passwd: password to database
        :param database: name of database
        :return: MySQL object
        """

        self._connection = mysql.connector.connect(
            host=host, user=user, passwd=passwd, database=database
        )
        return self

    @property
    def connection(self) -> MySQLConnection:
        """Connection method.

        :return: MySQLConnection object
        """

        return self._connection

    @property
    def cursor(self) -> MySQLCursor:
        """Cursor to database.

        Cursor function allows to execute sql commands

        :return: MySQLCursor object
        """

        return self.connection.cursor()

    def create_database(self, database_name: str) -> MySQL:
        """Create a new database.

        :param database_name: name of database
        :return: MySQL object
        """

        self.cursor.execute(f"CREATE DATABASE {database_name}")
        return self

    def create_table(self, table_name: str, **kwargs) -> MySQL:
        """Create a table with unlimited number of  columns.

        :param table_name: name of table
        :param kwargs: name of columns with column type
        :return: MySQL object
        """

        columns_with_type = ", ".join(
            f"{column} {column_type}" for column, column_type in kwargs.items()
        )
        print(columns_with_type)
        sql_formula = f"CREATE TABLE {table_name} ({columns_with_type})"
        print(sql_formula)
        self.cursor.execute(sql_formula)
        return self

    def insert_into_table(self, table_name: str, **kwargs) -> MySQL:
        """Insert data into table.

        :param table_name: name of table
        :param kwargs: name of columns and value
        :return: MySQL object
        """

        data = []
        for value in kwargs.values():
            data.append(f"{value}" if isinstance(value, (int, float)) else f"'{value}'")
        sql_formula = f"INSERT INTO {table_name} ({', '.join(kwargs.keys())}) VALUES ({', '.join(data)})"
        print(sql_formula)
        self.cursor.execute(sql_formula)
        self.connection.commit()
        return self


if __name__ == "__main__":
    mysql1 = MySQL()
    mysql1.login(
        host="localhost", user="root", passwd="1234Pass", database="input"
    ).insert_into_table("table7", col_1="ola", col_2="m")
