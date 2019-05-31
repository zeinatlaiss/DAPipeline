import os
from PyQt5.QtWidgets import *
import pandas as pd
from DApandaswidget import PandasModel
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_editincolumns.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_editcolumns(object):
    def setupUi(self, Form_editcolumns):
        Form_editcolumns.setObjectName("Form_editcolumns")
        Form_editcolumns.resize(251, 270)
        self.checkBox_renamecolumns = QtWidgets.QCheckBox(Form_editcolumns)
        self.checkBox_renamecolumns.setGeometry(QtCore.QRect(50, 60, 151, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_renamecolumns.setFont(font)
        self.checkBox_renamecolumns.setObjectName("checkBox_renamecolumns")
        self.checkBox_dropfromcolumns = QtWidgets.QCheckBox(Form_editcolumns)
        self.checkBox_dropfromcolumns.setGeometry(QtCore.QRect(50, 100, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_dropfromcolumns.setFont(font)
        self.checkBox_dropfromcolumns.setObjectName("checkBox_dropfromcolumns")
        self.checkBox_ordercolumns = QtWidgets.QCheckBox(Form_editcolumns)
        self.checkBox_ordercolumns.setGeometry(QtCore.QRect(50, 140, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_ordercolumns.setFont(font)
        self.checkBox_ordercolumns.setObjectName("checkBox_ordercolumns")
        self.checkBox_mergetwocolumns = QtWidgets.QCheckBox(Form_editcolumns)
        self.checkBox_mergetwocolumns.setGeometry(QtCore.QRect(50, 180, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_mergetwocolumns.setFont(font)
        self.checkBox_mergetwocolumns.setObjectName("checkBox_mergetwocolumns")
        self.lineEdit = QtWidgets.QLineEdit(Form_editcolumns)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(46, 47, 48);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_choose_editcolumns = QtWidgets.QPushButton(Form_editcolumns)
        self.pushButton_choose_editcolumns.setGeometry(QtCore.QRect(50, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_choose_editcolumns.setFont(font)
        self.pushButton_choose_editcolumns.setObjectName("pushButton_choose_editcolumns")
        self.lineEdit_filepath_editincolumns = QtWidgets.QLineEdit(Form_editcolumns)
        self.lineEdit_filepath_editincolumns.setGeometry(QtCore.QRect(0, 0, 251, 21))
        self.lineEdit_filepath_editincolumns.setFrame(False)
        self.lineEdit_filepath_editincolumns.setObjectName("lineEdit_filepath_editincolumns")

        self.pushButton_choose_editcolumns.clicked.connect(self.on_choose_clicked)

        self.retranslateUi(Form_editcolumns)
        QtCore.QMetaObject.connectSlotsByName(Form_editcolumns)

    def retranslateUi(self, Form_editcolumns):
        _translate = QtCore.QCoreApplication.translate
        Form_editcolumns.setWindowTitle(_translate("Form_editcolumns", "Edit columns"))
        self.checkBox_renamecolumns.setText(_translate("Form_editcolumns", "Rename columns"))
        self.checkBox_dropfromcolumns.setText(_translate("Form_editcolumns", "Drop from columns"))
        self.checkBox_ordercolumns.setText(_translate("Form_editcolumns", "Order columns"))
        self.checkBox_mergetwocolumns.setText(_translate("Form_editcolumns", "Merge 2 columns"))
        self.lineEdit.setText(_translate("Form_editcolumns", "Edit columns"))
        self.pushButton_choose_editcolumns.setText(_translate("Form_editcolumns", "Choose"))

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
            self.label_nbcpdid_new.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid_new.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_new.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid_new.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'X_CPD_ID' not in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_new.setText('No CPD_ID')
            self.label_nbbatchid_new.setText('No BATCH_ID')
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_new.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid_new.setText('No BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid_new.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid_new.setText('No X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_new.setText('No CPD_ID')
            self.label_nbbatchid_new.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid_new.setText('No X_CPD_ID')
            self.label_nbbatchid_new.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_dataframe_to_edit.setModel(model)
        if 'Plate' in df.columns:
            if 'Well' not in df.columns:
                self.lineEdit_plate_new.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_new.setText('No wells')
                self.getncpdsbatches(df)
            if 'Well' in df.columns:
                self.lineEdit_plate_new.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_new.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)
            if 'WELL' in df.columns:
                self.lineEdit_plate_new.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well_new.setText(str(len(df['WELL'])) + ' WELLs')
                self.getncpdsbatches(df)

    def setPlateWellText_intblview(self, df):
        if 'Plate' in df.columns and 'Well' in df.columns:
            self.lineEdit_plate_new.setText(str(df['Plate'].nunique()) + ' unique plate')
            self.lineEdit_well_new.setText(str(len(df['Well'])) + ' wells')

    def on_choose_clicked(self):
        # file = self.lineedit_file_path_to_edit
        file = self.lineedit_file_path_to_edit
        if file == 'File path':
            QMessageBox.information(None, "Error ",
                                    "No loaded file.\nPlease load a file first.",
                                    QMessageBox.Ok)
        if file != 'File path':
            exists = os.path.isfile(file)
            if exists:
                df = pd.read_csv(file)
                header = self.select_multicolumns()
                if (len(header) < 1):
                    QMessageBox.information(None, "Error ",
                                            "You must select a column.\nTry again",
                                            QMessageBox.Ok)
                if len(header) >= 1:
                    if self.checkBox_dropfromcolumns.isChecked() and not self.checkBox_mergetwocolumns.isChecked() and not self.checkBox_ordercolumns.isChecked() and not \
                            self.checkBox_renamecolumns.isChecked():
                        df5 = pd.read_csv(self.lineedit_file_path_to_edit)
                        d_dropped = df5.drop(header, axis=1)
                        d_dropped.to_csv(self.t1_new + '\\' + self.file_name1_new + '.csv', index=None)
                        self.reloaddata_fromfilepath(self.t1_new + '\\' + self.file_name1_new + '.csv')
                        if 'Plate' in d_dropped and 'Well' in d_dropped:
                            self.setPlateWellText_intblview(d_dropped)
                        if 'Plate' in d_dropped and 'Well' not in d_dropped:
                            self.lineEdit_plate_new.setText(str(d_dropped['Plate'].nunique()) + ' unique plate')
                            self.lineEdit_well_new.setText('No well')
                        if 'Plate' not in d_dropped and 'Well' in d_dropped:
                            self.lineEdit_plate_new.setText('No plate')
                            self.lineEdit_well_new.setText(str(len(d_dropped['Well'])) + ' wells')
                        if 'Plate' not in d_dropped and 'Well' not in d_dropped:
                            self.lineEdit_plate_new.setText('No plate')
                            self.lineEdit_well_new.setText('No well')
                        QMessageBox.information(None, "Dropped columns ",
                                                "Columns: " + str(
                                                    header) + " have been dropped from your file!\nFile successfully saved.",
                                                QMessageBox.Yes)

                    if not self.checkBox_dropfromcolumns.isChecked() and not self.checkBox_mergetwocolumns.isChecked() and self.checkBox_ordercolumns.isChecked() and not \
                            self.checkBox_renamecolumns.isChecked():
                        header = self.select_multicolumns()
                        df1 = pd.read_csv(self.lineedit_file_path_to_edit)
                        df1 = df1[header]
                        df1.to_csv(self.t1_new + '\\'   + self.file_name1_new + '.csv', index=None)
                        self.reloaddata_fromfilepath(self.t1_new + '\\'   + self.file_name1_new + '.csv')

                    if not self.checkBox_dropfromcolumns.isChecked() and self.checkBox_mergetwocolumns.isChecked() and not self.checkBox_ordercolumns.isChecked() \
                            and not self.checkBox_renamecolumns.isChecked():
                        if len(header) == 0:
                            QMessageBox.information(None, "Error",
                                                    "You must select only 2 columns.\nNo file to save!",
                                                    QMessageBox.Ok)
                        if (len(header) > 2 or len(header) < 2):
                            QMessageBox.information(None, "Error ",
                                                    "You can select only 2 columns.\nNo file to save!",
                                                    QMessageBox.Ok)
                        if len(header) == 2:
                            value_entered_column, okPressed = QInputDialog.getText(None, "Enter column name to add",
                                                                                   "Column name ",
                                                                                   QLineEdit.Normal, "")
                            if value_entered_column == '':
                                QMessageBox.information(None, "Error ",
                                                        "You have not entered a column name.\nNo file to save.",
                                                        QMessageBox.Ok)
                            if value_entered_column != '':
                                df6 = pd.read_csv(self.lineedit_file_path_to_edit)
                                if value_entered_column in df6.columns:
                                    if df6[header[0]].dtypes != str or df6[header[1]].dtypes != str:
                                        df6 = pd.read_csv(file, dtype={header[0]: str, header[1]: str})
                                        buttonReply = QMessageBox.question(None, 'Error',
                                                                           "The column " + str(
                                                                               value_entered_column) + " already exists in the file.\n"
                                                                                                       "Press Yes if you want to overwrite the column.\n"
                                                                                                       "Press No to ignore.",
                                                                           QMessageBox.Yes | QMessageBox.No,
                                                                           QMessageBox.Yes)
                                        if buttonReply == QMessageBox.Yes:
                                            df6[value_entered_column] = df6[header[0]] + '_' + df6[header[1]]
                                            df6.to_csv(self.t1_new + '\\' + self.file_name1_new + '.csv', index=None)
                                            self.reloaddata_fromfilepath(
                                                self.t1_new + '\\' + self.file_name1_new + '.csv')
                                        if buttonReply == QMessageBox.No:
                                            QMessageBox.information(None, "Error",
                                                                    "No file to save.",
                                                                    QMessageBox.Ok)

                                if value_entered_column not in df6.columns:
                                    if df6[header[0]].dtypes != str or df6[header[1]].dtypes != str:
                                        df6 = pd.read_csv(file, dtype={header[0]: str, header[1]: str})
                                        df6[value_entered_column] = df6[header[0]] + '_' + df6[header[1]]
                                        df6.to_csv(self.t1_new + '\\'   + self.file_name1_new + '.csv', index=None)
                                        self.reloaddata_fromfilepath(self.t1_new + '\\'   + self.file_name1_new + '.csv')
                                        # self.lineEdit_filepath.setText(t1 + '/'   + file_name1 + '.csv')
                                    if df6[header[0]].dtypes == str and df6[header[1]].dtypes == str:
                                        df6[value_entered_column] = df6[header[0]] + '_' + df6[header[1]]
                                        df6.to_csv(self.t1_new + '\\'   + self.file_name1_new + '.csv', index=None)
                                        self.reloaddata_fromfilepath(self.t1_new + '\\'   + self.file_name1_new + '.csv')

                    if not self.checkBox_dropfromcolumns.isChecked() and not self.checkBox_mergetwocolumns.isChecked() and not self.checkBox_ordercolumns.isChecked() \
                            and self.checkBox_renamecolumns.isChecked():
                        new_value, okPressed = QInputDialog.getText(None, "Value to rename value in column " + str(header),
                                                                    "Column name ",
                                                                    QLineEdit.Normal, "New column name for " + str(header))
                        if okPressed:
                            df10 = pd.read_csv(self.lineedit_file_path_to_edit)
                            if new_value in df10:
                                QMessageBox.information(None, "Error ",
                                                        "The value you just entered already exists in the file.\nNo file to save.",
                                                        QMessageBox.Ok)
                            if new_value not in df10:
                                df10.rename(columns={header[0]: new_value}, inplace=True)
                                df10.to_csv(self.t1_new + '\\'   + self.file_name1_new + '.csv', index=None)
                                # self.lineEdit_filepath.setText(t1 + '//'   + header + file_name1 + '.csv')
                                self.reloaddata_fromfilepath(self.t1_new + '\\'   + self.file_name1_new + '.csv')

                    if not self.checkBox_dropfromcolumns.isChecked() and not self.checkBox_mergetwocolumns.isChecked() and not self.checkBox_ordercolumns.isChecked() and not \
                            self.checkBox_renamecolumns.isChecked():
                        QMessageBox.information(None, "Error",
                                                "Please check at least one of the cases.",
                                                QMessageBox.Ok)

            else:
                QMessageBox.information(None, "Error",
                                        "The file does not exist anymore.",
                                        QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_editcolumns = QtWidgets.QWidget()
    ui = Ui_Form_editcolumns()
    ui.setupUi(Form_editcolumns)
    Form_editcolumns.show()
    sys.exit(app.exec_())

