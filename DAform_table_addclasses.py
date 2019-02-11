import pandas as pd
from PyQt5.QtWidgets import *
import string
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_table_addclasses.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_table_addclasses(object):
    def setupUi(self, form_table_addclasses):
        form_table_addclasses.setObjectName("form_table_addclasses")
        form_table_addclasses.resize(1275, 505)
        self.pushButton_loadfromdataframe = QtWidgets.QPushButton(form_table_addclasses)
        self.pushButton_loadfromdataframe.setGeometry(QtCore.QRect(1170, 460, 80, 21))
        self.pushButton_loadfromdataframe.setObjectName("pushButton_loadfromdataframe")
        self.tableWidget_toaddclasses = QtWidgets.QTableWidget(form_table_addclasses)
        self.tableWidget_toaddclasses.setGeometry(QtCore.QRect(20, 100, 1231, 351))
        self.tableWidget_toaddclasses.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_toaddclasses.setColumnCount(0)
        self.tableWidget_toaddclasses.setObjectName("tableWidget_toaddclasses")
        self.tableWidget_toaddclasses.setRowCount(0)
        self.tableWidget_toaddclasses.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_toaddclasses.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_toaddclasses.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_toaddclasses.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_toaddclasses.verticalHeader().setSortIndicatorShown(False)
        self.lineEdit_filepathfromdataframe = QtWidgets.QLineEdit(form_table_addclasses)
        self.lineEdit_filepathfromdataframe.setGeometry(QtCore.QRect(20, 20, 621, 21))
        self.lineEdit_filepathfromdataframe.setObjectName("lineEdit_filepathfromdataframe")
        self.comboBox_featuresfromdataframe = QtWidgets.QComboBox(form_table_addclasses)
        self.comboBox_featuresfromdataframe.setGeometry(QtCore.QRect(1040, 50, 211, 22))
        self.comboBox_featuresfromdataframe.setObjectName("comboBox_featuresfromdataframe")
        self.comboBox_plates = QtWidgets.QComboBox(form_table_addclasses)
        self.comboBox_plates.setGeometry(QtCore.QRect(830, 20, 421, 22))
        self.comboBox_plates.setObjectName("comboBox_plates")
        self.lineEdit_nbrofplates = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_nbrofplates.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.lineEdit_nbrofplates.setText("")
        self.lineEdit_nbrofplates.setObjectName("lineEdit_nbrofplates")
        self.lineEdit_nbrofcompounds = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_nbrofcompounds.setGeometry(QtCore.QRect(220, 60, 91, 16))
        self.lineEdit_nbrofcompounds.setText("")
        self.lineEdit_nbrofcompounds.setObjectName("lineEdit_nbrofcompounds")
        self.lineEdit_nbrofwells = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_nbrofwells.setGeometry(QtCore.QRect(130, 60, 91, 16))
        self.lineEdit_nbrofwells.setText("")
        self.lineEdit_nbrofwells.setObjectName("lineEdit_nbrofwells")
        self.lineEdit_plate_4 = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_plate_4.setGeometry(QtCore.QRect(490, 440, 91, 16))
        self.lineEdit_plate_4.setText("")
        self.lineEdit_plate_4.setObjectName("lineEdit_plate_4")
        self.lineEdit_nbrofbatches = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_nbrofbatches.setGeometry(QtCore.QRect(320, 60, 111, 16))
        self.lineEdit_nbrofbatches.setText("")
        self.lineEdit_nbrofbatches.setObjectName("lineEdit_nbrofbatches")
        self.lineEdit_nbrofrows = QtWidgets.QLabel(form_table_addclasses)
        self.lineEdit_nbrofrows.setGeometry(QtCore.QRect(450, 60, 101, 16))
        self.lineEdit_nbrofrows.setText("")
        self.lineEdit_nbrofrows.setObjectName("lineEdit_nbrofrows")
        self.pushButton_loadfileaddclasses = QtWidgets.QPushButton(form_table_addclasses)
        self.pushButton_loadfileaddclasses.setGeometry(QtCore.QRect(660, 20, 80, 21))
        self.pushButton_loadfileaddclasses.setObjectName("pushButton_loadfileaddclasses")

        cols = 24
        rows = 16
        l = list(string.ascii_uppercase)
        self.tableWidget_toaddclasses.setRowCount(rows)
        self.tableWidget_toaddclasses.setColumnCount(cols)
        # if j + 1 <= 9:
        #     if  self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1))) == df['Well']:
        #         self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1)))
        # if j + 1 >= 10:
        #     self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + str(j + 1)))

        self.tableWidget_toaddclasses.setVerticalHeaderLabels(l)
        self.pushButton_loadfileaddclasses.clicked.connect(self.on_loadFile_clicked)
        self.comboBox_featuresfromdataframe.currentTextChanged.connect(self.on_comboBox_featuresfromdataframe_changed)

        self.retranslateUi(form_table_addclasses)
        QtCore.QMetaObject.connectSlotsByName(form_table_addclasses)

    def retranslateUi(self, form_table_addclasses):
        _translate = QtCore.QCoreApplication.translate
        form_table_addclasses.setWindowTitle(_translate("form_table_addclasses", "Add classes form"))
        self.pushButton_loadfromdataframe.setText(_translate("form_table_addclasses", "Load"))
        self.pushButton_loadfileaddclasses.setText(_translate("form_table_addclasses", "Load file"))

    def on_loadFile_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepathfromdataframe.setText(fileName)
            df = pd.read_csv(fileName, low_memory=False)
            df_rows = df.count()
            cols = 24
            rows = 16
            l = list(string.ascii_uppercase)
            number_of_rows = self.tableWidget_toaddclasses.rowCount()
            number_of_columns = self.tableWidget_toaddclasses.columnCount()
            list_descriptors = df.columns
            print(list_descriptors)
            if 'Plate' in df.columns:
                list_plates = list(df['Plate'].drop_duplicates(keep="first"))
                nbr_rows = len(df)
                self.comboBox_plates.addItems((list_plates))
                self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
                self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
                self.comboBox_featuresfromdataframe.addItems(list_descriptors)

    def on_loadfromdataframe_clicked(self):
        print('1')
        self.getcellsvalues()
        print('2')
        df = pd.read_csv(
            'D:\RESULTS\\vl1vl2\\out.csv')
        df_rows = df.count()
        cols = 24
        rows = 16
        l = list(string.ascii_uppercase)
        self.lineEdit_filepathfromdataframe.setText(str('D:\RESULTS\\vl1vl2\\out.csv'))
        number_of_rows = self.tableWidget_toaddclasses.rowCount()
        number_of_columns = self.tableWidget_toaddclasses.columnCount()
        list_descriptors = df.columns
        if 'Plate' in df.columns:
            list_plates = list(df['Plate'].drop_duplicates(keep="first"))
            nbr_rows = len(df)
            self.comboBox_plates.addItems((list_plates))
            self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
            self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
            self.comboBox_featuresfromdataframe.addItems(list_descriptors)
            self.comboBox_featuresfromdataframe.currentTextChanged.connect(self.on_comboBox_featuresfromdataframe_changed)
            self.comboBox_plates.currentTextChanged.connect(self.on_comboBox_plates_changed)

    def getcellsvalues(self):
        print('3')
        selectedcells = self.tableWidget_toaddclasses.model().headerData(5, QtCore.Qt.Horizontal, QtCore.Qt.Vertical)
        # selectedcells = self.tableWidget_toaddclasses.selectionModel().selectedIndexes()
        print(selectedcells)
        self.tableWidget_toaddclasses.itemAt(1, 2).text()

    def on_comboBox_plates_changed(self):
        print('ok')

    def on_comboBox_featuresfromdataframe_changed(self, value_combox):
            file = self.lineEdit_filepathfromdataframe.text()
            if file == '':
                QMessageBox.information(None, "Error",
                                        "Please load a file first.",
                                        QMessageBox.Ok)
            if file != '':
                df = pd.read_csv(file)
                print(value_combox)
                cols = 24
                rows = 16
                l = list(string.ascii_uppercase)
                for k in range(len(l)):
                    for i in range(rows):
                        for j in range(cols):
                            for index, row in df.iterrows():
                                if  self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1))) == row['Well']:
                                    self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(str(df.loc[row, value_combox])))
                                # if  self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1))) == row['nbnuclei_wtdead']:
                                #     self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1)))

                        i += 1

    def fill_tablewidget(self):
        cols = 24
        rows = 16
        l = list(string.ascii_uppercase)
        for k in range(len(l)):
            for i in range(rows):
                for j in range(cols):
                    if j + 1 <= 9:
                        self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1)))
                    if j + 1 >= 10:
                        self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + str(j + 1)))
                i += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_table_addclasses = QtWidgets.QWidget()
    ui = Ui_form_table_addclasses()
    ui.setupUi(form_table_addclasses)
    form_table_addclasses.show()
    sys.exit(app.exec_())

