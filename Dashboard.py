__author__ = "Juan Esteban Londoño Tabares"

import sys
import pafy
import os
import urllib.request
import time
from threading import Thread
from ui.Dashboard import *
from ui.Descargas import Ui_Descargas

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
        self.vDescargas.btnAgregarVideo.clicked.connect(self.add_video)
        self.vDescargas.btnIniciarDescarga.clicked.connect(self.download_video)
        self.list_videos = []
        self.list_rutas = []

    def update_grid(self):
        self.vDescargas.tableWidget.setColumnCount(5)
        self.vDescargas.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Canción"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Progreso"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Tamaño"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Estado"))
        self.vDescargas.tableWidget.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Ubicación"))
        self.vDescargas.tableWidget.setColumnWidth(0, 277)
        self.vDescargas.tableWidget.setColumnWidth(1, 170)
        self.vDescargas.tableWidget.setColumnWidth(4, 175)

    def add_video(self):
        if len(self.vDescargas.txtUrlVideo.text()) != 0:
            global path_file
            url_video = self.vDescargas.txtUrlVideo.text()

            # Obtener Propiedades del video
            v_pafy = pafy.new(url_video)
            titulo_cancion = v_pafy.title
            stream_video = v_pafy.getbest(preftype='mp4')
            file_extension = stream_video.extension
            size_file = stream_video.get_filesize()
            size_file_mb = round(((size_file / 1024) / 1024), 2)

            # Agregando una nueva fila al QTableWidget
            count_row = self.vDescargas.tableWidget.rowCount()
            self.barra_progreso = QtGui.QProgressBar(self)
            self.barra_progreso.setProperty("value", 0)
            self.vDescargas.tableWidget.insertRow(count_row)
            self.vDescargas.tableWidget.setItem(count_row, 0, QtGui.QTableWidgetItem(titulo_cancion))
            self.vDescargas.tableWidget.setCellWidget(count_row, 1, self.barra_progreso)
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
                path_file = os.path.join(os.environ["USERPROFILE"]
                                         , 'Desktop', titulo_cancion) + '.' + file_extension

            self.list_videos.append(stream_video.url)
            self.list_rutas.append(path_file)
            print(self.list_videos)
            print(self.list_rutas)

            '''self.download_video(path_file)
            QtCore.QCoreApplication.processEvents()'''

        else:
            self.mostrar_mensaje('Mensaje Informativo', 'El video no existe, por favor verifique')

    def mostrar_mensaje(self, titulo, mensaje):
        mensaje_box = QtGui.QMessageBox(QtGui.QMessageBox.Information, titulo, mensaje, QtGui.QMessageBox.NoButton
                                        , self)
        mensaje_box.exec_()

    def download_video(self):
        # Ejecuta el metodo progress_report para ir mostrando el avance de la descarga
        start = time.time()
        threads = []
        print('rutas', self.list_rutas)
        print('url', self.list_videos)
        count = 0
        QtCore.QCoreApplication.processEvents()
        for url in self.list_videos:
            ruta = self.list_rutas[count]
            try:
                # urllib.request.urlretrieve(url, ruta, reporthook=self.progress_report)
                # QtCore.QCoreApplication.processEvents()
                print('url ', url, 'ruta ', ruta)
                # t = DownloadThread(url, ruta)
                t = Thread(target=self.descargar, args=[url, ruta])
                threads.append(t)
                t.start()
                print(url, ruta)
                QtCore.QCoreApplication.processEvents()
                for t in threads:
                    t.join()
                    print("Elapsed time: %s" % (time.time()-start))
            except ValueError:
                print('error')
                continue
            count += 1
        # print("Elapsed time: %s" % (time.time()-start))
        QtCore.QCoreApplication.processEvents()

    def progress_report(self, block_read, size_block, file_size):
        # total_size_mb = round(((file_size / 1024) / 1024), 2)
        total_download = block_read * size_block
        total_download_mb = round(((total_download / 1024) / 1024), 2)
        print(total_download_mb)
        self.vDescargas.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("hola" + str(total_download_mb)))
        self.barra_progreso.setMinimum(0)
        self.barra_progreso.setMaximum(file_size)
        self.barra_progreso.setValue(total_download)
        QtCore.QCoreApplication.processEvents()

    def descargar(self, url, ruta):
        print('entro', url)
        urllib.request.urlretrieve(url, ruta, reporthook=self.progress_report)
        print(url)


class DownloadThread(Thread):
    def __init__(self, url, file):
        self.url = url
        self.file = file
        super(DownloadThread, self).__init__()

    def run(self):
        urllib.request.urlretrieve(self.url, self.file, reporthook=self.progress_report)
        print(self.url)

    def progress_report(self, block_read, size_block, file_size):
        total_size_mb = round(((file_size / 1024) / 1024), 2)
        total_download = block_read * size_block
        total_download_mb = round(((total_download / 1024) / 1024), 2)
        print(total_download_mb)

if __name__ == "__main__":
    app_music = QtGui.QApplication(sys.argv)
    frm_dasboard = FrmDashboard()
    frm_dasboard.show()
    frm_descargas = FrmDescargas()
    frm_descargas.hide()
    sys.exit(app_music.exec_())