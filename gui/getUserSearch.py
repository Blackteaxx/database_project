# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getUserSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_getUserSearch(object):
    def setupUi(self, getUserSearch):
        getUserSearch.setObjectName("getUserSearch")
        getUserSearch.resize(711, 555)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(getUserSearch)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(getUserSearch)
        self.label.setStyleSheet("font: 16pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.getUserSearchDownLayout = QtWidgets.QHBoxLayout()
        self.getUserSearchDownLayout.setObjectName("getUserSearchDownLayout")
        self.verticalLayout.addLayout(self.getUserSearchDownLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(getUserSearch)
        QtCore.QMetaObject.connectSlotsByName(getUserSearch)

    def retranslateUi(self, getUserSearch):
        _translate = QtCore.QCoreApplication.translate
        getUserSearch.setWindowTitle(_translate("getUserSearch", "Form"))
        self.label.setText(_translate("getUserSearch", "搜索结果（用户）"))
