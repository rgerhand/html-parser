""" This file is responsible for mySQL tests"""
import pytest
from unittest.mock import MagicMock, patch
from MySQLClass import MySQL


# TODO
class MySQLTest:
    """ Method to test the connection """
    def test_connection(self):
        database_mock = MagicMock(spec=MySQL)
        database_mock.user = "test"
        database_mock.password = "test"
        database_mock.host = "localhost"
        database_mock.database_name = "testdb"
