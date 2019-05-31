from DApandaswidget import PandasModel
import os
from PyQt5.QtWidgets import *
import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_table_linkfiles.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_table_linkfiles(object):
    def setupUi(self, form_table_linkfiles):
        form_table_linkfiles.setObjectName("form_table_linkfiles")
        form_table_linkfiles.resize(1558, 948)
        self.pushButton1_tolinkfile = QtWidgets.QPushButton(form_table_linkfiles)
        self.pushButton1_tolinkfile.setGeometry(QtCore.QRect(700, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Aparajita")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1_tolinkfile.setFont(font)
        self.pushButton1_tolinkfile.setObjectName("pushButton1_tolinkfile")
        self.pushButton2_tolinkfile = QtWidgets.QPushButton(form_table_linkfiles)
        self.pushButton2_tolinkfile.setGeometry(QtCore.QRect(1460, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Aparajita")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton2_tolinkfile.setFont(font)
        self.pushButton2_tolinkfile.setObjectName("pushButton2_tolinkfile")
        self.lineEdit_filepath_firstfile = QtWidgets.QLineEdit(form_table_linkfiles)
        self.lineEdit_filepath_firstfile.setGeometry(QtCore.QRect(10, 60, 671, 21))
        self.lineEdit_filepath_firstfile.setObjectName("lineEdit_filepath_firstfile")
        self.lineEdit_filepath_secondfile = QtWidgets.QLineEdit(form_table_linkfiles)
        self.lineEdit_filepath_secondfile.setGeometry(QtCore.QRect(780, 60, 671, 21))
        self.lineEdit_filepath_secondfile.setObjectName("lineEdit_filepath_secondfile")
        self.pushButton_link = QtWidgets.QPushButton(form_table_linkfiles)
        self.pushButton_link.setGeometry(QtCore.QRect(1450, 870, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Aparajita")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_link.setFont(font)
        self.pushButton_link.setObjectName("pushButton_link")
        self.tableView_firstfile = QtWidgets.QTableView(form_table_linkfiles)
        self.tableView_firstfile.setGeometry(QtCore.QRect(10, 110, 751, 691))
        self.tableView_firstfile.setObjectName("tableView_firstfile")
        self.tableView_secondfile = QtWidgets.QTableView(form_table_linkfiles)
        self.tableView_secondfile.setGeometry(QtCore.QRect(780, 110, 741, 691))
        self.tableView_secondfile.setObjectName("tableView_secondfile")

        self.pushButton1_tolinkfile.clicked.connect(self.on_loadFile1_clicked)
        self.pushButton2_tolinkfile.clicked.connect(self.on_loadFile2_clicked)
        self.pushButton_link.clicked.connect(self.on_link_clicked)

        self.retranslateUi(form_table_linkfiles)
        QtCore.QMetaObject.connectSlotsByName(form_table_linkfiles)

    def retranslateUi(self, form_table_linkfiles):
        _translate = QtCore.QCoreApplication.translate
        form_table_linkfiles.setWindowTitle(_translate("form_table_linkfiles", "Link files"))
        self.pushButton1_tolinkfile.setText(_translate("form_table_linkfiles", "Load file"))
        self.pushButton2_tolinkfile.setText(_translate("form_table_linkfiles", "Load file"))
        self.pushButton_link.setText(_translate("form_table_linkfiles", "Link"))

    def on_loadFile1(self):
        fileName1 = self.lineEdit_filepath_firstfile.text()
        df1 = pd.read_csv(fileName1, low_memory=False)
        model = PandasModel(df1.head(1000))
        self.tableView_firstfile.setModel(model)

    def on_loadFile1_clicked(self):
        fileName1, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName1:
            exists = os.path.isfile(fileName1)
            if exists:
                self.lineEdit_filepath_firstfile.setText(fileName1)
                df1 = pd.read_csv(fileName1, low_memory=False)
                model = PandasModel(df1.head(1000))
                self.tableView_firstfile.setModel(model)

    def on_loadFile2_clicked(self):
        fileName2, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName2:
            exists = os.path.isfile(fileName2)
            if exists:
                self.lineEdit_filepath_secondfile.setText(fileName2)
                df2 = pd.read_csv(fileName2, low_memory=False)
                model = PandasModel(df2.head(1000))
                self.tableView_secondfile.setModel(model)

    def select_column1(self):
        col_nb1 = self.tableView_firstfile.currentIndex().column()
        column_name1 = self.tableView_firstfile.model().headerData(col_nb1, QtCore.Qt.Horizontal,
                                                                  QtCore.Qt.DisplayRole)
        return column_name1

    def select_column2(self):
        col_nb2 = self.tableView_secondfile.currentIndex().column()
        column_name2 = self.tableView_secondfile.model().headerData(col_nb2, QtCore.Qt.Horizontal,
                                                                   QtCore.Qt.DisplayRole)
        return column_name2

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_secondfile.setModel(model)

    def on_link_clicked(self):
        filename1 = self.lineEdit_filepath_firstfile.text()
        filename2 = self.lineEdit_filepath_secondfile.text()
        exists1 = os.path.isfile(filename1)
        exists2 = os.path.isfile(filename2)
        if not exists1 and not exists2:
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load files first.",
                                        QMessageBox.Ok)
        if exists1 and not exists2:
            QMessageBox.information(None, "Error ",
                                    "No loaded file.\nPlease load the second file.",
                                    QMessageBox.Ok)
        if exists1 and exists2:
            col1 = self.select_column1()
            col2 = self.select_column2()
            if len(col1) == 1 and len(col2) == 1:
                df1 = pd.read_csv(filename1)
                boolk = df1.duplicated(subset=col1[0], keep=False)
                df_duplicated = df1[boolk]
                if (len(df_duplicated) > 0):
                    buttonReply = QMessageBox.question(None, 'Error',
                                                       "Duplicated index in the column " + str(col1) + "\n"
                                                                                                         "Press Yes if you want to continue.\n"
                                                                                                         "Press No to ignore.",
                                                       QMessageBox.Yes | QMessageBox.No,
                                                       QMessageBox.Yes)
                    if buttonReply == QMessageBox.Yes:
                        df2 = pd.read_csv(filename2, index_col=col2)
                        self.reloaddata_fromfilepath(filename2)
                        self.lineEdit_filepath_secondfile.setText(filename2)
                        if col2[0] not in df2.columns:
                            print('3')
                        if col2[0] in df2.columns:
                            boolk = df2.duplicated(subset=col2[0], keep=False)
                            df_duplicated1 = df2[boolk]
                            if len(df_duplicated1) > 0:
                                QMessageBox.information(None, "Error",
                                                        "Duplicated index. You cannot link the file.\nNo file to save.",
                                                        QMessageBox.Ok)
                            if len(df_duplicated1) == 0:
                                QMessageBox.information(None, "Link files",
                                                        "The 2 files will be linked by the columns: " + str(col1) +
                                                        " and " + str(col2) + ".\nPlease select columns from the 2nd file to link the two files.",
                                                        QMessageBox.Ok)
                                col3 = self.select_column2()
                                # df2 = pd.read_csv(filename2, index_col=col2)

                                # d_merged = df.merge(df_withcpds, on=header[0])

                                # t1 = os.path.dirname(file)
                                # file_name1 = os.path.splitext(os.path.basename(file))[0]
                                # d_merged.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                # self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                # self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                # QMessageBox.information(None, "File linked",
                                #                         "Successfully linked and saved the files!",
                                #                         QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_table_linkfiles = QtWidgets.QWidget()
    ui = Ui_form_table_linkfiles()
    ui.setupUi(form_table_linkfiles)
    form_table_linkfiles.show()
    sys.exit(app.exec_())

