# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_info_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 534)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 5, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        self.reset_button = QtWidgets.QPushButton(Form)
        self.reset_button.setObjectName("reset_button")
        self.gridLayout.addWidget(self.reset_button, 9, 5, 1, 1)
        self.user_des_edit = QtWidgets.QPlainTextEdit(Form)
        self.user_des_edit.setObjectName("user_des_edit")
        self.gridLayout.addWidget(self.user_des_edit, 6, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 2, 1, 1)
        self.gender_combox = QtWidgets.QComboBox(Form)
        self.gender_combox.setObjectName("gender_combox")
        self.gridLayout.addWidget(self.gender_combox, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.user_label_combox = QtWidgets.QComboBox(Form)
        self.user_label_combox.setObjectName("user_label_combox")
        self.gridLayout.addWidget(self.user_label_combox, 7, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 4, 1, 1)
        self.password_edit = QtWidgets.QLineEdit(Form)
        self.password_edit.setObjectName("password_edit")
        self.gridLayout.addWidget(self.password_edit, 1, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.user_name_edit = QtWidgets.QLineEdit(Form)
        self.user_name_edit.setObjectName("user_name_edit")
        self.gridLayout.addWidget(self.user_name_edit, 3, 4, 1, 1)
        self.uid_eidt = QtWidgets.QLineEdit(Form)
        self.uid_eidt.setObjectName("uid_eidt")
        self.gridLayout.addWidget(self.uid_eidt, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.apply_button = QtWidgets.QPushButton(Form)
        self.apply_button.setObjectName("apply_button")
        self.gridLayout.addWidget(self.apply_button, 9, 6, 1, 1)
        self.acount_edit = QtWidgets.QLineEdit(Form)
        self.acount_edit.setObjectName("acount_edit")
        self.gridLayout.addWidget(self.acount_edit, 0, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "标签"))
        self.label_3.setText(_translate("Form", "用户ID"))
        self.label_4.setText(_translate("Form", "用户名"))
        self.reset_button.setText(_translate("Form", "重置"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_6.setText(_translate("Form", "生日"))
        self.label_5.setText(_translate("Form", "性别"))
        self.label.setText(_translate("Form", "账号"))
        self.apply_button.setText(_translate("Form", "确认更改"))
        self.label_7.setText(_translate("Form", "个人简介"))
