from pymongo import MongoClient
from helper.Constant import *


class Database:
    # MANEJO DE LA BASE DE DATOS INSERT, UPDATE, SELECT Y DELETE
    # URL de mongo db
    mongoClient = MongoClient(MONGO_URI)

    def init_db(self):
        # Obtenemos la base de datos default {music-downloader}
        return self.mongoClient.get_default_database()

    def insert_db(self, name_object, data):
        # Insert object en la base de datos
        db = self.init_db()
        table = db[name_object]
        result_insert = table.insert(data)
        if isinstance(result_insert, list):
            return True
        elif isinstance(result_insert, object):
            return True
        else:
            return False






