# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/python/dev/developing/pinguino/pinguino-ide/qtgui/frames/board_config.ui'
#
# Created: Thu Apr 24 23:04:05 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BoardConfig(object):
    def setupUi(self, BoardConfig):
        BoardConfig.setObjectName("BoardConfig")
        BoardConfig.resize(336, 398)
        self.gridLayout_5 = QtGui.QGridLayout(BoardConfig)
        self.gridLayout_5.setVerticalSpacing(14)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_arch = QtGui.QGroupBox(BoardConfig)
        self.groupBox_arch.setAutoFillBackground(False)
        self.groupBox_arch.setObjectName("groupBox_arch")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_arch)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_arch_8 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_8.setObjectName("radioButton_arch_8")
        self.gridLayout.addWidget(self.radioButton_arch_8, 0, 0, 1, 1)
        self.radioButton_arch_32 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_32.setObjectName("radioButton_arch_32")
        self.gridLayout.addWidget(self.radioButton_arch_32, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_arch, 0, 0, 1, 1)
        self.groupBox_mode = QtGui.QGroupBox(BoardConfig)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_mode)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_mode_icsp = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_icsp.setText("ICSP")
        self.radioButton_mode_icsp.setObjectName("radioButton_mode_icsp")
        self.gridLayout_2.addWidget(self.radioButton_mode_icsp, 0, 0, 1, 1)
        self.radioButton_mode_bootloader = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_bootloader.setObjectName("radioButton_mode_bootloader")
        self.gridLayout_2.addWidget(self.radioButton_mode_bootloader, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_mode, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(318, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 7, 0, 1, 1)
        self.groupBox_devices_8 = QtGui.QGroupBox(BoardConfig)
        self.groupBox_devices_8.setObjectName("groupBox_devices_8")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_devices_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_device_8 = QtGui.QGridLayout()
        self.gridLayout_device_8.setObjectName("gridLayout_device_8")
        self.gridLayout_4.addLayout(self.gridLayout_device_8, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_8, 4, 0, 1, 1)
        self.groupBox_bootloader = QtGui.QGroupBox(BoardConfig)
        self.groupBox_bootloader.setObjectName("groupBox_bootloader")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_bootloader)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_bootloader_v1_v2 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v1_v2.setText("v1.x or v2.x")
        self.radioButton_bootloader_v1_v2.setObjectName("radioButton_bootloader_v1_v2")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v1_v2, 0, 0, 1, 1)
        self.radioButton_bootloader_v4 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v4.setText("v4.x")
        self.radioButton_bootloader_v4.setObjectName("radioButton_bootloader_v4")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v4, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_bootloader, 3, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_cancel = QtGui.QPushButton(BoardConfig)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_6.addWidget(self.pushButton_cancel, 0, 0, 1, 1)
        self.pushButton_ok = QtGui.QPushButton(BoardConfig)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout_6.addWidget(self.pushButton_ok, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 9, 0, 1, 1)
        self.label_warning = QtGui.QLabel(BoardConfig)
        self.label_warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_5.addWidget(self.label_warning, 8, 0, 1, 1)
        self.groupBox_devices_32 = QtGui.QGroupBox(BoardConfig)
        self.groupBox_devices_32.setObjectName("groupBox_devices_32")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_devices_32)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_device_32 = QtGui.QGridLayout()
        self.gridLayout_device_32.setObjectName("gridLayout_device_32")
        self.gridLayout_7.addLayout(self.gridLayout_device_32, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_32, 6, 0, 1, 1)
        self.groupBox_extra = QtGui.QGroupBox(BoardConfig)
        self.groupBox_extra.setObjectName("groupBox_extra")
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_extra)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.checkBox_heapsize = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_heapsize.setObjectName("checkBox_heapsize")
        self.gridLayout_8.addWidget(self.checkBox_heapsize, 0, 0, 1, 1)
        self.checkBox_mips16 = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_mips16.setObjectName("checkBox_mips16")
        self.gridLayout_8.addWidget(self.checkBox_mips16, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_extra, 1, 0, 1, 1)

        self.retranslateUi(BoardConfig)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.groupBox_extra.setVisible)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.groupBox_devices_32.setVisible)
        QtCore.QObject.connect(self.radioButton_arch_8, QtCore.SIGNAL("toggled(bool)"), self.groupBox_devices_8.setVisible)
        QtCore.QObject.connect(self.groupBox_arch, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setVisible)
        QtCore.QObject.connect(self.radioButton_mode_bootloader, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setVisible)
        QtCore.QObject.connect(self.radioButton_mode_icsp, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setHidden)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setHidden)
        QtCore.QMetaObject.connectSlotsByName(BoardConfig)

    def retranslateUi(self, BoardConfig):
        BoardConfig.setWindowTitle(QtGui.QApplication.translate("BoardConfig", "Board Config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_arch.setTitle(QtGui.QApplication.translate("BoardConfig", "Architecture", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_8.setText(QtGui.QApplication.translate("BoardConfig", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_32.setText(QtGui.QApplication.translate("BoardConfig", "32-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_mode.setTitle(QtGui.QApplication.translate("BoardConfig", "Progamming mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_mode_bootloader.setText(QtGui.QApplication.translate("BoardConfig", "Bootloader", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_8.setTitle(QtGui.QApplication.translate("BoardConfig", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_bootloader.setTitle(QtGui.QApplication.translate("BoardConfig", "Bootloader", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("BoardConfig", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ok.setText(QtGui.QApplication.translate("BoardConfig", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.label_warning.setText(QtGui.QApplication.translate("BoardConfig", "warning!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_32.setTitle(QtGui.QApplication.translate("BoardConfig", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_extra.setTitle(QtGui.QApplication.translate("BoardConfig", "32-bit extra options", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_heapsize.setText(QtGui.QApplication.translate("BoardConfig", "HEAPSIZE", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_mips16.setText(QtGui.QApplication.translate("BoardConfig", "MIPS16", None, QtGui.QApplication.UnicodeUTF8))

