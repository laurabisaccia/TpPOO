import pandas as pd
from peewee import *

database = SqliteDatabase('obras_urbanas.db')

class GestionarObra:
    @classmethod
    def extraer_datos(cls, dataset_path):
       
        df = pd.read_csv(dataset_path)
        print(df.head()) 
       
        return df

    @classmethod
    def conectar_db(cls):
        database.connect()
        print("Conexión a la base de datos establecida.")
        return database