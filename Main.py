import sys
import pafy
import os
import subprocess
import urllib.request

from Login import Login
from helper.Encrypt import Encrypt
from ui.Dashboard import *
from ui.Descargas import Ui_Descargas
from ui.Login import UiLogin
from dal.Database import Database

__author__ = "Juan Esteban Londoño Tabares"
__youtube__ = "https://www.youtube.com"


class FrmDashboard(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FrmDashboard, self).__init__(parent)
        self.vDashboard = Ui_Form()
        self.vDashboard.setupUi(self)
        self.vDashboard.btnDescargas.clicked.connect(self.abrir_descargas)
        self.setWindowTitle("Juanes30 Musica")

    @staticmethod
    def abrir_descargas():
        frm_descargas.show()


class FrmDescargas(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FrmDescargas, self).__init__(parent)
        self.vDescargas = Ui_Descargas()
        self.vDescargas.setupUi(self)
        self.setWindowTitle("Descargas")
        self.update_grid()  # Cargamos grid con las propiedades basicas
        self.fill_combo_formats()
        self.vDescargas.btnAgregarVideo.clicked.connect(self.add_video)
        self.vDescargas.btnIniciarDescarga.clicked.connect(self.download_video)
        self.count = 0
        self.list_videos = []
        self.list_rutas = []
        self.list_formato = []
        self.list_titulo_cancion = []
        self.file_format = "mp4"

    def fill_combo_formats(self):
        icon_mp4 = QtGui.QIcon()
        icon_mp4.addPixmap(QtGui.QPixmap("images/icon_mp4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vDescargas.cBoxFormato.addItem(icon_mp4, "mp4")

        icon_3gp = QtGui.QIcon()
        icon_3gp.addPixmap(QtGui.QPixmap("images/icon_3gp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vDescargas.cBoxFormato.addItem(icon_3gp, "3gp")

        icon_webm = QtGui.QIcon()
        icon_webm.addPixmap(QtGui.QPixmap("images/icon_webm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vDescargas.cBoxFormato.addItem(icon_webm, "webm")

        icon_flv = QtGui.QIcon()
        icon_flv.addPixmap(QtGui.QPixmap("images/icon_flv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vDescargas.cBoxFormato.addItem(icon_flv, "flv")

        icon_mp3 = QtGui.QIcon()
        icon_mp3.addPixmap(QtGui.QPixmap("images/icon_mp3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vDescargas.cBoxFormato.addItem(icon_mp3, "mp3")

    def update_grid(self):
        self.vDescargas.tableWidget.setColumnCount(5)
        self.vDescargas.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Canción"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Progreso"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Tamaño"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Estado"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Ubicación"))
        self.vDescargas.tableWidget.setColumnWidth(0, 277)
        self.vDescargas.tableWidget.setColumnWidth(1, 170)
        self.vDescargas.tableWidget.setColumnWidth(3, 75)
        self.vDescargas.tableWidget.setColumnWidth(4, 175)

    def add_video(self):
        if len(self.vDescargas.txtUrlVideo.text()) != 0:
            global path_file
            url_video = self.vDescargas.txtUrlVideo.text()

            # Obtener Propiedades del video
            v_pafy = pafy.new(url_video)
            titulo_cancion = v_pafy.title
            self.file_format = self.vDescargas.cBoxFormato.currentText()

            if self.file_format == "mp3":
                stream = v_pafy.getbestaudio()
                file_extension = stream.extension
                size_file = stream.get_filesize()
                size_file_mb = round(((size_file / 1024) / 1024), 2)
            else:
                stream = v_pafy.getbest(preftype=self.file_format)
                file_extension = stream.extension
                size_file = stream.get_filesize()
                size_file_mb = round(((size_file / 1024) / 1024), 2)

            # Agregando una nueva fila al QTableWidget
            count_row = self.vDescargas.tableWidget.rowCount()
            self.vDescargas.tableWidget.insertRow(count_row)
            self.vDescargas.tableWidget.setItem(count_row, 0, QtGui.QTableWidgetItem(titulo_cancion))
            self.vDescargas.tableWidget.setItem(count_row, 2, QtGui.QTableWidgetItem(str(size_file_mb) + " MB"))
            self.vDescargas.tableWidget.setItem(count_row, 3, QtGui.QTableWidgetItem("Pendiente"))
            self.vDescargas.tableWidget.setRowHeight(count_row, 19)

            # Limpiar Url Video
            self.vDescargas.txtUrlVideo.setText("")
            self.vDescargas.txtUrlVideo.setFocus()

            titulo_cancion = str(titulo_cancion).replace('_', '')
            titulo_cancion = str(titulo_cancion).replace('-', '')
            titulo_cancion = str(titulo_cancion).replace('(', '')
            titulo_cancion = str(titulo_cancion).replace(')', '')

            if 'win32' in sys.platform or 'win64' in sys.platform:
                path_file = os.path.join(os.environ["USERPROFILE"], 'Desktop', titulo_cancion) + '.' + file_extension

            self.list_videos.append(stream.url)
            self.list_rutas.append(path_file)
            self.list_formato.append(self.vDescargas.cBoxFormato.currentText())
            self.list_titulo_cancion.append(titulo_cancion)

        else:
            self.mostrar_mensaje('Mensaje Informativo', 'El video no existe, por favor verifique')

    def mostrar_mensaje(self, titulo, mensaje):
        mensaje_box = QtGui.QMessageBox(QtGui.QMessageBox.Information, titulo, mensaje, QtGui.QMessageBox.NoButton,
                                        self)
        mensaje_box.exec_()

    def download_video(self):
        # Ejecuta el metodo progress_report para ir mostrando el avance de la descarga
        self.vDescargas.btnIniciarDescarga.setEnabled(False)
        QtCore.QCoreApplication.processEvents()
        for url in self.list_videos:
            ruta = self.list_rutas[self.count]
            formato = self.list_formato[self.count]
            titulo = self.list_titulo_cancion[self.count]
            try:
                urllib.request.urlretrieve(url, ruta, reporthook=self.progress_report)
                self.vDescargas.tableWidget.setItem(self.count, 1, QtGui.QTableWidgetItem("Total Descargado 100%"))
                self.vDescargas.tableWidget.setItem(self.count, 3, QtGui.QTableWidgetItem("Completado"))
                if formato == "mp3":
                    m4a = os.path.join(os.environ["USERPROFILE"], 'Desktop', titulo) + '.' + 'm4a'
                    mp3 = os.path.join(os.environ["USERPROFILE"], 'Desktop', titulo) + '.' + 'mp3'
                    self.convert_mp3('./ffmpeg -i \"%s\" -y \"%s\"' % (m4a, mp3))
                    os.remove(m4a)

            except ValueError:
                print('error')
                continue
            self.count += 1
        QtCore.QCoreApplication.processEvents()
        self.vDescargas.btnIniciarDescarga.setEnabled(True)
        self.list_videos = []

    def progress_report(self, block_read, size_block, file_size):
        total_size_mb = round(((file_size / 1024) / 1024), 2)
        total_download = block_read * size_block
        total_download_mb = round(((total_download / 1024) / 1024), 2)
        try:
            download_percentage = round((total_download_mb * 100) / total_size_mb, 2)
            self.vDescargas.tableWidget.setItem(self.count, 1, QtGui.QTableWidgetItem('Total Descargado '
                                                                                      + str(download_percentage) + "%"))
        except ZeroDivisionError:
            print('Se produce una Divicion por Cero')
        QtCore.QCoreApplication.processEvents()

    @staticmethod
    def convert_mp3(var_archivo):
        if 'win32' in sys.platform:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            with (subprocess.Popen(var_archivo, stdout=subprocess.PIPE, startupinfo=startupinfo)):
                return
        else:
            os.system('chmod +x ffmpeg')
            subprocess.check_output(var_archivo, shell=True)


# class FrmLogin(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(FrmLogin, self).__init__(parent)
#         self.vLogin = UiLogin()
#         self.vLogin.setup_ui(self)
#         d = Database()
#         SEED_DATA = [
#             {
#                 'decade': '1970s',
#                 'artist': 'Debby Boone',
#                 'song': 'You Light Up My Life',
#                 'weeksAtOne': 10
#             },
#             {
#                 'decade': '1980s',
#                 'artist': 'Olivia Newton-John',
#                 'song': 'Physical',
#                 'weeksAtOne': 10
#             },
#             {
#                 'decade': '1990s',
#                 'artist': 'Mariah Carey',
#                 'song': 'One Sweet Day',
#                 'weeksAtOne': 16
#             }
#         ]
        # d.insert_db(name_object="Cliente", data=SEED_DATA)


if __name__ == "__main__":
    app_music = QtGui.QApplication(sys.argv)
    frm_dasboard = FrmDashboard()
    frm_dasboard.hide()
    frm_descargas = FrmDescargas()
    frm_descargas.hide()
    frm_login = Login()
    frm_login.show()
    sys.exit(app_music.exec_())
