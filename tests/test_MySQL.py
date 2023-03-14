""" This file is responsible for mySQL tests"""
import pytest
from unittest.mock import Mock, patch
from MySQLClass import MySQL


# TODO
class MySQLTest:
    @patch('MySQLClass.MySQL.login')
    def test_connection(self, mock_db):
        """ Method to test the connection """
        mock_db.return_value = 'MySQLConnection'
        result = MySQL.login()
        assert result == 'MySQLConnection'

    @patch('MySQLClass.MySQL.cursor')
    def test_cursor(self, mock_cursor):
        """ Method to test the cursor """
        mock_cursor.return_value = 'MySQLCursor'
        result = MySQL.cursor()
        assert result == 'MySQLCursor'


inst = MySQLTest()
inst.test_cursor()



