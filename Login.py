from PySide import QtGui

from Dashboard import FrmDashboard
from core.LoginCore import LoginCore
from helper import Constant
from helper.Encrypt import Encrypt
from helper.Enums import Enums
from helper.Utility import Utility
from model.UsuarioModel import UsuarioModel
from ui.Login import UiLogin


class Login(QtGui.QMainWindow, UiLogin):
    """ CONTROLA EL FORMULARIO DE LOGIN """

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.login = UiLogin()
        self.login.setup_ui(self)
        self.enum_login = Enums().validation_login()
        self.dashboard_form = None

        # Controles de la vista
        self.label_version = self.login.label_version
        self.line_edit_password = self.login.line_edit_password
        self.line_edit_usuario = self.login.line_edit_usuario
        self.label_usuario_mensaje = self.login.label_usuario_mensaje
        self.label_password_mensaje = self.login.label_password_mensaje

        # Eventos de los Controles
        self.login.pBtn_Ingresar.clicked.connect(self.attempt_login)
        self.login.pBtn_registrarse.clicked.connect(self.attempt_register)

        # Ejecutamos las funciones
        self.init_ui()

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
        flag_login = True

        resultado, enum_login, mensaje = self.validation_required_field()  # Validamos la contraseña
        if not resultado:  # Si el resultado es {False}, entonces validamos cual fue el problema
            if enum_login == self.enum_login.ERROR_USER:  # Si hay problemas con el campo Usuario
                self.label_usuario_mensaje.setVisible(True)
                self.label_usuario_mensaje.setText(mensaje)
                flag_login = False
            elif enum_login == self.enum_login.ERROR_PASSWORD:  # Si hay problemas con el campo Password
                self.label_password_mensaje.setVisible(True)
                self.label_password_mensaje.setText(mensaje)
                flag_login = False

        if flag_login:  # si no hay problemas de validaciones intentamos ingresar.
            try:
                login_core = LoginCore()
                encrypt = Encrypt()
                usuario_model = UsuarioModel(usuario=self.line_edit_usuario.text(),
                                             clave=self.line_edit_password.text())
                usuario_model_encrypt = encrypt.encrypt_object(usuario_model)
                result_login = login_core.login_core(usuario_model=usuario_model_encrypt)
                if result_login:
                    self.show_dashboard()

            except Exception as ex:
                Utility.show_message(Constant.MESSAGE_TITLE_INFORMATION, str(ex), QtGui.QMessageBox.Information)

    def attempt_register(self):
        """ Tratamos de realizar el login realizando todas las validaciones
        y consultas necesarias para el ingreso
        """
        self.init_ui()  # limpiamos los errores, si los habian
        flag_register = True

        resultado, enum_login, mensaje = self.validation_required_field()  # Validamos la contraseña
        if not resultado:  # Si el resultado es {False}, entonces validamos cual fue el problema
            if enum_login == self.enum_login.ERROR_USER:  # Si hay problemas con el campo Usuario
                self.label_usuario_mensaje.setVisible(True)
                self.label_usuario_mensaje.setText(mensaje)
                flag_register = False
            elif enum_login == self.enum_login.ERROR_PASSWORD:  # Si hay problemas con el campo Password
                self.label_password_mensaje.setVisible(True)
                self.label_password_mensaje.setText(mensaje)
                flag_register = False

        if flag_register:  # si no hay problemas de validaciones intentamos ingresar.
            login_core = LoginCore()
            usuario_model = UsuarioModel(usuario=self.line_edit_usuario.text(), clave=self.line_edit_password.text())
            login_core.register_user(usuario_model=usuario_model)

    def validation_required_field(self):
        """ Validamos que todos los campos esten debidamente llenados """
        password = self.line_edit_password.text()
        user = self.line_edit_usuario.text()

        if not user and len(user) < 3:
            return False, self.enum_login.ERROR_USER, Constant.MESSAGE_ERROR_USUARIO_TAMANIO
        elif not password and len(password) < 4:
            return False, self.enum_login.ERROR_PASSWORD, Constant.MESSAGE_ERROR_PASSWORD_TAMANIO
        return True, self.enum_login.SUCCESS, Constant.MESSAGE_SUCCESS_OK

    def show_dashboard(self):
        """
        Muestra el formulario de Dashboard y oculta el actual
        """
        if not self.dashboard_form:
            self.dashboard_form = FrmDashboard()
        if self.dashboard_form.isVisible():
            self.dashboard_form.hide()
        else:
            self.close()
            self.dashboard_form.show()
