import os
from matplotlib import cm
import matplotlib
import pandas as pd
from PyQt5.QtWidgets import *
import string
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_table_addclasses.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_table_addclasses(object):
    def setupUi(self, form_table_addclasses):
        form_table_addclasses.setObjectName("form_table_addclasses")
        form_table_addclasses.resize(1262, 593)
        self.pushButton_apply = QtWidgets.QPushButton(form_table_addclasses)
        self.pushButton_apply.setGeometry(QtCore.QRect(1170, 550, 80, 21))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.tableWidget_toaddclasses = QtWidgets.QTableWidget(form_table_addclasses)
        self.tableWidget_toaddclasses.setGeometry(QtCore.QRect(20, 170, 1231, 351))
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
        self.comboBox_addclass = QtWidgets.QComboBox(form_table_addclasses)
        self.comboBox_addclass.setGeometry(QtCore.QRect(1170, 80, 81, 21))
        self.comboBox_addclass.setObjectName("comboBox_addclass")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.comboBox_addclass.addItem("")
        self.lineEdit_class = QtWidgets.QLineEdit(form_table_addclasses)
        self.lineEdit_class.setGeometry(QtCore.QRect(1172, 120, 81, 21))
        self.lineEdit_class.setObjectName("lineEdit_class")

        cols = 24
        rows = 16
        ll2 = list(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24'])

        l = list(string.ascii_uppercase)
        self.tableWidget_toaddclasses.setRowCount(rows)
        self.tableWidget_toaddclasses.setColumnCount(cols)
        # if j + 1 <= 9:
        #     if  self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1))) == df['Well']:
        #         self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1)))
        # if j + 1 >= 10:
        #     self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + str(j + 1)))

        self.tableWidget_toaddclasses.setVerticalHeaderLabels(l)
        self.tableWidget_toaddclasses.setHorizontalHeaderLabels(ll2)

        self.pushButton_loadfileaddclasses.clicked.connect(self.on_loadFile_clicked)
        self.pushButton_apply.clicked.connect(self.on_class_clicked)
        self.comboBox_featuresfromdataframe.currentTextChanged.connect(self.on_comboBox_featuresfromdataframe_changed)
        self.comboBox_plates.currentTextChanged.connect(self.on_comboBoxplates_changed)
        self.comboBox_addclass.currentTextChanged.connect(self.on_comboBoxaddclass_changed)

        self.retranslateUi(form_table_addclasses)
        QtCore.QMetaObject.connectSlotsByName(form_table_addclasses)

    def retranslateUi(self, form_table_addclasses):
        _translate = QtCore.QCoreApplication.translate
        form_table_addclasses.setWindowTitle(_translate("form_table_addclasses", "Add classes form"))
        self.pushButton_apply.setText(_translate("form_table_addclasses", "Apply"))
        self.pushButton_loadfileaddclasses.setText(_translate("form_table_addclasses", "Load file"))
        self.comboBox_addclass.setItemText(0, _translate("form_table_addclasses", "Add class"))
        self.comboBox_addclass.setItemText(1, _translate("form_table_addclasses", "Class 0"))
        self.comboBox_addclass.setItemText(2, _translate("form_table_addclasses", "Class 1"))
        self.comboBox_addclass.setItemText(3, _translate("form_table_addclasses", "Class 2"))
        self.comboBox_addclass.setItemText(4, _translate("form_table_addclasses", "Class 3"))
        self.comboBox_addclass.setItemText(5, _translate("form_table_addclasses", "Class 4"))
        self.comboBox_addclass.setItemText(6, _translate("form_table_addclasses", "Class 5"))
        self.comboBox_addclass.setItemText(7, _translate("form_table_addclasses", "Class 6"))
        self.comboBox_addclass.setItemText(8, _translate("form_table_addclasses", "Class 7"))
        self.comboBox_addclass.setItemText(9, _translate("form_table_addclasses", "Class 8"))
        self.comboBox_addclass.setItemText(10, _translate("form_table_addclasses", "Class 9"))
        self.comboBox_addclass.setItemText(11, _translate("form_table_addclasses", "Class 10"))
        self.comboBox_addclass.setItemText(12, _translate("form_table_addclasses", "Class 11"))
        self.comboBox_addclass.setItemText(13, _translate("form_table_addclasses", "Class 12"))
        self.lineEdit_class.setText(_translate("form_table_addclasses", "Add Class"))

    def interpolate(self, val, y0, x0, y1, x1):
        return (val - x0) * (y1 - y0) / (x1 - x0) + y0

    def baases(self, val):
        if val <= 0.75:
            return 0
        if val <= -0.25:
            return self.interpolate(val, 0.0, -0.75, 1.0, -0.25)
        if val <= 0.25:
            return 1.0
        if val <= 0.75:
            return self.interpolate(val, 1.0, 0.25, 0.0, 0.75)
        else:
            return 0.0

    def red(self, gray):
        return self.baases(gray - 0.5)

    def green(self, gray):
        return self.baases(gray)

    def blue(self, gray):
        return self.baases(gray + 0.5)

    def getminmax(self):
        n = self.tableWidget_toaddclasses.rowCount()
        m = self.tableWidget_toaddclasses.columnCount()
        fileList = []
        for i in range(0, n):
            for j in range(0, m):
                item = self.tableWidget_toaddclasses.item(i, j)
                if item and item.text():
                    fileList.append(float(item.text()))
        min_val = min(fileList)
        max_val = max(fileList)
        return min_val, max_val, fileList

    def coloring(self):
        cmap = matplotlib.cm.autumn

    def get_color_colormap(self, val_min, val_max, val):

        vv = ((float(val) - float(val_min)) / float(val_max)) * 255.0
        # norm = matplotlib.colors.Normalize(val_min, val_max)
        # col = cmap(norm(val))
        return vv

    def select_multicolumns(self):
        list_col = []
        totalColumns = self.tableWidget_toaddclasses.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.tableWidget_toaddclasses.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                           QtCore.Qt.DisplayRole)
            list_col.append(column_name)
        return list_col

    def on_comboBoxaddclass_changed(self):
        cb_value = self.comboBox_addclass.currentText()
        class_nb = cb_value.split(" ")[1]
        self.ll = class_nb

    def on_class_clicked(self):
        file = self.lineEdit_filepathfromdataframe.text()
        # if str(self.lineEdit_class) == 'Add Class' and str(self.comboBox_addclass) != 'Add class':
        #     QMessageBox.information(None, "Error ",
        #                             "Please enter a class number in the text line or the combobox.",
        #                             QMessageBox.Ok)
        exists = os.path.isfile(file)
        if exists:
        # # if self.comboBox_addclass == 'Add class' and self.comboBox_addclass != 'Add class':
        # #     print('ff')
        # if self.comboBox_addclass != 'Add class' and self.comboBox_addclass == 'Add class':
            print('1')
            t1 = os.path.dirname(file)
            file_name1 = os.path.splitext(os.path.basename(file))[0]
            list_columnselected = self.select_multicolumns()
            if not self.select_multicolumns():
                print('vo')
            if self.select_multicolumns():
                if file == '':
                    QMessageBox.information(None, "Error ",
                                            "No loaded file.\nPlease load a file first.",
                                            QMessageBox.Ok)
                if file != '':
                    df = pd.read_csv(file)

                    if 'Well' not in df:
                        self.lineEdit_filepathfromdataframe.setText('')
                        QMessageBox.information(None, "Error ",
                                                "The column Well is not in the file.\nTry again.",
                                                QMessageBox.Ok)

                    if 'Well' in df:
                        list_plates = list(df['Plate'])
                        nbr_rows = len(df)
                        self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
                        self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
                        df1 = df
                        if 'Class' not in df1:
                            # if (self.comboBox_addclass.currentText() == "Add class"):
                            # else:
                                # for i in range(len(list_columnselected)):
                            cl_nb = self.ll
                            #     for i in range(len(list_columnselected)):
                            df1['c'] = df1['Well'].apply(lambda x: any([k in x for k in list_columnselected]))
                            if df1['c'].any() == True:
                                dff1 = df1[df1['c'] == True]
                                dff2 = df1[df1['c'] == False]
                                dff1['Class'] = cl_nb
                                dff2['Class'] = ''
                                dff_conc = pd.concat([dff1, dff2])
                                d_dropped = dff_conc.drop('c', axis=1)
                                d_dropped.to_csv(t1 + '\\' + file_name1 + '.csv', index=None)
                                self.on_reloadFile_clicked(t1 + '\\' + file_name1 + '.csv')
                                # self.comboBox_featuresfromdataframe.clear()
                                self.comboBox_featuresfromdataframe.addItem('Descriptor', 'ss')
                                d_dropped = pd.read_csv(t1 + '\\' + file_name1 + '.csv')
                                list_descriptors = d_dropped.columns
                                self.comboBox_featuresfromdataframe.addItems(list_descriptors)

                        df2 = df
                        if 'Class' in df2:
                            buttonReply = QMessageBox.question(None, 'Mean and STD',
                                                               "The column 'Class' already exists in the file.\n"
                                                               "Press Yes if you want to edit the Class.\n"
                                                               "Press No to ignore.\n",
                                                               QMessageBox.Yes | QMessageBox.No,
                                                               QMessageBox.Yes)
                            if buttonReply == QMessageBox.Yes:
                                if (self.comboBox_addclass.currentText() == "Add class"):
                                    QMessageBox.information(None, "Error ",
                                                            "Please enter a class number from the combobox.\nTry again.",
                                                            QMessageBox.Ok)
                                else:
                                    cl_nb = self.ll
                                    df2['c'] = df2['Well'].apply(lambda x: any([k in x for k in list_columnselected]))
                                    if df2['c'].any() == True:
                                        dfff1 = df2[df2['c'] == True]
                                        dfff2 = df2[df2['c'] == False]
                                        dfff1['Class'] = cl_nb
                                        dff_conc1 = pd.concat([dfff1, dfff2])
                                        d_dropped1 = dff_conc1.drop('c', axis=1)
                                        d_dropped1.to_csv(t1 + '\\' + file_name1 + '.csv', index=None)
                                        self.lineEdit_filepathfromdataframe.setText(t1 + '\\' + file_name1 + '.csv')
                                    self.on_reloadFile_clicked(t1 + '\\' + file_name1 + '.csv')
                                    d_dropped1 = pd.read_csv(t1 + '\\' + file_name1 + '.csv')
                                    list_descriptors = d_dropped1.columns
                                    self.comboBox_featuresfromdataframe.addItems(list_descriptors)

            else:
                QMessageBox.information(None, "Error",
                                        "File does not exist anymore.\nPlesse load a file.",
                                        QMessageBox.Ok)

    def load_dict(self, plate, desc):
        df_plate = self.df[self.df["Plate"] == plate]
        if 'Well' not in df_plate:
            print('no')
        if 'Well' in df_plate:
            keys = df_plate["Well"]
            values = df_plate[desc]
            dict_well = dict(zip(keys, values))
            return dict_well

    def on_reloadFile_clicked(self, file):
        self.tableWidget_toaddclasses.clearContents()
        self.comboBox_plates.clear()
        self.lineEdit_filepathfromdataframe.setText(file)
        df = pd.read_csv(file, low_memory=False)
        if 'Well' not in df:
            self.lineEdit_filepathfromdataframe.setText('')
            QMessageBox.information(None, "Error ",
                                    "The column Well is not in the file.\nTry again.",
                                    QMessageBox.Ok)
        if 'Well' in df:
            df_rows = df.count()
            cols = 24
            rows = 16
            l = list(string.ascii_uppercase)
            number_of_rows = self.tableWidget_toaddclasses.rowCount()
            number_of_columns = self.tableWidget_toaddclasses.columnCount()
            list_descriptors = df.columns
            list_plates = list(df['Plate'].drop_duplicates(keep="first"))
            nbr_rows = len(df)
            self.comboBox_plates.addItems((list_plates))
            self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
            self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
            self.df = df

    def on_loadFile_clicked(self):
        self.tableWidget_toaddclasses.clearContents()
        self.comboBox_plates.clear()
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepathfromdataframe.setText(fileName)
            df = pd.read_csv(fileName, low_memory=False)
            if 'Well' not in df:
                self.lineEdit_filepathfromdataframe.setText('')
                QMessageBox.information(None, "Error ",
                                        "The column Well is not in the file.\nTry again.",
                                        QMessageBox.Ok)
            if 'Well' in df:
                df_rows = df.count()
                cols = 24
                rows = 16
                l = list(string.ascii_uppercase)
                number_of_rows = self.tableWidget_toaddclasses.rowCount()
                number_of_columns = self.tableWidget_toaddclasses.columnCount()
                list_descriptors = df.columns
                if 'Plate' in df.columns:
                    list_plates = list(df['Plate'].drop_duplicates(keep="first"))
                    nbr_rows = len(df)
                    self.comboBox_plates.addItems((list_plates))
                    self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
                    self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
                    self.comboBox_featuresfromdataframe.addItem('Descriptor', 'ss')
                    self.comboBox_featuresfromdataframe.addItems(list_descriptors)
                    self.descriptors_df = list_descriptors
                    self.df = df

    def loadFile(self):
        fileName = self.lineEdit_filepathfromdataframe.text()
        if fileName == 'File path':
            QMessageBox.information(None, "Error ",
                                    "Please load a file first.",
                                    QMessageBox.Ok)
        if fileName != 'File path':
            df = pd.read_csv(fileName, low_memory=False)
            if 'Well' not in df:
                self.lineEdit_filepathfromdataframe.setText('')
                QMessageBox.information(None, "Error ",
                                        "The column Well is not in the file.\nTry again.",
                                        QMessageBox.Ok)
            if 'Well' in df:
                df_rows = df.count()
                cols = 24
                rows = 16
                l = list(string.ascii_uppercase)
                number_of_rows = self.tableWidget_toaddclasses.rowCount()
                number_of_columns = self.tableWidget_toaddclasses.columnCount()
                list_descriptors = df.columns
                if 'Plate' in df.columns:
                    list_plates = list(df['Plate'].drop_duplicates(keep="first"))
                    nbr_rows = len(df)
                    self.comboBox_plates.addItems((list_plates))
                    self.lineEdit_nbrofplates.setText(str(len(list_plates)) + ' plates')
                    self.lineEdit_nbrofwells.setText(str(nbr_rows) + ' wells')
                    self.comboBox_featuresfromdataframe.addItem('Descriptor', 'ss')
                    self.comboBox_featuresfromdataframe.addItems(list_descriptors)
                    self.df = df

    def on_comboBoxplates_changed(self):
        self.tableWidget_toaddclasses.clearContents()
        self.comboBox_featuresfromdataframe.setCurrentIndex(0)

    def on_comboBox_featuresfromdataframe_changed(self):
        self.fill_tablewidget()

    def fill_tablewidget(self):
        cols = 24
        rows = 16
        ll1 = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])
        ll2 = list(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24'])
        plate_cb = self.comboBox_plates.currentText()
        desc_cb = self.comboBox_featuresfromdataframe.currentText()
        if desc_cb != 'Descriptor':
            dict_table_well = self.load_dict(plate_cb, desc_cb)
            for row, i in enumerate(range(len(ll1))):
                for col, j in enumerate(range(len(ll2))):
                    well_from_list = str(ll1[row]) + str(ll2[col])
                    value = 0
                    if well_from_list in dict_table_well.keys():
                        value = dict_table_well[well_from_list]
                        item = QTableWidgetItem(str(value))
                        self.tableWidget_toaddclasses.setItem(row, col, item)

    # def on_class_clicked(self):
    #         cols = 24
    #         rows = 16
    #         ll1 = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])
    #         ll2 = list(
    #             ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    #             '19', '20', '21', '22', '23', '24'])
    #         plate_cb = self.comboBox_plates.currentText()
    #         min_value, max_value, list_ = self.getminmax()
    #         desc_cb = self.comboBox_featuresfromdataframe.currentText()
    #         if desc_cb != 'Descriptor':
    #             dict_table_well = self.load_dict(plate_cb, desc_cb)
    #             for row, i in enumerate(range(len(ll1))):
    #                 for col, j in enumerate(range(len(ll2))):
    #                     well_from_list = str(ll1[row]) + str(ll2[col])
    #                     if well_from_list in dict_table_well.keys():
    #                         value = dict_table_well[well_from_list]
    #                         item = QTableWidgetItem(str(value))
    #                         self.tableWidget_toaddclasses.setItem(row, col, item)
    #                         color_value = self.get_color_colormap(min_value, max_value, value)
    #                         if color_value < 255 / 10:
    #                             self.tableWidget_toaddclasses.item(row, col).setBackground(QtGui.QColor(int(0), int(0), int(color_value)*10))
    #                         if (color_value > 255 / 10) and (color_value < 255 / 3):
    #                             self.tableWidget_toaddclasses.item(row, col).setBackground(QtGui.QColor(int(0), int(color_value)*3, int(0)))
    #                         if color_value > 255 / 3:
    #                             self.tableWidget_toaddclasses.item(row, col).setBackground(QtGui.QColor(int(color_value), int(0), int(0)))

    # def fill_tablewidget(self):
    #     cols = 24
    #     rows = 16
    #     l = list(string.ascii_uppercase)
    #     for k in range(len(l)):
    #         for i in range(rows):
    #             for j in range(cols):
    #                 if j + 1 <= 9:
    #                     self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + '0' + str(j + 1)))
    #                 print(k)
    #                 if j + 1 >= 10:
    #                     self.tableWidget_toaddclasses.setItem(i + k, j, QTableWidgetItem(l[k] + str(j + 1)))
    #                 print(k)
    #             i += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_table_addclasses = QtWidgets.QWidget()
    ui = Ui_form_table_addclasses()
    ui.setupUi(form_table_addclasses)
    form_table_addclasses.show()
    sys.exit(app.exec_())

