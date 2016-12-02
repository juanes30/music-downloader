class UsuarioModel:
    def __init__(self, usuario, nombre_completo, correo, clave):
        self.__usuario = usuario
        self.__nombre_completo = nombre_completo
        self.__correo = correo
        self.__clave = clave

    @property
    def usuario(self):
        return self.__usuario

    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @property
    def correo(self):
        return self.__correo

    @property
    def clave(self):
        return self.__clave
