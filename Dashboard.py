from PySide import QtGui

from ui.Dashboard import Ui_Form


class FrmDashboard(QtGui.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(FrmDashboard, self).__init__(parent)
        self.vDashboard = Ui_Form()
        self.vDashboard.setupUi(self)
        self.vDashboard.btnDescargas.clicked.connect(self.abrir_descargas)
        self.setWindowTitle("Juanes30 Musica")

    @staticmethod
    def abrir_descargas():
        # frm_descargas.show()
        pass
