# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Title_block.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 160)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Layout = QtWidgets.QHBoxLayout()
        self.Layout.setObjectName("Layout")
        self.label_combox = QtWidgets.QComboBox(Form)
        self.label_combox.setObjectName("label_combox")
        self.Layout.addWidget(self.label_combox)
        self.search_edit = QtWidgets.QLineEdit(Form)
        self.search_edit.setObjectName("search_edit")
        self.Layout.addWidget(self.search_edit)
        self.search_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setObjectName("search_button")
        self.Layout.addWidget(self.search_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout.addItem(spacerItem)
        self.Layout.setStretch(0, 1)
        self.Layout.setStretch(1, 5)
        self.Layout.setStretch(2, 1)
        self.Layout.setStretch(3, 20)
        self.verticalLayout.addLayout(self.Layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_button.setText(_translate("Form", "搜索"))
