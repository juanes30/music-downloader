# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\juan.londono\Proyectos\PycharmProjects\juanes30-musica\ui\Descargas.ui'
#
# Created: Sun Nov 20 23:02:29 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class UiDescargas(object):
    def setup_ui(self, descargas):
        descargas.setObjectName("Descargas")
        descargas.resize(876, 594)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        descargas.setWindowIcon(icon)
        descargas.setInputMethodHints(QtCore.Qt.ImhNone)
        self.logo_app = QtGui.QPushButton(descargas)
        self.logo_app.setEnabled(True)
        self.logo_app.setGeometry(QtCore.QRect(40, 540, 41, 31))
        self.logo_app.setAutoFillBackground(False)
        self.logo_app.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/pythonLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_app.setIcon(icon1)
        self.logo_app.setIconSize(QtCore.QSize(33, 33))
        self.logo_app.setFlat(True)
        self.logo_app.setObjectName("logo_app")
        self.lbl_titulo_carpeta_guardado = QtGui.QLabel(descargas)
        self.lbl_titulo_carpeta_guardado.setGeometry(QtCore.QRect(540, 529, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.lbl_titulo_carpeta_guardado.setFont(font)
        self.lbl_titulo_carpeta_guardado.setObjectName("lbl_titulo_carpeta_guardado")
        self.lbl_version = QtGui.QLabel(descargas)
        self.lbl_version.setGeometry(QtCore.QRect(30, 570, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lbl_version.setFont(font)
        self.lbl_version.setObjectName("lbl_version")
        self.btn_seleccionar_ruta_guardado = QtGui.QPushButton(descargas)
        self.btn_seleccionar_ruta_guardado.setGeometry(QtCore.QRect(540, 559, 34, 34))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_seleccionar_ruta_guardado.setFont(font)
        self.btn_seleccionar_ruta_guardado.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_seleccionar_ruta_guardado.setAutoFillBackground(False)
        self.btn_seleccionar_ruta_guardado.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_seleccionar_ruta_guardado.setIcon(icon2)
        self.btn_seleccionar_ruta_guardado.setIconSize(QtCore.QSize(35, 35))
        self.btn_seleccionar_ruta_guardado.setFlat(True)
        self.btn_seleccionar_ruta_guardado.setObjectName("btn_seleccionar_ruta_guardado")
        self.lbl_ruta = QtGui.QLabel(descargas)
        self.lbl_ruta.setGeometry(QtCore.QRect(580, 570, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setBold(False)
        self.lbl_ruta.setFont(font)
        self.lbl_ruta.setCursor(QtCore.Qt.PointingHandCursor)
        self.lbl_ruta.setObjectName("lbl_ruta")
        self.logo_app_3 = QtGui.QPushButton(descargas)
        self.logo_app_3.setGeometry(QtCore.QRect(830, 0, 41, 31))
        self.logo_app_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.logo_app_3.setAutoFillBackground(False)
        self.logo_app_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/googleDrive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_app_3.setIcon(icon3)
        self.logo_app_3.setIconSize(QtCore.QSize(25, 25))
        self.logo_app_3.setFlat(True)
        self.logo_app_3.setObjectName("logo_app_3")
        self.line = QtGui.QFrame(descargas)
        self.line.setGeometry(QtCore.QRect(17, 30, 841, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblUrlVideo = QtGui.QLabel(descargas)
        self.lblUrlVideo.setGeometry(QtCore.QRect(30, 50, 190, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblUrlVideo.setFont(font)
        self.lblUrlVideo.setObjectName("lblUrlVideo")
        self.lbl_titulo_formulario = QtGui.QLabel(descargas)
        self.lbl_titulo_formulario.setGeometry(QtCore.QRect(50, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.lbl_titulo_formulario.setFont(font)
        self.lbl_titulo_formulario.setObjectName("lbl_titulo_formulario")
        self.logo_app_2 = QtGui.QPushButton(descargas)
        self.logo_app_2.setGeometry(QtCore.QRect(10, 0, 31, 31))
        self.logo_app_2.setAutoFillBackground(False)
        self.logo_app_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_app_2.setIcon(icon4)
        self.logo_app_2.setIconSize(QtCore.QSize(28, 28))
        self.logo_app_2.setFlat(True)
        self.logo_app_2.setObjectName("logo_app_2")
        self.line_3 = QtGui.QFrame(descargas)
        self.line_3.setGeometry(QtCore.QRect(10, 490, 851, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.widget = QtGui.QWidget(descargas)
        self.widget.setGeometry(QtCore.QRect(11, 79, 856, 345))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.txtUrlVideo = QtGui.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtUrlVideo.setFont(font)
        self.txtUrlVideo.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtUrlVideo.setText("")
        self.txtUrlVideo.setObjectName("txtUrlVideo")
        self.verticalLayout_3.addWidget(self.txtUrlVideo)
        spacerItem1 = QtGui.QSpacerItem(608, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnBuscar = QtGui.QPushButton(self.widget)
        self.btnBuscar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnBuscar.setAutoFillBackground(False)
        self.btnBuscar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon5)
        self.btnBuscar.setIconSize(QtCore.QSize(42, 42))
        self.btnBuscar.setFlat(True)
        self.btnBuscar.setObjectName("btnBuscar")
        self.verticalLayout_2.addWidget(self.btnBuscar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAgregarVideo = QtGui.QPushButton(self.widget)
        self.btnAgregarVideo.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnAgregarVideo.setAutoFillBackground(False)
        self.btnAgregarVideo.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregarVideo.setIcon(icon6)
        self.btnAgregarVideo.setIconSize(QtCore.QSize(42, 42))
        self.btnAgregarVideo.setFlat(True)
        self.btnAgregarVideo.setObjectName("btnAgregarVideo")
        self.verticalLayout.addWidget(self.btnAgregarVideo)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_4 = QtGui.QFrame(self.widget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblFormato = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblFormato.setFont(font)
        self.lblFormato.setObjectName("lblFormato")
        self.horizontalLayout.addWidget(self.lblFormato)
        self.cBoxFormato = QtGui.QComboBox(self.widget)
        self.cBoxFormato.setObjectName("cBoxFormato")
        self.horizontalLayout.addWidget(self.cBoxFormato)
        spacerItem2 = QtGui.QSpacerItem(258, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnIniciarDescarga = QtGui.QPushButton(self.widget)
        self.btnIniciarDescarga.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnIniciarDescarga.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIniciarDescarga.setIcon(icon7)
        self.btnIniciarDescarga.setIconSize(QtCore.QSize(35, 35))
        self.btnIniciarDescarga.setFlat(True)
        self.btnIniciarDescarga.setObjectName("btnIniciarDescarga")
        self.horizontalLayout.addWidget(self.btnIniciarDescarga)
        spacerItem3 = QtGui.QSpacerItem(398, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)

        self.retranslateUi(descargas)
        QtCore.QMetaObject.connectSlotsByName(descargas)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_titulo_carpeta_guardado.setText(QtGui.QApplication.translate("Dialog", "Carpeta de Guardado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_version.setText(QtGui.QApplication.translate("Dialog", "Version: 0.2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ruta.setText(QtGui.QApplication.translate("Dialog", "Ruta Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUrlVideo.setText(QtGui.QApplication.translate("Dialog", "Busca o Ingresa la URL", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_titulo_formulario.setText(QtGui.QApplication.translate("Dialog", "Descargar Musica", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFormato.setText(QtGui.QApplication.translate("Dialog", "Formato", None, QtGui.QApplication.UnicodeUTF8))

