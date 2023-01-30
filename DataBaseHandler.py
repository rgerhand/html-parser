""" This file created and interface for databases"""
from abc import abstractmethod, ABC

"""
    DatabaseMain class

        Methods:
            - login()               - responsible for login to database
            - create_database()     - responsible for creating database
"""


class DatabaseMain(ABC):
    """ Database interface class"""
    @abstractmethod
    def login(self, **kwargs: dict) -> True:
        """ This is abstract login method"""
        pass

    @abstractmethod
    def create_database(self, database_name: str) -> True:
        """ This is abstract create database method"""
        pass
