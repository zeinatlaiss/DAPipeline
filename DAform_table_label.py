import pandas as pd
from skimage import io
import os
from PyQt5.QtWidgets import *
import string
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_table_label.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_table_label(object):
    def setupUi(self, form_table_label):
        form_table_label.setObjectName("form_table_label")
        form_table_label.resize(1548, 552)
        self.tableWidget_tolabel = QtWidgets.QTableWidget(form_table_label)
        self.tableWidget_tolabel.setGeometry(QtCore.QRect(310, 90, 1221, 351))
        self.tableWidget_tolabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_tolabel.setColumnCount(0)
        self.tableWidget_tolabel.setObjectName("tableWidget_tolabel")
        self.tableWidget_tolabel.setRowCount(0)
        self.tableWidget_tolabel.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_tolabel.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_tolabel.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_tolabel.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_tolabel.verticalHeader().setSortIndicatorShown(False)
        self.pushButton_labelplatebyplate = QtWidgets.QPushButton(form_table_label)
        self.pushButton_labelplatebyplate.setGeometry(QtCore.QRect(1291, 470, 111, 31))
        self.pushButton_labelplatebyplate.setObjectName("pushButton_labelplatebyplate")
        self.comboBox_plates = QtWidgets.QComboBox(form_table_label)
        self.comboBox_plates.setGeometry(QtCore.QRect(20, 40, 261, 31))
        self.comboBox_plates.setObjectName("comboBox_plates")
        self.lineEdit_labelname = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_labelname.setGeometry(QtCore.QRect(150, 170, 121, 21))
        self.lineEdit_labelname.setObjectName("lineEdit_labelname")
        self.pushButton_selectfolder = QtWidgets.QPushButton(form_table_label)
        self.pushButton_selectfolder.setGeometry(QtCore.QRect(1171, 470, 101, 31))
        self.pushButton_selectfolder.setObjectName("pushButton_selectfolder")
        self.lineEdit_nbrplates = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_nbrplates.setGeometry(QtCore.QRect(910, 40, 121, 31))
        self.lineEdit_nbrplates.setText("")
        self.lineEdit_nbrplates.setFrame(False)
        self.lineEdit_nbrplates.setObjectName("lineEdit_nbrplates")
        self.pushButton_labelallplates = QtWidgets.QPushButton(form_table_label)
        self.pushButton_labelallplates.setGeometry(QtCore.QRect(1420, 470, 111, 31))
        self.pushButton_labelallplates.setObjectName("pushButton_labelallplates")
        self.checkBox_channel2 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel2.setGeometry(QtCore.QRect(20, 320, 72, 19))
        self.checkBox_channel2.setObjectName("checkBox_channel2")
        self.lineEdit_thresholdch1 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch1.setGeometry(QtCore.QRect(150, 270, 121, 21))
        self.lineEdit_thresholdch1.setObjectName("lineEdit_thresholdch1")
        self.lineEdit_thresholdch4 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch4.setGeometry(QtCore.QRect(150, 420, 121, 21))
        self.lineEdit_thresholdch4.setObjectName("lineEdit_thresholdch4")
        self.checkBox_channel4 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel4.setGeometry(QtCore.QRect(20, 420, 72, 19))
        self.checkBox_channel4.setObjectName("checkBox_channel4")
        self.lineEdit_thresholdch3 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch3.setGeometry(QtCore.QRect(150, 370, 121, 21))
        self.lineEdit_thresholdch3.setObjectName("lineEdit_thresholdch3")
        self.checkBox_channel3 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel3.setGeometry(QtCore.QRect(20, 370, 72, 19))
        self.checkBox_channel3.setObjectName("checkBox_channel3")
        self.lineEdit_thresholdch0 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch0.setGeometry(QtCore.QRect(150, 220, 121, 21))
        self.lineEdit_thresholdch0.setObjectName("lineEdit_thresholdch0")
        self.checkBox_channel0 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel0.setGeometry(QtCore.QRect(20, 220, 81, 19))
        self.checkBox_channel0.setObjectName("checkBox_channel0")
        self.lineEdit_thresholdch2 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch2.setGeometry(QtCore.QRect(150, 320, 121, 21))
        self.lineEdit_thresholdch2.setObjectName("lineEdit_thresholdch2")
        self.checkBox_channel1 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel1.setGeometry(QtCore.QRect(20, 270, 72, 19))
        self.checkBox_channel1.setObjectName("checkBox_channel1")
        self.pushButton_apply = QtWidgets.QPushButton(form_table_label)
        self.pushButton_apply.setGeometry(QtCore.QRect(150, 470, 91, 31))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.pushButton_display = QtWidgets.QPushButton(form_table_label)
        self.pushButton_display.setGeometry(QtCore.QRect(20, 470, 91, 31))
        self.pushButton_display.setObjectName("pushButton_display")
        self.pushButton_selectfromfile = QtWidgets.QPushButton(form_table_label)
        self.pushButton_selectfromfile.setGeometry(QtCore.QRect(1060, 470, 91, 31))
        self.pushButton_selectfromfile.setObjectName("pushButton_selectfromfile")
        self.comboBox_descriptors = QtWidgets.QComboBox(form_table_label)
        self.comboBox_descriptors.setGeometry(QtCore.QRect(20, 90, 261, 31))
        self.comboBox_descriptors.setObjectName("comboBox_descriptors")
        self.lineEdit_nbrimages = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_nbrimages.setGeometry(QtCore.QRect(1060, 40, 121, 31))
        self.lineEdit_nbrimages.setText("")
        self.lineEdit_nbrimages.setFrame(False)
        self.lineEdit_nbrimages.setObjectName("lineEdit_nbrimages")
        self.lineEdit_filepathtoload = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_filepathtoload.setGeometry(QtCore.QRect(310, 40, 571, 31))
        self.lineEdit_filepathtoload.setText("")
        self.lineEdit_filepathtoload.setFrame(False)
        self.lineEdit_filepathtoload.setObjectName("lineEdit_filepathtoload")

        cols = 24
        rows = 16
        ll2 = list(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24'])

        l = list(string.ascii_uppercase)
        self.tableWidget_tolabel.setRowCount(rows)
        self.tableWidget_tolabel.setColumnCount(cols)
        self.tableWidget_tolabel.setVerticalHeaderLabels(l)
        self.tableWidget_tolabel.setHorizontalHeaderLabels(ll2)

        self.pushButton_selectfolder.clicked.connect(self.on_selectfolder_clicked)
        self.pushButton_labelallplates.clicked.connect(self.on_labelallplates_clicked)
        self.pushButton_apply.clicked.connect(self.on_apply_clicked)
        self.comboBox_descriptors.currentTextChanged.connect(self.on_comboBoxdescriptors_changed)
        self.comboBox_plates.currentTextChanged.connect(self.on_comboBoxplates_changed)
        self.pushButton_selectfromfile.clicked.connect(self.on_selectfile_clicked)
        self.pushButton_labelallplates.clicked.connect(self.on_labelallplates_clicked)

        self.retranslateUi(form_table_label)
        QtCore.QMetaObject.connectSlotsByName(form_table_label)

    def retranslateUi(self, form_table_label):
        _translate = QtCore.QCoreApplication.translate
        form_table_label.setWindowTitle(_translate("form_table_label", "Label"))
        self.pushButton_labelplatebyplate.setText(_translate("form_table_label", "Label plate by plate"))
        self.lineEdit_labelname.setText(_translate("form_table_label", "Label name"))
        self.pushButton_selectfolder.setText(_translate("form_table_label", "Select from folder"))
        self.pushButton_labelallplates.setText(_translate("form_table_label", "Label all plates"))
        self.checkBox_channel2.setText(_translate("form_table_label", "Channel 2"))
        self.lineEdit_thresholdch1.setText(_translate("form_table_label", "Threshold CH1"))
        self.lineEdit_thresholdch4.setText(_translate("form_table_label", "Threshold CH4"))
        self.checkBox_channel4.setText(_translate("form_table_label", "Channel 4"))
        self.lineEdit_thresholdch3.setText(_translate("form_table_label", "Threshold CH3"))
        self.checkBox_channel3.setText(_translate("form_table_label", "Channel 3"))
        self.lineEdit_thresholdch0.setText(_translate("form_table_label", "Threshold CH0"))
        self.checkBox_channel0.setText(_translate("form_table_label", "Channel 0"))
        self.lineEdit_thresholdch2.setText(_translate("form_table_label", "Threshold CH2"))
        self.checkBox_channel1.setText(_translate("form_table_label", "Channel 1"))
        self.pushButton_apply.setText(_translate("form_table_label", "Apply"))
        self.pushButton_display.setText(_translate("form_table_label", "Display"))
        self.pushButton_selectfromfile.setText(_translate("form_table_label", "Select from file"))

    def loadFile_label(self):
        print('Load file')
        fileName = self.lineEdit_filepathtoload.text()
        if fileName == ' ':
            QMessageBox.information(None, "Error ",
                                    "Please load a file first.",
                                    QMessageBox.Ok)
        if fileName != ' ':
            df = pd.read_csv(fileName, low_memory=False)
            if 'Well' not in df:
                self.lineEdit_filepathtoload.setText('')
                QMessageBox.information(None, "Error ",
                                        "The column Well is not in the file.\nTry again.",
                                        QMessageBox.Ok)
            if 'Well' in df:
                df_rows = df.count()
                cols = 24
                rows = 16
                l = list(string.ascii_uppercase)
                number_of_rows = self.tableWidget_tolabel.rowCount()
                number_of_columns = self.tableWidget_tolabel.columnCount()
                list_descriptors = df.columns
                if 'Plate' in df.columns:
                    list_plates = list(df['Plate'].drop_duplicates(keep="first"))
                    nbr_rows = len(df)
                    self.comboBox_plates.addItems((list_plates))
                    self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')
                    # self.comboBox_featuresfromdataframe.addItem('Descriptor', 'ss')
                    # self.comboBox_featuresfromdataframe.addItems(list_descriptors)
                    self.df = df

    def select_folder(self):
        print('select folder')
        my_dir = QFileDialog.getExistingDirectory(
            None,
            "Select folder",
            "",
            QFileDialog.ShowDirsOnly)
        if my_dir:
            roots = []
            dirs = []
            files = []
            for r, d, f in os.walk(my_dir):
                for file in f:
                    if '.tif' in file:
                        self.r_toloop = r
                        self.d_toloop = d
                        files.append(os.path.join(r, file))
                        print(len(files))
                    # self.filespath = files
                # rr = r.split("\\")[-1]
                # roots.append(rr)
                for dir_in in d:
                    if dir_in:
                        print(dir_in)
                        dirs.append(dir_in)
                    print(dirs)

        # if self.d_toloop:
        #     list_plates = list(self.d_toloop)
        #     self.comboBox_plates.addItems((list_plates))
        #     self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')

    def select_multicolumns(self):
        print('multicol')
        list_col = []
        totalColumns = self.tableWidget_tolabel.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.tableWidget_tolabel.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                           QtCore.Qt.DisplayRole)
            list_col.append(column_name)
        return list_col

    def on_apply_clicked(self):
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            QMessageBox.information(None, "Error",
                                    "Please check at least one of the above cases.",
                                    QMessageBox.Ok)
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('0')

        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('1')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('2')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('3')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('4')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('5')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('6')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('7')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and not \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('8')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('29')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('9')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('28')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('17')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('18')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('19')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('20')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('21')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('22')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('25')
        if self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('23')
        if self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('26')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('10')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('11')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('12')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('24')
        if not self.checkBox_channel0.isChecked() and self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('24')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('27')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and not self.checkBox_channel4.isChecked():
            print('13')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        self.checkBox_channel2.isChecked() and not self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('15')
        if not self.checkBox_channel0.isChecked() and not self.checkBox_channel1.isChecked() and \
                        not self.checkBox_channel2.isChecked() and self.checkBox_channel3.isChecked() and self.checkBox_channel4.isChecked():
            print('16')

    def get_filespath(self):
        print('get filepath')
        for filename in self.filespath:
            # print(filename)
            print('ok')
            # print(filename.split('_')[-1])
            if filename.split('_')[-1] == 'C01':
                ch0 = io.imread(filename, -1)
                nuc = ch0 > self.lineEdit_thresholdch0
                # ch0_thr = np.multiply(ch0, nuc)

    def on_selectfolder_clicked(self):
        print('folder')
        self.select_folder()
        # self.for_loop()
        print('end select folder')
        # if self.d_toloop:
        #     list_plates = list(self.d_toloop)
        #     self.comboBox_plates.addItems((list_plates))
        #     self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')

    def on_reloadFile_clicked(self, file):
        self.tableWidget_tolabel.clearContents()
        self.comboBox_plates.clear()
        self.lineEdit_filepathtoload.setText(file)
        df = pd.read_csv(file, low_memory=False)
        if 'Well' not in df:
            self.lineEdit_filepathtoload.setText('')
            QMessageBox.information(None, "Error ",
                                    "The column Well is not in the file.\nTry again.",
                                    QMessageBox.Ok)
        if 'Well' in df:
            df_rows = df.count()
            cols = 24
            rows = 16
            l = list(string.ascii_uppercase)
            number_of_rows = self.tableWidget_tolabel.rowCount()
            number_of_columns = self.tableWidget_tolabel.columnCount()
            list_descriptors = df.columns
            list_plates = list(df['Plate'].drop_duplicates(keep="first"))
            nbr_rows = len(df)
            self.comboBox_plates.addItems((list_plates))
            self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')
            self.lineEdit_nbrimages.setText(str(nbr_rows) + ' wells')
            self.df = df

    def on_labelallplates_clicked(self):
        print('label ok')
        if (not self.comboBox_plates.currentText()):
            QMessageBox.information(None, "Error ",
                                    "Empty combo box.\nPlease load a file or select a folder to load plates.",
                                    QMessageBox.Ok)
        if (self.comboBox_plates.currentText()):
            if 'Class' not in self.comboBox_descriptors.currentText() and 'label' not in self.comboBox_descriptors.currentText():
                if not self.select_multicolumns():
                    QMessageBox.information(None, "Error ",
                                            "Please select column first.",
                                            QMessageBox.Ok)
                if self.select_multicolumns():
                    if self.lineEdit_labelname.text() == 'Label name':
                        print('f')
                        QMessageBox.information(None, "Error ",
                                                "Please enter a label name.\nYou can not label wihout entering a label name.",
                                                QMessageBox.Ok)
                    if self.lineEdit_labelname.text() != 'Label name':
                        print('d')
                        list_columnselected = self.select_multicolumns()
                        print(list_columnselected)
                        # for i in range(len(list_columnselected)):
                        #     print(list_columnselected[i])
                        #     col_nb = list_columnselected[i]

            if 'Class' in self.comboBox_descriptors.currentText():
                buttonReply = QMessageBox.question(None, 'Data already labelled',
                                                    "The loaded plates are already labelled.\n"
                                                    "Press Yes if you want to relabel using the line edit Label name.\n"
                                                    "Press No to keep same label.\n",
                                                   QMessageBox.Yes | QMessageBox.No,
                                                   QMessageBox.Yes)
                if buttonReply == QMessageBox.Yes:
                    if 'label' in self.df.columns:
                        d = self.df.drop(['label'], axis=1)
                        print(d)
                        t1 = os.path.dirname(self.lineEdit_filepathtoload.text())
                        file_name1 = os.path.splitext(os.path.basename(self.lineEdit_filepathtoload.text()))[0]
                        d.to_csv(t1 + '\\' + file_name1 + '.csv', index=None)
                        self.lineEdit_filepathtoload.setText(t1 + '\\' + file_name1 + '.csv')
                        self.on_reloadFile_clicked(t1 + '\\' + file_name1 + '.csv')
                        if not self.select_multicolumns():
                            QMessageBox.information(None, "Error ",
                                                    "Please select column first.",
                                                    QMessageBox.Ok)
                        if self.select_multicolumns():
                            if self.lineEdit_labelname.text() == 'Label name':
                                print('no label')
                                QMessageBox.information(None, "Error ",
                                                        "Please enter a label name in order to label your data.\n",
                                                        QMessageBox.Ok)
                            if self.lineEdit_labelname.text() != 'Label name':
                                list_columnselected = self.select_multicolumns()
                                print(list_columnselected)

                    if 'Class' in self.df.columns:
                        d = self.df.drop(['Class'], axis=1)
                        print(d)
                        t1 = os.path.dirname(self.lineEdit_filepathtoload.text())
                        file_name1 = os.path.splitext(os.path.basename(self.lineEdit_filepathtoload.text()))[0]
                        d.to_csv(t1 + '\\' + file_name1 + '.csv', index=None)
                        self.lineEdit_filepathtoload.setText(t1 + '\\' + file_name1 + '.csv')
                        self.on_reloadFile_clicked(t1 + '\\' + file_name1 + '.csv')
                        if not self.select_multicolumns():
                            QMessageBox.information(None, "Error ",
                                                    "Please select column first.",
                                                    QMessageBox.Ok)
                        if self.select_multicolumns():
                            if self.lineEdit_labelname.text() == 'Label name':
                                QMessageBox.information(None, "Error ",
                                                        "Please enter a label name in order to label your data.\n",
                                                        QMessageBox.Ok)
                            if self.lineEdit_labelname.text() != 'Label name':
                                list_columnselected = self.select_multicolumns()
                                print(list_columnselected)


    def on_comboBoxplates_changed(self):
        self.tableWidget_tolabel.clearContents()
        # self.comboBox_descriptors.setCurrentIndex(0)
        self.on_comboBoxdescriptors_changed()

    def on_comboBoxdescriptors_changed(self):
        self.fill_tablewidget()

    def load_dict(self, plate, desc):
        df_plate = self.df[self.df["Plate"] == plate]
        if 'Well' not in df_plate:
            print('no')
        if 'Well' in df_plate:
            keys = df_plate["Well"]
            values = df_plate[desc]
            dict_well = dict(zip(keys, values))
            return dict_well

    def fill_tablewidget(self):
        cols = 24
        rows = 16
        ll1 = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])
        ll2 = list(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24'])
        plate_cb = self.comboBox_plates.currentText()
        desc_cb = self.comboBox_descriptors.currentText()
        if desc_cb != 'Descriptor':
            dict_table_well = self.load_dict(plate_cb, desc_cb)
            for row, i in enumerate(range(len(ll1))):
                for col, j in enumerate(range(len(ll2))):
                    well_from_list = str(ll1[row]) + str(ll2[col])
                    value = 0
                    if well_from_list in dict_table_well.keys():
                        value = dict_table_well[well_from_list]
                        item = QTableWidgetItem(str(value))
                        self.tableWidget_tolabel.setItem(row, col, item)


    def on_selectfile_clicked(self):
        self.tableWidget_tolabel.clearContents()
        self.comboBox_plates.clear()
        self.comboBox_descriptors.addItem('Descriptor', 'ss')
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            exists = os.path.isfile(fileName)
            if exists:
                self.lineEdit_filepathtoload.setText(fileName)
                df = pd.read_csv(fileName, low_memory=False)
                if 'Well' not in df:
                    self.lineEdit_filepathtoload.setText('  ')
                    QMessageBox.information(None, "Error ",
                                            "The column Well is not in the file.\nTry again.",
                                            QMessageBox.Ok)
                if 'Well' in df:
                    df_rows = df.count()
                    cols = 24
                    rows = 16
                    l = list(string.ascii_uppercase)
                    number_of_rows = self.tableWidget_tolabel.rowCount()
                    number_of_columns = self.tableWidget_tolabel.columnCount()
                    list_descriptors = df.columns
                    list_plates = list(df['Plate'].drop_duplicates(keep="first"))
                    nbr_rows = len(df)
                    self.comboBox_plates.addItems((list_plates))
                    self.lineEdit_nbrimages.setText(str(len(df['Well'])) + ' wells')
                    self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')
                    self.df = df
                    list_descriptors = df.columns
                    print(list_descriptors)
                    self.comboBox_descriptors.addItems(list_descriptors)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_table_label = QtWidgets.QWidget()
    ui = Ui_form_table_label()
    ui.setupUi(form_table_label)
    form_table_label.show()
    sys.exit(app.exec_())

