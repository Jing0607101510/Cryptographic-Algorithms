# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElGamal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 735)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 171, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 10, 161, 31))
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 10, 181, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 50, 411, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 90, 491, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(320, 100, 72, 15))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 260, 581, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 72, 15))
        self.label_8.setObjectName("label_8")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(70, 280, 491, 111))
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 550, 72, 15))
        self.label_9.setObjectName("label_9")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 540, 491, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gen_key = QtWidgets.QPushButton(Form)
        self.gen_key.setGeometry(QtCore.QRect(70, 140, 93, 28))
        self.gen_key.setObjectName("gen_key")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 180, 421, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gen_random = QtWidgets.QPushButton(Form)
        self.gen_random.setGeometry(QtCore.QRect(70, 220, 93, 28))
        self.gen_random.setObjectName("gen_random")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(70, 400, 491, 121))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 72, 15))
        self.label_10.setObjectName("label_10")
        self.gen = QtWidgets.QPushButton(Form)
        self.gen.setGeometry(QtCore.QRect(70, 690, 93, 28))
        self.gen.setObjectName("gen")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(220, 690, 93, 28))
        self.clear1.setObjectName("clear1")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(570, -20, 20, 731))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 131, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(590, 50, 361, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(590, 300, 72, 15))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(590, 160, 121, 16))
        self.label_12.setObjectName("label_12")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(590, 180, 361, 111))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(600, 550, 121, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(590, 580, 361, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.varify = QtWidgets.QPushButton(Form)
        self.varify.setGeometry(QtCore.QRect(600, 630, 93, 28))
        self.varify.setObjectName("varify")
        self.clear2 = QtWidgets.QPushButton(Form)
        self.clear2.setGeometry(QtCore.QRect(740, 630, 93, 28))
        self.clear2.setObjectName("clear2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "素数"))
        self.label_2.setText(_translate("Form", "素数的本原根"))
        self.lineEdit_1.setText(_translate("Form", "1004535809"))
        self.lineEdit_2.setText(_translate("Form", "3"))
        self.label_3.setText(_translate("Form", "随机数（a私钥）"))
        self.label_5.setText(_translate("Form", "公钥"))
        self.label_8.setText(_translate("Form", "明文："))
        self.label_9.setText(_translate("Form", "数字签名："))
        self.gen_key.setText(_translate("Form", "密钥生成"))
        self.label_4.setText(_translate("Form", "选择的随机数K"))
        self.gen_random.setText(_translate("Form", "随机数生成"))
        self.label_10.setText(_translate("Form", "SHA512："))
        self.gen.setText(_translate("Form", "生成"))
        self.clear1.setText(_translate("Form", "清除"))
        self.label_6.setText(_translate("Form", "消息的Hash码："))
        self.label_12.setText(_translate("Form", "获取的数字签名："))
        self.label_13.setText(_translate("Form", "签名是否合法："))
        self.varify.setText(_translate("Form", "验证"))
        self.clear2.setText(_translate("Form", "清除"))

