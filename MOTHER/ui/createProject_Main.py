# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\256\PROJECTS\NSI\PREP\PIPELINE\.dev\UI\createProject_Main_02.ui'
#
# Created: Thu Jul 05 11:55:45 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateProject(object):
    def setupUi(self, CreateProject):
        CreateProject.setObjectName("CreateProject")
        CreateProject.resize(340, 348)
        self.centralwidget = QtGui.QWidget(CreateProject)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_setFolder = QtGui.QPushButton(self.groupBox_2)
        self.btn_setFolder.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_setFolder.setObjectName("btn_setFolder")
        self.verticalLayout_2.addWidget(self.btn_setFolder)
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lin_name = QtGui.QLineEdit(self.groupBox)
        self.lin_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lin_name.setObjectName("lin_name")
        self.verticalLayout_3.addWidget(self.lin_name)
        self.verticalLayout.addWidget(self.splitter)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lab_path = QtGui.QLabel(self.groupBox_3)
        self.lab_path.setObjectName("lab_path")
        self.verticalLayout_4.addWidget(self.lab_path)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.chb_skipSG = QtGui.QCheckBox(self.groupBox_4)
        self.chb_skipSG.setEnabled(True)
        self.chb_skipSG.setChecked(True)
        self.chb_skipSG.setObjectName("chb_skipSG")
        self.verticalLayout_5.addWidget(self.chb_skipSG)
        self.btn_setupSG = QtGui.QPushButton(self.groupBox_4)
        self.btn_setupSG.setObjectName("btn_setupSG")
        self.verticalLayout_5.addWidget(self.btn_setupSG)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.btn_create = QtGui.QPushButton(self.centralwidget)
        self.btn_create.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_create.setObjectName("btn_create")
        self.verticalLayout.addWidget(self.btn_create)
        CreateProject.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CreateProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CreateProject.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CreateProject)
        self.statusbar.setObjectName("statusbar")
        CreateProject.setStatusBar(self.statusbar)
        self.act_docs = QtGui.QAction(CreateProject)
        self.act_docs.setObjectName("act_docs")
        self.act_help = QtGui.QAction(CreateProject)
        self.act_help.setObjectName("act_help")
        self.menuHelp.addAction(self.act_docs)
        self.menuHelp.addAction(self.act_help)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(CreateProject)
        QtCore.QMetaObject.connectSlotsByName(CreateProject)

    def retranslateUi(self, CreateProject):
        CreateProject.setWindowTitle(QtGui.QApplication.translate("CreateProject", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CreateProject", "Project Location", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_setFolder.setText(QtGui.QApplication.translate("CreateProject", " SET LOCATION", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CreateProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("CreateProject", "Project Root Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_path.setText(QtGui.QApplication.translate("CreateProject", "C:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("CreateProject", "Shotgun Project Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_skipSG.setText(QtGui.QApplication.translate("CreateProject", "Skip Shotgun project creation", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_setupSG.setText(QtGui.QApplication.translate("CreateProject", "SETUP SHOTGUN PROJECT", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create.setText(QtGui.QApplication.translate("CreateProject", "CREATE PROJECT", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("CreateProject", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.act_docs.setText(QtGui.QApplication.translate("CreateProject", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.act_help.setText(QtGui.QApplication.translate("CreateProject", "Create Project help", None, QtGui.QApplication.UnicodeUTF8))

