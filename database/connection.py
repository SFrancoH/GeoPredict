from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker

import json

with open('config.json', 'r') as file:
    data = json.load(file)

engine = create_engine(f"sqlite:///{data["censo_db"]}",echo=True)
Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
         