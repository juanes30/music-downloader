# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Descargas.ui'
#
# Created: Wed Feb 25 14:02:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Descargas(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(920, 507)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 27, 901, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblUrlVideo = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lblUrlVideo.setFont(font)
        self.lblUrlVideo.setObjectName("lblUrlVideo")
        self.verticalLayout.addWidget(self.lblUrlVideo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtUrlVideo = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtUrlVideo.setFont(font)
        self.txtUrlVideo.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtUrlVideo.setText("")
        self.txtUrlVideo.setObjectName("txtUrlVideo")
        self.horizontalLayout.addWidget(self.txtUrlVideo)
        self.btnAgregarVideo = QtGui.QPushButton(self.layoutWidget)
        self.btnAgregarVideo.setAutoFillBackground(False)
        self.btnAgregarVideo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregarVideo.setIcon(icon)
        self.btnAgregarVideo.setIconSize(QtCore.QSize(42, 42))
        self.btnAgregarVideo.setFlat(True)
        self.btnAgregarVideo.setObjectName("btnAgregarVideo")
        self.horizontalLayout.addWidget(self.btnAgregarVideo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lblFormato = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblFormato.setFont(font)
        self.lblFormato.setObjectName("lblFormato")
        self.horizontalLayout_2.addWidget(self.lblFormato)
        self.cBoxFormato = QtGui.QComboBox(self.layoutWidget)
        self.cBoxFormato.setObjectName("cBoxFormato")
        self.horizontalLayout_2.addWidget(self.cBoxFormato)
        spacerItem1 = QtGui.QSpacerItem(258, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnIniciarDescarga = QtGui.QPushButton(self.layoutWidget)
        self.btnIniciarDescarga.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIniciarDescarga.setIcon(icon1)
        self.btnIniciarDescarga.setIconSize(QtCore.QSize(35, 35))
        self.btnIniciarDescarga.setFlat(True)
        self.btnIniciarDescarga.setObjectName("btnIniciarDescarga")
        self.horizontalLayout_2.addWidget(self.btnIniciarDescarga)
        spacerItem2 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUrlVideo.setText(QtGui.QApplication.translate("Dialog", "Ingresa la URL del video", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFormato.setText(QtGui.QApplication.translate("Dialog", "Formato", None, QtGui.QApplication.UnicodeUTF8))

