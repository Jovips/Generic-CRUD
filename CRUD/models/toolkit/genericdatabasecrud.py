import sqlite3 as sql
from ..configs.database_access_configs import DB_CREDENCIAIS

class GenericDatabaseCRUD : # alterar o nome do seu CRUD

    def __init__(self, db_name: str, db_user: str, db_pass: str) -> None:

        self.db_name = db_name 
        self.db_user = db_user 
        self.db_pass = db_pass 

        self.db_conn = None    
        self.db_cursor = None  
    

    def login(self) -> bool:

        if self.db_user == DB_CREDENCIAIS['USERNAME'] and  DB_CREDENCIAIS['PASSWORD'] == self.db_pass:
            return True
    

    def connect(self) -> bool:

        if self.login():
            self.db_conn = sql.connect(self.db_name)
            self.db_cursor = self.db_conn.cursor()
            return True
    

    def disconnect(self) -> None:

        if self.connect():
            self.db_conn.close()

    
    def create(self, table_name: str, sql_query: str) -> None:

        if self.connect():
            self.db_cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} ({sql_query})"
            )
            self.db_conn.commit()
            self.disconnect()
    

    def delete(self, table_name: str) -> None:

        if self.connect():
            self.db_cursor.execute(
                f"DROP TABLE {table_name}"
            )
            self.db_conn.commit()
            self.disconnect()


    def get_tables_from_database(self) -> tuple:

        if self.connect():
            tables = self.db_cursor.execute(
                "SELECT * FROM sqlite_master WHERE type='table'"
            ).fetchall()
            self.db_conn.commit()
            self.disconnect()

            return tuple([table_name[1] for table_name in tables])
    

    def get_columns_from(self, table_name: str) -> tuple:

        if self.connect():
            columns = self.db_cursor.execute(
                f"SELECT * FROM {table_name}"
            ).description
            self.db_conn.commit()
            self.disconnect()

            return tuple([column[0] for column in columns])
    

 

    def insert(self, values: tuple, table_name: str) -> None:

        
        columns = self.get_columns_from(table_name)[1:]
        
        if self.connect():
            self.db_cursor.execute(
                f"INSERT INTO {table_name} {columns} VALUES {values}"
            )
            self.db_conn.commit()
            self.disconnect()
    

    def select_by_id(self, id: int, table_name: str) -> list[tuple[any]]:

        if self.connect():
            data = self.db_cursor.execute(
                f"SELECT * FROM {table_name} WHERE id={id}"
            ).fetchall()
            self.disconnect()

            return data

    
    def select_all_from(self, table_name: str) -> list[tuple[any]]:

        if self.connect():
            data = self.db_cursor.execute(
                f"SELECT * FROM {table_name}"
            ).fetchall()
            self.disconnect()

            return data
    

    def update_cell_by_id(self, cell_name: str, value: any, id: int, table_name: str) -> None:

        if self.connect():
            self.db_cursor.execute(
                f"UPDATE {table_name} SET {cell_name}={value} WHERE id={id}"
            )
            self.db_conn.commit()
            self.disconnect()
    

    def delete_data(self, id: int, table_name: str) -> None:

        if self.connect():
            self.db_cursor.execute(
                f"DELETE FROM {table_name} WHERE id={id}"
            )
            self.db_conn.commit()
            self.disconnect()
    

    def delete_all_from(self, table_name: str) -> None:
 
        if self.connect():
            self.db_cursor.execute(
                f"DELETE FROM {table_name}"
            )
            self.db_conn.commit()
            self.disconnect()
