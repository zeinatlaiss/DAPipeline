# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_traindl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_checkboxes_trainDL(object):
    def setupUi(self, form_checkboxes_trainDL):
        form_checkboxes_trainDL.setObjectName("form_checkboxes_trainDL")
        form_checkboxes_trainDL.resize(308, 288)
        self.checkBox_nasnet = QtWidgets.QCheckBox(form_checkboxes_trainDL)
        self.checkBox_nasnet.setGeometry(QtCore.QRect(80, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_nasnet.setFont(font)
        self.checkBox_nasnet.setObjectName("checkBox_nasnet")
        self.checkBox_nasnetlarge = QtWidgets.QCheckBox(form_checkboxes_trainDL)
        self.checkBox_nasnetlarge.setGeometry(QtCore.QRect(80, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_nasnetlarge.setFont(font)
        self.checkBox_nasnetlarge.setObjectName("checkBox_nasnetlarge")
        self.checkBox_inceptionresnet = QtWidgets.QCheckBox(form_checkboxes_trainDL)
        self.checkBox_inceptionresnet.setGeometry(QtCore.QRect(80, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_inceptionresnet.setFont(font)
        self.checkBox_inceptionresnet.setObjectName("checkBox_inceptionresnet")
        self.checkBox_densenet = QtWidgets.QCheckBox(form_checkboxes_trainDL)
        self.checkBox_densenet.setGeometry(QtCore.QRect(80, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_densenet.setFont(font)
        self.checkBox_densenet.setObjectName("checkBox_densenet")
        self.pushButton_applymodel = QtWidgets.QPushButton(form_checkboxes_trainDL)
        self.pushButton_applymodel.setGeometry(QtCore.QRect(80, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_applymodel.setFont(font)
        self.pushButton_applymodel.setObjectName("pushButton_applymodel")
        self.label = QtWidgets.QLabel(form_checkboxes_trainDL)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(form_checkboxes_trainDL)
        QtCore.QMetaObject.connectSlotsByName(form_checkboxes_trainDL)

    def retranslateUi(self, form_checkboxes_trainDL):
        _translate = QtCore.QCoreApplication.translate
        form_checkboxes_trainDL.setWindowTitle(_translate("form_checkboxes_trainDL", "Deep learning models"))
        self.checkBox_nasnet.setText(_translate("form_checkboxes_trainDL", "NASNET"))
        self.checkBox_nasnetlarge.setText(_translate("form_checkboxes_trainDL", "NASNET LARGE"))
        self.checkBox_inceptionresnet.setText(_translate("form_checkboxes_trainDL", "Inception RESNET"))
        self.checkBox_densenet.setText(_translate("form_checkboxes_trainDL", "Dense NET"))
        self.pushButton_applymodel.setText(_translate("form_checkboxes_trainDL", "Apply"))
        self.label.setText(_translate("form_checkboxes_trainDL", "Choose a model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_checkboxes_trainDL = QtWidgets.QWidget()
    ui = Ui_form_checkboxes_trainDL()
    ui.setupUi(form_checkboxes_trainDL)
    form_checkboxes_trainDL.show()
    sys.exit(app.exec_())

