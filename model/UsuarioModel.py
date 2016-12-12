class UsuarioModel:
    def __init__(self, usuario=None, nombre_completo=None, correo=None, clave=None):
        if usuario is None:
            usuario = ""

        if nombre_completo is None:
            nombre_completo = ""

        if correo is None:
            correo = ""

        if clave is None:
            clave = ""

        self.usuario = usuario
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.clave = clave
