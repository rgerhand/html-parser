from abc import abstractmethod, ABC


class DatabaseMain(ABC):
    """ Database interface class"""
    @abstractmethod
    def login(self, **kwargs):
        """ This is abstract login method"""
        pass

    @abstractmethod
    def create_database(self, database_name):
        """ This is abstract create database method"""
        pass
