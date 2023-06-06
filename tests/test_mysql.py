""" This file is responsible for mySQL tests"""
from unittest.mock import patch

import pytest

from python_src.database_files.mysql_class import MySQL

# pytest.markparam
#TODO edit docstring


class TestMySQL:
    @pytest.fixture()
    def mysql_object(self, mocker):
        mocker.patch("python_src.database_files.mysql_class.mysql.connector.connect")
        return MySQL().login("test", "test", "test", "test")

    @patch("python_src.database_files.mysql_class.mysql.connector.connect")
    def test_connection(self, mock_connector):
        """Method to test the connection."""
        obj = MySQL()
        result = obj.login("host11", "user11", "passw11", "data11")
        assert result == obj
        mock_connector.assert_called_once_with(
            host="host11", user="user11", passwd="passw11", database="data11"
        )

    def test_cursor(self, mysql_object):
        """Method to test the cursor"""
        assert mysql_object.cursor == mysql_object.connection.cursor.return_value
        pass

    def test_create_database(self, mysql_object):
        assert mysql_object.create_database("test_db") == mysql_object
        mysql_object.cursor.execute.assert_called_with("CREATE DATABASE test_db")
        mysql_object.cursor.execute.assert_called_once()
        mysql_object.cursor.execute.assert_called_once_with("CREATE DATABASE test_db")
        assert mysql_object.cursor.execute.call_count == 1

    @pytest.mark.parametrize(
        "table_name, col_name, expected_values",
        [
            ("Table_1", {"col_1": "TINYINT"}, "col_1 TINYINT"),
            ("Table_2", {"col_1": "SMALLINT"}, "col_1 SMALLINT"),
            ("Table_3", {"col_2": "FLOAT"}, "col_2 FLOAT"),
            (
                "Table_4",
                {
                    "col_3": "CHAR(255)",
                    "col_31": "CHAR(255)",
                    "col_32": "INT",
                    "col_33": "INT",
                },
                "col_3 CHAR(255), col_31 CHAR(255), col_32 INT, col_33 INT",
            ),
        ],
    )
    def test_create_table(self, mysql_object, table_name, col_name, expected_values):
        mysql_object.create_table(table_name, **col_name)

        expected_query = f"CREATE TABLE {table_name} ({expected_values})"

        mysql_object.cursor.execute.assert_called_with(expected_query)

    @pytest.mark.parametrize(
        "table_name, columns, expected_columns, expected_values",
        [
            ("Table_1", {"col_1": 255}, "col_1", "255"),
            (
                "Table_2",
                {"col_2": "Test_1", "col_21": 99.99, "col_22": "Test_2", "col_23": 255},
                "col_2, col_21, col_22, col_23",
                "'Test_1', 99.99, 'Test_2', 255",
            ),
            ("Table_3", {"col_3": "Test_3"}, "col_3", "'Test_3'"),
            (
                "Table_4",
                {"col_4": "Test_4", "col_41": "Test_44"},
                "col_4, col_41",
                "'Test_4', 'Test_44'",
            ),
            ("Table_5", {"col_5": 0, "col_51": 255}, "col_5, col_51", "0, 255"),
        ],
    )
    def test_insert_into_table(
        self, mysql_object, table_name, columns, expected_columns, expected_values
    ):
        mysql_object.insert_into_table(table_name, **columns)

        expected_query = (
            f"INSERT INTO {table_name} ({expected_columns}) "
            f"VALUES ({expected_values})"
        )

        mysql_object.cursor.execute.assert_called_with(expected_query)


# inst = MySQLTest()
# inst.test_connection()
