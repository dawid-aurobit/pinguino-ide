# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/.virtualenvs/pinguino_env/pinguino/pinguino-ide/qtgui/frames/paths.ui'
#
# Created: Sat Jan 25 17:07:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Paths(object):
    def setupUi(self, Paths):
        Paths.setObjectName("Paths")
        Paths.resize(737, 246)
        self.gridLayout_5 = QtGui.QGridLayout(Paths)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtGui.QGroupBox(Paths)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_sdcc_bin = QtGui.QPushButton(self.groupBox)
        self.pushButton_sdcc_bin.setObjectName("pushButton_sdcc_bin")
        self.gridLayout_3.addWidget(self.pushButton_sdcc_bin, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_sdcc_bin = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_sdcc_bin.setObjectName("lineEdit_sdcc_bin")
        self.gridLayout_3.addWidget(self.lineEdit_sdcc_bin, 0, 1, 1, 1)
        self.lineEdit_pinguino_8_libs = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pinguino_8_libs.setObjectName("lineEdit_pinguino_8_libs")
        self.gridLayout_3.addWidget(self.lineEdit_pinguino_8_libs, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_pinguino_8_libs = QtGui.QPushButton(self.groupBox)
        self.pushButton_pinguino_8_libs.setObjectName("pushButton_pinguino_8_libs")
        self.gridLayout_3.addWidget(self.pushButton_pinguino_8_libs, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Paths)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_gcc_bin = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_gcc_bin.setObjectName("pushButton_gcc_bin")
        self.gridLayout_4.addWidget(self.pushButton_gcc_bin, 0, 2, 1, 1)
        self.lineEdit_gcc_bin = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_gcc_bin.setObjectName("lineEdit_gcc_bin")
        self.gridLayout_4.addWidget(self.lineEdit_gcc_bin, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_pinguino_32_libs = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_pinguino_32_libs.setObjectName("lineEdit_pinguino_32_libs")
        self.gridLayout_4.addWidget(self.lineEdit_pinguino_32_libs, 1, 1, 1, 1)
        self.pushButton_pinguino_32_libs = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_pinguino_32_libs.setObjectName("pushButton_pinguino_32_libs")
        self.gridLayout_4.addWidget(self.pushButton_pinguino_32_libs, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(304, 23, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_close = QtGui.QPushButton(Paths)
        self.pushButton_close.setMinimumSize(QtCore.QSize(165, 0))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Paths)
        QtCore.QMetaObject.connectSlotsByName(Paths)

    def retranslateUi(self, Paths):
        Paths.setWindowTitle(QtGui.QApplication.translate("Paths", "Pinguino Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Paths", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sdcc_bin.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Paths", "SDCC compiler:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Paths", "Libraries:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pinguino_8_libs.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Paths", "32-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_gcc_bin.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Paths", "GCC compiler:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Paths", "Libraries:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pinguino_32_libs.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("Paths", "Close", None, QtGui.QApplication.UnicodeUTF8))

