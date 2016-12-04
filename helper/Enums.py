class Enums:

    def init_enum(*args):
        enums = dict(zip(args, range(len(args))))  # Creamos un diccionario con los argumentos enviados
        # enums = {"argumento1": 0, "argumento2": 1, ...}
        return type('Enum', (), enums)

    def validation_login(self):
        return self.init_enum("ERROR_USER", "ERROR_PASSWORD", "SUCCESS")
