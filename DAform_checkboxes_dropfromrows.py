from DApandaswidget import PandasModel
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
        Form_CheckBoxes.resize(909, 636)
        self.checkBox_nan = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_nan.setGeometry(QtCore.QRect(50, 440, 131, 19))
        self.checkBox_nan.setObjectName("checkBox_nan")
        self.checkBox_missingvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_missingvalue.setGeometry(QtCore.QRect(50, 470, 141, 19))
        self.checkBox_missingvalue.setObjectName("checkBox_missingvalue")
        self.checkBox_value = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_value.setGeometry(QtCore.QRect(50, 500, 131, 19))
        self.checkBox_value.setObjectName("checkBox_value")
        self.pushButton_apply = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_apply.setGeometry(QtCore.QRect(50, 570, 80, 21))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_drop = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_drop.setGeometry(QtCore.QRect(30, 410, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setObjectName("label_drop")
        self.lineEdit_filepath_checkboxes = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_filepath_checkboxes.setGeometry(QtCore.QRect(20, 20, 771, 21))
        self.lineEdit_filepath_checkboxes.setObjectName("lineEdit_filepath_checkboxes")
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(810, 20, 80, 21))
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.tableView_dropfromrows = QtWidgets.QTableView(Form_CheckBoxes)
        self.tableView_dropfromrows.setGeometry(QtCore.QRect(20, 60, 871, 341))
        self.tableView_dropfromrows.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_dropfromrows.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_dropfromrows.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_dropfromrows.setObjectName("tableView_dropfromrows")
        self.checkBox_valueendswith = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_valueendswith.setGeometry(QtCore.QRect(50, 530, 101, 19))
        self.checkBox_valueendswith.setObjectName("checkBox_valueendswith")

        self.lineEdit_filepath_checkboxes.setText('')
        self.pushButton_apply.clicked.connect(self.on_apply_clicked)
        self.pushButton_loadfile.clicked.connect(self.on_loadFilecheckboxes_clicked)

        self.retranslateUi(Form_CheckBoxes)
        QtCore.QMetaObject.connectSlotsByName(Form_CheckBoxes)

    def retranslateUi(self, Form_CheckBoxes):
        _translate = QtCore.QCoreApplication.translate
        Form_CheckBoxes.setWindowTitle(_translate("Form_CheckBoxes", "Drop from rows"))
        self.checkBox_nan.setText(_translate("Form_CheckBoxes", "nan values in file"))
        self.checkBox_missingvalue.setText(_translate("Form_CheckBoxes", "missing value in column "))
        self.checkBox_value.setText(_translate("Form_CheckBoxes", "specific value in column"))
        self.pushButton_apply.setText(_translate("Form_CheckBoxes", "Apply"))
        self.label_drop.setText(_translate("Form_CheckBoxes", "Drop"))
        self.pushButton_loadfile.setText(_translate("Form_CheckBoxes", "Load file"))
        self.checkBox_valueendswith.setText(_translate("Form_CheckBoxes", "value ends with "))

    def select_column(self):
        col_nb = self.tableView_dropfromrows.currentIndex().column()
        column_name = self.tableView_dropfromrows.model().headerData(col_nb, QtCore.Qt.Horizontal,
                                                                  QtCore.Qt.DisplayRole)
        return column_name

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_dropfromrows.setModel(model)

    def on_loadFilecheckboxes_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepath_checkboxes.setText(fileName)
            df = pd.read_csv(fileName, low_memory=False)
            model = PandasModel(df.head(10))
            self.tableView_dropfromrows.setModel(model)

    def on_apply_clicked(self):
        file = self.lineEdit_filepath_checkboxes.text()
        if file == '':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
        if file != '':
            exists = os.path.isfile(file)
            if exists:
                df = pd.read_csv(file)
                header = self.select_column()
                if (len(header) < 1):
                    QMessageBox.information(None, "Error ",
                                            "You must select a column.\nTry again",
                                            QMessageBox.Ok)
                if len(header) >= 1:
                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked():
                        QMessageBox.information(None, "Error",
                                                "Please check at least one of the above cases.",
                                                QMessageBox.Ok)
                    if self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked():
                        if not np.where(df.applymap(lambda x: x == '')):
                            QMessageBox.information(None, "Error",
                                                    "NAN values do not exist in the column "  +header + "selected.",
                                                    QMessageBox.Ok)
                        if np.where(df.applymap(lambda x: x == '')):
                            df1 = df.dropna(how='any')
                            dir = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            df1.to_csv( dir + '\\'+ file_name1 + '_droppedNAN.csv', index=None)
                            QMessageBox.information(None, "NAN dropped",
                                                    "NAN values have been dropped from all the files.",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath_checkboxes.setText(dir + '/'+ file_name1 + '_droppedNAN.csv')
                            self.reloaddata_fromfilepath(dir + '/'+ file_name1 + '_droppedNAN.csv')
                            # Form_CheckBoxes.hide()

                    if self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not self.checkBox_nan.isChecked() and not \
                            self.checkBox_valueendswith.isChecked():

                        if df[header].dtypes != str:
                            df = pd.read_csv(file,
                                             dtype={header: str})
                            df[header].fillna("missing", inplace=True)
                            if any(df[header] == 'missing') == False:
                                QMessageBox.information(None, "No missing values",
                                                        "No missing values to drop in the column " + str(header) +".\nNo file to save.", QMessageBox.Ok)
                            if any(df[header] == 'missing') == True:
                                d = df[df[header] == 'missing']
                                df.drop(df.loc[df[header] == 'missing'].index, inplace=True)
                                dir = os.path.dirname(file)
                                file_name1 = os.path.splitext(os.path.basename(file))[0]
                                df.to_csv(dir + '\\' + file_name1 + '_droppedMissingValues.csv', index=None)
                                QMessageBox.information(None, "Missing values",
                                                        str(len(d)) + " empty cells have been dropped from the column " +  str(header) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.lineEdit_filepath_checkboxes.setText(dir + '/' + file_name1 + '_droppedMissingValues.csv')
                                self.reloaddata_fromfilepath(dir + '\\' + file_name1 + '_droppedMissingValues.csv')

                        if df[header].dtypes == str:
                            df[header].fillna("missing", inplace=True)
                            if any(df[header] == 'missing') == False:
                                QMessageBox.information(None, "No missing values",
                                                        "No missing values to drop in the column " + str(header) +".\nNo file to save.", QMessageBox.Ok)
                            if any(df[header] == 'missing') == True:
                                d = df[df[header] == 'missing']
                                df.drop(df.loc[df[header] == 'missing'].index, inplace=True)
                                dir = os.path.dirname(file)
                                file_name1 = os.path.splitext(os.path.basename(file))[0]
                                df.to_csv(dir + '\\' + file_name1 + '_droppedMissingValues.csv', index=None)
                                QMessageBox.information(None, "Missing values",
                                                        str(len(d)) + " empty cells have been dropped from the column " +  str(header) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.lineEdit_filepath_checkboxes.setText(dir + '/' + file_name1 + '_droppedMissingValues.csv')
                                self.reloaddata_fromfilepath(dir + '\\' + file_name1 + '_droppedMissingValues.csv')
                                # Form_CheckBoxes.hide()

                    if self.checkBox_valueendswith.isChecked() and not self.checkBox_value.isChecked() and not self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_nan.isChecked():
                        value_in_rows, okPressed = QInputDialog.getText(None,
                                                                        "Enter a value to drop from " + str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        df_dropped = df.drop(df[(df[header].str.contains(value_in_rows))].index)
                        dir = os.path.dirname(file)
                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                        df_dropped.to_csv(dir + '\\' + file_name1 + '_droppedvaluesendwith.csv', index=None)
                        QMessageBox.information(None, "Value ends with " + str(value_in_rows) + "dropped",
                                                "All values end with " + str(value_in_rows) + " have been dropped from the file.",
                                                QMessageBox.Ok)
                        self.lineEdit_filepath_checkboxes.setText(dir + '/' + file_name1 + '_droppedvaluesendwith.csv')
                        self.reloaddata_fromfilepath(dir + '/' + file_name1 + '_droppedvaluesendwith.csv')

                    if self.checkBox_value.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_nan.isChecked() and not \
                            self.checkBox_valueendswith.isChecked():
                        value_in_rows, okPressed = QInputDialog.getText(None, "Enter a value to drop from " +  str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        # if type(value_in_rows) == int:
                        if not np.where(df.applymap(lambda x: x == value_in_rows)):
                            print('1f')
                        if np.where(df.applymap(lambda x: x == value_in_rows)):
                            df = df[(df[[header]] != value_in_rows).all(axis=1)]
                            dir = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            df.to_csv(dir + '\\' + file_name1 + '_droppedValue_str.csv', index=None)
                            QMessageBox.information(None, "Specific values",
                                                    "The value " + str(value_in_rows) + " have been dropped from " + str(header) ,
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath_checkboxes.setText(dir + '/' + file_name1 + '_droppedValue_str.csv')
                            self.reloaddata_fromfilepath(dir + '\\' + file_name1 + '_droppedValue_str.csv')

            else:
                QMessageBox.information(None, "Error",
                                        "The loaded file does not exist anymore.\nPlease load a file.",
                                        QMessageBox.Ok)

                     # Form_CheckBoxes.hide()

                    # if type(value_in_rows) == str:
                    #
                    #     value_in_rows_str = str(value_in_rows)
                    #     df.drop(df.loc[df[header] == value_in_rows_str].index, inplace=True)
                    #     dir = os.path.dirname(file)
                    #     file_name1 = os.path.splitext(os.path.basename(file))[0]
                    #     df.to_csv(dir + '\\' + file_name1 + '_droppedValue_str.csv', index=None)
                    #     QMessageBox.information(None, "Specific values",
                    #                             "The value " + str(value_in_rows) + " have been dropped from " + str(header) ,
                    #                             QMessageBox.Ok)
                    #     self.lineEdit_filepath_checkboxes.setText(dir + '/' + file_name1 + '_droppedValue_str.csv')
                    #     self.reloaddata_fromfilepath(dir + '\\' + file_name1 + '_droppedValue_str.csv')
                    #      # Form_CheckBoxes.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_CheckBoxes = QtWidgets.QWidget()
    ui = Ui_Form_CheckBoxes()
    ui.setupUi(Form_CheckBoxes)
    Form_CheckBoxes.show()
    sys.exit(app.exec_())

