# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_humtoolow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_humtoolow(object):
    def setupUi(self, Dialog_humtoolow):
        Dialog_humtoolow.setObjectName("Dialog_humtoolow")
        Dialog_humtoolow.resize(530, 210)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_humtoolow)
        self.buttonBox.setGeometry(QtCore.QRect(167, 167, 341, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame_2 = QtWidgets.QFrame(Dialog_humtoolow)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 512, 192))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgba(255, 255, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(175, 5, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.frame_2.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(Dialog_humtoolow)
        self.buttonBox.accepted.connect(Dialog_humtoolow.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_humtoolow.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_humtoolow)

    def retranslateUi(self, Dialog_humtoolow):
        _translate = QtCore.QCoreApplication.translate
        Dialog_humtoolow.setWindowTitle(_translate("Dialog_humtoolow", "Dialog"))
        self.label.setText(_translate("Dialog_humtoolow", "警告：湿度过低！"))
        self.label_2.setText(_translate("Dialog_humtoolow", "该节点处湿度过低！请及时检查车间情况，确保生产安全！"))
        self.label_3.setText(_translate("Dialog_humtoolow", "正常湿度范围：50%-60%"))
