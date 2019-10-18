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
        Form_CheckBoxes.resize(690, 223)
        self.checkBox_nan = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_nan.setGeometry(QtCore.QRect(20, 50, 131, 19))
        self.checkBox_nan.setObjectName("checkBox_nan")
        self.checkBox_missingvalue = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_missingvalue.setGeometry(QtCore.QRect(20, 80, 141, 19))
        self.checkBox_missingvalue.setObjectName("checkBox_missingvalue")
        self.pushButton_apply = QtWidgets.QPushButton(Form_CheckBoxes)
        self.pushButton_apply.setGeometry(QtCore.QRect(570, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_drop = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_drop.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setObjectName("label_drop")
        self.checkBox_valueendswith = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_valueendswith.setGeometry(QtCore.QRect(20, 110, 51, 19))
        self.checkBox_valueendswith.setObjectName("checkBox_valueendswith")
        self.label_rename = QtWidgets.QLabel(Form_CheckBoxes)
        self.label_rename.setGeometry(QtCore.QRect(220, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rename.setFont(font)
        self.label_rename.setObjectName("label_rename")
        self.lineEdit_valuetorename_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetorename_text.setGeometry(QtCore.QRect(290, 50, 131, 21))
        self.lineEdit_valuetorename_text.setText("")
        self.lineEdit_valuetorename_text.setObjectName("lineEdit_valuetorename_text")
        self.lineEdit_newvalue_text = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_newvalue_text.setGeometry(QtCore.QRect(290, 110, 131, 21))
        self.lineEdit_newvalue_text.setText("")
        self.lineEdit_newvalue_text.setObjectName("lineEdit_newvalue_text")
        self.checkBox_text = QtWidgets.QCheckBox(Form_CheckBoxes)
        self.checkBox_text.setGeometry(QtCore.QRect(220, 50, 72, 19))
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
        self.lineEdit_valuetodrop = QtWidgets.QLineEdit(Form_CheckBoxes)
        self.lineEdit_valuetodrop.setGeometry(QtCore.QRect(70, 110, 91, 21))
        self.lineEdit_valuetodrop.setText("")
        self.lineEdit_valuetodrop.setObjectName("lineEdit_valuetodrop")

        self.pushButton_apply.clicked.connect(self.on_apply_clicked)
        print('1')
        self.retranslateUi(Form_CheckBoxes)
        QtCore.QMetaObject.connectSlotsByName(Form_CheckBoxes)

    def retranslateUi(self, Form_CheckBoxes):
        _translate = QtCore.QCoreApplication.translate
        Form_CheckBoxes.setWindowTitle(_translate("Form_CheckBoxes", "Edit in rows"))
        self.checkBox_nan.setText(_translate("Form_CheckBoxes", "missing values in file"))
        self.checkBox_missingvalue.setText(_translate("Form_CheckBoxes", "missing values in column "))
        self.pushButton_apply.setText(_translate("Form_CheckBoxes", "APPLY"))
        self.label_drop.setText(_translate("Form_CheckBoxes", "Drop from rows"))
        self.checkBox_valueendswith.setText(_translate("Form_CheckBoxes", "value"))
        self.label_rename.setText(_translate("Form_CheckBoxes", "Rename values in rows"))
        self.checkBox_text.setText(_translate("Form_CheckBoxes", "Rename"))
        self.label.setText(_translate("Form_CheckBoxes", "to"))
        self.label_keep.setText(_translate("Form_CheckBoxes", "Keep values in rows"))
        self.checkBox_keepvalue.setText(_translate("Form_CheckBoxes", "Keep the value"))

    def getncpdsbatches(self, dataframe):
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'compound_id' in dataframe.columns and 'batch_id' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['compound_id'].nunique()) + ' unique compound_id')
            self.label_nbbatchid.setText(str(dataframe['batch_id'].nunique()) + ' unique batch_id')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'X_CPD_ID' not in dataframe.columns and \
                'BATCH_ID' not in dataframe.columns and 'compound_id' not in dataframe.columns and \
                'batch_id' not in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid.setText('No X_BATCH_ID')
        if 'compound_id' in dataframe.columns and 'batch_id' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['compound_id'].nunique()) + ' unique compound_id')
            self.label_nbbatchid.setText('No batch_id')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No X_CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        if 'compound_id' not in dataframe.columns and 'batch_id' in dataframe.columns:
            self.label_nbcpdid.setText('No compound_id')
            self.label_nbbatchid.setText(str(dataframe['batch_id'].nunique()) + ' unique batch_id')
        if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No X_CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')

        #
        # if 'CPD_ID' in dataframe.columns and 'BATCH_ID' in dataframe.columns:
        #     self.label_nbcpdid_rows.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
        #     self.label_nbbatchid_rows.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        # if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
        #     self.label_nbcpdid_rows.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
        #     self.label_nbbatchid_rows.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        # if 'CPD_ID' not in dataframe.columns and 'X_CPD_ID' not in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
        #     self.label_nbcpdid_rows.setText('No CPD_ID')
        #     self.label_nbbatchid_rows.setText('No BATCH_ID')
        # if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
        #     self.label_nbcpdid_rows.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
        #     self.label_nbbatchid_rows.setText('No BATCH_ID')
        # if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' not in dataframe.columns:
        #     self.label_nbcpdid_rows.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
        #     self.label_nbbatchid_rows.setText('No X_BATCH_ID')
        # if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
        #     self.label_nbcpdid_rows.setText('No CPD_ID')
        #     self.label_nbbatchid_rows.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        # if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
        #     self.label_nbcpdid_rows.setText('No X_CPD_ID')
        #     self.label_nbbatchid_rows.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')

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

    def select_multicolumns(self):
        list_col = []
        totalColumns = self.tableView_dataframe_to_edit.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.tableView_dataframe_to_edit.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                      QtCore.Qt.DisplayRole)
            list_col.append(column_name)
        return list_col

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
                header = self.select_multicolumns()
                if len(header) == 0:
                    QMessageBox.information(None, "Error",
                                            "You must select at least one column.\nNo file to save!",
                                            QMessageBox.Ok)
                if len(header) >= 1:
                    print('3')
                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        QMessageBox.information(None, "Error",
                                                "Please check at least one of the above cases.",
                                                QMessageBox.Ok)
                    if self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        print('g')
                        dd6 = df
                        if np.where(pd.isnull(df[header[0]].values)):
                            print('3333')
                        # if not np.where(df.applymap(lambda x: x == '')):
                            QMessageBox.information(None, "Error",
                                                    "NAN values do not exist in the column " + header + "selected.",
                                                    QMessageBox.Ok)
                        if  not np.where(pd.isnull(df[header[0]].values)):
                            print('777')
                        # if np.where(dd6.applymap(lambda x: x == '')):
                            buttonReply = QMessageBox.question(None, 'Drop from the file',
                                                               "You are about to delete all the data corresponding to NAN values in the file.\n"
                                                               "Yes to continue.\n"
                                                               "No to ignore.\n",
                                                               QMessageBox.Yes | QMessageBox.No,
                                                               QMessageBox.Yes)
                            if buttonReply == QMessageBox.Yes:
                                dd7 = dd6.dropna(how='any')
                                QMessageBox.information(None, "NAN dropped",
                                                        "NAN values have been dropped from all the file.",
                                                        QMessageBox.Ok)
                                dd7.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        if df[header[0]].dtypes != str:
                            df = pd.read_csv(file,
                                             dtype={header[0]: str})
                            df[header[0]].fillna("missing", inplace=True)
                            if any(df[header[0]] == 'missing') == False:
                                QMessageBox.information(None, "No missing values",
                                                        "No missing values to drop in the column " + str(
                                                            header) + ".\nNo file to save.", QMessageBox.Ok)

                            if any(df[header[0]] == 'missing') == True:
                                print('missing values')
                                buttonReply = QMessageBox.question(None, 'Delete from rows',
                                                                   "You are about to delete the data corresponding to missing or NAN values from the column " \
                                                                   +str(header[0])+ " in the file.\n"
                                                                   "Yes to continue.\n"
                                                                   "No to ignore.\n",
                                                                   QMessageBox.Yes | QMessageBox.No,
                                                                   QMessageBox.Yes)
                                if buttonReply == QMessageBox.Yes:
                                    d = df[df[header[0]] == 'missing']
                                    df.drop(df.loc[df[header[0]] == 'missing'].index, inplace=True)
                                    df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                    QMessageBox.information(None, "Missing values",
                                                            str(len(
                                                                d)) + " rows have been dropped from the column " + str(
                                                                header[0]) + "\nFile saved.",
                                                            QMessageBox.Ok)
                                    self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                        if df[header[0]].dtypes == str:
                            df[header[0]].fillna("missing", inplace=True)
                            if any(df[header[0]] == 'missing') == False:
                                QMessageBox.information(None, "No missing values",
                                                        "No missing values to drop in the column " + str(
                                                            header[0]) + ".\nNo file to save.", QMessageBox.Ok)
                            if any(df[header[0]] == 'missing') == True:
                                d = df[df[header[0]] == 'missing']
                                df.drop(df.loc[df[header[0]] == 'missing'].index, inplace=True)
                                df.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                QMessageBox.information(None, "Missing values",
                                                        str(len(
                                                            d)) + " empty cells have been dropped from the column " + str(
                                                            header[0]) + "\nSaved file.",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        print('f')
                        dd4 =  df
                        print('fd')
                        value_in_rows = self.lineEdit_valuetodrop.text()
                        # if np.where(pd.isnull(dd4[header[0]].values)):
                        # if np.nan in dd4[header[0]].values:
                                    # self.lineEdit_valuetodrop.text() not in dd4[header[0]].values:
                        print('ffff')
                        if np.where(dd4[header[0]].values.applymap(lambda x: x == '')):
                            QMessageBox.information(None, "NAN values",
                                                    "You have nan values in the file, please drop them first.",
                                                    QMessageBox.Ok)
                            # if not np.where(dd4.applymap(lambda x: x == '')):
                        # if np.nan not in dd4[header[0]].values:
                        if not np.where(pd.isnull(dd4[header[0]].values)):
                            print('djfjg')
                            print(header[0])
                            if self.lineEdit_valuetodrop.text() not in dd4[header[0]].values:
                                print('gggg')
                                QMessageBox.information(None, "Error ",
                                                        "The value " + str(
                                                            self.lineEdit_valuetodrop.text()) + " does not exist in the column " + str(
                                                            header) + ".\nTry again",
                                                        QMessageBox.Ok)
                            if self.lineEdit_valuetodrop.text() in dd4[header[0]].values:
                                dd = dd4
                                print('fjfklfl')
                                df_dropped = dd.drop(dd[(dd[header[0]].str.contains(self.lineEdit_valuetodrop.text()))].index)
                                print('g')
                                df_dropped.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                print('gg')
                                QMessageBox.information(None, "Value ends with " + str(value_in_rows) + "dropped",
                                                        "All values end with " + str(
                                                            value_in_rows) + " have been dropped from the file.",
                                                        QMessageBox.Ok)
                                print('fff')
                                self.reloaddata_fromfilepath(self.t1_rows + '/' + self.file_name1_rows + '.csv')

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and not self.checkBox_keepvalue.isChecked() and self.checkBox_text.isChecked():
                        dd1 = df
                        if self.lineEdit_valuetorename_text.text() in dd1[header[0]].values:
                            dd1[header[0]] = dd1[header[0]].replace(
                                {self.lineEdit_valuetorename_text.text(): self.lineEdit_newvalue_text.text()})
                            dd1.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                            QMessageBox.information(None, "Value renamed",
                                                    "The value " + str(
                                                        self.lineEdit_valuetorename_text.text()) + " in the column " + str(
                                                        header[0])
                                                    + " has been renamed.\nSaved file.",
                                                    QMessageBox.Ok)
                            self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')
                        # dd2 = df
                        # if self.lineEdit_valuetorename_text.text() not in dd2[header[0]].values:
                        #     QMessageBox.information(None, "Error ",
                        #                             "You cannot rename the value " + str(
                        #                                 self.lineEdit_valuetorename_text.text()) + " because it does not exist in the column " + str(
                        #                                 header[0]) + ".\nTry again",
                        #                             QMessageBox.Ok)

                    if not self.checkBox_nan.isChecked() and not self.checkBox_missingvalue.isChecked() and not \
                            self.checkBox_valueendswith.isChecked() and self.checkBox_keepvalue.isChecked() and not self.checkBox_text.isChecked():
                        print('djfjfjfkkf')
                        val_keep = self.lineEdit_valuetokeep.text()
                        print('fllflflfl')
                        if val_keep == '':
                            print('egk')
                            QMessageBox.information(None, "Specific values",
                                                    "No value entered.\nPlease enter a value that you need to keep.",
                                                    QMessageBox.Ok)
                        if val_keep != '':
                            print(';eee')
                            d2 = df
                            print('efff')
                            if self.lineEdit_valuetokeep.text() not in d2[header].values:
                                print('djfjdjf')
                                # if np.where(d2.applymap(lambda x: x != val_keep)):
                                QMessageBox.information(None, "Specific values",
                                "The value " + str(
                                    self.lineEdit_valuetokeep.text()) + " does not exist in the file.\nNo file to save.",
                                    QMessageBox.Ok)
                            d3 = df
                            print('1')
                            if self.lineEdit_valuetokeep.text() in d3[header[0]].values:
                                print('2')
                                r = str(self.lineEdit_valuetokeep.text())
                                print('55')
                                d3 = d3[(d3[[header[0]]] == r).all(axis=1)]
                                print('4')
                                d3.to_csv(self.t1_rows + '\\' + self.file_name1_rows + '.csv', index=None)
                                print('5')
                                QMessageBox.information(None, "Specific values",
                                                        "The value " + str(
                                                            r) + " have been kept in " + str(header[0]),
                                                        QMessageBox.Ok)
                                print('6')
                                self.reloaddata_fromfilepath(self.t1_rows + '\\' + self.file_name1_rows + '.csv')
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

