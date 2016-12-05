from pymongo import MongoClient
from helper.Constant import *


class Database:
    """ MANEJO DE LA BASE DE DATOS INSERT, UPDATE, SELECT Y DELETE """
    mongoClient = MongoClient(MONGO_URI)  # URL de mongo db

    def __init__(self):
        self.db = self.mongoClient.get_default_database()  # Obtenemos la base de datos default {music-downloader}

    def select_db(self, name_object, filter_data=None):
        """ Obtiene uno o todos los registros de una tabla """
        table = self.db[name_object]

        if filter_data is None:
            return table

        return table.find_one(filter=filter_data)

    def insert_db(self, name_object, data):
        """ INSERTA UNO O VARIOS REGISTROS """
        table = self.db[name_object]  # Creamos u obtenemos la tabla desde mongo
        result_insert = table.insert(data)  # Insertamos los datos en la tabla
        if isinstance(result_insert, list):  # Validamos si el resultado es una lista
            return True
        elif isinstance(result_insert, object):  # Validamos si el resultado es un object
            return True
        else:  # si no guardo nada
            return False

    def update_db(self, name_object, filter_data, data):
        """ ACTUALIZA UNO O VARIOS REGISTROS """
        table = self.db[name_object]

        if isinstance(data, list):
            result = table.update_many(filter=filter_data, update={"$inc": data})
            return result.modified_count
        elif isinstance(data, object):
            result = table.update_one(filter=filter_data, update={"$inc": data})
            return result.modified_count

        return 0

    def delete_db(self, name_object, data):
        """ ELIMINAR UNO O VARIOS ELEMENTOS """
        table = self.db[name_object]  # Creamos u obtenemos la tabla desde mongo
        if isinstance(data, list):  # Insertamos los datos en la tabla
            result = table.delete_one(filter=data)
            return result.deleted_count
        elif isinstance(data, object):  # Validamos si el resultado es un object
            result = table.delete_many(filter=data)
            return result.deleted_count

        return 0
