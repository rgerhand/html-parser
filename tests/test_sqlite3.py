""" This file is responsible for SQLite3 tests"""
import pytest
from unittest.mock import patch
from python_src.database_files.sqlite_class import SqliteClass, sqlite3


class TestSQLite:
    @pytest.fixture()
    def sqlite3_object(self):
        db = SqliteClass()
        return db

    @pytest.fixture()
    def sqlite3_connected(self, mocker, sqlite3_object):
        mocker.patch("python_src.database_files.sqlite_class.sqlite3.connect")
        sqlite3_object.create_database("Database_1")
        return sqlite3_object

    def test_connection(self, sqlite3_connected):
        """Method to test the connection"""
        assert sqlite3_connected.connection == sqlite3.connect.return_value

    def test_cursor(self, sqlite3_connected):
        """Method to test the cursor"""
        assert (
            sqlite3_connected.cursor == sqlite3.connect.return_value.cursor.return_value
        )

    @patch("python_src.database_files.sqlite_class.sqlite3.connect")
    def test_create_database(self, mock_connect, sqlite3_object):
        """Method to test the creation of database"""
        assert sqlite3_object.create_database("Database_1") == sqlite3_object
        mock_connect.assert_called_once_with("Database_1")

    # TODO add pytest.parametrize
    def test_create_table(self, sqlite3_connected):
        """Method to test the creation of table"""
        assert (
            sqlite3_connected.create_table("Table_1", "col_1", "col_2")
            == sqlite3_connected
        )
        sqlite3_connected.cursor.execute.assert_called_once_with(
            "CREATE TABLE Table_1 (col_1,col_2)"
        )

    # TODO delate input from basic method
    def test_insert_table(self, sqlite3_connected):
        """Method to test the creation of database"""
        sqlite3_connected.insert_into_table(
            "Database_1", col_1="test_55", col_2="test_22"
        )
