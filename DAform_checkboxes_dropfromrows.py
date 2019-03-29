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
        Form_CheckBoxes.resize(957, 668)
        self.checkBox_nan = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_nan.setGeometry(QtCore.QRect(20, 500, 131, 19))
        self.checkBox_nan.setObjectName("checkBox_nan")
        self.checkBox_missingvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_missingvalue.setGeometry(QtCore.QRect(20, 530, 141, 19))
        self.checkBox_missingvalue.setObjectName("checkBox_missingvalue")
        self.checkBox_value = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_value.setGeometry(QtCore.QRect(20, 560, 131, 19))
        self.checkBox_value.setObjectName("checkBox_value")
        self.pushButton_apply = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_apply.setGeometry(QtCore.QRect(850, 600, 80, 21))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_drop = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_drop.setGeometry(QtCore.QRect(20, 470, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setObjectName("label_drop")
        self.lineEdit_filepath_checkboxes = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_filepath_checkboxes.setGeometry(QtCore.QRect(20, 20, 791, 21))
        self.lineEdit_filepath_checkboxes.setObjectName("lineEdit_filepath_checkboxes")
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(850, 20, 80, 21))
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.tableView_dropfromrows = QtWidgets.QTableView(Form_CheckBoxes)
        self.tableView_dropfromrows.setGeometry(QtCore.QRect(20, 60, 911, 381))
        self.tableView_dropfromrows.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_dropfromrows.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_dropfromrows.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_dropfromrows.setObjectName("tableView_dropfromrows")
        self.checkBox_valueendswith = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_valueendswith.setGeometry(QtCore.QRect(20, 590, 101, 19))
        self.checkBox_valueendswith.setObjectName("checkBox_valueendswith")
        self.label_rename = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_rename.setGeometry(QtCore.QRect(270, 470, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rename.setFont(font)
        self.label_rename.setObjectName("label_rename")
        self.lineEdit_valuetorename_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetorename_text.setGeometry(QtCore.QRect(340, 500, 131, 21))
        self.lineEdit_valuetorename_text.setText("")
        self.lineEdit_valuetorename_text.setObjectName("lineEdit_valuetorename_text")
        self.lineEdit_newvalue_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_newvalue_text.setGeometry(QtCore.QRect(502, 500, 131, 21))
        self.lineEdit_newvalue_text.setText("")
        self.lineEdit_newvalue_text.setObjectName("lineEdit_newvalue_text")
        self.checkBox_text = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_text.setGeometry(QtCore.QRect(270, 500, 72, 19))
        self.checkBox_text.setObjectName("checkBox_text")
        self.label = QtWidgets.QLabel(Form_CheckBoxes)
        self.label.setGeometry(QtCore.QRect(480, 500, 21, 16))
        self.label.setObjectName("label")
        self.label_keep = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_keep.setGeometry(QtCore.QRect(700, 470, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_keep.setFont(font)
        self.label_keep.setObjectName("label_keep")
        self.checkBox_keepvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_keepvalue.setGeometry(QtCore.QRect(700, 500, 101, 19))
        self.checkBox_keepvalue.setObjectName("checkBox_keepvalue")
        self.lineEdit_valuetokeep = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetokeep.setGeometry(QtCore.QRect(800, 500, 131, 21))
        self.lineEdit_valuetokeep.setText("")
        self.lineEdit_valuetokeep.setObjectName("lineEdit_valuetokeep")

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
        self.label_drop.setText(_translate("Form_CheckBoxes", "Drop from rows"))
        self.pushButton_loadfile.setText(_translate("Form_CheckBoxes", "Load file"))
        self.checkBox_valueendswith.setText(_translate("Form_CheckBoxes", "value ends with "))
        self.label_rename.setText(_translate("Form_CheckBoxes", "Rename values in rows"))
        self.checkBox_text.setText(_translate("Form_CheckBoxes", "Rename"))
        self.label.setText(_translate("Form_CheckBoxes", "to"))
        self.label_keep.setText(_translate("Form_CheckBoxes", "Keep values in rows"))
        self.checkBox_keepvalue.setText(_translate("Form_CheckBoxes", "Keep the value"))


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
            model = PandasModel(df.head(500))
            self.tableView_dropfromrows.setModel(model)

    def loadFile(self):
        fileName = self.lineEdit_filepath_checkboxes.text()
        df = pd.read_csv(fileName, low_memory=False)
        model = PandasModel(df.head(500))
        self.tableView_dropfromrows.setModel(model)
        self.df = df

    def on_apply_clicked(self):
        file = self.lineEdit_filepath_checkboxes.text()
        if file == '':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
        if file != '':

            exists = os.path.isfile(file)
            if exists:
                t1 = os.path.dirname(file)
                file_name1 = os.path.splitext(os.path.basename(file))[0]
                df = pd.read_csv(file)
                header = self.select_column()
                if (len(header) < 1):
                    QMessageBox.information(None, "Error ",
                                            "You must select a column.\nTry again",
                                            QMessageBox.Ok)
                if len(header) >= 1:
                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_text.isChecked() and not self.checkBox_keepvalue.isChecked() :
                        QMessageBox.information(None, "Error",
                                                "Please check at least one of the cases.",
                                                QMessageBox.Ok)

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_text.isChecked() and self.checkBox_keepvalue.isChecked():
                        df = pd.read_csv(file)
                        header = self.select_column()

                        if len(header) ==0:
                            QMessageBox.information(None, "Error ",
                                                    "You must select a column.\nTry again",
                                                    QMessageBox.Ok)
                        if len(header) > 0:
                            df = pd.read_csv(file, dtype={header: str})
                            if self.lineEdit_valuetokeep.text() not in df[header].values:
                                QMessageBox.information(None, "Error ",
                                                        "The value " + str(self.lineEdit_valuetokeep.text()) +
                                                        " does not exist in the column " + str(header) + ".\nTry again",
                                                        QMessageBox.Ok)


                            if self.lineEdit_valuetokeep.text() in df[header].values:
                                value = self.lineEdit_valuetokeep.text()
                                df = df[df[header] ==value]
                                df.to_csv(t1 + '\\' + 'kept_' + header + '_' + file_name1 + '.csv', index=None)
                                QMessageBox.information(None, "Value renamed",
                                                        "The value " + str(self.lineEdit_valuetokeep.text()) +
                                                        " has been kept in the column " + str(
                                                            header) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(
                                    t1 + '\\' + 'kept_' + header + '_' + file_name1 + '.csv')
                                self.lineEdit_filepath_checkboxes.setText(
                                    t1 + '/' + 'kept_' + header + '_' + file_name1 + '.csv')



                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked()and not self.checkBox_keepvalue.isChecked() and self.checkBox_text.isChecked():
                        df = pd.read_csv(file)
                        header = self.select_column()
                        if len(header) ==0:
                            QMessageBox.information(None, "Error ",
                                                    "You must select a column.\nTry again",
                                                    QMessageBox.Ok)
                        if len(header) > 0:
                            df = pd.read_csv(file, dtype={header: str})
                            if self.lineEdit_valuetorename_text.text() not in df[header].values:
                                QMessageBox.information(None, "Error ",
                                                            "The value " + str(self.lineEdit_valuetorename_text.text()) +
                                                        " does not exist in the column " +  str(header) + ".\nTry again",
                                                            QMessageBox.Ok)
                            if self.lineEdit_valuetorename_text.text() in df[header].values:
                                df[header] = df[header].replace(
                                    {self.lineEdit_valuetorename_text.text(): self.lineEdit_newvalue_text.text()})
                                df.to_csv(t1 + '\\' + 'renamed_' + header + '_' + file_name1 + '.csv', index=None)
                                QMessageBox.information(None, "Value renamed",
                                                        "The value " + str(self.lineEdit_valuetorename_text.text()) +
                                                        " in the column " + str(header) + " has been renamed.\nSaved file.",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(t1 + '\\' + 'renamed_' + header + '_' + file_name1 + '.csv')
                                self.lineEdit_filepath_checkboxes.setText(
                                    t1 + '/' + 'renamed_' + header + '_' + file_name1 + '.csv')

                    if not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not self.checkBox_text.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_nan.isChecked():
                        if not np.where(df.applymap(lambda x: x == '')):
                            QMessageBox.information(None, "Error",
                                                    "NAN values do not exist in the column "  +header + "selected.",
                                                    QMessageBox.Ok)
                        if np.where(df.applymap(lambda x: x == '')):
                            df1 = df.dropna(how='any')
                            df1.to_csv( t1 + '\\'+ file_name1 + '_droppedNAN.csv', index=None)
                            QMessageBox.information(None, "NAN dropped",
                                                    "NAN values have been dropped from all the files.",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath_checkboxes.setText(t1 + '/'+ file_name1 + '_droppedNAN.csv')
                            self.reloaddata_fromfilepath(t1 + '/'+ file_name1 + '_droppedNAN.csv')
                            # Form_CheckBoxes.hide()

                    if not self.checkBox_value.isChecked() and not self.checkBox_nan.isChecked() and not self.checkBox_text.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_missingvalue.isChecked() :
                        df = pd.read_csv(file, dtype={header: str})
                        df[header].fillna("missing", inplace=True)
                        if any(df[header] == 'missing') == False:
                            QMessageBox.information(None, "No missing values",
                                                    "No missing values to drop in the column " + str(header) +".\nNo file to save.", QMessageBox.Ok)
                        if any(df[header] == 'missing') == True:
                            d = df[df[header] == 'missing']
                            df.drop(df.loc[df[header] == 'missing'].index, inplace=True)
                            df.to_csv(t1 + '\\' + file_name1 + '_droppedMissingValues.csv', index=None)
                            QMessageBox.information(None, "Missing values",
                                                    str(len(d)) + " empty cells have been dropped from the column " +  str(header) + "\nSaved file.",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath_checkboxes.setText(t1 + '/' + file_name1 + '_droppedMissingValues.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + file_name1 + '_droppedMissingValues.csv')
                            # Form_CheckBoxes.hide()

                    if not self.checkBox_value.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_text.isChecked() and not \
                            self.checkBox_nan.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_valueendswith.isChecked() :
                        value_in_rows, okPressed = QInputDialog.getText(None,
                                                                        "Enter a value to drop from " + str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        df_dropped = df.drop(df[(df[header].str.contains(value_in_rows))].index)
                        df_dropped.to_csv(t1 + '\\' + file_name1 + '_droppedvaluesendwith.csv', index=None)
                        QMessageBox.information(None, "Value ends with " + str(value_in_rows) + "dropped",
                                                "All values end with " + str(value_in_rows) + " have been dropped from the file.",
                                                QMessageBox.Ok)
                        self.lineEdit_filepath_checkboxes.setText(t1 + '/' + file_name1 + '_droppedvaluesendwith.csv')
                        self.reloaddata_fromfilepath(t1 + '/' + file_name1 + '_droppedvaluesendwith.csv')

                    if not self.checkBox_missingvalue.isChecked() and not self.checkBox_nan.isChecked() and not self.checkBox_text.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_value.isChecked() :
                        value_in_rows, okPressed = QInputDialog.getText(None, "Enter a value to drop from " +  str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        if not np.where(df.applymap(lambda x: x == value_in_rows)):
                            print('1f')
                        if np.where(df.applymap(lambda x: x == value_in_rows)):
                            df = df[(df[[header]] != value_in_rows).all(axis=1)]
                            df.to_csv(t1 + '\\' + file_name1 + '_droppedValue_str.csv', index=None)
                            QMessageBox.information(None, "Specific values",
                                                    "The value " + str(value_in_rows) + " have been dropped from " + str(header) ,
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath_checkboxes.setText(t1 + '/' + file_name1 + '_droppedValue_str.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + file_name1 + '_droppedValue_str.csv')
            else:
                QMessageBox.information(None, "Error",
                                        "The loaded file does not exist anymore.\nPlease load a file.",
                                        QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_CheckBoxes = QtWidgets.QWidget()
    ui = Ui_Form_CheckBoxes()
    ui.setupUi(Form_CheckBoxes)
    Form_CheckBoxes.show()
    sys.exit(app.exec_())

