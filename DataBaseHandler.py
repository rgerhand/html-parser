""" This file creates the interface for databases"""
from abc import abstractmethod, ABC
from typing import Any

"""
    DatabaseMain class

        Methods:
            - login()               - responsible for login to database
            - connection()          - responsible for connection with database
            - cursor()              - responsible for creating cursor to database
            - create_database()     - responsible for creating database
            - create_table()        - responsible for creating table
            - insert_into_table()   - responsible for insert data into table
"""


class DatabaseMain(ABC):
    """ Database interface class"""

    @abstractmethod
    def login(self, **kwargs) -> Any:
        """ Method to login with database"""
        pass

    @abstractmethod
    def connection(self) -> Any:
        """ Method to connect with database"""
        pass

    @abstractmethod
    def cursor(self) -> Any:
        """ Method to create a cursor"""
        pass

    @abstractmethod
    def create_database(self, database_name: str) -> None:
        """ Method to create database"""
        pass

    @abstractmethod
    def create_table(self, table_name: str, **kwargs) -> None:
        """ Method to create table"""
        pass

    @abstractmethod
    def insert_into_table(self, table_name: str, *args) -> None:
        """ Method to insert data into table"""
        pass
