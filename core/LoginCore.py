import json

from dal.Database import Database


class LoginCore:
    database = Database()

    def login_core(self, usuario_model):
        usuario_json = eval(json.dumps(usuario_model.__dict__))
        result = self.database.select_db(name_object="Usuario", filter_data=usuario_json)
        if isinstance(result, object):
            return True

    def register_user(self, usuario_model):
        try:
            usuario_json = eval(json.dumps(usuario_model.__dict__))
            self.database.insert_db(name_object="Usuario", data=usuario_json)
        except Exception as ex:
            print(ex)
