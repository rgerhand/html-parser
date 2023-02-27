""" This file is responsible for SQLite3 tests"""
import pytest
from SQLiteClass import *
import sqlite3


@pytest.fixture()
def database():
    """ Method to create database"""
    db = SqliteClass().create_database('test_database.db')

    return db


def test_create_database(database):
    """ Method to test the creation of database """
    assert isinstance(database.connection, sqlite3.Connection)


# TODO
def test_create_table(database):
    """ Method to test the creation of table """
    database.create_table('test_table', 'test_kol_1', 'test_kol_2')
    tables_names = database.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    tables = tables_names.fetchall()
    print(tables)

