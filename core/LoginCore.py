import json

from dal.Database import Database
from helper import Constant
from helper.Encrypt import Encrypt


class LoginCore:
    database = Database()

    def login_core(self, usuario_model) -> bool:
        """
        Consulta si el usuario y clave son validos
        :param usuario_model: UsuarioModel class
        :return: bool resultado de la validacion
        """
        usuario_json = eval(json.dumps(usuario_model.__dict__))
        result = self.database.select_db(name_object="Usuario", filter_data=usuario_json)
        if isinstance(result, object) and result is not None:
            return True
        return False

    def register_user(self, usuario_model):
        """
        Agrega un usuario a la base de datos encryptando los datos
        enviados por el usuario.
        :param usuario_model: recibe un model {UsuarioModel}
        """
        try:
            encrypt = Encrypt()
            usuario_model_encrypt = encrypt.encrypt_object(usuario_model)  # Encrypt el model UsuarioModel.
            usuario_json = eval(json.dumps(usuario_model_encrypt.__dict__))  # Creamos un json del UsuarioModel
            self.database.insert_db(name_object="Usuario", data=usuario_json)  # Insertamos el usuario en MongoDB
        except:
            raise Exception(Constant.MESSAGE_ERROR_LOGIN)
