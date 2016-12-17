from PySide import QtGui

from helper import Constant
from ui.Dashboard import Ui_Form


class FrmDashboard(QtGui.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(FrmDashboard, self).__init__(parent)
        self.setupUi(self)
        self.btnDescargas.clicked.connect(self.abrir_descargas)
        self.setWindowTitle("Juanes30 Musica")

        self.init_ui()

    def init_ui(self):
        version_app = str(self.label_version.text()).replace('0.0.0', Constant.VERSION_APP)
        self.label_version.setText(version_app)
        self.label_nombre_usuario.setText(Constant.USUARIO)

    @staticmethod
    def abrir_descargas():
        # frm_descargas.show()
        pass
