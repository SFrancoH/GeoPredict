from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker 

class DatabaseConnection:
    
    def __init__(self, db_url):
        # Inicializa la conexión a la base de datos especificada en db_url

        self.db_url = db_url 
        self.engine = create_engine(self.db_url, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine) 

        # Mapeo automático de las tablas de la base de datos a objetos de Python
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        
        # Cargar metadatos
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    def get_session(self): 
        return self.SessionLocal()

    def close_session(self):
        self.engine.dispose()
