# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeabreezeGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gb_spec = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_spec.setEnabled(False)
        self.gb_spec.setObjectName("gb_spec")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_spec)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gb_spec_int_time = QtWidgets.QGroupBox(self.gb_spec)
        self.gb_spec_int_time.setMinimumSize(QtCore.QSize(0, 0))
        self.gb_spec_int_time.setObjectName("gb_spec_int_time")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gb_spec_int_time)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sb_spec_int_time = QtWidgets.QSpinBox(self.gb_spec_int_time)
        self.sb_spec_int_time.setMinimum(10)
        self.sb_spec_int_time.setMaximum(10000)
        self.sb_spec_int_time.setSingleStep(10)
        self.sb_spec_int_time.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.sb_spec_int_time.setObjectName("sb_spec_int_time")
        self.horizontalLayout.addWidget(self.sb_spec_int_time)
        self.bt_spec_set_int_time = QtWidgets.QPushButton(self.gb_spec_int_time)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_spec_set_int_time.sizePolicy().hasHeightForWidth())
        self.bt_spec_set_int_time.setSizePolicy(sizePolicy)
        self.bt_spec_set_int_time.setObjectName("bt_spec_set_int_time")
        self.horizontalLayout.addWidget(self.bt_spec_set_int_time)
        self.gridLayout_2.addWidget(self.gb_spec_int_time, 2, 0, 1, 1)
        self.gb_spec_acquisition = QtWidgets.QGroupBox(self.gb_spec)
        self.gb_spec_acquisition.setObjectName("gb_spec_acquisition")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gb_spec_acquisition)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_spec_acquire = QtWidgets.QPushButton(self.gb_spec_acquisition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_spec_acquire.sizePolicy().hasHeightForWidth())
        self.bt_spec_acquire.setSizePolicy(sizePolicy)
        self.bt_spec_acquire.setObjectName("bt_spec_acquire")
        self.horizontalLayout_2.addWidget(self.bt_spec_acquire)
        self.line = QtWidgets.QFrame(self.gb_spec_acquisition)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.rb_spec_contin_acquisition = QtWidgets.QRadioButton(self.gb_spec_acquisition)
        self.rb_spec_contin_acquisition.setObjectName("rb_spec_contin_acquisition")
        self.horizontalLayout_2.addWidget(self.rb_spec_contin_acquisition)
        self.gridLayout_2.addWidget(self.gb_spec_acquisition, 2, 1, 1, 1)
        self.lbl_spec_status = QtWidgets.QLabel(self.gb_spec)
        self.lbl_spec_status.setObjectName("lbl_spec_status")
        self.gridLayout_2.addWidget(self.lbl_spec_status, 0, 0, 1, 2)
        self.spectrum_plot = GraphicsLayoutWidget(self.gb_spec)
        self.spectrum_plot.setObjectName("spectrum_plot")
        self.gridLayout_2.addWidget(self.spectrum_plot, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.gb_spec, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSpectrometer = QtWidgets.QMenu(self.menubar)
        self.menuSpectrometer.setObjectName("menuSpectrometer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_connect_spec = QtWidgets.QAction(MainWindow)
        self.action_connect_spec.setObjectName("action_connect_spec")
        self.action_disconnect_spec = QtWidgets.QAction(MainWindow)
        self.action_disconnect_spec.setEnabled(False)
        self.action_disconnect_spec.setObjectName("action_disconnect_spec")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_connect_camera = QtWidgets.QAction(MainWindow)
        self.action_connect_camera.setObjectName("action_connect_camera")
        self.action_disconnect_camera = QtWidgets.QAction(MainWindow)
        self.action_disconnect_camera.setEnabled(False)
        self.action_disconnect_camera.setObjectName("action_disconnect_camera")
        self.menuFile.addAction(self.action_save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuSpectrometer.addAction(self.action_connect_spec)
        self.menuSpectrometer.addAction(self.action_disconnect_spec)
        self.menuSpectrometer.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSpectrometer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PL-Microscope"))
        self.gb_spec.setTitle(_translate("MainWindow", "Spectrometer"))
        self.gb_spec_int_time.setTitle(_translate("MainWindow", "Integration Time / ms"))
        self.bt_spec_set_int_time.setText(_translate("MainWindow", "Set"))
        self.gb_spec_acquisition.setTitle(_translate("MainWindow", "Spectromter Acquisition"))
        self.bt_spec_acquire.setText(_translate("MainWindow", "Aquire Spectrum"))
        self.rb_spec_contin_acquisition.setText(_translate("MainWindow", "Continuous Acquisition"))
        self.lbl_spec_status.setText(_translate("MainWindow", "No spectrometer connected"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSpectrometer.setTitle(_translate("MainWindow", "Spectrometer"))
        self.action_connect_spec.setText(_translate("MainWindow", "Connect"))
        self.action_disconnect_spec.setText(_translate("MainWindow", "Disconnect"))
        self.action_save.setText(_translate("MainWindow", "&Save"))
        self.action_save.setStatusTip(_translate("MainWindow", "Save current spectrum and image"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_quit.setText(_translate("MainWindow", "&Quit"))
        self.action_quit.setStatusTip(_translate("MainWindow", "Quit the application"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_connect_camera.setText(_translate("MainWindow", "Connect"))
        self.action_disconnect_camera.setText(_translate("MainWindow", "Disconnect"))
from pyqtgraph import GraphicsLayoutWidget