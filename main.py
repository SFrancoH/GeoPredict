import json
from database.connection import DatabaseConnection
from database.crud import CRUD
import pandas as pd

def read_config(): 
   with open("config.json", "r") as file:
      config = json.load(file)
   return config
    

def main():
   config = read_config()
   censo_db = DatabaseConnection(config["censo_db"])
   crud = CRUD(censo_db)
   print(crud.get_table_names())
   print(crud.get_columns_names(crud.get_table_names()))
   censo_pd = pd.DataFrame(crud.get_all("audiencias"))
   print(censo_pd)


if __name__ == '__main__':
    main()