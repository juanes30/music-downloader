import json

from dal.Database import Database
from helper import Constant
from helper.Encrypt import Encrypt


class LoginCore:
    database = Database()
    encrypt = Encrypt()

    def login_core(self, usuario_model) -> bool:
        """
        Consulta si el usuario y clave son validos
        :param usuario_model: UsuarioModel class
        :return: bool resultado de la validacion
        """
        usuario_json = eval(json.dumps(usuario_model.__dict__))
        result = self.database.select_db(name_object="Usuario", filter_data=usuario_json)
        if isinstance(result, object) and result is not None:
            Constant.USUARIO = self.encrypt.decrypt(eval(result["usuario"]))
            return True
        return False

    def register_user(self, usuario_model):
        """
        Agrega un usuario a la base de datos encryptando los datos
        enviados por el usuario.
        :param usuario_model: recibe un model {UsuarioModel}
        :return bool resultado de el registro de un nuevo usuario
        """
        try:
            usuario_model_encrypt = self.encrypt.encrypt_object(usuario_model)  # Encrypt el model UsuarioModel.
            usuario_json = eval(json.dumps(usuario_model_encrypt.__dict__))  # Creamos un json del UsuarioModel
            find_user = self.database.select_db(name_object="Usuario", filter_data=usuario_json)
            if isinstance(find_user, object) and find_user is not None:
                raise Exception(Constant.MESSAGE_ERROR_SIGN_UP_ALREADY_USER)

            # Insertamos el usuario en MongoDB
            return self.database.insert_db(name_object="Usuario", data=usuario_json)
        except Exception as ex:
            raise Exception(Constant.MESSAGE_ERROR_SIGN_UP + "\nError: " + str(ex))
