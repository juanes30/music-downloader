__author__ = "Juan Esteban Londoño Tabares"

import sys
import pafy
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
        self.update_grid()  # Cargamos grid con las propiedades basicas
        self.vDescargas.btnAgregarVideo.clicked.connect(self.add_video)

    def update_grid(self):
        self.vDescargas.tableWidget.setColumnCount(5)
        self.vDescargas.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Canción"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Progreso"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Tamaño"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Estado"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Ubicación"))
        self.vDescargas.tableWidget.setColumnWidth(0, 230)
        self.vDescargas.tableWidget.setColumnWidth(1, 170)
        self.vDescargas.tableWidget.setColumnWidth(4, 135)

    def add_video(self):
        if len(self.vDescargas.txtUrlVideo.text()) != 0:
            url_video = self.vDescargas.txtUrlVideo.text()
            v_pafy = pafy.new(url_video)
            titulo_cancion = v_pafy.title
            barra_progreso = QtGui.QProgressBar(self)
            barra_progreso.setProperty("value", 24)
            barra_progreso.setObjectName("barra_progreso")
            count_row = self.vDescargas.tableWidget.rowCount()
            self.vDescargas.tableWidget.insertRow(count_row)
            self.vDescargas.tableWidget.setItem(count_row, 0, QtGui.QTableWidgetItem(titulo_cancion))
            self.vDescargas.tableWidget.setCellWidget(count_row, 1, barra_progreso)
            self.vDescargas.tableWidget.setRowHeight(count_row, 19)
        else:
            self.mostrar_mensaje('El video no existe, por favor verifique')

    def mostrar_mensaje(self, titulo, mensaje):
        mensaje_box = QtGui.QMessageBox(QtGui.QMessageBox.Information, titulo, mensaje, QtGui.QMessageBox.NoButton
                                        , self)
        mensaje_box.exec_()

if __name__ == "__main__":
    app_music = QtGui.QApplication(sys.argv)
    frm_dasboard = FrmDashboard()
    frm_dasboard.show()
    frm_descargas = FrmDescargas()
    frm_descargas.hide()
    sys.exit(app_music.exec_())