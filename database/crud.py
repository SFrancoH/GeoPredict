from sqlalchemy.orm import Session
from database.connection import DatabaseConnection

class CRUD:

    def __init__(self, db_connection: DatabaseConnection):
        #Inicializa el CRUD con la conexión a la base de datos.
        self.db_connection = db_connection
        self.metadata = db_connection.metadata

    def get_table_names(self):
        #Obtiene los nombres de las tablas en la base de datos.
        return list(self.metadata.tables.keys())

    def get_columns_names(self, table_names):
        #Obtiene los nombres de las columnas de una tabla específica.
        if isinstance(table_names, str):  # Si es un solo nombre, convertirlo en lista
           table_names = [table_names]

        result = {}
        for table_name in table_names:
            if table_name in self.metadata.tables:
               table = self.metadata.tables[table_name]
               result[table_name] = [{"name": column.name, "type": str(column.type)} for column in table.columns]
            else:
               print(f" La tabla '{table_name}' no existe en la base de datos.")
               result[table_name] = None  # Se marca como `None` si la tabla no existe
        
        return result



    def get_all(self, table_name):
        #Obtiene todos los registros de una tabla específica.
        with self.db_connection.get_session() as session:
            table = self.metadata.tables.get(table_name)
            if table is None:
                print("La tabla no existe.")
                return []
            else:
                rows = session.query(table).all()
                dict_rows = [row._asdict() for row in rows]
                return dict_rows

    def insert(self, table_name, data):
        #Inserta un nuevo registro en la tabla especificada.
        with self.db_connection.get_session() as session:
            table = self.metadata.tables.get(table_name)
            if table is None:
                print("La tabla no existe.")
            else:
                insert_stmt = table.insert().values(**data)
                session.execute(insert_stmt)
                session.commit()

    def update(self, table_name, record_id, updated_data):
        #Actualiza un registro en la tabla especificada.
        with self.db_connection.get_session() as session:
            table = self.metadata.tables.get(table_name)
            if table is None:
                print("La tabla no existe.")
            else:
                update_stmt = table.update().where(table.c.id == record_id).values(**updated_data)
                session.execute(update_stmt)
                session.commit()

    def delete(self, table_name, record_id):
        #Elimina un registro de la tabla especificada
        with self.db_connection.get_session() as session:
            table = self.metadata.tables.get(table_name)
            if table is None:
                print("La tabla no existe.")
            else:
                delete_stmt = table.delete().where(table.c.id == record_id)
                session.execute(delete_stmt)
                session.commit()

