from PySide import QtGui

from helper import Constant
from helper.Enums import Enums
from ui.Login import UiLogin


class Login(QtGui.QWidget):
    """ CONTROLA EL FORMULARIO DE LOGIN """

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.login = UiLogin()
        self.login.setup_ui(self)
        self.enum_login = Enums().validation_login()

        # Controles de la vista
        self.label_version = self.login.label_version
        self.line_edit_password = self.login.line_edit_password
        self.line_edit_usuario = self.login.line_edit_usuario
        self.label_usuario_mensaje = self.login.label_usuario_mensaje
        self.label_password_mensaje = self.login.label_password_mensaje

        # Eventos de los Controles
        self.login.pBtn_Ingresar.clicked.connect(self.attempt_login)

        # Ejecutamos las funciones
        self.init_ui()

        # init

    def init_ui(self):
        """ Configuramos la UI"""
        self.label_usuario_mensaje.setVisible(False)
        self.label_password_mensaje.setVisible(False)

        # Asignamos la version actual del aplicativo
        version_app = str(self.label_version.text()).replace('0.0.0', Constant.VERSION_APP)
        self.label_version.setText(version_app)

    def attempt_login(self):
        """ Tratamos de realizar el login realizando todas las validaciones
        y consultas necesarias para el ingreso
        """
        self.init_ui()  # limpiamos los errores, si los habian

        resultado, enum_login, mensaje = self.validation_required_field()  # Validamos la contraseña
        if not resultado:  # Si el resultado es {False}, entonces validamos cual fue el problema
            if enum_login == self.enum_login.ERROR_USER:  # Si hay problemas con el campo Usuario
                self.label_usuario_mensaje.setVisible(True)
                self.label_usuario_mensaje.setText(mensaje)
            elif enum_login == self.enum_login.ERROR_PASSWORD:  # Si hay problemas con el campo Password
                self.label_password_mensaje.setVisible(True)
                self.label_password_mensaje.setText(mensaje)

    def validation_required_field(self):
        """ Validamos que todos los campos esten debidamente llenados """
        password = self.line_edit_password.text()
        user = self.line_edit_usuario.text()

        if not user and len(user) < 3:
            return False, self.enum_login.ERROR_USER, Constant.MESSAGE_ERROR_USUARIO_TAMANIO
        elif not password and len(password) < 4:
            return False, self.enum_login.ERROR_PASSWORD, Constant.MESSAGE_ERROR_PASSWORD_TAMANIO
        return True, self.enum_login.SUCCESS, Constant.MESSAGE_SUCCESS_OK
