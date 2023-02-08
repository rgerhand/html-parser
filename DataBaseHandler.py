""" This file creates the interface for databases"""
from abc import abstractmethod, ABC

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
    def login(self, **kwargs) -> True:
        """ Method to login with database"""
        pass

    @abstractmethod
    def connection(self) -> True:
        """ Method to connect with database"""
        pass

    @abstractmethod
    def cursor(self) -> True:
        """ Method to create a cursor"""
        pass

    @abstractmethod
    def create_database(self, database_name: str) -> True:
        """ Method to create database"""
        pass

    @abstractmethod
    def create_table(self, table_name: str, **kwargs) -> True:
        """ Method to create table"""
        pass

    @abstractmethod
    def insert_into_table(self, table_name: str, *args) -> True:
        """ Method to insert data into table"""
        pass
