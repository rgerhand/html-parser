import sqlite3
from DataBaseHandler import DatabaseMain


class SqliteClass(DatabaseMain):
    """ SQLITE Class"""
    def __init__(self, database_name, table_name):
        """Sending parameters to create a base and table"""
        self.con = sqlite3.connect(database_name)
        self.table_name = table_name

    def login(self, **kwargs):
        """ Login to database"""
        pass

    def create_database(self, database_name):
        """Create new database"""
        pass

    def create_table(self):
        """ Create table with two rows"""
        cur = self.con.cursor()
        cur.execute(f"CREATE TABLE {self.table_name}(country text, population text)")

    def insert_into_table(self):
        """ Insert data into table"""
        cur = self.con.cursor()
        sql_formula = f'''
                INSERT INTO {self.table_name} (country, population) VALUES (?,?)'''
        test1 = ('test1', '12321')
        cur.execute(sql_formula, test1)
        self.con.commit()


sqlite1 = SqliteClass('test2.db', 'tabela1')
sqlite1.login()
sqlite1.create_table()
sqlite1.insert_into_table()
#sqlite1.create_database("test1")
#sqlite1.create_table("world")
