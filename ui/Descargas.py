# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Descargas.ui'
#
# Created: Sun Feb  8 17:30:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Descargas(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 449)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtUrlVideo = QtGui.QLineEdit(Dialog)
        self.txtUrlVideo.setGeometry(QtCore.QRect(50, 50, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtUrlVideo.setFont(font)
        self.txtUrlVideo.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtUrlVideo.setText("")
        self.txtUrlVideo.setObjectName("txtUrlVideo")
        self.lblUrlVideo = QtGui.QLabel(Dialog)
        self.lblUrlVideo.setGeometry(QtCore.QRect(50, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lblUrlVideo.setFont(font)
        self.lblUrlVideo.setObjectName("lblUrlVideo")
        self.btnBuscar = QtGui.QPushButton(Dialog)
        self.btnBuscar.setGeometry(QtCore.QRect(570, 50, 41, 31))
        self.btnBuscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(42, 42))
        self.btnBuscar.setFlat(True)
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 671, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUrlVideo.setText(QtGui.QApplication.translate("Dialog", "Ingresa la URL del video", None, QtGui.QApplication.UnicodeUTF8))



