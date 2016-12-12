from Crypto import Random
from Crypto.PublicKey import RSA
from pathlib import Path

from helper.Constant import PATH_FILE_KEY_PEM


class Encrypt:
    @staticmethod
    def generate_key():
        """ GENERA UNA CLAVE ALEATORIA """
        random_generator = Random.new().read
        return RSA.generate(1024, random_generator)  # return Key

    def encrypt(self, data_to_encrypt):
        """ ENCRYPTA  UN TEXTO"""
        data_to_encrypt_byte = bytes(data_to_encrypt, 'ASCII')
        key = self.get_key_file()
        public_key = key.publickey()
        a = public_key.encrypt(data_to_encrypt_byte, 32)  # Encrypt Data
        return a

    def decrypt(self, encrypt_data, key=None) -> str:
        """ DESENCRYPTA UN TEXTO """
        if key is None:
            key = self.get_key_file()
        value = key.decrypt(encrypt_data)
        return str(value, 'utf-8')

    @staticmethod
    def create_key_file():
        """ Crear key file PEM """
        key = RSA.generate(2048)
        file_pem = open(PATH_FILE_KEY_PEM, "wb")
        file_pem.write(key.exportKey())
        file_pem.close()

    def get_key_file(self):
        """ Obtener la llave almacenado en el archivo """
        file = Path("private_key.pem")
        # Validamos si el archivo existe
        if not file.is_file():
            self.create_key_file()

        # Leemos el archivo
        file_pem = open(file.name, "r")
        return RSA.importKey(file_pem.read())

    def encrypt_object(self, obj) -> object:
        """ Encrypta todo el objeto que se le envie como parametro """
        obj_result = obj  # Creamos un objeto resultado del mismo tipo.
        for prop in obj.__dict__:  # Recorremos todas las propiedades del objeto.
            value = getattr(obj, prop)

            # Validamos que la propiedad no se un metodo y que el valor no este vacio
            if not callable(value) and not (not value):
                value_encrypt = self.encrypt(value)  # Encryptamos el valor de la propiedad
                setattr(obj_result, prop, str(value_encrypt))  # Asignamos el valor encryptado al objeto resultado.
            elif not callable(value):  # Si, la propiedad esta con valor vacio no es necesario encryptarlo.
                setattr(obj_result, prop, str(value))  # Asignamos el valor encryptado al objeto resultado.
        return obj_result
