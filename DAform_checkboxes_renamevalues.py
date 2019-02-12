from DAPandas_widget import PandasModel
import os
from PyQt5.QtWidgets import *
import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_checkboxes_renamevalues.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_checkboxes_RenameValues(object):
    def setupUi(self, Form_checkboxes_RenameValues):
        Form_checkboxes_RenameValues.setObjectName("Form_checkboxes_RenameValues")
        Form_checkboxes_RenameValues.resize(944, 455)
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_checkboxes_RenameValues)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(850, 30, 80, 21))
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.lineEdit_filepath_checkboxes_renamevalues = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_filepath_checkboxes_renamevalues.setGeometry(QtCore.QRect(10, 30, 781, 21))
        self.lineEdit_filepath_checkboxes_renamevalues.setObjectName("lineEdit_filepath_checkboxes_renamevalues")
        self.checkBox_text = QtWidgets.QCheckBox(Form_checkboxes_RenameValues)
        self.checkBox_text.setGeometry(QtCore.QRect(20, 240, 72, 19))
        self.checkBox_text.setObjectName("checkBox_text")
        self.checkBox_number = QtWidgets.QCheckBox(Form_checkboxes_RenameValues)
        self.checkBox_number.setGeometry(QtCore.QRect(20, 280, 72, 19))
        self.checkBox_number.setObjectName("checkBox_number")
        self.pushButton_apply = QtWidgets.QPushButton(Form_checkboxes_RenameValues)
        self.pushButton_apply.setGeometry(QtCore.QRect(20, 370, 80, 21))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.label_rename = QtWidgets.QLabel(Form_checkboxes_RenameValues)
        self.label_rename.setGeometry(QtCore.QRect(20, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_rename.setFont(font)
        self.label_rename.setObjectName("label_rename")
        self.checkBox_decimal = QtWidgets.QCheckBox(Form_checkboxes_RenameValues)
        self.checkBox_decimal.setGeometry(QtCore.QRect(20, 320, 72, 19))
        self.checkBox_decimal.setObjectName("checkBox_decimal")
        self.tableView_renamevalues = QtWidgets.QTableView(Form_checkboxes_RenameValues)
        self.tableView_renamevalues.setGeometry(QtCore.QRect(10, 60, 921, 131))
        self.tableView_renamevalues.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_renamevalues.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_renamevalues.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_renamevalues.setObjectName("tableView_renamevalues")
        self.lineEdit_valuetorename_text = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_valuetorename_text.setGeometry(QtCore.QRect(90, 240, 113, 21))
        self.lineEdit_valuetorename_text.setObjectName("lineEdit_valuetorename_text")
        self.lineEdit_newvalue_text = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_newvalue_text.setGeometry(QtCore.QRect(240, 240, 113, 21))
        self.lineEdit_newvalue_text.setObjectName("lineEdit_newvalue_text")
        self.label = QtWidgets.QLabel(Form_checkboxes_RenameValues)
        self.label.setGeometry(QtCore.QRect(210, 240, 21, 16))
        self.label.setObjectName("label")
        self.lineEdit_valuetorename_number = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_valuetorename_number.setGeometry(QtCore.QRect(90, 280, 113, 21))
        self.lineEdit_valuetorename_number.setObjectName("lineEdit_valuetorename_number")
        self.lineEdit_newvalue_number = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_newvalue_number.setGeometry(QtCore.QRect(240, 280, 113, 21))
        self.lineEdit_newvalue_number.setObjectName("lineEdit_newvalue_number")
        self.lineEdit_valuetorename_decimal = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_valuetorename_decimal.setGeometry(QtCore.QRect(90, 320, 113, 21))
        self.lineEdit_valuetorename_decimal.setObjectName("lineEdit_valuetorename_decimal")
        self.lineEdit_newvalue_decimal = QtWidgets.QLineEdit(Form_checkboxes_RenameValues)
        self.lineEdit_newvalue_decimal.setGeometry(QtCore.QRect(240, 320, 113, 21))
        self.lineEdit_newvalue_decimal.setObjectName("lineEdit_newvalue_decimal")
        self.label_2 = QtWidgets.QLabel(Form_checkboxes_RenameValues)
        self.label_2.setGeometry(QtCore.QRect(210, 280, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_checkboxes_RenameValues)
        self.label_3.setGeometry(QtCore.QRect(210, 320, 21, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit_filepath_checkboxes_renamevalues.setText('')
        self.pushButton_apply.clicked.connect(self.on_apply_clicked)
        self.pushButton_loadfile.clicked.connect(self.on_loadfile_clicked)

        self.retranslateUi(Form_checkboxes_RenameValues)
        QtCore.QMetaObject.connectSlotsByName(Form_checkboxes_RenameValues)

    def retranslateUi(self, Form_checkboxes_RenameValues):
        _translate = QtCore.QCoreApplication.translate
        Form_checkboxes_RenameValues.setWindowTitle(_translate("Form_checkboxes_RenameValues", "Form"))
        self.pushButton_loadfile.setText(_translate("Form_checkboxes_RenameValues", "Load file"))
        self.checkBox_text.setText(_translate("Form_checkboxes_RenameValues", "Text"))
        self.checkBox_number.setText(_translate("Form_checkboxes_RenameValues", "Number"))
        self.pushButton_apply.setText(_translate("Form_checkboxes_RenameValues", "Apply"))
        self.label_rename.setText(_translate("Form_checkboxes_RenameValues", "Rename"))
        self.checkBox_decimal.setText(_translate("Form_checkboxes_RenameValues", "Decimal"))
        self.lineEdit_valuetorename_text.setText(_translate("Form_checkboxes_RenameValues", "Value to rename"))
        self.lineEdit_newvalue_text.setText(_translate("Form_checkboxes_RenameValues", "new value"))
        self.label.setText(_translate("Form_checkboxes_RenameValues", "to"))
        self.lineEdit_valuetorename_number.setText(_translate("Form_checkboxes_RenameValues", "Value to rename"))
        self.lineEdit_newvalue_number.setText(_translate("Form_checkboxes_RenameValues", "new value"))
        self.lineEdit_valuetorename_decimal.setText(_translate("Form_checkboxes_RenameValues", "Value to rename"))
        self.lineEdit_newvalue_decimal.setText(_translate("Form_checkboxes_RenameValues", "new value"))
        self.label_2.setText(_translate("Form_checkboxes_RenameValues", "to"))
        self.label_3.setText(_translate("Form_checkboxes_RenameValues", "to"))

    def on_loadfile_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepath_checkboxes_renamevalues.setText(fileName)
            df = pd.read_csv(fileName, low_memory=False)
            model = PandasModel(df.head(10))
            self.tableView_renamevalues.setModel(model)

    def select_column(self):
        col_nb = self.tableView_renamevalues.currentIndex().column()
        column_name = self.tableView_renamevalues.model().headerData(col_nb, QtCore.Qt.Horizontal,
                                                                  QtCore.Qt.DisplayRole)
        return column_name

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_renamevalues.setModel(model)

    def on_apply_clicked(self):
        file = self.lineEdit_filepath_checkboxes_renamevalues.text()
        if file == '':
            QMessageBox.information(None, "Error ",
                                    "No loaded file.\nPlease load a file first.",
                                    QMessageBox.Ok)
        if file != '':
            df = pd.read_csv(file)
            header = self.select_column()
            if (len(header) < 1):
                QMessageBox.information(None, "Error ",
                                        "You must select a column.\nTry again",
                                        QMessageBox.Ok)
            if len(header) >= 1:
                if self.checkBox_text.isChecked() and self.checkBox_decimal.isChecked() and not self.checkBox_number.isChecked():
                    QMessageBox.information(None, "Error ",
                                            "You must check only one case.\nTry again",
                                            QMessageBox.Ok)

                if not self.checkBox_text.isChecked() and self.checkBox_decimal.isChecked() and self.checkBox_number.isChecked():
                    QMessageBox.information(None, "Error ",
                                            "You must check only one case.\nTry again",
                                            QMessageBox.Ok)

                if self.checkBox_text.isChecked() and not self.checkBox_decimal.isChecked() and self.checkBox_number.isChecked():
                    QMessageBox.information(None, "Error ",
                                            "You must check only one case.\nTry again",
                                            QMessageBox.Ok)

                if self.checkBox_text.isChecked() and not self.checkBox_decimal.isChecked() and not self.checkBox_number.isChecked():
                    df[header] = df[header].replace({self.lineEdit_valuetorename_text.text(): self.lineEdit_newvalue_text.text()})
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'RenameText_' + header + '_' + file_name1 + '.csv', index=None)
                    QMessageBox.information(None, "Value renamed",
                                            "The value has been renamed.\nSaved file.",
                                            QMessageBox.Ok)
                    self.reloaddata_fromfilepath(t1 + '\\' + 'RenameText_' + header + '_' + file_name1 + '.csv')
                    self.lineEdit_filepath_checkboxes_renamevalues.setText(t1 + '/' + 'RenameText_' + header + '_' + file_name1 + '.csv')

                if self.checkBox_number.isChecked() and not self.checkBox_decimal.isChecked() and not self.checkBox_text.isChecked():
                    value_entered1 = str(self.lineEdit_valuetorename_number.text())
                    value_entered2 = str(self.lineEdit_newvalue_number.text())
                    df[header] = df[header].replace({value_entered1: value_entered2})
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'RenameNumber_' + header + '_' + file_name1 + '.csv', index=None)
                    QMessageBox.information(None, "Value renamed",
                                            "The value has been renamed.\nSaved file.",
                                            QMessageBox.Ok)
                    self.reloaddata_fromfilepath(t1 + '\\' + 'RenameNumber_' + header + '_' + file_name1 + '.csv')
                    self.lineEdit_filepath_checkboxes_renamevalues.setText(
                        t1 + '/' + 'RenameNumber_' + header + '_' + file_name1 + '.csv')

                if self.checkBox_decimal.isChecked() and not self.checkBox_text.isChecked() and not self.checkBox_number.isChecked():
                    value_entered1 = str(self.lineEdit_valuetorename_decimal.text())
                    print(value_entered1)
                    value_entered2 = str(self.lineEdit_newvalue_decimal.text())
                    print(value_entered2)
                    df[header] = df[header].replace({value_entered1: value_entered2})
                    print('ok')
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'RenameDecimal_' + header + '_' + file_name1 + '.csv', index=None)
                    QMessageBox.information(None, "Value renamed",
                                            "The value has been renamed.\nSaved file.",
                                            QMessageBox.Ok)
                    print('whyyyy')
                    self.reloaddata_fromfilepath(t1 + '\\' + 'RenameDecimal_' + header + '_' + file_name1 + '.csv')
                    print('whyyyyyyyyyy')
                    self.lineEdit_filepath_checkboxes_renamevalues.setText(
                        t1 + '/' + 'RenameDecimal_' + header + '_' + file_name1 + '.csv')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_checkboxes_RenameValues = QtWidgets.QWidget()
    ui = Ui_Form_checkboxes_RenameValues()
    ui.setupUi(Form_checkboxes_RenameValues)
    Form_checkboxes_RenameValues.show()
    sys.exit(app.exec_())

