from DApandaswidget import PandasModel
import numpy as np
import os
from PyQt5.QtWidgets import *
import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_dropfromrows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_CheckBoxes(object):
    def setupUi(self, Form_CheckBoxes):
        Form_CheckBoxes.setObjectName("Form_CheckBoxes")
        Form_CheckBoxes.resize(702, 223)
        self.checkBox_nan = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_nan.setGeometry(QtCore.QRect(10, 50, 131, 19))
        self.checkBox_nan.setObjectName("checkBox_nan")
        self.checkBox_missingvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_missingvalue.setGeometry(QtCore.QRect(10, 80, 141, 19))
        self.checkBox_missingvalue.setObjectName("checkBox_missingvalue")
        self.checkBox_value = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_value.setGeometry(QtCore.QRect(10, 110, 131, 19))
        self.checkBox_value.setObjectName("checkBox_value")
        self.pushButton_apply = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_apply.setGeometry(QtCore.QRect(580, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_drop = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_drop.setGeometry(QtCore.QRect(10, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setObjectName("label_drop")
        self.checkBox_valueendswith = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_valueendswith.setGeometry(QtCore.QRect(10, 140, 101, 19))
        self.checkBox_valueendswith.setObjectName("checkBox_valueendswith")
        self.label_rename = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_rename.setGeometry(QtCore.QRect(200, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rename.setFont(font)
        self.label_rename.setObjectName("label_rename")
        self.lineEdit_valuetorename_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetorename_text.setGeometry(QtCore.QRect(270, 50, 131, 21))
        self.lineEdit_valuetorename_text.setText("")
        self.lineEdit_valuetorename_text.setObjectName("lineEdit_valuetorename_text")
        self.lineEdit_newvalue_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_newvalue_text.setGeometry(QtCore.QRect(270, 110, 131, 21))
        self.lineEdit_newvalue_text.setText("")
        self.lineEdit_newvalue_text.setObjectName("lineEdit_newvalue_text")
        self.checkBox_text = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_text.setGeometry(QtCore.QRect(200, 50, 72, 19))
        self.checkBox_text.setObjectName("checkBox_text")
        self.label = QtWidgets.QLabel(Form_CheckBoxes)
        self.label.setGeometry(QtCore.QRect(330, 80, 21, 16))
        self.label.setObjectName("label")
        self.label_keep = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_keep.setGeometry(QtCore.QRect(450, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_keep.setFont(font)
        self.label_keep.setObjectName("label_keep")
        self.checkBox_keepvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_keepvalue.setGeometry(QtCore.QRect(450, 50, 101, 19))
        self.checkBox_keepvalue.setObjectName("checkBox_keepvalue")
        self.lineEdit_valuetokeep = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetokeep.setGeometry(QtCore.QRect(550, 50, 131, 21))
        self.lineEdit_valuetokeep.setText("")
        self.lineEdit_valuetokeep.setObjectName("lineEdit_valuetokeep")

        self.pushButton_apply.clicked.connect(self.on_apply_clicked)

        self.retranslateUi(Form_CheckBoxes)
        QtCore.QMetaObject.connectSlotsByName(Form_CheckBoxes)

    def retranslateUi(self, Form_CheckBoxes):
        _translate = QtCore.QCoreApplication.translate
        Form_CheckBoxes.setWindowTitle(_translate("Form_CheckBoxes", "Drop from rows"))
        self.checkBox_nan.setText(_translate("Form_CheckBoxes", "nan values in file"))
        self.checkBox_missingvalue.setText(_translate("Form_CheckBoxes", "missing value in column "))
        self.checkBox_value.setText(_translate("Form_CheckBoxes", "specific value in column"))
        self.pushButton_apply.setText(_translate("Form_CheckBoxes", "APPLY"))
        self.label_drop.setText(_translate("Form_CheckBoxes", "Drop from rows"))
        self.checkBox_valueendswith.setText(_translate("Form_CheckBoxes", "value ends with "))
        self.label_rename.setText(_translate("Form_CheckBoxes", "Rename values in rows"))
        self.checkBox_text.setText(_translate("Form_CheckBoxes", "Rename"))
        self.label.setText(_translate("Form_CheckBoxes", "to"))
        self.label_keep.setText(_translate("Form_CheckBoxes", "Keep values in rows"))
        self.checkBox_keepvalue.setText(_translate("Form_CheckBoxes", "Keep the value"))

    def select_multicolumns(self):
        list_col = []
        totalColumns = self.tableView_dataframe_to_edit.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.tableView_dataframe_to_edit.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                      QtCore.Qt.DisplayRole)
            list_col.append(column_name)
        return list_col

    def getncpdsbatches(self, dataframe):
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_rows.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid_rows.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_rows.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid_rows.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'X_CPD_ID' not in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_rows.setText('No CPD_ID')
            self.label_nbbatchid_rows.setText('No BATCH_ID')
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_rows.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid_rows.setText('No BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_rows.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid_rows.setText('No X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_rows.setText('No CPD_ID')
            self.label_nbbatchid_rows.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_rows.setText('No X_CPD_ID')
            self.label_nbbatchid_rows.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_dataframe_to_edit.setModel(model)
        if 'Plate' in df.columns:
            if 'Well' not in df.columns:
                self.lineEdit_plate_rows.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_rows.setText('No wells')
                self.getncpdsbatches(df)
            if 'Well' in df.columns:
                self.lineEdit_plate_rows.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_rows.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)
            if 'WELL' in df.columns:
                self.lineEdit_plate_rows.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_rows.setText(str(len(df['WELL'])) + ' WELLs')
                self.getncpdsbatches(df)

    def setPlateWellText_intblview(self, df):
        if 'Plate' in df.columns and 'Well' in df.columns:
            self.lineEdit_plate_rows.setText(str(df['Plate'].nunique()) + ' unique plate')
            self.lineEdit_well_rows.setText(str(len(df['Well'])) + ' wells')

    def select_column(self):
        col_nb = self.tableView_dataframe_to_edit.currentIndex().column()
        column_name = self.tableView_dataframe_to_edit.model().headerData(col_nb, QtCore.Qt.Horizontal,
                                                                  QtCore.Qt.DisplayRole)
        return column_name

    # def select_column(self):
    #     col_nb = self.tableView_dropfromrows.currentIndex().column()
    #     column_name = self.tableView_dropfromrows.model().headerData(col_nb, QtCore.Qt.Horizontal,
    #                                                               QtCore.Qt.DisplayRole)
    #     return column_name
    #
    # def reloaddata_fromfilepath(self, file):
    #     df = pd.read_csv(file)
    #     model = PandasModel(df.head(500))
    #     self.tableView_dropfromrows.setModel(model)
    #
    # def on_loadFilecheckboxes_clicked(self):
    #     fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
    #                                               "",
    #                                               "CSV Files (*.csv)")
    #     if fileName:
    #         self.lineEdit_filepath_checkboxes.setText(fileName)
    #         df = pd.read_csv(fileName, low_memory=False)
    #         model = PandasModel(df.head(10))
    #         self.tableView_dropfromrows.setModel(model)

    def on_apply_clicked(self):
        file = self.lineedit_file_path_to_edit
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
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        QMessageBox.information(None, "Error",
                                                "Please check at least one of the above cases.",
                                                QMessageBox.Ok)
                    if self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                                self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        if not np.where(df.applymap(lambda x: x == '')):
                            QMessageBox.information(None, "Error",
                                                    "NAN values do not exist in the column "  +header + "selected.",
                                                    QMessageBox.Ok)
                        if np.where(df.applymap(lambda x: x == '')):
                            df1 = df.dropna(how='any')
                            QMessageBox.information(None, "NAN dropped",
                                                    "NAN values have been dropped from all the files.",
                                                    QMessageBox.Ok)
                            df1.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                            self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')
                            # Form_CheckBoxes.hide()

                    if not self.checkBox_nan.isChecked() and self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
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
                                df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                QMessageBox.information(None, "Missing values",
                                                        str(len(d)) + " empty cells have been dropped from the column " +  str(header) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                        if df[header].dtypes == str:
                            df[header].fillna("missing", inplace=True)
                            if any(df[header] == 'missing') == False:
                                QMessageBox.information(None, "No missing values",
                                                        "No missing values to drop in the column " + str(header) +".\nNo file to save.", QMessageBox.Ok)
                            if any(df[header] == 'missing') == True:
                                d = df[df[header] == 'missing']
                                df.drop(df.loc[df[header] == 'missing'].index, inplace=True)
                                df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                QMessageBox.information(None, "Missing values",
                                                        str(len(d)) + " empty cells have been dropped from the column " +  str(header) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')
                                # Form_CheckBoxes.hide()

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        value_in_rows, okPressed = QInputDialog.getText(None,
                                                                        "Enter a value to drop from " + str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        df_dropped = df.drop(df[(df[header].str.contains(value_in_rows))].index)
                        df_dropped.to_csv(self.t1_rows + '\\' + self.file_name1_rows +'.csv', index=None)
                        QMessageBox.information(None, "Value ends with " + str(value_in_rows) + "dropped",
                                                "All values end with " + str(value_in_rows) + " have been dropped from the file.",
                                                QMessageBox.Ok)
                        self.reloaddata_fromfilepath(self.t1_rows + '/' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_text.isChecked():

                        if self.lineEdit_valuetorename_text.text() not in df[header].values:
                            QMessageBox.information(None, "Error ",
                                                        "The value " + str(self.lineEdit_valuetorename_text.text()) + " does not exist in the column " +  str(header) + ".\nTry again",
                                                        QMessageBox.Ok)
                        if self.lineEdit_valuetorename_text.text() in df[header].values:
                            df[header] = df[header].replace(
                                {self.lineEdit_valuetorename_text.text(): self.lineEdit_newvalue_text.text()})
                            df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                            QMessageBox.information(None, "Value renamed",
                                                    "The value " + str(self.lineEdit_valuetorename_text.text()) + " in the column " + str(header)
                                                    + " has been renamed.\nSaved file.",
                                                    QMessageBox.Ok)
                            self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        val_keep = self.lineEdit_valuetokeep.text()
                        if val_keep == '':
                            QMessageBox.information(None, "Specific values",
                                                    "No value entered.\nPlease enter a value that you need to keep.",
                                                    QMessageBox.Ok)
                        d2 = df
                        d3 = df
                        if val_keep!='':
                            if np.where(d2.applymap(lambda x: x != val_keep)):
                                QMessageBox.information(None, "Specific values",
                                                        "The value " + str(self.lineEdit_valuetokeep.text()) + " does not exist in the file.\nNo file to save.",
                                                        QMessageBox.Ok)
                            if np.where(d3.applymap(lambda x: x == val_keep)):
                                r = str(self.lineEdit_valuetokeep.text())
                                d3 = d3[(d3[[header]] == r).all(axis=1)]
                                d3.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                QMessageBox.information(None, "Specific values",
                                                        "The value " + str(
                                                            r) + " have been kept in " + str(header),
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and self.checkBox_value.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():

                        value_in_rows, okPressed = QInputDialog.getText(None, "Enter a value to drop from " +  str(header),
                                                                        "Value to drop ",
                                                                        QLineEdit.Normal, "")
                        # if type(value_in_rows) == int:
                        if not np.where(df.applymap(lambda x: x == value_in_rows)):
                            print('1f')
                        if np.where(df.applymap(lambda x: x == value_in_rows)):
                            df = df[(df[[header]] != value_in_rows).all(axis=1)]
                            df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                            QMessageBox.information(None, "Specific values",
                                                    "The value " + str(value_in_rows) + " have been dropped from " + str(header) ,
                                                    QMessageBox.Ok)
                            # self.lineedit_file_path_to_edit.setText(dir + '/' + file_name1 + '_droppedValue_str.csv')
                            self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

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

