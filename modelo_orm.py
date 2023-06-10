from peewee import *
import os

sqlite_db = SqliteDatabase(os.getcwd()+'/'+'obras_urbanas.db', pragmas={'journal_mode': 'wal'})

try:
    sqlite_db.connect()
    #La base de datos se crea cuando intenta conectarse por primera vez y no la encuentra.
except OperationalError as e:
    print("Se ha generado un error en la conexion a la BD.", e)
    exit()