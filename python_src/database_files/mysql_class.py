""" This file is responsible for operations executed on MySQL database"""
from __future__ import annotations
import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from python_src.database_files.data_base_handler import DatabaseMain

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
    """MySQL Class"""

    def __init__(self):
        self._connection: MySQLConnection | None = None

    def login(self, host: str, user: str, passwd: str, database: str = "") -> MySQL:
        """Login to database"""
        self._connection = mysql.connector.connect(
            host=host, user=user, passwd=passwd, database=database
        )
        return self

    @property
    def connection(self) -> MySQLConnection:
        """Connection method"""
        return self._connection

    @property
    def cursor(self) -> MySQLCursor:
        """Cursor to database"""
        return self.connection.cursor()

    def create_database(self, database_name: str) -> MySQL:
        """Create the database"""
        self.cursor.execute(f"CREATE DATABASE {database_name}")
        return self

    def create_table(self, table_name: str, **kwargs) -> MySQL:
        """Create a table with unlimited number of  columns"""
        columns_with_type = ", ".join(
            f"{column} {column_type}" for column, column_type in kwargs.items()
        )
        print(columns_with_type)
        sql_formula = f"CREATE TABLE {table_name} ({columns_with_type})"
        print(sql_formula)
        self.cursor.execute(sql_formula)
        return self

    def insert_into_table(self, table_name: str, **kwargs) -> MySQL:
        """Insert data into table"""
        data = []
        for value in kwargs.values():
            data.append(f"{value}" if isinstance(value, (int, float)) else f"'{value}'")
        sql_formula = f"INSERT INTO {table_name} ({', '.join(kwargs.keys())}) VALUES ({', '.join(data)})"
        print(sql_formula)
        self.cursor.execute(sql_formula)
        self.connection.commit()
        return self


mysql1 = MySQL()
mysql1.login(
    host="localhost", user="root", passwd="1234Pass", database="input"
).insert_into_table("table7", col_1="ola", col_2="m")
