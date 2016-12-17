from PySide import QtGui

from Descargas import FrmDescargas
from helper import Constant
from ui.Dashboard import Ui_Form

__author__ = "Juan Esteban Londoño Tabares"


class FrmDashboard(QtGui.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(FrmDashboard, self).__init__(parent)
        self.setupUi(self)
        self.btnDescargas.clicked.connect(self.abrir_descargas)
        self.setWindowTitle("Juanes30 Musica")
        self.descargas_form = None

        self.init_ui()

    def init_ui(self):
        version_app = str(self.label_version.text()).replace('0.0.0', Constant.VERSION_APP)
        self.label_version.setText(version_app)
        self.label_nombre_usuario.setText(Constant.USUARIO)

    def abrir_descargas(self):
        if not self.descargas_form:
            self.descargas_form = FrmDescargas()
        if self.descargas_form.isVisible():
            self.descargas_form.hide()
        else:
            self.descargas_form.show()


