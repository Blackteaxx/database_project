# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 864)
        self.C = QtWidgets.QWidget(MainWindow)
        self.C.setObjectName("C")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.C)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setObjectName("top_layout")
        self.verticalLayout_2.addLayout(self.top_layout)
        self.line = QtWidgets.QFrame(self.C)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.middle_layout = QtWidgets.QHBoxLayout()
        self.middle_layout.setSpacing(0)
        self.middle_layout.setObjectName("middle_layout")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.middle_layout.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setObjectName("right_layout")
        self.middle_layout.addLayout(self.right_layout)
        self.middle_layout.setStretch(0, 2)
        self.middle_layout.setStretch(1, 10)
        self.verticalLayout.addLayout(self.middle_layout)
        self.bottom_layout2 = QtWidgets.QVBoxLayout()
        self.bottom_layout2.setObjectName("bottom_layout2")
        self.line_2 = QtWidgets.QFrame(self.C)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.bottom_layout2.addWidget(self.line_2)
        self.bottom_layout = QtWidgets.QVBoxLayout()
        self.bottom_layout.setObjectName("bottom_layout")
        self.bottom_layout2.addLayout(self.bottom_layout)
        self.verticalLayout.addLayout(self.bottom_layout2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.C)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
