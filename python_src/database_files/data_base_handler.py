""" This file creates the interface for databases"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DatabaseMain(ABC):
    """Abstract class to manage databases.

    Methods:
        - login()               - responsible for login to database
        - connection()          - responsible for connecting with database
        - cursor()              - responsible for creating cursor to database
        - create_database()     - responsible for creating database
        - create_table()        - responsible for creating table in database
        - insert_into_table()   - responsible for insert data into table
    """

    @abstractmethod
    def login(self, **kwargs) -> DatabaseMain:
        """Abstract method to log to database with specific credentials.

        :param kwargs: credentials needed to log into databases
        :return: DatabaseMain object
        """

        pass

    @abstractmethod
    def connection(self) -> Any:
        """Abstract method to connect with database.

        :return: any object
        """

        pass

    @abstractmethod
    def cursor(self) -> Any:
        """Abstract method to create a cursor.

        :return: any object
        """

        pass

    @abstractmethod
    def create_database(self, database_name: str) -> DatabaseMain:
        """Abstract method to create database.

        :param database_name: nome of database
        :return: DatabaseMain object
        """

        pass

    @abstractmethod
    def create_table(self, table_name: str, **kwargs) -> DatabaseMain:
        """Abstract method to create table.

        :param table_name: name of table
        :param kwargs: names of columns with types for sqlite3 and without types for mysql
        :return: DatabaseMain object
        """

        pass

    @abstractmethod
    def insert_into_table(self, table_name: str, **kwargs) -> DatabaseMain:
        """Abstract method to insert data to table.

        :param table_name: name of table
        :param kwargs: names of columns with values
        :return: DatabaseMain object
        """

        pass
