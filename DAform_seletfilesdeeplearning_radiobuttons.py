from joblib import Parallel, delayed
from PyQt5.QtWidgets import *
from DAform_table_label import Ui_form_table_label
import numpy as np
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_seletfilesdeeplearning_radiobuttons.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_selectfiles(object):

    def openwindow_form_tablelabel(self):
        print('first')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_form_table_label()
        self.ui.setupUi(self.window)
        # self.fill_tablewidget_fromdatfiles()
        self.window.show()

    def setupUi(self, Form_selectfiles):
        Form_selectfiles.setObjectName("Form_selectfiles")
        Form_selectfiles.resize(212, 175)
        self.radioButton_datfiles = QtWidgets.QRadioButton(Form_selectfiles)
        self.radioButton_datfiles.setGeometry(QtCore.QRect(70, 30, 84, 19))
        self.radioButton_datfiles.setObjectName("radioButton_datfiles")
        self.radioButton_pklfiles = QtWidgets.QRadioButton(Form_selectfiles)
        self.radioButton_pklfiles.setGeometry(QtCore.QRect(70, 70, 84, 19))
        self.radioButton_pklfiles.setObjectName("radioButton_pklfiles")
        self.pushButton_selectfiles = QtWidgets.QPushButton(Form_selectfiles)
        self.pushButton_selectfiles.setGeometry(QtCore.QRect(70, 110, 81, 31))
        self.pushButton_selectfiles.setObjectName("pushButton_selectfiles")

        self.pushButton_selectfiles.clicked.connect(self.on_selectfiles_clicked)
        # self.ui.comboBox_plates.currentTextChanged.connect(self.on_comboBoxplatesdatfiles_changed)

        self.retranslateUi(Form_selectfiles)
        QtCore.QMetaObject.connectSlotsByName(Form_selectfiles)

    def retranslateUi(self, Form_selectfiles):
        _translate = QtCore.QCoreApplication.translate
        Form_selectfiles.setWindowTitle(_translate("Form_selectfiles", "Select files"))
        self.radioButton_datfiles.setText(_translate("Form_selectfiles", ".dat files"))
        self.radioButton_pklfiles.setText(_translate("Form_selectfiles", ".pkl files"))
        self.pushButton_selectfiles.setText(_translate("Form_selectfiles", "Select"))

    def select_multicolumns(self):
        print('3')
        list_col = []
        totalColumns = self.ui.tableWidget_tolabel.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.ui.tableWidget_tolabel.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                           QtCore.Qt.DisplayRole)
            list_col.append(column_name)
            if len(list_col) > 0:
                print(list_col)
        return list_col

    def on_selectfiles_clicked(self):
        print('select files')
        if self.radioButton_datfiles.isChecked() and not self.radioButton_pklfiles.isChecked():
            filter = ".dat(*.dat)"
            filename, _ = QFileDialog.getOpenFileNames(None, "Select .dat files",
                                                       "",
                                                       filter)
            if filename:
                list_files = []
                list_wells = []
                list_plates = []
                for i in filename:
                    well_name = i.split(".")[0].split("_")[-1]
                    plate_name = i.split(".")[0].split("_")[-3]
                    list_files.append(i)
                    list_wells.append(well_name)
                    list_plates.append(plate_name)
                    self.platename = plate_name
                    self.wellname = well_name
                if len(list_files) != 0 and len(list_wells) != 0:
                    self.l_files = list_files
                    self.l_wells = list_wells
                    self.l_plates = list_plates
                    self.openwindow_form_tablelabel()
                    self.fill_tablewidget_fromdatfiles()
                    listcols = self.select_multicolumns()
                    print(listcols)

                    # data = Parallel(n_jobs=60, verbose=50, max_nbytes=None)(delayed(self.read_file)(i) for i in self.l_files)
                    # self.read_file()
                    # if len(self.listcols)== 0:
                    #     self.listcols = self.select_multicolumns()
                    #     self.classvalues, self.texteditvalues = self.ui.on_apply_clicked()
                    #     print(self.listcols)
                    # if len(self.listcols) > 0:
                    #     print('list of columns in apply clicked', self.listcols)
                    # if len(self.listcols) == 0:
                    #     print('The selection not finished yet')
                    # return self.l_plates, self.l_files, self.l_wells
                # else:
                #     print('no file has been selected\nEmpty lists')

        # if not self.radioButton_datfiles.isChecked() and self.radioButton_pklfiles.isChecked():
        #     filter = ".pkl(*.pkl)"
        #     filename, _ = QFileDialog.getOpenFileNames(None, "Select .pkl files",
        #                                                "",
        #                                                filter)
        #     if filename:
        #         list_files = []
        #         list_wells = []
        #         list_plates = []
        #         for i in filename:
        #             well_name = i.split(".")[0].split("_")[-1]
        #             plate_name = i.split(".")[0].split("_")[-2]
        #             list_files.append(i)
        #             list_wells.append(well_name)
        #             list_plates.append(plate_name)
        #         if len(list_files) != 0 and len(list_wells) != 0:
        #             print(list_plates, list_files, list_wells)
        #             self.l_files = list_files
        #             self.l_wells = list_wells
        #             self.l_plates = list_plates
        #             self.openwindow_form_tablelabel()
        #             return self.l_plates, self.l_files, self.l_wells
        #         else:
        #             print('no file has been selected\nEmpty lists')

    def fill_tablewidget_fromdatfiles(self):
        print('2')
        cols = 24
        rows = 16
        ll1 = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])
        ll2 = list(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24'])
        for row, i in enumerate(range(len(ll1))):
            for col, j in enumerate(range(len(ll2))):
                well_from_list = str(ll1[row]) + str(ll2[col])
                value = 0
                for w1 in range(len(self.l_wells)):
                    if well_from_list == self.l_wells[w1]:
                        value = self.l_wells[w1]
                        item = QTableWidgetItem(str(value))
                        self.ui.tableWidget_tolabel.setItem(row, col, item)

                        #     if len(list_columnselected) > 0:
                        #         self.labelname = textedit_value
                        #         self.l_cols = list_columnselected
                        #         self.classnb = class_value
                        #         return self.l_cols, self.labelname

                        #     if self.l__cols:
                        #         for i in self.l_wells:
                        #             well_nb = int(i[1:3])
                        #             # print('list of columns', self.l__cols)
                        #             if well_nb in self.l__cols:
                        #                 print('well nb', well_nb)
                        #             else:
                        #                 print('not in the list')
                        #                 os.rename('D:\PYTHON CODE\DAPipeline\FinalFiles\\' + self.platename+'\\'+'_well_'+ i + '.dat',
                        #                           'D:\PYTHON CODE\DAPipeline\FinalFiles\\'+ self.platename+'\\'+'_well_'+ self.wellname + '_label_'+ self.ui.labelname + '.dat')

    def on_comboBoxplatesdatfiles_changed(self):
        # print('combo')
        self.ui.tableWidget_tolabel.clearContents()
        # self.comboBox_descriptors.setCurrentIndex(0)
        # self.fill_tablewidget_fromdatfiles()

    def read_file(self):
        data = np.fromfile(self.l_files, dtype=np.float32)
        nbr_crop = data.shape[0] / (256 * 256 * 3)
        crop = np.array_split(data, nbr_crop)
        crop = np.array(crop).reshape(int(nbr_crop), 3, 256, 256)
        crop_2 = crop.transpose(0, 2, 3, 1)

    def add_label_infilename(self):
        print('add label in filename')
        for i in self.l_wells:
            well_nb = int(i[1:3])
            print(well_nb)
            # print(self.l__cols)
            # # if len(self.l__cols) == 0:
            # #     QMessageBox.information(None, "Select columns to label",
            # #                             "Please select columns to label",
            # #                             QMessageBox.Ok)
            # # if len(self.l__cols) == 0:
            # #     print('1')
            # if len(self.l__cols) > 0:
            #     print('list of columns', self.l__cols)
            #     if well_nb in self.l__cols:
            #         print('well nb', well_nb)
            # #     else:
            # #         print('not in the list')
            # #     os.rename('D:\PYTHON CODE\DAPipeline\FinalFiles\\' + self.platename+'\\'+'_well_'+ i + '.dat',
            # #               'D:\PYTHON CODE\DAPipeline\FinalFiles\\'+ self.platename+'\\'+'_well_'+ self.wellname + '_label_'+ self.ui.labelname + '.dat')
            # #     print('1')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_selectfiles = QtWidgets.QWidget()
    ui = Ui_Form_selectfiles()
    ui.setupUi(Form_selectfiles)
    Form_selectfiles.show()
    sys.exit(app.exec_())
