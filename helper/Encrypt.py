from Crypto import Random
from Crypto.PublicKey import RSA
from pathlib import Path
from helper.Constant import PATH_FILE_KEY_PEM


class Encrypt:
    @staticmethod
    def generate_key():
        random_generator = Random.new().read
        return RSA.generate(1024, random_generator)  # return Key

    def encrypt(self, data_to_encrypt):
        data_to_encrypt_byte = bytes(data_to_encrypt, 'ASCII')
        key = self.get_key_file()
        public_key = key.publickey()
        encrypt_data = public_key.encrypt(data_to_encrypt_byte, 32)
        self.decrypt(encrypt_data, key)

    @staticmethod
    def decrypt(encrypt_data, key):
        value = key.decrypt(encrypt_data)
        return str(value, 'utf-8')

    @staticmethod
    def create_key_file():
        # Crear key file PEM
        key = RSA.generate(2048)
        file_pem = open(PATH_FILE_KEY_PEM, "wb")
        file_pem.write(key.exportKey())
        file_pem.close()

    def get_key_file(self):
        # Obtenemos la llave almacenado en el archivo
        file = Path()
        # Validamos si el archivo existe
        if not file.is_file():
            self.create_key_file()

        # Leemos el archivo
        file_pem = open(file.name, "r")
        return RSA.importKey(file_pem.read())
