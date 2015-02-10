__author__ = "Juan Esteban Londoño Tabares"

import sys
from ui.Dashboard import *
from ui.Descargas import Ui_Descargas

__youtube__ = "https://www.youtube.com"


class FrmDashboard(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FrmDashboard, self).__init__(parent)
        self.vDashboard = Ui_Form()
        self.vDashboard.setupUi(self)
        self.vDashboard.btnDescargas.clicked.connect(self.abrir_descargas)

    @staticmethod
    def abrir_descargas():
        frm_descargas.show()


class FrmDescargas(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FrmDescargas, self).__init__(parent)
        self.vDescargas = Ui_Descargas()
        self.vDescargas.setupUi(self)
        self.modificar_grid()  # Cargamos grid con las propiedades basicas
        self.vDescargas.tableWidget.setRowCount(5)
        self.vDescargas.tableWidget.setRowHeight(0, 19)
        self.vDescargas.tableWidget.setItem(1, 0, QtGui.QTableWidgetItem("hola"))
        self.barra_progreso = QtGui.QProgressBar(self)
        self.barra_progreso.setProperty("value", 24)
        self.barra_progreso.setObjectName("barra_progreso")
        self.vDescargas.tableWidget.setCellWidget(0, 1, self.barra_progreso)

        dat = self.vDescargas.tableWidget.rowCount()
        print(dat)

    def setmydata(self):
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QtGui.QTableWidgetItem(item)
                self.vDescargas.tableWidget.setItem(m, n, newitem)
                m += 1
            n += 1

    def modificar_grid(self):
        self.vDescargas.tableWidget.setColumnCount(5)
        self.vDescargas.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Canción"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Progreso"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Tamaño"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Estado"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Ubicación"))
        self.vDescargas.tableWidget.setColumnWidth(0, 67)
        self.vDescargas.tableWidget.setColumnWidth(1, 250)
        self.vDescargas.tableWidget.setColumnWidth(4, 135)

if __name__ == "__main__":
    app_music = QtGui.QApplication(sys.argv)
    frm_dasboard = FrmDashboard()
    frm_dasboard.show()
    frm_descargas = FrmDescargas()
    frm_descargas.hide()
    sys.exit(app_music.exec_())