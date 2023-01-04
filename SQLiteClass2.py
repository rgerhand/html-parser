import sqlite3
from DataBaseHandler import DatabaseMain


class SqliteClass2(DatabaseMain):
    """ SQLITE Class"""

    def login(self, **kwargs):
        """ Login to database"""
        pass

    def create_database(self, database_name):
        """Create new database"""
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

    def create_table(self, table_name, columns):
        """ Create table with two rows"""
        sql_create_table_formula = f"CREATE TABLE {table_name}({columns})"
        self.cursor.execute(sql_create_table_formula)
        self.connect.commit()

    def insert_into_table(self, table_name, columns):
        """ Insert data into table"""
        sql_formula_to_insert = f'''
                INSERT INTO {table_name} ({columns}) VALUES (?,?)'''
        test1 = ('test1col1', '12321col2')
        self.cursor.execute(sql_formula_to_insert, test1)
        self.connect.commit()


sqlite1 = SqliteClass2()
sqlite1.login()
sqlite1.create_database("TestDB.db")
sqlite1.create_table('table2', 'col1, col2')
sqlite1.insert_into_table('table1', 'col1, col2')
