from DAform_table_label import Ui_form_table_label
from keras.layers import Dropout
from keras.utils.training_utils import multi_gpu_model
from keras.layers import add, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Input, Dense
from keras.models import Model
from keras.layers.convolutional import Conv2D
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_traindl.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_checkboxes_trainDL(object):

    def openwindow_form_tablelabel(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_form_table_label()
        self.class_nb = self.ui.lineEdit_class.text()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, form_checkboxes_trainDL):
        form_checkboxes_trainDL.setObjectName("form_checkboxes_trainDL")
        form_checkboxes_trainDL.resize(275, 347)
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
        self.pushButton_applymodel.setGeometry(QtCore.QRect(80, 270, 91, 31))
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
        self.checkBox_toyresnet = QtWidgets.QCheckBox(form_checkboxes_trainDL)
        self.checkBox_toyresnet.setGeometry(QtCore.QRect(80, 220, 101, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_toyresnet.setFont(font)
        self.checkBox_toyresnet.setObjectName("checkBox_toyresnet")

        self.pushButton_applymodel.clicked.connect(self.on_applymodel_clicked)

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
        self.checkBox_toyresnet.setText(_translate("form_checkboxes_trainDL", "Toy Resnet"))

    def on_applymodel_clicked(self):
        if not self.checkBox_densenet.isChecked() and not self.checkBox_inceptionresnet.isChecked() \
                and not self.checkBox_nasnet.isChecked() and not self.checkBox_nasnetlarge.isChecked() \
                and self.checkBox_toyresnet.isChecked():
            # input shape to enter in parameters
            inputs = Input(shape=(256,256,3), name='img')
            x = Conv2D(32, 3, activation='relu')(inputs)
            x = Conv2D(64, 3, activation='relu')(x)
            block_1_output = MaxPooling2D(3)(x)

            x = Conv2D(64, 3, activation='relu', padding='same')(block_1_output)
            x = Conv2D(64, 3, activation='relu', padding='same')(x)
            block_2_output = add([x, block_1_output])

            x = Conv2D(64, 3, activation='relu', padding='same')(block_2_output)
            x = Conv2D(64, 3, activation='relu', padding='same')(x)
            block_3_output = add([x, block_2_output])

            x = Conv2D(64, 3, activation='relu')(block_3_output)
            x = GlobalAveragePooling2D()(x)
            x = Dense(256, activation='relu', name='dense_layer')(x)
            x = Dropout(0.5)(x)
            outputs = Dense(self.class_nb, activation='softmax')(x)

            model = Model(inputs, outputs, name='toy_resnet')
            model = multi_gpu_model(model, gpus=4)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_checkboxes_trainDL = QtWidgets.QWidget()
    ui = Ui_form_checkboxes_trainDL()
    ui.setupUi(form_checkboxes_trainDL)
    form_checkboxes_trainDL.show()
    sys.exit(app.exec_())
