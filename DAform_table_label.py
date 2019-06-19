import numpy as np
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
        form_table_label.resize(1519, 492)
        self.tableWidget_tolabel = QtWidgets.QTableWidget(form_table_label)
        self.tableWidget_tolabel.setGeometry(QtCore.QRect(310, 40, 1151, 351))
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
        self.pushButton_labelplatebyplate.setGeometry(QtCore.QRect(1230, 420, 111, 31))
        self.pushButton_labelplatebyplate.setObjectName("pushButton_labelplatebyplate")
        self.comboBox_plates = QtWidgets.QComboBox(form_table_label)
        self.comboBox_plates.setGeometry(QtCore.QRect(20, 40, 261, 31))
        self.comboBox_plates.setObjectName("comboBox_plates")
        self.lineEdit_labelname = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_labelname.setGeometry(QtCore.QRect(150, 110, 131, 31))
        self.lineEdit_labelname.setObjectName("lineEdit_labelname")
        self.pushButton_selectfolder = QtWidgets.QPushButton(form_table_label)
        self.pushButton_selectfolder.setGeometry(QtCore.QRect(1130, 420, 80, 31))
        self.pushButton_selectfolder.setObjectName("pushButton_selectfolder")
        self.lineEdit_nbrplates = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_nbrplates.setGeometry(QtCore.QRect(20, 110, 121, 31))
        self.lineEdit_nbrplates.setText("")
        self.lineEdit_nbrplates.setObjectName("lineEdit_nbrplates")
        self.pushButton_labelallplates = QtWidgets.QPushButton(form_table_label)
        self.pushButton_labelallplates.setGeometry(QtCore.QRect(1350, 420, 111, 31))
        self.pushButton_labelallplates.setObjectName("pushButton_labelallplates")
        self.checkBox_channel2 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel2.setGeometry(QtCore.QRect(20, 270, 72, 19))
        self.checkBox_channel2.setObjectName("checkBox_channel2")
        self.lineEdit_thresholdch1 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch1.setGeometry(QtCore.QRect(110, 220, 113, 21))
        self.lineEdit_thresholdch1.setObjectName("lineEdit_thresholdch1")
        self.lineEdit_thresholdch4 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch4.setGeometry(QtCore.QRect(110, 370, 113, 21))
        self.lineEdit_thresholdch4.setObjectName("lineEdit_thresholdch4")
        self.checkBox_channel4 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel4.setGeometry(QtCore.QRect(20, 370, 72, 19))
        self.checkBox_channel4.setObjectName("checkBox_channel4")
        self.lineEdit_thresholdch3 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch3.setGeometry(QtCore.QRect(110, 320, 113, 21))
        self.lineEdit_thresholdch3.setObjectName("lineEdit_thresholdch3")
        self.checkBox_channel3 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel3.setGeometry(QtCore.QRect(20, 320, 72, 19))
        self.checkBox_channel3.setObjectName("checkBox_channel3")
        self.lineEdit_thresholdch0 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch0.setGeometry(QtCore.QRect(110, 170, 113, 21))
        self.lineEdit_thresholdch0.setObjectName("lineEdit_thresholdch0")
        self.checkBox_channel0 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel0.setGeometry(QtCore.QRect(20, 170, 72, 19))
        self.checkBox_channel0.setObjectName("checkBox_channel0")
        self.lineEdit_thresholdch2 = QtWidgets.QLineEdit(form_table_label)
        self.lineEdit_thresholdch2.setGeometry(QtCore.QRect(110, 270, 113, 21))
        self.lineEdit_thresholdch2.setObjectName("lineEdit_thresholdch2")
        self.checkBox_channel1 = QtWidgets.QCheckBox(form_table_label)
        self.checkBox_channel1.setGeometry(QtCore.QRect(20, 220, 72, 19))
        self.checkBox_channel1.setObjectName("checkBox_channel1")
        self.pushButton_apply = QtWidgets.QPushButton(form_table_label)
        self.pushButton_apply.setGeometry(QtCore.QRect(140, 420, 80, 31))
        self.pushButton_apply.setObjectName("pushButton_apply")

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
        self.comboBox_plates.currentTextChanged.connect(self.on_comboBoxplates_changed)

        self.retranslateUi(form_table_label)
        QtCore.QMetaObject.connectSlotsByName(form_table_label)

    def retranslateUi(self, form_table_label):
        _translate = QtCore.QCoreApplication.translate
        form_table_label.setWindowTitle(_translate("form_table_label", "Label"))
        self.pushButton_labelplatebyplate.setText(_translate("form_table_label", "Label plate by plate"))
        self.lineEdit_labelname.setText(_translate("form_table_label", "Label name"))
        self.pushButton_selectfolder.setText(_translate("form_table_label", "Select folder"))
        self.pushButton_labelallplates.setText(_translate("form_table_label", "Label all plates"))
        self.checkBox_channel2.setText(_translate("form_table_label", "Channel 2"))
        self.lineEdit_thresholdch1.setText(_translate("form_table_label", "Thresholds CH1"))
        self.lineEdit_thresholdch4.setText(_translate("form_table_label", "Thresholds CH4"))
        self.checkBox_channel4.setText(_translate("form_table_label", "Channel 4"))
        self.lineEdit_thresholdch3.setText(_translate("form_table_label", "Thresholds CH3"))
        self.checkBox_channel3.setText(_translate("form_table_label", "Channel 3"))
        self.lineEdit_thresholdch0.setText(_translate("form_table_label", "Thresholds CH0"))
        self.checkBox_channel0.setText(_translate("form_table_label", "Channel 0"))
        self.lineEdit_thresholdch2.setText(_translate("form_table_label", "Thresholds CH2"))
        self.checkBox_channel1.setText(_translate("form_table_label", "Channel 1"))
        self.pushButton_apply.setText(_translate("form_table_label", "Apply"))

    def select_folder(self):
        print('2')
        my_dir = QFileDialog.getExistingDirectory(
            None,
            "Select folder",
            "",
            QFileDialog.ShowDirsOnly)
        if my_dir:
            print('my dir')
            print(my_dir)
            files = []
            for r, d, f in os.walk(my_dir):
                for file in f:
                    print('file')
                    print(file)
                    if '.tif' in file:
                        self.r_toloop = r
                        self.d_toloop = d
                        print('d')
                        print(self.d_toloop)
                    files.append(os.path.join(r, file))
                self.filespath = files
            print(files)
        if self.d_toloop:
            list_plates = list(self.d_toloop)
            self.comboBox_plates.addItems((list_plates))
            self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')
            print('out')

    def select_multicolumns(self):
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
        for filename in self.filespath:
            print(filename)
            print(filename.split('_')[-1])
            if filename.split('_')[-1] == 'C01':
                ch0 = io.imread(filename, -1)
                nuc = ch0 > self.lineEdit_thresholdch0
                # ch0_thr = np.multiply(ch0, nuc)

    def on_selectfolder_clicked(self):
        print('1')
        self.select_folder()
        print('dldl')
        # if self.d_toloop:
        #     list_plates = list(self.d_toloop)
        #     self.comboBox_plates.addItems((list_plates))
        #     self.lineEdit_nbrplates.setText(str(len(list_plates)) + ' plates')

    def on_labelallplates_clicked(self):
        if (not self.comboBox_plates.currentText()):
            QMessageBox.information(None, "Error ",
                                    "Empty combo box.\nPlease select folder first to load plates.",
                                    QMessageBox.Ok)
        if (self.comboBox_plates.currentText()):
            if not self.select_multicolumns():
                QMessageBox.information(None, "Error ",
                                        "Please select column first.",
                                        QMessageBox.Ok)
            if self.select_multicolumns():
                if self.lineEdit_labelname.text() == 'Label name':
                    QMessageBox.information(None, "Error ",
                                            "Please enter a label name.\nYou can not label wihout entering a label name.",
                                            QMessageBox.Ok)
                if self.lineEdit_labelname.text() != 'Label name':
                    list_columnselected = self.select_multicolumns()
                    print(list_columnselected)
                    # for i in range(len(list_columnselected)):
                    #     print(list_columnselected[i])
                    #     col_nb = list_columnselected[i]

    def on_comboBoxplates_changed(self):
        self.tableWidget_tolabel.clearContents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_table_label = QtWidgets.QWidget()
    ui = Ui_form_table_label()
    ui.setupUi(form_table_label)
    form_table_label.show()
    sys.exit(app.exec_())

