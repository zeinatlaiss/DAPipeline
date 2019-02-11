import numpy as np
import os
from PyQt5.QtWidgets import *
import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_dropfromrows.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_CheckBoxes(object):
    def setupUi(self, Form_CheckBoxes):
        Form_CheckBoxes.setObjectName("Form_CheckBoxes")
        Form_CheckBoxes.resize(707, 281)
        self.checkBox_nan = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_nan.setGeometry(QtCore.QRect(60, 120, 72, 19))
        self.checkBox_nan.setObjectName("checkBox_nan")
        self.checkBox_missingvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_missingvalue.setGeometry(QtCore.QRect(60, 150, 91, 19))
        self.checkBox_missingvalue.setObjectName("checkBox_missingvalue")
        self.checkBox_value = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_value.setGeometry(QtCore.QRect(60, 180, 72, 19))
        self.checkBox_value.setObjectName("checkBox_value")
        self.pushButton_apply = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_apply.setGeometry(QtCore.QRect(70, 220, 80, 21))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_drop = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_drop.setGeometry(QtCore.QRect(20, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setObjectName("label_drop")
        self.lineEdit_filepath_checkboxes = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_filepath_checkboxes.setGeometry(QtCore.QRect(20, 20, 571, 21))
        self.lineEdit_filepath_checkboxes.setObjectName("lineEdit_filepath_checkboxes")
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(610, 20, 80, 21))
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")

        self.lineEdit_filepath_checkboxes.setText('')
        self.pushButton_apply.clicked.connect(self.on_apply_clicked)
        self.pushButton_loadfile.clicked.connect(self.on_loadFilecheckboxes_clicked)

        self.retranslateUi(Form_CheckBoxes)
        QtCore.QMetaObject.connectSlotsByName(Form_CheckBoxes)

    def retranslateUi(self, Form_CheckBoxes):
        _translate = QtCore.QCoreApplication.translate
        Form_CheckBoxes.setWindowTitle(_translate("Form_CheckBoxes", "Drop values from rows form "))
        self.checkBox_nan.setText(_translate("Form_CheckBoxes", "nan"))
        self.checkBox_missingvalue.setText(_translate("Form_CheckBoxes", "missing value"))
        self.checkBox_value.setText(_translate("Form_CheckBoxes", "value"))
        self.pushButton_apply.setText(_translate("Form_CheckBoxes", "Apply"))
        self.label_drop.setText(_translate("Form_CheckBoxes", "Drop"))
        self.pushButton_loadfile.setText(_translate("Form_CheckBoxes", "Load file"))

    def on_loadFilecheckboxes_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepath_checkboxes.setText(fileName)

    def show_it(self, linedit):
        self.lineEdit_filepath_checkboxes.setText(linedit)

    def on_apply_clicked(self):
        file = self.lineEdit_filepath_checkboxes.text()
        if file == '':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
        if file != '':
            df = pd.read_csv(file)
            if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked():
                QMessageBox.information(None, "Error",
                                        "Please check at least one of the above cases.",
                                        QMessageBox.Ok)
            if self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked():
                if np.where(df.applymap(lambda x: x == '')):
                    df1 = df.dropna(how='any')
                    dir = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df1.to_csv( dir + '\\'+ file_name1 + '_droppedNAN.csv', index=None)
                    QMessageBox.information(None, "NAN dropped",
                                            "NAN values have been dropped from all the files.",
                                            QMessageBox.Ok)
                    # Form_CheckBoxes.hide()

            if self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked():
                value_entered, okPressed = QInputDialog.getText(None, "Enter column name to drop nan values", "Column name ",
                                                                QLineEdit.Normal, "")

                if value_entered not in df.columns:
                    QMessageBox.information(None, "Error",
                                            "The column " + str(value_entered) + " selected is not in the file.\nTry with another column",
                                            QMessageBox.Ok)
                if value_entered in df.columns:
                    df[value_entered].fillna("missing", inplace=True)
                    df.drop(df.loc[df[value_entered] == 'missing'].index, inplace=True)
                    dir = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(dir + '\\' + file_name1 + '_droppedMissingValues.csv', index=None)
                    QMessageBox.information(None, "Missing values dropped",
                                            "Missing values have been dropped.",
                                            QMessageBox.Ok)
                # Form_CheckBoxes.hide()

            if self.checkBox_value.isChecked():
                value_entered, okPressed = QInputDialog.getText(None, "Enter column name to drop nan values",
                                                                "Column name ",
                                                                QLineEdit.Normal, "")
                if value_entered in df.columns:
                    value_in_rows, okPressed = QInputDialog.getText(None, "Enter a value to drop from " +  str(value_entered),
                                                                    "Value to drop ",
                                                                    QLineEdit.Normal, "")
                    df.drop(df.loc[df[value_entered] == value_in_rows].index, inplace=True)
                    dir = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(dir + '\\' + file_name1 + '_droppedValue.csv', index=None)
                    QMessageBox.information(None, "Missing values dropped",
                                            "Missing values have been dropped.",
                                            QMessageBox.Ok)
                # Form_CheckBoxes.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_CheckBoxes = QtWidgets.QWidget()
    ui = Ui_Form_CheckBoxes()
    ui.setupUi(Form_CheckBoxes)
    Form_CheckBoxes.show()
    sys.exit(app.exec_())

