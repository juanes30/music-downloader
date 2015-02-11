# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Descargas.ui'
#
# Created: Tue Feb 10 21:31:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Descargas(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(879, 510)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 841, 471))
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
        self.btnAgregarVideo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregarVideo.setIcon(icon)
        self.btnAgregarVideo.setIconSize(QtCore.QSize(42, 42))
        self.btnAgregarVideo.setFlat(True)
        self.btnAgregarVideo.setObjectName("btnAgregarVideo")
        self.horizontalLayout.addWidget(self.btnAgregarVideo)
        self.verticalLayout.addLayout(self.horizontalLayout)
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

