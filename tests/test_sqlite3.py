""" This file is responsible for SQLite3 tests"""
import pytest
from unittest.mock import Mock, patch
from SQLiteClass import SqliteClass


class TestSQLite:
    @pytest.fixture()
    def sqlite3_object(self):
        db = SqliteClass()
        return db

    def test_login(self, sqlite3_object):
        result = sqlite3_object.login()
        assert result.assert_called()

    @patch('SQLiteClass.sqlite3.connect')
    def test_connection(self, mock_connection):
        """ Method to test the connection """
        obj_1 = SqliteClass()
        result = obj_1.login()
        assert result == mock_connection


    def test_cursor(self, sqlite3_object):
        """ Method to test the cursor """
        assert sqlite3_object.cursor() == sqlite3_object.connection().return_value()

    @patch('SQLiteClass.sqlite3.connect')
    def test_create_database(self, mock_create_database):
        """ Method to test the creation of database """
        obj_1 = SqliteClass()
        result = obj_1.create_database('test_1')
        mock_create_database.assert_called_once_with('test_1')


# TODO
def test_create_table(database):
    """ Method to test the creation of table """
    database.create_table('test_table', 'test_kol_1', 'test_kol_2')
    tables_names = database.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    tables = tables_names.fetchall()
    print(tables)

