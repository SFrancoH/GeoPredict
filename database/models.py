from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from database.connection import engine


Base = automap_base()
Base.prepare(engine, reflect=True)

metadata = MetaData()
metadata.reflect(bind=engine)

for Tables in metadata.tables.keys():
    print(Tables)