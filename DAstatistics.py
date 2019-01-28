import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PyQt5.QtWidgets import *
import pandas as pd

from DApandaswidget import PandasModel
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_loaddataframe.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_loadDataframe(object):
    def setupUi(self, Form_loadDataframe):
        Form_loadDataframe.setObjectName("Form_loadDataframe")
        Form_loadDataframe.setEnabled(True)
        Form_loadDataframe.resize(1455, 876)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_loadDataframe.sizePolicy().hasHeightForWidth())
        Form_loadDataframe.setSizePolicy(sizePolicy)
        Form_loadDataframe.setSizeIncrement(QtCore.QSize(25, 25))
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(650, 60, 61, 21))
        self.pushButton_loadfile.setMouseTracking(False)
        self.pushButton_loadfile.setAutoFillBackground(False)
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.lineEdit_filepath = QtWidgets.QLineEdit(Form_loadDataframe)
        self.lineEdit_filepath.setGeometry(QtCore.QRect(10, 60, 631, 21))
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.comboBox_plot = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_plot.setGeometry(QtCore.QRect(1010, 120, 151, 22))
        self.comboBox_plot.setObjectName("comboBox_plot")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.pushButton_concatfiles = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_concatfiles.setGeometry(QtCore.QRect(720, 60, 101, 21))
        self.pushButton_concatfiles.setObjectName("pushButton_concatfiles")
        self.lineEdit_plate = QtWidgets.QLabel(Form_loadDataframe)
        self.lineEdit_plate.setGeometry(QtCore.QRect(20, 110, 91, 16))
        self.lineEdit_plate.setText("")
        self.lineEdit_plate.setObjectName("lineEdit_plate")
        self.lineEdit_well = QtWidgets.QLabel(Form_loadDataframe)
        self.lineEdit_well.setGeometry(QtCore.QRect(150, 110, 81, 16))
        self.lineEdit_well.setText("")
        self.lineEdit_well.setObjectName("lineEdit_well")
        self.tableView_dataframe = QtWidgets.QTableView(Form_loadDataframe)
        self.tableView_dataframe.setGeometry(QtCore.QRect(10, 190, 1431, 671))
        self.tableView_dataframe.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_dataframe.setDragEnabled(True)
        self.tableView_dataframe.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableView_dataframe.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_dataframe.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_dataframe.setSortingEnabled(True)
        self.tableView_dataframe.setObjectName("tableView_dataframe")
        self.comboBox_duplicates = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_duplicates.setGeometry(QtCore.QRect(1170, 90, 131, 22))
        self.comboBox_duplicates.setObjectName("comboBox_duplicates")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_dropfrom = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_dropfrom.setGeometry(QtCore.QRect(1010, 90, 151, 22))
        self.comboBox_dropfrom.setObjectName("comboBox_dropfrom")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_addcolumn = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_addcolumn.setGeometry(QtCore.QRect(1010, 60, 151, 22))
        self.comboBox_addcolumn.setObjectName("comboBox_addcolumn")
        self.comboBox_addcolumn.addItem("")
        self.comboBox_addcolumn.addItem("")
        self.comboBox_linkfileby = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_linkfileby.setGeometry(QtCore.QRect(1310, 90, 131, 22))
        self.comboBox_linkfileby.setObjectName("comboBox_linkfileby")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_machinelearning = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_machinelearning.setGeometry(QtCore.QRect(1310, 150, 131, 22))
        self.comboBox_machinelearning.setObjectName("comboBox_machinelearning")
        self.comboBox_machinelearning.addItem("")
        self.comboBox_machinelearning.addItem("")
        self.comboBox_normalize = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_normalize.setGeometry(QtCore.QRect(1170, 120, 131, 22))
        self.comboBox_normalize.setObjectName("comboBox_normalize")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_removeoutliers = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_removeoutliers.setGeometry(QtCore.QRect(1170, 60, 271, 22))
        self.comboBox_removeoutliers.setObjectName("comboBox_removeoutliers")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_extracthits = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_extracthits.setGeometry(QtCore.QRect(1310, 120, 131, 22))
        self.comboBox_extracthits.setObjectName("comboBox_extracthits")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_statistics = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_statistics.setGeometry(QtCore.QRect(1010, 150, 151, 22))
        self.comboBox_statistics.setObjectName("comboBox_statistics")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.pushButton_addclasses = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_addclasses.setGeometry(QtCore.QRect(830, 60, 80, 21))
        self.pushButton_addclasses.setObjectName("pushButton_addclasses")
        self.comboBox_aggregate = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_aggregate.setGeometry(QtCore.QRect(1170, 150, 131, 22))
        self.comboBox_aggregate.setObjectName("comboBox_aggregate")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.label_nbcpdid = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbcpdid.setGeometry(QtCore.QRect(250, 110, 101, 16))
        self.label_nbcpdid.setText("")
        self.label_nbcpdid.setObjectName("label_nbcpdid")
        self.label_nbbatchid = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbbatchid.setGeometry(QtCore.QRect(360, 110, 111, 16))
        self.label_nbbatchid.setText("")
        self.label_nbbatchid.setObjectName("label_nbbatchid")
        self.label_nbrrows = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbrrows.setGeometry(QtCore.QRect(490, 110, 101, 16))
        self.label_nbrrows.setText("")
        self.label_nbrrows.setObjectName("label_nbrrows")
        self.lineEdit_filepath.setText('File path')
        self.pushButton_loadfile.clicked.connect(self.on_loadFile_clicked)
        self.pushButton_addclasses.clicked.connect(self.on_addclasses_clicked)
        self.pushButton_concatfiles.clicked.connect(self.on_concatenatefiles_clicked)
        # self.pushButton_addclasses.clicked.connect(self.on_addclasses_clicked)
        self.comboBox_duplicates.currentTextChanged.connect(self.on_comboboxduplicates_changed)
        self.comboBox_dropfrom.currentTextChanged.connect(self.on_comboboxdropfrom_changed)
        self.comboBox_addcolumn.currentTextChanged.connect(self.on_comboboxaddcolumn_changed)
        self.comboBox_linkfileby.currentTextChanged.connect(self.on_linkfileby_changed)
        self.comboBox_extracthits.currentTextChanged.connect(self.on_comboboxactivecompounds_changed)
        self.comboBox_removeoutliers.currentTextChanged.connect(self.on_comboboxremoveoutliers_changed)
        self.comboBox_machinelearning.currentTextChanged.connect(self.on_machinelearning_changed)
        self.comboBox_statistics.currentTextChanged.connect(self.on_statistics_changed)
        self.comboBox_normalize.currentTextChanged.connect(self.on_normalize_changed)
        self.comboBox_plot.currentTextChanged.connect(self.on_plot_changed)
        self.comboBox_aggregate.currentTextChanged.connect(self.on_comboboxaggregate_changed)

        self.retranslateUi(Form_loadDataframe)
        QtCore.QMetaObject.connectSlotsByName(Form_loadDataframe)

    def retranslateUi(self, Form_loadDataframe):
        _translate = QtCore.QCoreApplication.translate
        Form_loadDataframe.setWindowTitle(_translate("Form_loadDataframe", "Form"))
        self.pushButton_loadfile.setText(_translate("Form_loadDataframe", "Load File"))
        self.comboBox_plot.setItemText(0, _translate("Form_loadDataframe", "Plot"))
        self.comboBox_plot.setItemText(1, _translate("Form_loadDataframe", "Correlation"))
        self.comboBox_plot.setItemText(2, _translate("Form_loadDataframe", "Swarm plot with error bar"))
        self.comboBox_plot.setItemText(3, _translate("Form_loadDataframe", "Swarm plot without error bar"))
        self.comboBox_plot.setItemText(4, _translate("Form_loadDataframe", "Error bar"))
        self.pushButton_concatfiles.setText(_translate("Form_loadDataframe", "Concatenate Files"))
        self.comboBox_duplicates.setItemText(0, _translate("Form_loadDataframe", "Duplicates"))
        self.comboBox_duplicates.setItemText(1, _translate("Form_loadDataframe", "Get duplicated values"))
        self.comboBox_duplicates.setItemText(2, _translate("Form_loadDataframe", "Number of duplicates"))
        self.comboBox_duplicates.setItemText(3, _translate("Form_loadDataframe", "Drop duplicated values"))
        self.comboBox_dropfrom.setItemText(0, _translate("Form_loadDataframe", "Drop / Change"))
        self.comboBox_dropfrom.setItemText(1, _translate("Form_loadDataframe", "Drop from columns"))
        self.comboBox_dropfrom.setItemText(2, _translate("Form_loadDataframe", "Drop from rows"))
        self.comboBox_dropfrom.setItemText(3, _translate("Form_loadDataframe", "Rename value in rows"))
        self.comboBox_dropfrom.setItemText(4, _translate("Form_loadDataframe", "Extract value from rows"))
        self.comboBox_dropfrom.setItemText(5, _translate("Form_loadDataframe", "Rename columns"))
        self.comboBox_addcolumn.setItemText(0, _translate("Form_loadDataframe", "Add column"))
        self.comboBox_addcolumn.setItemText(1, _translate("Form_loadDataframe", "New column"))
        self.comboBox_linkfileby.setItemText(0, _translate("Form_loadDataframe", "Link file by"))
        self.comboBox_linkfileby.setItemText(1, _translate("Form_loadDataframe", "Well"))
        self.comboBox_linkfileby.setItemText(2, _translate("Form_loadDataframe", "Plate_Well"))
        self.comboBox_machinelearning.setItemText(0, _translate("Form_loadDataframe", "Machine learning"))
        self.comboBox_machinelearning.setItemText(1, _translate("Form_loadDataframe", "LDA"))
        self.comboBox_normalize.setItemText(0, _translate("Form_loadDataframe", "Normalise"))
        self.comboBox_normalize.setItemText(1, _translate("Form_loadDataframe", "Median"))
        self.comboBox_normalize.setItemText(2, _translate("Form_loadDataframe", "Mean"))
        self.comboBox_normalize.setItemText(3, _translate("Form_loadDataframe", "Min-Max"))
        self.comboBox_removeoutliers.setItemText(0, _translate("Form_loadDataframe", "Remove outliers"))
        self.comboBox_removeoutliers.setItemText(1, _translate("Form_loadDataframe",
                                                               "Mean-value*sigma <value< Mean+value*sigma"))
        self.comboBox_removeoutliers.setItemText(2, _translate("Form_loadDataframe", "> mean"))
        self.comboBox_removeoutliers.setItemText(3, _translate("Form_loadDataframe", "> value"))
        self.comboBox_extracthits.setItemText(0, _translate("Form_loadDataframe", "Detect compounds"))
        self.comboBox_extracthits.setItemText(1, _translate("Form_loadDataframe", "> mean + value * sigma"))
        self.comboBox_extracthits.setItemText(2, _translate("Form_loadDataframe", "> mean - value * sigma"))
        self.comboBox_extracthits.setItemText(3, _translate("Form_loadDataframe", "< mean - value * sigma"))
        self.comboBox_extracthits.setItemText(4, _translate("Form_loadDataframe", "> mean"))
        self.comboBox_extracthits.setItemText(5, _translate("Form_loadDataframe", "< mean"))
        self.comboBox_extracthits.setItemText(6, _translate("Form_loadDataframe", "> value"))
        self.comboBox_extracthits.setItemText(7, _translate("Form_loadDataframe", "< value"))
        self.comboBox_statistics.setItemText(0, _translate("Form_loadDataframe", "Statistics"))
        self.comboBox_statistics.setItemText(1, _translate("Form_loadDataframe", "Z factor & Robust Z factor"))
        self.comboBox_statistics.setItemText(2, _translate("Form_loadDataframe", "Mean and STD"))
        self.comboBox_statistics.setItemText(3, _translate("Form_loadDataframe", "Intersection"))
        self.comboBox_statistics.setItemText(4, _translate("Form_loadDataframe", "Union"))
        self.pushButton_addclasses.setText(_translate("Form_loadDataframe", "Add classes"))
        self.comboBox_aggregate.setItemText(0, _translate("Form_loadDataframe", "Aggregate"))
        self.comboBox_aggregate.setItemText(1, _translate("Form_loadDataframe", "Aggregate - Min Max Mean Sum STD"))
        self.comboBox_aggregate.setItemText(2, _translate("Form_loadDataframe", "Aggregated grouping by"))

    def on_normalize_changed(self, value_nor):
        if (value_nor == "Mean"):
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet..",
                                    QMessageBox.Ok)

        if (value_nor == "Median"):
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet.",
                                    QMessageBox.Ok)
        if (value_nor == "Min-Max"):
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet.",
                                    QMessageBox.Ok)

    def on_statistics_changed(self, value_st):
        file = self.lineEdit_filepath.text()
        if value_st == "Mean and STD":
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                columnname = self.select_column()
                df = pd.read_csv(file)
                df['Check_if_String'] = [isinstance(x, str) for x in df[columnname]]
                if df['Check_if_String'].any() == True:
                    QMessageBox.information(None, "Error",
                                            "The column " + columnname + " selected contains string.\nPlease select another column.",
                                            QMessageBox.Ok)

                if df['Check_if_String'].any() == False:
                    if df[columnname].isna().any() == True or  df[columnname].isnull().any() == True:
                        print('1')
                        buttonReply = QMessageBox.question(None, 'Mean and STD',
                                        "The column " + columnname + " selected contains nan or inf values.\n"
                                                                     "Press Yes if you want to ignore the inf and nan values.\n"
                                                                     "Press No to select another column.\n",
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
                        if buttonReply == QMessageBox.Yes:
                            mean_df = df[columnname].mean()
                            std_df = df[columnname].std()
                            QMessageBox.information(None, "Mean and STD ",
                                                    "Mean = " + " " + str(mean_df) + " \n" + "STD = " + str(std_df),
                                                    QMessageBox.Ok)

                        if buttonReply == QMessageBox.No:
                            print('no pressed')
                    if df[columnname].isna().any() == False:
                        mean_df = df[columnname].mean()
                        std_df = df[columnname].std()
                        QMessageBox.information(None, "Mean and STD ",
                                                "Mean = " + " " + str(mean_df) + " \n" + "STD = " + str(std_df),
                                                QMessageBox.Ok)

        self.comboBox_statistics.setCurrentText("Statistics")

        if value_st == "Z factor & Robust Z factor":
            QMessageBox.information(None, "Not imp ",
                                    "Not implemented yet..",
                                    QMessageBox.Ok)

        if value_st == "Intersection":
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file:
                fileName1 = file
                file1 = pd.read_csv(fileName1)
                header = self.select_column()
                fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to get the intersection",
                                                           "",
                                                           "CSV Files (*.csv)")
                if fileName2:
                    file2 = pd.read_csv(fileName2)
                    inter = file2[file2[header].isin(file1[header])]
                    if len(inter) == 0:
                        QMessageBox.information(None, "Error ",
                                                "No intersecton between the 2 files.\nNo file to save.",
                                                QMessageBox.Ok)
                    if len(inter) > 0:
                        QMessageBox.information(None, "Intersection",
                                                "The number of intersected data = " + str(len(inter)) + "\nSaved file.",
                                                QMessageBox.Ok)
                        t1 = fileName1.split('/')[2]
                        t2 = fileName1.split('/')[0]
                        t3 = fileName1.split('/')[1]
                        outfile = t2 + '\\' + t3 + '\\' + t1 + '\\' + t1 + '_intersection.csv'
                        inter.to_csv(outfile, index=None)
                        self.lineEdit_filepath.setText(t2 + '//' + t3 + '//' + t1 + '//' + t1 + '_intersection.csv')
                        self.setPlateWellText_intblview(inter)
                        self.reloaddata_fromfilepath(outfile)
            self.comboBox_statistics.setCurrentText("Statistics")

        if value_st == "Union":
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file:
                fileName1 = file
                file1 = pd.read_csv(fileName1)
                header = self.select_column()
                fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to get the union",
                                                           "",
                                                           "CSV Files (*.csv)")
                if fileName2:
                    file2 = pd.read_csv(fileName2)
                    union = pd.concat([file1, file2], ignore_index=True).drop_duplicates().reset_index(drop=True)
                    print(union)
                    union.to_csv('D:\\RESULTS\\vl1vl2\\out.csv', index=None)
                    if len(union) == 0:
                        QMessageBox.information(None, "Error ",
                                                "No union between the 2 files.\nNo file to save.",
                                                QMessageBox.Ok)
                    if len(union) > 0:
                        QMessageBox.information(None, "Union",
                                                "The number of union data = " + str(len(union)) + "\nSaved file.",
                                                QMessageBox.Ok)
                        t1 = fileName1.split('/')[2]
                        t2 = fileName1.split('/')[0]
                        t3 = fileName1.split('/')[1]
                        outfile = t2 + '\\' + t3 + '\\' + t1 + '\\' + t1 + '_union.csv'
                        union.to_csv(outfile, index=None)
                        self.lineEdit_filepath.setText(t2 + '//' + t3 + '//' + t1 + '//' + t1 + '_union.csv')
                        self.setPlateWellText_intblview(union)
                        self.reloaddata_fromfilepath(outfile)
            self.comboBox_statistics.setCurrentText("Statistics")

    def on_machinelearning_changed(self, value_ch):
        file = self.lineEdit_filepath.text()
        if value_ch == "LDA":
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet..",
                                    QMessageBox.Ok)

    def on_comboboxactivecompounds_changed(self, value_c):
        file = self.lineEdit_filepath.text()
        if (value_c == "> mean + value * sigma"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Active_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Active_compounds':
                    value_sigma1, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                    stdval = df_toremoveout[columnname].std()
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Active_compounds'] = 'notactive'
                    df_toremoveout['Active_compounds'][
                        (df_toremoveout[columnname] >= meanval + value_sigma1 * stdval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('notactive'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No active compound",
                                                "You have no active compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        out_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if out_dir:
                            t1 = out_dir.split('/')[2]
                            outfile = out_dir + '//' + t1 + '_Active_compounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column " + str(
                                                        columnname) + " when value > " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(out_dir + '/' + 'Active_compounds.csv')
                            self.reloaddata_fromfilepath(outfile)
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> mean - value * sigma"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Active_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'NonToxic_Compounds':
                    value_sigma1, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                    stdval = df_toremoveout[columnname].std()
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['NonToxic_Compounds'] = 'toxic'
                    df_toremoveout['NonToxic_Compounds'][
                        (df_toremoveout[columnname] >= meanval + value_sigma1 * stdval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['NonToxic_Compounds'].str.contains('toxic'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "Non toxic compounds",
                                                "You have no toxic compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        out_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if out_dir:
                            t1 = out_dir.split('/')[2]
                            outfile = out_dir + '//' + t1 + 'toxiccompounds.csv'
                            data_dropped.to_csv(outfile, index=None)

                            QMessageBox.information(None, "Toxic coumpounds",
                                                    str(len(data_dropped)) +
                                                    " toxic compounds were detected using the column " + str(
                                                        columnname) + " when value > " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(out_dir + '/' + t1 + 'toxiccompounds.csv')
                            self.reloaddata_fromfilepath(outfile)
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "< mean - value * sigma"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                print('dodo')
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Toxic_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Toxic_compounds':
                    print('ogjdk')
                    value_sigma1, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                    stdval = df_toremoveout[columnname].std()
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Toxic_compounds'] = 'not toxic'
                    df_toremoveout['Toxic_compounds'][(df_toremoveout[columnname] <= meanval - value_sigma1 * stdval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Toxic_compounds'].str.contains('not toxic'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No toxic compound",
                                                "You have no toxic compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        out_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if out_dir:
                            t1 = out_dir.split('/')[2]
                            outfile = out_dir + '//' + t1 + '_Toxic_compounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Toxic coumpounds",
                                                    str(len(data_dropped)) +
                                                    " toxic compounds were detected using the column " + str(
                                                        columnname) + " when value < " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(out_dir + '/' + 'Toxic_compounds.csv')
                            self.reloaddata_fromfilepath(outfile)

            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> mean"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Outliers':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect compounds\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Active_compounds':
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Active_compounds'] = 'notactivecpd'
                    df_toremoveout['Active_compounds'][(df_toremoveout[columnname] > meanval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    print(len(df_toremoveout))
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('notactivecpd'))].index)
                    if len(df_toremoveout) < 1 :
                        QMessageBox.information(None, "No active compound",
                                                "You have no active compound"
                                                + " \nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) >= 1:
                        print('oldodj')
                        out_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        t1 = out_dir.split('/')[2]
                        if out_dir:
                            outfile = out_dir + '//' + t1 + '_activecompounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Active compounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds based on the column " + str(
                                                        columnname)+ 'when value > ' + str() + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                out_dir + '/' + t1 + '_activecompounds.csv')

                            self.reloaddata_fromfilepath(
                                out_dir + '/' + t1 + '_activecompounds.csv')

            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "< mean"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Active_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Active_compounds':
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Active_compounds'] = 'notactive'
                    df_toremoveout['Active_compounds'][(df_toremoveout[columnname] < meanval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('notactive'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No active compound",
                                                "You have no active compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        my_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if my_dir:
                            outfile = my_dir + '//' + 'Active_compounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column " + str(
                                                        columnname) + " when mean < " + str(meanval)
                                                    + "\nSuccessfully saved the file",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(my_dir + '/' + 'Active_compounds.csv')
                            self.reloaddata_fromfilepath(outfile)

        self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> value"):
            print('value')
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Active_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)

                if columnname != 'Active_compounds':
                    value_v, ok = QInputDialog.getDouble(None, "Input", "Value:")
                    df_toremoveout['Active_compounds'] = 'notactive'
                    df_toremoveout['Active_compounds'][(df_toremoveout[columnname] >= value_v)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('notactive'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No active compound",
                                                "You have no active compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        my_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if my_dir:
                            outfile = my_dir + '//' + 'Active_compounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            self.lineEdit_filepath.setText(my_dir + '/' + 'Active_compounds.csv')
                            self.reloaddata_fromfilepath(outfile)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column " + str(
                                                        columnname) + " when value < " + str(value_v)
                                                    + "\nSuccessfully saved the file",
                                                    QMessageBox.Ok)

            self.comboBox_statistics.setCurrentText("Detect compounds")

        if (value_c == "< value"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Active_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Active_compounds':
                    value_v, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                    stdval = df_toremoveout[columnname].std()
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Active_compounds'] = 'not active'
                    df_toremoveout['Active_compounds'][(df_toremoveout[columnname] <= value_v)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('not active'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No active compound",
                                                "You have no active compound"
                                                + "\nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        my_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if my_dir:
                            outfile = my_dir + '//' + 'Active_compounds.csv'
                            data_dropped.to_csv(outfile, index=None)
                            self.lineEdit_filepath.setText(my_dir + '/' + 'Active_compounds.csv')
                            self.reloaddata_fromfilepath(outfile)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column " + str(
                                                        columnname) + " at " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file",
                                                    QMessageBox.Ok)

            self.comboBox_statistics.setCurrentText("Detect compounds")

    def on_comboboxremoveoutliers_changed(self, value_cb):
        file = self.lineEdit_filepath.text()
        if (value_cb == "Mean-value*sigma <value< Mean+value*sigma"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Outliers':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to remove the outliers\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Outliers':
                    value_sigma1, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                    if value_sigma1:
                        stdval = df_toremoveout[columnname].std()
                        meanval = df_toremoveout[columnname].mean()
                        df_toremoveout['Outliers'] = 'outlier'
                        df_toremoveout['Outliers'][(df_toremoveout[columnname] >= meanval + value_sigma1 * stdval) |
                                                   (df_toremoveout[columnname] <= meanval - value_sigma1 * stdval)] = \
                            df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                        data_dropped = df_toremoveout.drop(
                            df_toremoveout[(df_toremoveout['Outliers'].str.contains('outlier'))].index)
                        if len(data_dropped) < 1:
                            QMessageBox.information(None, "No Outliers",
                                                    "You have no outliers"
                                                    + " \nNo file to save",
                                                    QMessageBox.Ok)
                        if len(data_dropped) >=1:
                            out_dir = QFileDialog.getExistingDirectory(
                                None,
                                "Select output folder",
                                "",
                                QFileDialog.ShowDirsOnly)
                            t1 = out_dir.split('/')[2]
                            if out_dir:
                                outfile = out_dir + '//' + t1 + '_WithoutOutliers_' + str(value_sigma1) + 'sigma.csv'
                                data_dropped.to_csv(outfile, index=None)
                                self.lineEdit_filepath.setText(
                                    out_dir + '/' + t1 + '_WithoutOutliers_' + str(value_sigma1) + 'sigma.csv')
                                QMessageBox.information(None, "Outliers",
                                                        str(len(df_toremoveout) - len(data_dropped)) +
                                                        " outliers have been removed using the column " + str(
                                                            columnname) + '.\n'
                                                        + "Successfully saved the file!",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromfilepath(out_dir + '/' + t1 + '_WithoutOutliers_' + str(value_sigma1) + 'sigma.csv')
            self.comboBox_removeoutliers.setCurrentText("Remove outliers")

        if (value_cb == "> mean"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Outliers':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to remove the outliers\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Outliers':
                    meanval = df_toremoveout[columnname].mean()
                    df_toremoveout['Outliers'] = 'outlier'
                    df_toremoveout['Outliers'][(df_toremoveout[columnname] > meanval)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Outliers'].str.contains('outlier'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No Outliers",
                                                "You have no outliers"
                                                + " \nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        out_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        t1 = out_dir.split('/')[2]
                        if out_dir:
                            outfile = out_dir + '//' + t1 + '_WithoutOutliers.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Outliers",
                                                    str(len(df_toremoveout) - len(data_dropped)) +
                                                    " outliers have been removed using the column " + str(
                                                        columnname) + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                out_dir + '/' + t1 + '_WithoutOutliers.csv')
                            self.reloaddata_fromfilepath(
                                out_dir + '/' + t1 + '_WithoutOutliers.csv')

            self.comboBox_removeoutliers.setCurrentText("Remove outliers")

        if (value_cb == "> value"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Outliers':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to remove the outliers\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Outliers':
                    value_out, ok = QInputDialog.getDouble(None, "Input", "Value:")
                    df_toremoveout['Outliers'] = 'outlier'
                    df_toremoveout['Outliers'][(df_toremoveout[columnname] >= value_out)] = \
                        df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                    data_dropped = df_toremoveout.drop(
                        df_toremoveout[(df_toremoveout['Outliers'].str.contains('outlier'))].index)
                    if len(data_dropped) <= 1:
                        QMessageBox.information(None, "No Outliers",
                                                "You have no outliers"
                                                + " \nNo file to save",
                                                QMessageBox.Ok)
                    if len(data_dropped) > 2:
                        my_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select output folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if my_dir:
                            outfile = my_dir + '//' + 'WithoutOutliers_gt_' + str(value_out) + '.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Outliers",
                                                    str(len(df_toremoveout) - len(data_dropped)) +
                                                    " outliers have been rejected using the column " + str(
                                                        columnname) + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                my_dir + '/' + 'WithoutOutliers_gt_' + str(value_out) + '.csv')
                            self.reloaddata_fromfilepath(
                                my_dir + '/' + 'WithoutOutliers_gt_' + str(value_out) + '.csv')
            self.comboBox_removeoutliers.setCurrentText("Remove outliers")

    def select_multicolumns(self):
        list_col = []
        totalColumns = self.tableView_dataframe.selectionModel().selectedColumns()
        for idx in totalColumns:
            column_name = self.tableView_dataframe.model().headerData(idx.column(), QtCore.Qt.Horizontal,
                                                                      QtCore.Qt.DisplayRole)
            list_col.append(column_name)
        return list_col

    def select_column(self):
        col_nb = self.tableView_dataframe.currentIndex().column()
        column_name = self.tableView_dataframe.model().headerData(col_nb, QtCore.Qt.Horizontal,
                                                                  QtCore.Qt.DisplayRole)
        return column_name

    def reloaddata_fromdir(self, dir):
        self.lineEdit_filepath.setText('reloaded data')
        list_files = []
        for root, dirs, files in os.walk(dir):
            for file_read in files:
                df = pd.read_csv(root + '\\' + file_read)
                list_files.append(df)
                b = pd.DataFrame(pd.concat(list_files, axis=1))
                model = PandasModel(b.head(100))
                self.tableView_dataframe.setModel(model)
                if ('Plate' in b.columns and 'Well' in b.columns):
                    self.lineEdit_plate.setText(str(b['Plate'].nunique()) + ' plates')
                    self.lineEdit_well.setText(str(len(b['Well'])) + ' wells')
                    self.getncpdsbatches(b)

                if ('Plate' not in b.columns and 'Well' not in b.columns):
                    self.lineEdit_plate.setText('No plate')
                    self.lineEdit_well.setText('No wells')
                    self.getncpdsbatches(b)

                if ('Plate' not in b.columns and 'Well' in b.columns):
                    self.lineEdit_plate.setText('No plate')
                    self.lineEdit_well.setText(str(len(b['Well'])) + ' wells')
                    self.getncpdsbatches(b)

                if ('Plate' in b.columns and 'Well' not in b.columns):
                    self.lineEdit_plate.setText(str(b['Plate'].nunique()) + ' plates')
                    self.lineEdit_well.setText('No wells')
                    self.getncpdsbatches(b)

    def reloaddata_fromDF(self, df):
        if self.lineEdit_filepath.setText('reloaded data'):
            model = PandasModel(df.head(100))
            self.tableView_dataframe.setModel(model)
        if not self.lineEdit_filepath.setText('reloaded data'):
            model = PandasModel(df.head(100))
            self.tableView_dataframe.setModel(model)
            if ('Plate' in df.columns and 'Well' in df.columns):
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)

            if ('Plate' not in df.columns and 'Well' not in df.columns):
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText('No wells')
                self.getncpdsbatches(df)

            if ('Plate' not in df.columns and 'Well' in df.columns):
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)

            if ('Plate' in df.columns and 'Well' not in df.columns):
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText('No wells')
                self.getncpdsbatches(df)

    def setPlateWellText_intblview(self, df):
        self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' unique plate')
        self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_dataframe.setModel(model)
        if ('Plate' in df.columns and 'Well' in df.columns):
            self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
            self.getncpdsbatches(df)

        if ('Plate' not in df.columns and 'Well' not in df.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df)

        if ('Plate' not in df.columns and 'Well' in df.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
            self.getncpdsbatches(df)

        if ('Plate' in df.columns and 'Well' not in df.columns):
            self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df)

    def reloaddata_fromdataframe(self, df1, head_nb):
        model = PandasModel(df1.head(head_nb))
        self.tableView_dataframe.setModel(model)
        if ('Plate' in df1.columns and 'Well' in df1.columns):
            self.lineEdit_plate.setText(str(df1['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText(str(len(df1['Well'])) + ' wells')
            self.getncpdsbatches(df1)

        if ('Plate' not in df1.columns and 'Well' not in df1.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df1)

        if ('Plate' not in df1.columns and 'Well' in df1.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df1['Well'])) + ' wells')
            self.getncpdsbatches(df1)

        if ('Plate' in df1.columns and 'Well' not in df1.columns):
            self.lineEdit_plate.setText(str(df1['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df1)

    def on_plot_changed(self, vl):
        if (vl == 'Correlation'):
            file = self.lineEdit_filepath.text()

        if (vl == 'Swarm plot with error bar'):
            file = self.lineEdit_filepath.text()
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                header = self.select_multicolumns()
                df_1 = pd.read_csv(file)

                if len(header) < 2:
                    QMessageBox.information(None, "Error",
                                            "Please select at least 3 columns to plot.",
                                            QMessageBox.Ok)
                if len(header) > 5:
                    QMessageBox.information(None, "Error",
                                            "Please select at least 3 columns or 5 columns to plot.",
                                            QMessageBox.Ok)
                if len(header) == 5:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    header_yaxis2 = header[2]
                    header_yaxis3 = header[3]
                    header_yaxis4 = header[4]
                    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(5, 5), sharey=False, constrained_layout=True)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.5, ci='sd', ax=axs[0, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange',
                                  ax=axs[0, 0])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, capsize=.5, ci='sd', ax=axs[0, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, size=3, color='orange',
                                  ax=axs[0, 1])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, capsize=.5, ci='sd', ax=axs[1, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, size=3, color='orange',
                                  ax=axs[1, 0])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, capsize=.5, ci='sd', ax=axs[1, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, size=3, color='orange',
                                  ax=axs[1, 1])
                    plt.show()

                if len(header) == 2:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.5, ci='sd')
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange')
                    plt.xticks(rotation=0, size=10)
                    plt.show()
            self.comboBox_plot.setCurrentText("Plot")

        if (vl == 'Swarm plot without error bar'):
            file = self.lineEdit_filepath.text()
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                header = self.select_multicolumns()
                df_1 = pd.read_csv(file)

                if len(header) < 2:
                    QMessageBox.information(None, "Error",
                                            "Please select at least 3 columns to plot.",
                                            QMessageBox.Ok)
                if len(header) > 5:
                    QMessageBox.information(None, "Error",
                                            "Please select at least 3 columns or 5 columns to plot.",
                                            QMessageBox.Ok)
                if len(header) == 5:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    header_yaxis2 = header[2]
                    header_yaxis3 = header[3]
                    header_yaxis4 = header[4]
                    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(5, 5), sharey=False, constrained_layout=True)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.0, ci=False, ax=axs[0, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange',
                                  ax=axs[0, 0])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, capsize=.0, ci=False, ax=axs[0, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, size=3, color='orange',
                                  ax=axs[0, 1])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, capsize=.0, ci=False, ax=axs[1, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, size=3, color='orange',
                                  ax=axs[1, 0])
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, capsize=.0, ci=False, ax=axs[1, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, size=3, color='orange',
                                  ax=axs[1, 1])
                    plt.xticks(rotation=0, size=10)
                    plt.show()

                if len(header) == 2:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.5, ci='sd')
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange')
                    plt.xticks(rotation=0, size=10)
                    plt.show()
            self.comboBox_plot.setCurrentText("Plot")

    def on_comboboxaggregate_changed(self, value_agg):
        if (value_agg == 'Aggregated grouping by'):
            QMessageBox.information(None, "No imp",
                                    "Not implemented yet",
                                    QMessageBox.Ok)
        if (value_agg == 'Aggregate - Min Max Mean Sum STD'):
            file = self.lineEdit_filepath.text()
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file)
                header = self.select_column()
                if 'Class' in df.columns:
                    if (len(header) < 1):
                        QMessageBox.information(None, "Error ",
                                                "You must select a column No file to save \nTry again",
                                                QMessageBox.Ok)
                    if len(header) >= 1:
                        t1 = file.split('/')[2]
                        t2 = file.split('/')[0]
                        t3 = file.split('/')[1]
                        df_AGG = df.groupby(header).agg({'min', 'max', 'mean', 'sum', 'std'})
                        outfile = t2 + '\\' + t3 + '\\' + t1 + '\\' + t1 + '_agg.csv'
                        df_AGG.to_csv(outfile)
                        self.lineEdit_filepath.setText(t2 + '//' + t3 + '//' + t1 + '//' + t1 + '_agg.csv')
                        self.reloaddata_fromfilepath(outfile)
                        QMessageBox.information(None, "Aggregate",
                                                "File has been successfully saved!",
                                                QMessageBox.Ok)
            self.comboBox_aggregate.setCurrentText("Aggregate")

    def on_linkfileby_changed(self, value_):
        file = self.lineEdit_filepath.text()
        if (value_ == 'Plate_Well'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                file = self.lineEdit_filepath.text()
                df = pd.read_csv(file)
                if 'Plate_Well' in df.columns:
                    if (len(df['Plate_Well']) - df['Plate_Well'].nunique() > 0):
                        QMessageBox.information(None, "Error ",
                                                "The column Plate_Well has duplicated values, you cannot link the file \n No file to save",
                                                QMessageBox.Ok)

                    if (len(df['Plate_Well']) - df['Plate_Well'].nunique() == 0):
                        df.set_index('Plate_Well', inplace=True)
                        fileName_cpds, _ = QFileDialog.getOpenFileName(None, "Load File with Platebarcode and CPD_ID",
                                                                       "",
                                                                       "CSV Files (*.csv)")
                        if fileName_cpds:
                            df_withcpds = pd.read_csv(fileName_cpds, index_col=['Plate_Well'], low_memory=False)
                            my_dir_finalfile = QFileDialog.getExistingDirectory(
                                None,
                                "Select output folder",
                                "",
                                QFileDialog.ShowDirsOnly)
                            t1 = my_dir_finalfile.split('/')[2]
                            df['CPD_ID'] = df_withcpds['X_CPD_ID']
                            df['BATCH_ID'] = df_withcpds['X_BATCH_ID']
                            df['CPDid_BATCHid'] = df_withcpds['X_CPD_ID'] + '_' + df_withcpds['X_BATCH_ID']
                            df['Concentration'] = df_withcpds['Concentration (uM)']
                            df.to_csv(my_dir_finalfile + '\\' + t1 + '_LinkedFile.csv')
                            QMessageBox.information(None, "File linked ",
                                                    "Successfully linked and saved the file!",
                                                    QMessageBox.
                                                    Ok)
                            self.reloaddata_fromDF(df)

                if 'Plate_Well' not in df.columns:
                    file = self.lineEdit_filepath.text()
                    df = pd.read_csv(file)
                    my_dir_finalfile = QFileDialog.getExistingDirectory(
                        None,
                        "Select an output folder",
                        "D:\\RESULTS\\test_GUI\\",
                        QFileDialog.ShowDirsOnly)

                    if my_dir_finalfile:
                        t1 = my_dir_finalfile.split('/')[2]
                        df['Plate_Well'] = df['Plate'] + '_' + df['Well']
                        df.to_csv(my_dir_finalfile + '\\' + t1 + '_Plate_Well.csv', index=None)
                        if (len(df['Plate_Well']) - df['Plate_Well'].nunique() > 0):
                            QMessageBox.information(None, "Error ",
                                                    "The column Plate_Well has duplicated values, you cannot link the file \n The Plate_Well file has been saved",
                                                    QMessageBox.Ok)

                        if (len(df['Plate_Well']) - df['Plate_Well'].nunique() == 0):
                            fileName_platebarcode, _ = QFileDialog.getOpenFileName(None,
                                                                                   "Load File with Platebarcode and CPD_ID",
                                                                                   "D:\RESULTS\\test_GUI\\",
                                                                                   "CSV Files (*.csv)")
                            if fileName_platebarcode:

                                df_withcpds = pd.read_csv(fileName_platebarcode, index_col=['PLATEBARCODE'],
                                                          low_memory=False)
                                fileName_sanofi, _ = QFileDialog.getOpenFileName(None, "Load File with Plate sanofi",
                                                                                 "D:\RESULTS\\test_GUI\\",
                                                                                 "CSV Files (*.csv)")
                                if fileName_sanofi:
                                    df_Platetracking = pd.read_csv(fileName_sanofi, low_memory=False)
                                    if 'cpds_plate' not in df_Platetracking:
                                        QMessageBox.information(None, "Error",
                                                                "File could not be linked the column to link does not exist in the file \n No file to save",
                                                                QMessageBox.Ok)
                                    if 'cpds_plate' in df_Platetracking:
                                        df_Platetracking = pd.read_csv(fileName_sanofi, index_col=['cpds_plate'],
                                                                       low_memory=False)
                                        df_withcpds['Plate'] = df_Platetracking['cells_plate']

                                        df_withcpds['Plate_Well'] = df_withcpds['Plate'] + '_' + df_withcpds['WELL']
                                        df_withcpds.fillna("Nothing", inplace=True)
                                        d = df_withcpds.drop(
                                            df_withcpds[(df_withcpds.Plate.str.contains("Nothing"))].index)
                                        d.to_csv(my_dir_finalfile + "\\" + t1 + '_Filewithcpds_and_Plate.csv',
                                                 index=None)
                                        df_dropped = pd.read_csv(
                                            my_dir_finalfile + "\\" + t1 + '_Filewithcpds_and_Plate.csv',
                                            index_col=['Plate_Well'])
                                        df['CPD_ID'] = df_dropped['X_CPD_ID']
                                        df['BATCH_ID'] = df_dropped['X_BATCH_ID']
                                        df.to_csv(my_dir_finalfile + t1 + '_LinkedFile.csv', index=None)
                                        QMessageBox.information(None, "File linked ",
                                                                "Successfully linked and saved the file!",
                                                                QMessageBox.Ok)
            self.comboBox_linkfileby.setCurrentText('Link file by')

        if (value_ == 'Well'):
            file = self.lineEdit_filepath.text()
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file)
                if 'Well' not in df.columns:
                    QMessageBox.information(None, "Error ",
                                            "The column Well does not exist in the file\nYou cannot link your file.",
                                            QMessageBox.Ok)
                if 'Well' in df.columns:

                    my_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select input folder",
                        "",
                        QFileDialog.ShowDirsOnly)
                    out_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select output folder",
                        "",
                        QFileDialog.ShowDirsOnly)
                    if my_dir:
                        if out_dir:
                            fileName_cpds, _ = QFileDialog.getOpenFileName(None,
                                                                           "Load File with Platebarcode, CPD_ID and BATCH_ID",
                                                                           "",
                                                                           "CSV Files (*.csv)")
                            if fileName_cpds:
                                for root, dirs, files in os.walk(my_dir):
                                    for file_read in files:
                                        df = pd.read_csv(root + '\\' + file_read, index_col='Well')
                                        df_cpds = pd.read_csv(fileName_cpds, index_col='Well')
                                        df_cpds['PLATEBARCODE'] = df['Plate_Sanofi']
                                        df_cpds.to_csv(out_dir + '\\' + 'LinkedFile_' + file_read)
                                QMessageBox.information(None, "File linked",
                                                        "Successfully linked and saved the files!",
                                                        QMessageBox.Ok)
            self.comboBox_linkfileby.setCurrentText('Link file by')

    def on_comboboxaddcolumn_changed(self, _value):
        file = self.lineEdit_filepath.text()

        if (_value == 'New column'):
            if file == "File path":
                print(file)
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                d1 = pd.read_csv(file)
                value_entered, okPressed = QInputDialog.getText(None, "Enter column name to add", "Column name ",
                                                                QLineEdit.Normal, "")
                if (value_entered in d1.columns):
                    QMessageBox.information(None, "Error ",
                                            "The column " + value_entered + " you entered already exists \nNo file to save ",
                                            QMessageBox.Ok)

                if (value_entered == ''):
                    QMessageBox.information(None, "Error ",
                                            "No entry value !\nPlease enter a value in the input text.",
                                            QMessageBox.Ok)
                if (value_entered not in d1.columns):
                    if (value_entered == 'Plate_Well'):
                        if ('Plate' in d1.columns and 'Well' in d1.columns and 'Plate_Sanofi' in d1.columns):
                            QMessageBox.information(None, "Error ",
                                                    "You cannot add the column Plate_Well. The column Plate_Sanofi exists in the file.\nPlease use the option "
                                                    "PlateSanofi_Well to add the column.",
                                                    QMessageBox.Ok)

                if (value_entered not in d1.columns):
                    if (value_entered == 'Plate_Well'):
                        if ('Plate' in d1.columns and 'Well' in d1.columns and 'Plate_Sanofi' not in d1.columns):
                            d1['Plate_Well'] = d1['Plate'] + '_' + d1['Well']
                            out_dir = QFileDialog.getExistingDirectory(
                                None,
                                "Select output folder",
                                "",
                                QFileDialog.ShowDirsOnly)
                            if out_dir:
                                t1 = out_dir.split('/')[2]
                                d1.to_csv(out_dir + '\\' + t1 + '_Plate_Well.csv', index=None)
                                QMessageBox.information(None, "Column added ",
                                                        "The column " + value_entered + " has been successfully added.\nSuccessfully saved the file!",
                                                        QMessageBox.Ok)
                                self.reloaddata_fromDF(d1)
                                print('8')
                                self.lineEdit_filepath.setText(out_dir + '//' + t1 + '_Plate_Well.csv')
                                print('9')
                        if ('Plate' not in d1.columns or 'Well' not in d1.columns):
                            QMessageBox.information(None, "Error ",
                                                    "The column Plate or Well not in the file! No column to add!\nNo file to save.",
                                                    QMessageBox.Ok)

                    if (value_entered == 'PlateSanofi_Well'):
                        my_dir = QFileDialog.getExistingDirectory(
                            None,
                            "Select input folder",
                            "",
                            QFileDialog.ShowDirsOnly)
                        if my_dir:
                            out_dir = QFileDialog.getExistingDirectory(
                                None,
                                "Select output folder",
                                "",
                                QFileDialog.ShowDirsOnly)
                            t1 = out_dir.split('/')[2]
                            if out_dir:
                                list_files = []
                                for root, dirs, files in os.walk(my_dir):
                                    for file_read in files:
                                        df = pd.read_csv(root + '\\' + file_read)
                                        if ('Plate_Sanofi' in df.columns and 'Well' in df.columns):
                                            df['PlateSanofi_Well'] = df['Plate_Sanofi'] + '_' + df['Well']
                                            df.to_csv(out_dir + '\\' + t1 + '_PlateSanofi_Well_' + file_read,
                                                      index=None)
                                            list_files.append(df)
                                            b = pd.DataFrame(pd.concat(list_files, axis=0))
                                            self.setPlateWellText_intblview(df)
                                            self.lineEdit_filepath.setText(
                                                out_dir + '/' + t1 + '_PlateSanofi_Well_' + file_read)
                                            self.reloaddata_fromfilepath(
                                                out_dir + '/' + t1 + '_PlateSanofi_Well_' + file_read)
                                    buttonReply = QMessageBox.question(None, 'Concatenated file',
                                                                       "Press Yes if you want to save the concatenated file.\n"
                                                                       "Press No to ignore.",
                                                                       QMessageBox.Yes | QMessageBox.No,
                                                                       QMessageBox.Yes)
                                    if buttonReply == QMessageBox.Yes:
                                        b.to_csv(out_dir + '\\' + t1 + '_Concat_withPlateSanofiWell.csv', index=None)
                                        self.reloaddata_fromfilepath(out_dir +
                                                                     '\\' + t1 + '_Concat_withPlateSanofiWell.csv')
                                        self.lineEdit_filepath.setText(
                                            out_dir +
                                            '\\' + t1 + '_Concat_withPlateSanofiWell.csv')

                                    if buttonReply == QMessageBox.No:
                                        self.reloaddata_fromdataframe(b, 9)
                                        self.comboBox_dropfrom.setCurrentText('Drop / Change')
                                        self.lineEdit_filepath.setText(
                                            out_dir +
                                            '\\' + t1 + '_Concat_withPlateSanofiWell.csv')

                                if ('Plate_Sanofi' not in df.columns or 'Well' not in df.columns):
                                    QMessageBox.information(None, "Error ",
                                                            "The column Plate, Well or Plate_Sanofi not in the file! No column to add!\nNo file to save.",
                                                            QMessageBox.Ok)
                self.comboBox_addcolumn.setCurrentText('Add column')

    def on_comboboxdropfrom_changed(self, val):
        file = self.lineEdit_filepath.text()

        if (val == 'Extract value from rows'):
            QMessageBox.information(None, "Not imp",
                                        "Not implemented yet..",
                                        QMessageBox.Ok)

        if (val == 'Rename value in rows'):
            QMessageBox.information(None, "Not imp",
                                        "Not implemented yet",
                                        QMessageBox.Ok)

        if (val == 'Rename columns'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file)
                header = self.select_column()
                if len(header) == 0:
                    QMessageBox.information(None, "Error ",
                                            "You must select a column No file to save \nTry again",
                                            QMessageBox.Ok)
                if len(header) > 1:
                    new_value, okPressed = QInputDialog.getText(None, "Value to rename value in column " + str(header),
                                                                "Column name ",
                                                                QLineEdit.Normal, "New column name for " + str(header))
                    if okPressed:
                        if new_value in df:
                            QMessageBox.information(None, "Error ",
                                                    "The value you just entered already exists in the file.\nNo file to save.",
                                                    QMessageBox.Ok)
                        if new_value not in df:
                            df.rename(columns={header: new_value}, inplace=True)
                            out_dir = QFileDialog.getExistingDirectory(
                                None,
                                "Select output folder",
                                "",
                                QFileDialog.ShowDirsOnly)
                            if out_dir:
                                t1 = out_dir.split('/')[2]
                                df.to_csv(out_dir + '\\' + t1 + '_renamedcolumn_' + header + '.csv', index=None)
                                self.reloaddata_fromfilepath(out_dir + '\\' + t1 + '_renamedcolumn_' + header + '.csv')
                                self.lineEdit_filepath.setText(out_dir + '/' + t1 + '_renamedcolumn_' + header + '.csv')
                                self.setPlateWellText_intblview(df)

            self.comboBox_dropfrom.setCurrentText('Drop / Change')

        if (val == 'Drop from columns'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":

                df = pd.read_csv(file)

                header = self.select_multicolumns()

                if (len(header) == 0):
                    QMessageBox.information(None, "Error ",
                                            "You must select a column.\nNo file to save!",
                                            QMessageBox.Ok)
                if len(header) > 0:
                    out_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select output folder",
                        "",
                        QFileDialog.ShowDirsOnly)

                    if out_dir:
                        t1 = out_dir.split('/')[2]
                        d_dropped = df.drop(header, axis=1)

                        fileoutput = '_afterdroppedcolumn' + '.csv'
                        d_dropped.to_csv(out_dir + '\\' + t1 + fileoutput, index=None)

                        self.reloaddata_fromDF(d_dropped)

                        self.lineEdit_filepath.setText(out_dir + '/' + t1 + '_afterdroppedcolumn' + '.csv')

                        if 'Plate' in d_dropped and 'Well' in d_dropped:
                            self.setPlateWellText_intblview(d_dropped)

                        if 'Plate' in d_dropped and 'Well' not in d_dropped:
                            self.lineEdit_plate.setText(str(d_dropped['Plate'].nunique()) + ' unique plate')
                            self.lineEdit_well.setText('No well')
                        if 'Plate' not in d_dropped and 'Well' in d_dropped:
                            self.lineEdit_plate.setText('No plate')
                            self.lineEdit_well.setText(str(len(d_dropped['Well'])) + ' wells')
                        if 'Plate' not in d_dropped and 'Well' not in d_dropped:
                            self.lineEdit_plate.setText('No plate')
                            self.lineEdit_well.setText('No well')
                        QMessageBox.information(None, "Dropped columns ",
                                                "Columns: " + str(
                                                    header) + " have been dropped from your file!\nFile successfully saved.",
                                                QMessageBox.Ok)

            self.comboBox_dropfrom.setCurrentText('Drop / Change')

        if (val == 'Drop from rows'):
            if file == 'File path':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                header = self.select_column()
                file = self.lineEdit_filepath.text()
                df = pd.read_csv(file)
                value_entered, okPressed = QInputDialog.getText(None, "Value to drop from rows", "Value to drop ",
                                                                QLineEdit.Normal, "")
                if (value_entered in df[header].values):
                    my_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select output folder",
                        "",
                        QFileDialog.ShowDirsOnly)
                    t1 = my_dir.split('/')[2]
                    d = df[~(df[header].str.contains(value_entered, na=False))]
                    d.to_csv(my_dir + '\\' + t1 + '_row_file_dropped.csv', index=None)
                    self.lineEdit_filepath.setText(my_dir + '/' + t1 + '_row_file_dropped.csv')
                    self.reloaddata_fromfilepath(my_dir + '\\' + t1 + '_row_file_dropped.csv')
                    QMessageBox.information(None, "Dropped rows ",
                                            "The value " + str(
                                                value_entered) + " you entered has been dropped from column " + str(
                                                header) + "\nSuccessfully saved the file!",
                                            QMessageBox.Ok)

                    if ('Plate' in b.columns and 'Well' in b.columns):
                        print('ee')
                        self.lineEdit_plate.setText(str(b['Plate'].nunique()) + ' plates')
                        self.lineEdit_well.setText(str(len(b['Well'])) + ' wells')
                        self.getncpdsbatches(b)

                    if ('Plate' not in b.columns and 'Well' not in b.columns):
                        print('pp')
                        self.lineEdit_plate.setText('No plate')
                        self.lineEdit_well.setText('No wells')
                        self.getncpdsbatches(b)

                    if ('Plate' not in b.columns and 'Well' in b.columns):
                        print('qq')
                        self.lineEdit_plate.setText('No plate')
                        self.lineEdit_well.setText(str(len(b['Well'])) + ' wells')
                        print('oo')
                        self.getncpdsbatches(b)

                    if ('Plate' in b.columns and 'Well' not in b.columns):
                        print('ka')
                        self.lineEdit_plate.setText(str(b['Plate'].nunique()) + ' plates')
                        self.lineEdit_well.setText('No wells')
                        self.getncpdsbatches(b)

                if (value_entered not in df[header].values):
                    QMessageBox.information(None, "Error",
                                            "No value to drop.\nThe value " + str(
                                                value_entered) + " does not exist in the column " + str(
                                                header) + "\nNo file to save.",
                                            QMessageBox.Ok)
                    print('00')
            self.comboBox_dropfrom.setCurrentText('Drop / Change')

    def on_comboboxduplicates_changed(self, value):
        file = self.lineEdit_filepath.text()
        if (value == 'Get duplicated values'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_mask = pd.read_csv(file, low_memory=False)
                header = self.select_column()
                boolk = df_mask.duplicated(subset=header, keep=False)
                df_duplicated = df_mask[boolk]
                if (len(df_duplicated) == 0):
                    QMessageBox.information(None, "Duplicated values ",
                                            "No duplicated values have been detected in the column" + str(
                                                header) + "!\nNo file to save.",
                                            QMessageBox.Ok)
                if (len(df_duplicated) > 1):
                    out_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select a folder",
                        "",
                        QFileDialog.ShowDirsOnly)
                    t1 = out_dir.split('/')[2]
                    QMessageBox.information(None, "Duplicated values ",
                                            str(len(
                                                df_duplicated)) + " duplicated values have been detected in the column " + str(
                                                header) +
                                            ".\nSuccessfully saved the file!",
                                            QMessageBox.Ok)
                    df_duplicated.to_csv(out_dir + '\\' + t1 + '_duplicatedValuesfrom_' + header + '.csv', index=None)
                    self.setPlateWellText_intblview(df_duplicated)
                    self.reloaddata_fromfilepath(out_dir + '//' + t1 + '_duplicatedValuesfrom_' + header + '.csv')
                    self.lineEdit_filepath.setText(out_dir + '/' + t1 + '_duplicatedValuesfrom_' + header + '.csv')
            self.comboBox_duplicates.setCurrentText('Duplicates')

        if (value == 'Number of duplicates'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file, low_memory=False)
                header = self.select_column()
                nb_unique_header = df[header].nunique()
                if (len(df[header]) - nb_unique_header == 0):
                    QMessageBox.information(None, "Number of duplicates",
                                            "You have no duplicated values in the column" + str(header),
                                            QMessageBox.Ok)
                if (len(df[header]) - nb_unique_header > 0):
                    QMessageBox.information(None, "Number of duplicates",
                                            str(nb_unique_header) + " duplicated " + str(header) + '\n' + "",
                                            QMessageBox.Ok)
            self.comboBox_duplicates.setCurrentText('Duplicates')

        if (value == 'Drop duplicated values'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file, low_memory=False)
                len_init = len(df)
                header = self.select_column()
                df.drop_duplicates(subset=header, inplace=True)
                if (len_init - len(df) == 0):
                    QMessageBox.information(None, "Dropped duplicates",
                                            "No value has been dropped from " + str(header) + "\nNo file to save",
                                            QMessageBox.Ok)
                if (len_init - len(df) > 0):
                    out_dir = QFileDialog.getExistingDirectory(
                        None,
                        "Select output folder",
                        "",
                        QFileDialog.ShowDirsOnly)
                    if out_dir:
                        t1 = out_dir.split('/')[2]
                        df.to_csv(out_dir + '\\' + t1 + '_afterdropduplicatesfrom_' + header + '.csv', index=None)
                        self.setPlateWellText_intblview(df)
                        self.lineEdit_filepath.setText(
                            out_dir + '/' + t1 + '_afterdropduplicatesfrom_' + header + '.csv')
                        self.reloaddata_fromfilepath(
                            out_dir + '//' + t1 + '_afterdropduplicatesfrom_' + header + '.csv')
                        QMessageBox.information(None, "Dropped duplicates",
                                                str(len_init - len(df)) + " value has been dropped from " + str(
                                                    header) + "\nYour file has been saved",
                                                QMessageBox.Ok)

            self.comboBox_duplicates.setCurrentText('Duplicates')

    def getncpdsbatches(self, dataframe):
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')

    def on_addclasses_clicked(self):
        QMessageBox.information(None, "Not imp",
                                "Not implemented yet..",
                                QMessageBox.Ok)

    def on_loadFile_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            self.lineEdit_filepath.setText(fileName)
            df = pd.read_csv(fileName, low_memory=False)
            model = PandasModel(df.head(1000))
            self.tableView_dataframe.setModel(model)
            if ('Plate' in df.columns and 'Well' in df.columns):
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)

            if ('Plate' not in df.columns and 'Well' not in df.columns):
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText('No well')
                self.getncpdsbatches(df)

            if ('Plate' not in df.columns and 'Well' in df.columns):
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)

            if ('Plate' in df.columns and 'Well' not in df.columns):
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText('No well')
                self.getncpdsbatches(df)

    def on_concatenatefiles_clicked(self):
        filter = "CSV (*.csv)"
        filename, _ = QFileDialog.getOpenFileNames(None, "Select CSV files to concatenate",
                                                   "",
                                                   filter)
        if filename:
            my_dir = QFileDialog.getExistingDirectory(
                None,
                "Select output folder",
                "",
                QFileDialog.ShowDirsOnly)
            t1 = my_dir.split('/')[2]
            if my_dir:
                list_files = []
                for i in filename:
                    df = pd.read_csv(i)
                    list_files.append(df)
                    b = pd.DataFrame(pd.concat(list_files, axis=0))
                    b.to_csv(my_dir +
                             '//' + t1 + '_Concatenated_File.csv', index=None)
                    self.reloaddata_fromfilepath(my_dir +
                                                 '//' + t1 + '_Concatenated_File.csv')
                    self.lineEdit_filepath.setText(my_dir + '/' + t1 + '_Concatenated_File.csv')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form_loadDataframe = QtWidgets.QWidget()
    ui = Ui_Form_loadDataframe()
    ui.setupUi(Form_loadDataframe)
    Form_loadDataframe.show()
    sys.exit(app.exec_())
