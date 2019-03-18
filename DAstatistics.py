from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PyQt5.QtWidgets import *
import pandas as pd
from requests.packages.urllib3.packages.six.moves import xrange
from DAform_checkboxes_dropfromrows import Ui_Form_CheckBoxes
from DAform_table_addclasses import Ui_form_table_addclasses
from DApandaswidget import PandasModel
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_loaddataframe.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_loadDataframe(object):
    def openwindow_form_checkboxes(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_CheckBoxes()
        self.ui.setupUi(self.window)
        # Form_loadDataframe.hide()
        self.window.show()

    def openwindow_addclasses(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_form_table_addclasses()
        self.ui.setupUi(self.window)
        # Form_loadDataframe.hide()
        self.window.show()
    def setupUi(self, Form_loadDataframe):
        Form_loadDataframe.setObjectName("Form_loadDataframe")
        Form_loadDataframe.setEnabled(True)
        Form_loadDataframe.resize(1477, 876)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_loadDataframe.sizePolicy().hasHeightForWidth())
        Form_loadDataframe.setSizePolicy(sizePolicy)
        Form_loadDataframe.setSizeIncrement(QtCore.QSize(25, 25))
        self.pushButton_loadfile = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(650, 30, 61, 21))
        self.pushButton_loadfile.setMouseTracking(False)
        self.pushButton_loadfile.setAutoFillBackground(False)
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.lineEdit_filepath = QtWidgets.QLineEdit(Form_loadDataframe)
        self.lineEdit_filepath.setGeometry(QtCore.QRect(10, 30, 631, 21))
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.comboBox_plot = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_plot.setGeometry(QtCore.QRect(1010, 150, 271, 22))
        self.comboBox_plot.setObjectName("comboBox_plot")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.pushButton_concatfiles = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_concatfiles.setGeometry(QtCore.QRect(720, 30, 101, 21))
        self.pushButton_concatfiles.setObjectName("pushButton_concatfiles")
        self.lineEdit_plate = QtWidgets.QLabel(Form_loadDataframe)
        self.lineEdit_plate.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.lineEdit_plate.setText("")
        self.lineEdit_plate.setObjectName("lineEdit_plate")
        self.lineEdit_well = QtWidgets.QLabel(Form_loadDataframe)
        self.lineEdit_well.setGeometry(QtCore.QRect(130, 80, 121, 20))
        self.lineEdit_well.setText("")
        self.lineEdit_well.setObjectName("lineEdit_well")
        self.tableView_dataframe = QtWidgets.QTableView(Form_loadDataframe)
        self.tableView_dataframe.setGeometry(QtCore.QRect(10, 200, 1451, 671))
        self.tableView_dataframe.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_dataframe.setDragEnabled(True)
        self.tableView_dataframe.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableView_dataframe.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_dataframe.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_dataframe.setSortingEnabled(True)
        self.tableView_dataframe.setObjectName("tableView_dataframe")
        self.comboBox_duplicates = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_duplicates.setGeometry(QtCore.QRect(1290, 30, 171, 22))
        self.comboBox_duplicates.setObjectName("comboBox_duplicates")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_dropfrom = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_dropfrom.setGeometry(QtCore.QRect(1010, 30, 271, 22))
        self.comboBox_dropfrom.setObjectName("comboBox_dropfrom")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_dropfrom.addItem("")
        self.comboBox_linkfileby = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_linkfileby.setGeometry(QtCore.QRect(1290, 90, 171, 22))
        self.comboBox_linkfileby.setObjectName("comboBox_linkfileby")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_linkfileby.addItem("")
        self.comboBox_machinelearning = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_machinelearning.setGeometry(QtCore.QRect(1290, 150, 171, 22))
        self.comboBox_machinelearning.setObjectName("comboBox_machinelearning")
        self.comboBox_machinelearning.addItem("")
        self.comboBox_machinelearning.addItem("")
        self.comboBox_normalize = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_normalize.setGeometry(QtCore.QRect(1290, 60, 171, 22))
        self.comboBox_normalize.setObjectName("comboBox_normalize")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_removeoutliers = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_removeoutliers.setGeometry(QtCore.QRect(1010, 60, 271, 22))
        self.comboBox_removeoutliers.setObjectName("comboBox_removeoutliers")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_extracthits = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_extracthits.setGeometry(QtCore.QRect(1290, 120, 171, 22))
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
        self.comboBox_statistics.setGeometry(QtCore.QRect(1010, 120, 271, 22))
        self.comboBox_statistics.setObjectName("comboBox_statistics")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.pushButton_addclasses = QtWidgets.QPushButton(Form_loadDataframe)
        self.pushButton_addclasses.setGeometry(QtCore.QRect(830, 30, 80, 21))
        self.pushButton_addclasses.setObjectName("pushButton_addclasses")
        self.comboBox_aggregate = QtWidgets.QComboBox(Form_loadDataframe)
        self.comboBox_aggregate.setGeometry(QtCore.QRect(1010, 90, 271, 22))
        self.comboBox_aggregate.setObjectName("comboBox_aggregate")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.label_nbcpdid = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbcpdid.setGeometry(QtCore.QRect(260, 80, 131, 20))
        self.label_nbcpdid.setText("")
        self.label_nbcpdid.setObjectName("label_nbcpdid")
        self.label_nbbatchid = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbbatchid.setGeometry(QtCore.QRect(410, 80, 131, 20))
        self.label_nbbatchid.setText("")
        self.label_nbbatchid.setObjectName("label_nbbatchid")
        self.label_nbrrows = QtWidgets.QLabel(Form_loadDataframe)
        self.label_nbrrows.setGeometry(QtCore.QRect(570, 80, 131, 21))
        self.label_nbrrows.setText("")
        self.label_nbrrows.setObjectName("label_nbrrows")

        self.lineEdit_filepath.setText('File path')
        self.pushButton_loadfile.clicked.connect(self.on_loadFile_clicked)
        self.pushButton_concatfiles.clicked.connect(self.on_concatenatefiles_clicked)
        self.pushButton_addclasses.clicked.connect(self.on_addclasses_clicked)
        self.comboBox_duplicates.currentTextChanged.connect(self.on_comboboxduplicates_changed)
        self.comboBox_dropfrom.currentTextChanged.connect(self.on_comboboxdropfrom_changed)
        self.comboBox_linkfileby.currentTextChanged.connect(self.on_linkfileby_changed)
        self.comboBox_extracthits.currentTextChanged.connect(self.on_comboboxactivecompounds_changed)
        self.comboBox_removeoutliers.currentTextChanged.connect(self.on_comboboxremoveoutliers_changed)
        self.comboBox_machinelearning.currentTextChanged.connect(self.on_machinelearning_changed)
        self.comboBox_statistics.currentTextChanged.connect(self.on_statistics_changed)
        self.comboBox_normalize.currentTextChanged.connect(self.on_comboboxnormalize_changed)
        self.comboBox_plot.currentTextChanged.connect(self.on_plot_changed)
        self.comboBox_aggregate.currentTextChanged.connect(self.on_comboboxaggregate_changed)

        self.retranslateUi(Form_loadDataframe)
        QtCore.QMetaObject.connectSlotsByName(Form_loadDataframe)

    def retranslateUi(self, Form_loadDataframe):
        _translate = QtCore.QCoreApplication.translate
        Form_loadDataframe.setWindowTitle(_translate("Form_loadDataframe", "Main window"))
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
        self.comboBox_dropfrom.setItemText(0, _translate("Form_loadDataframe", "Edit rows columns"))
        self.comboBox_dropfrom.setItemText(1, _translate("Form_loadDataframe", "Merge 2 columns"))
        self.comboBox_dropfrom.setItemText(2, _translate("Form_loadDataframe", "Rename columns"))
        self.comboBox_dropfrom.setItemText(3, _translate("Form_loadDataframe", "Drop from columns"))
        self.comboBox_dropfrom.setItemText(4, _translate("Form_loadDataframe", "Order columns"))
        self.comboBox_dropfrom.setItemText(5, _translate("Form_loadDataframe", "Drop/ Rename/ Keep values in rows"))
        self.comboBox_dropfrom.setItemText(6, _translate("Form_loadDataframe", "Rename value in rows"))
        self.comboBox_dropfrom.setItemText(7, _translate("Form_loadDataframe", "Extract value from rows"))
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
        self.comboBox_removeoutliers.setItemText(1, _translate("Form_loadDataframe", "Mean-value*sigma <value< Mean+value*sigma"))
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
        self.comboBox_statistics.setItemText(5, _translate("Form_loadDataframe", "Merge 2 dataframes"))
        self.pushButton_addclasses.setText(_translate("Form_loadDataframe", "Add classes"))
        self.comboBox_aggregate.setItemText(0, _translate("Form_loadDataframe", "Aggregate"))
        self.comboBox_aggregate.setItemText(1, _translate("Form_loadDataframe", "Aggregate - Min Max Mean Sum STD"))
        self.comboBox_aggregate.setItemText(2, _translate("Form_loadDataframe", "Aggregate grouping by"))


    def on_comboboxnormalize_changed(self, value_nor):
        file = self.lineEdit_filepath.text()
        if (value_nor == "Mean"):
            if file == 'File path':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                df2 = pd.read_csv(file)
                t1 = os.path.dirname(file)
                file_name1 = os.path.splitext(os.path.basename(file))[0]
                if 'Plate' not in df2.columns and 'Class' not in df2.columns:
                    QMessageBox.information(None, "Error ",
                                            "Columns 'Plate' and 'Class' do not exist in the file.\nYou cannot apply the normalisation",
                                            QMessageBox.Ok)
                if 'Plate' in df2.columns:
                    if 'Class' not in df2.columns:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Class' does not exist in the file.\nYou cannot apply the normalisation",
                                                QMessageBox.Ok)
                    if 'Class' in df2.columns:
                        df2_grp = df2.groupby('Plate')
                        for grp in df2_grp:
                            for column in grp[1]._get_numeric_data():
                                if column != 'Class' and column != 'Concentration': # and column != 'CPD_ID' and column != 'BATCH_ID':
                                    max_a = np.max(grp[1].query('Class == 2')[column])
                                    max_b = np.max(grp[1].query('Class == 1')[column])
                                    if max_a < max_b:
                                        max_cp = np.mean(grp[1].query('Class == 1')[column])
                                    else:
                                        max_cp = np.mean(grp[1].query('Class == 2')[column])
                                    coeff = grp[1][column] / max_cp
                                    grp[1][column] = coeff
                                    grp[1].to_csv(t1 + '\\' +grp[0]+'.csv', index=None)
                        QMessageBox.information(None, "Mean normalisation",
                            str(len(df2_grp['Plate'].nunique())) + " plates have been normalised.\nSaved files.",
                            QMessageBox.Ok)
        self.comboBox_normalize.setCurrentText("Normalise")

        if (value_nor == "Median"):
            df2 = pd.read_csv(file)
            t1 = os.path.dirname(file)
            file_name1 = os.path.splitext(os.path.basename(file))[0]
            if 'Plate' not in df2.columns and 'Class' not in df2.columns:
                QMessageBox.information(None, "Error ",
                                        "Columns 'Plate' and 'Class' do not exist in the file.\nYou cannot apply the normalisation",
                                        QMessageBox.Ok)
            if 'Plate' in df2.columns:
                if 'Class' not in df2.columns:
                    QMessageBox.information(None, "Error ",
                                            "Column 'Class' does not exist in the file.\nYou cannot apply the normalisation",
                                            QMessageBox.Ok)
                if 'Class' in df2.columns:
                    df2_grp = df2.groupby('Plate')
                    for grp in df2_grp:
                        for column in grp[1]._get_numeric_data():
                            if column != 'Class' and column != 'Concentration':  # and column != 'CPD_ID' and column != 'BATCH_ID':
                                max_a = np.max(grp[1].query('Class == 2')[column])
                                max_b = np.max(grp[1].query('Class == 1')[column])
                                if max_a < max_b:
                                    max_cp = np.median(grp[1].query('Class == 1')[column])
                                else:
                                    max_cp = np.median(grp[1].query('Class == 2')[column])
                                coeff = grp[1][column] / max_cp
                                grp[1][column] = coeff
                                grp[1].to_csv(t1 + '\\' + grp[0] + '.csv', index=None)
                    QMessageBox.information(None, "Median normalisation",
                                            str(len(df2_grp[
                                                        'Plate'].nunique())) + " plates have been normalised.\nSaved files.",
                                            QMessageBox.Ok)
        self.comboBox_normalize.setCurrentText("Normalise")

        if (value_nor == "Min-Max"):
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet.",
                                    QMessageBox.Ok)
        self.comboBox_normalize.setCurrentText("Normalise")

    def on_statistics_changed(self, value_st):
        file = self.lineEdit_filepath.text()
        t1 = os.path.dirname(file)
        file_name1 = os.path.splitext(os.path.basename(file))[0]

        if value_st == "Merge 2 dataframes":
            df1 =  pd.read_csv(file)
            header = self.select_column()
            if not header:
                print('1')
            if header:
                fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to get the intersection",
                                                           "",
                                                           "CSV Files (*.csv)")
                if fileName2:
                    df2 = pd.read_csv(fileName2)
                    mergedStuff = pd.merge(df1, df2, on=[header], how='inner')
                    if len(mergedStuff) == 0:
                        QMessageBox.information(None, "No merge","You have no values in common between the 2 files.\nNo file to save.", QMessageBox.Ok)

                    if len(mergedStuff) > 0:
                        mergedStuff.to_csv(t1 + '\\' + 'merged_' + header +'_'+ file_name1 + '.csv', index=None)
                        self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + header +'_'+ file_name1 + '.csv')
                        self.lineEdit_filepath.setText(t1 + '\\' + 'merged_' + header +'_'+ file_name1 + '.csv')
                        QMessageBox.information(None, "Merge",
                                                "Successfully merged the 2 files"  + "\nSaved file.",
                                                QMessageBox.Ok)

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

                    if df[columnname].isna().any() == False:
                        mean_df = df[columnname].mean()
                        std_df = df[columnname].std()
                        QMessageBox.information(None, "Mean and STD ",
                                                "Mean = " + " " + str(mean_df) + " \n" + "STD = " + str(std_df),
                                                QMessageBox.Ok)
        self.comboBox_statistics.setCurrentText("Statistics")

        if value_st == "Z factor & Robust Z factor":
            file = self.lineEdit_filepath.text()
            if file == 'File path':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                df = pd.read_csv(file)
                if 'Plate' not in df.columns:
                    QMessageBox.information(None, "Error ",
                                            "Column 'Plate' does not exist in the file.",
                                            QMessageBox.Ok)
                if 'Plate' in df.columns:
                    if 'Class' not in df.columns:
                        QMessageBox.information(None, "Error ",
                                                "The column Class does not exist in the loaded file.\nPlease add the column Class first.",
                                                QMessageBox.Ok)
                    if 'Class' in df.columns:
                        header = self.select_column()
                        if header:
                            if (df['Plate'].nunique() == 1):
                                pos_data = df[df['Class'] == 1]
                                neg_data = df[df['Class'] == 2]
                                Z_factor = 1 - ((3 * (np.std(neg_data) + np.std(pos_data))) / (np.abs(np.mean(neg_data) - np.mean(pos_data))))
                                QMessageBox.information(None, "Z factor",
                                                        "Z factor " + str(header) + " = " + str(Z_factor[header]), QMessageBox.Ok)
                            if (df['Plate'].nunique() > 1):
                                QMessageBox.information(None, "Error ",
                                                        "The Plate is not unique.\nPlease group your data first.",
                                                        QMessageBox.Ok)
        if value_st == "Intersection":
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file:
                fileName1 = file
                file1 = pd.read_csv(fileName1)
                header1 = self.select_column()
                if (len(header1) < 1):
                    QMessageBox.information(None, "Error ",
                                            "Please select a column first.",
                                            QMessageBox.Ok)
                if (len(header1) >= 1):
                    fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to get the intersection",
                                                               "",
                                                               "CSV Files (*.csv)")
                    if fileName2:
                        file2 = pd.read_csv(fileName2)
                        header2 = self.select_column()
                        if not header2:
                            QMessageBox.information(None, "Error ",
                                                    "Please select a column first.",
                                                    QMessageBox.Ok)
                        if header2:
                            inter = file2[file2[header2].isin(file1[header1])]
                            if len(inter) == 0:
                                QMessageBox.information(None, "Error ",
                                                        "No intersecton between the 2 files.\nNo file to save.",
                                                        QMessageBox.Ok)
                            if len(inter) > 0:
                                t1 = os.path.dirname(fileName1)
                                file_name1 = os.path.splitext(os.path.basename(fileName1))[0]
                                inter.to_csv(t1 + '\\' + 'Intersection_' + file_name1 + '.csv', index=None)
                                self.reloaddata_fromfilepath(t1 + '\\' + 'Intersection_' + file_name1 + '.csv')
                                self.lineEdit_filepath.setText(t1 + '/' + 'Intersection_' + file_name1 + '.csv')
                                QMessageBox.information(None, "Intersection",
                                            "The number of intersected data = " + str(len(inter)) + "\nSaved file.",
                                            QMessageBox.Ok)
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
                if not header:
                    QMessageBox.information(None, "Error ",
                                            "Please select a column first.",
                                            QMessageBox.Ok)
                if header:
                    fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to get the union",
                                                               "",
                                                               "CSV Files (*.csv)")
                    if fileName2:
                        file2 = pd.read_csv(fileName2)
                        union = pd.concat([file1, file2], ignore_index=True).drop_duplicates().reset_index(drop=True)
                        if len(union) == 0:
                            QMessageBox.information(None, "Error ",
                                                    "No union between the 2 files.\nNo file to save.",
                                                    QMessageBox.Ok)
                        if len(union) > 0:
                            t1 = os.path.dirname(fileName1)
                            file_name1 = os.path.splitext(os.path.basename(fileName1))[0]
                            union.to_csv(t1 + '\\' + 'Union_' + file_name1 + '.csv', index=None)
                            self.reloaddata_fromfilepath(t1 + '\\' + 'Union_' + file_name1 + '.csv')
                            self.lineEdit_filepath.setText(t1 + '/' + 'Union_' + file_name1 + '.csv')
                            QMessageBox.information(None, "Union",
                                                    "The number of union data = " + str(len(union)) + "\nSaved file.",
                                                    QMessageBox.Ok)
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
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
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            data_dropped.to_csv(t1 + '\\' + 'Activecpds_' +  file_name1 + '.csv', index=None)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column '" + str(
                                                        columnname) + "' when value > " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '//' + 'Activecpds_' +  file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'Activecpds_' +  file_name1 + '.csv')
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
                        value_sigma1, ok = QInputDialog.getDouble(None, "Input", "Sigma:")
                        # Neg = df_tot[df_tot['Class'] == 2]
                        # Pos = df_tot[df_tot['Class'] == 1]
                        # Cpd = df_tot[df_tot['Class'] == 3]
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
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            data_dropped.to_csv(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv', index=None)
                            QMessageBox.information(None, "Toxic coumpounds",
                                                    str(len(data_dropped)) +
                                                    " toxic compounds were detected using the column '" + str(
                                                        columnname) + "' when value > " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '//' + 'ToxCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv')
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "< mean - value * sigma"):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_column()
                if columnname == 'Toxic_compounds':
                    QMessageBox.information(None, "Error ",
                                            "Please select a column to detect the active compounds.\nTry again. No file to save",
                                            QMessageBox.Ok)
                if columnname != 'Toxic_compounds':
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
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
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            data_dropped.to_csv(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv', index=None)
                            QMessageBox.information(None, "Toxic coumpounds",
                                                    str(len(data_dropped)) +
                                                    " toxic compounds were detected using the column " + str(
                                                        columnname) + " when value < " + str(meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '//' + 'ToxCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv')

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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
                        meanval = df_toremoveout[columnname].mean()
                        df_toremoveout['Active_compounds'] = 'notactivecpd'
                        df_toremoveout['Active_compounds'][(df_toremoveout[columnname] > meanval)] = \
                            df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                        data_dropped = df_toremoveout.drop(
                            df_toremoveout[(df_toremoveout['Active_compounds'].str.contains('notactivecpd'))].index)
                        if len(df_toremoveout) < 1 :
                            QMessageBox.information(None, "No active compound",
                                                    "You have no active compound"
                                                    + " \nNo file to save",
                                                    QMessageBox.Ok)
                        if len(data_dropped) >= 1:
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            data_dropped.to_csv(t1 + '\\' + 'ActiveCpds_' + file_name1 + '.csv', index=None)
                            QMessageBox.information(None, "Active compounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds based on the column " + str(
                                                        columnname)+ 'when value > ' + str() + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                t1 + '//' + 'ActiveCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(
                                t1 + '\\' + 'ActiveCpds_' + file_name1 + '.csv')
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
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
                                                        " active compounds were detected using the column '" + str(
                                                            columnname) + "' when mean < " + str(meanval)
                                                        + "\nSuccessfully saved the file",
                                                        QMessageBox.Ok)
                                self.lineEdit_filepath.setText(my_dir + '/' + 'Active_compounds.csv')
                                self.reloaddata_fromfilepath(outfile)
        self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> value"):
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
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
                                                        " active compounds were detected using the column '" + str(
                                                            columnname) + "' when value < " + str(value_v)
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
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
            print('dkdkdkdk')
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                print('dmdk')
                columnname = self.select_column()
                print(columnname)
                df1 = pd.read_csv(file)
                if df1[columnname].dtypes == str or df1[columnname].dtypes == bool or df1[columnname].dtypes == object :
                    print('fmjfkkd')
                if df1[columnname].dtypes != str or df1[columnname].dtypes != bool or df1[columnname].dtypes != object:
                    if columnname == 'Outliers':
                        QMessageBox.information(None, "Error ",
                                                "Please select a column to remove the outliers\nTry again. No file to save",
                                                QMessageBox.Ok)
                    if columnname != 'Outliers':
                        if 'Well' not in df_toremoveout:
                            QMessageBox.information(None, "Error ",
                                                    "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                    QMessageBox.Ok)
                        if 'Well' in df_toremoveout:
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
                                    t1 = os.path.dirname(file)
                                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                                    outfile = t1 + '\\' + '_WithoutOutliers_' + str(value_sigma1) + 'sigma' + file_name1 +'.csv'
                                    data_dropped.to_csv(outfile, index=None)
                                    self.lineEdit_filepath.setText(
                                        t1 + '//' + '_WithoutOutliers_' + str(
                                            value_sigma1) + 'sigma' + file_name1 + '.csv')
                                    QMessageBox.information(None, "Outliers",
                                                            str(len(df_toremoveout) - len(data_dropped)) +
                                                            " outliers have been removed using the column " + str(
                                                                columnname) + '.\n'
                                                            + "Successfully saved the file!",
                                                            QMessageBox.Ok)
                                    self.reloaddata_fromfilepath( t1 + '\\' + '_WithoutOutliers_' + str(value_sigma1) + 'sigma' + file_name1 +'.csv')
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
                        if 'Well' not in df_toremoveout:
                            QMessageBox.information(None, "Error ",
                                                    "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                    QMessageBox.Ok)
                        if 'Well' in df_toremoveout:
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
                                t1 = os.path.dirname(file)
                                file_name1 = os.path.splitext(os.path.basename(file))[0]
                                outfile = t1 + '\\'+  '_WithoutOutliers' +  file_name1+ '.csv'
                                data_dropped.to_csv(outfile, index=None)
                                QMessageBox.information(None, "Outliers",
                                                        str(len(df_toremoveout) - len(data_dropped)) +
                                                        " outliers have been removed using the column " + str(
                                                            columnname) + '.\n'
                                                        + "Successfully saved the file!",
                                                        QMessageBox.Ok)
                                self.lineEdit_filepath.setText(
                                    t1 + '//' + '_WithoutOutliers' + file_name1 + '.csv')
                                self.reloaddata_fromfilepath( t1 + '\\'+  '_WithoutOutliers' +  file_name1+ '.csv')
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
                    if 'Well' not in df_toremoveout:
                        QMessageBox.information(None, "Error ",
                                                "Column 'Well' does not exist in the file. You cannot remove the outliers.\nNo file to save.",
                                                QMessageBox.Ok)
                    if 'Well' in df_toremoveout:
                        value_out, ok = QInputDialog.getDouble(None, "Input", "Value:")
                        if value_out:
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

        if ('Plate' in df.columns and 'WELL' in df.columns):
            self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
            self.getncpdsbatches(df)

        if ('Plate' not in df.columns and 'Well' not in df.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df)

        if ('Plate' not in df.columns and 'Well' in df.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
            self.getncpdsbatches(df)

        if ('Plate' not in df.columns and 'WELL' in df.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
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

        if ('Plate' in df1.columns and 'WELL' in df1.columns):
            self.lineEdit_plate.setText(str(df1['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText(str(len(df1['WELL'])) + ' WELLs')
            self.getncpdsbatches(df1)

        if ('Plate' not in df1.columns and 'Well' not in df1.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df1)

        if ('Plate' not in df1.columns and 'Well' in df1.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df1['Well'])) + ' wells')
            self.getncpdsbatches(df1)

        if ('Plate' not in df1.columns and 'WELL' in df1.columns):
            self.lineEdit_plate.setText('No plate')
            self.lineEdit_well.setText(str(len(df1['WELL'])) + ' WELLs')
            self.getncpdsbatches(df1)

        if ('Plate' in df1.columns and 'Well' not in df1.columns):
            self.lineEdit_plate.setText(str(df1['Plate'].nunique()) + ' plates')
            self.lineEdit_well.setText('No wells')
            self.getncpdsbatches(df1)

    def on_plot_changed(self, vl):
        if (vl == 'Correlation'):
            file = self.lineEdit_filepath.text()
            if file == 'File path':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                df_data1 = pd.read_csv(file)
                if 'Class' not in df_data1.columns:
                    QMessageBox.information(None, "Error ",
                                            "Columns class is missing from the file.\nPlease add the column Class first.",
                                            QMessageBox.Ok)
                header1 = self.select_column()

                if 'Class' in df_data1.columns and header1 in df_data1.columns:
                    file2, _ = QFileDialog.getOpenFileName(None, "Load second file to plot the correlation",
                                                                   "",
                                                                   "CSV Files (*.csv)")
                    if file2:
                        df_data2 = pd.read_csv(file2)
                        if len(df_data1) != len(df_data2):
                            QMessageBox.information(None, "Correlation Error",
                                                    "Correlation cannot be applied. Please load another file\nDifferent number of rows.",
                                                    QMessageBox.Ok)
                            if len(df_data1) == len(df_data2):
                                self.reloaddata_fromfilepath(file2)
                                self.lineEdit_filepath.setText(str(file2))
                                if header1:
                                    if 'Class' in df_data1.columns:
                                        if 'Class' in df_data2.columns:
                                            df_data1 = df_data1[df_data1['Class'] == 3]
                                            df_data2 = df_data2[df_data2['Class'] == 3]
                                            plt.scatter(df_data1['Perc_SenescentCells'].values, df_data2['Perc_SenescentCells'].values)
                                            plt.ylim([0, 2])
                                            plt.xlim([0, 2])
                                            plt.show()
                                            QMessageBox.information(None, "Correlation ",
                                                                    "Correlation = " + str(np.corrcoef(df_data1[header1].values,
                                                                                                       df_data2[header1])),
                                                                    QMessageBox.Ok)

        self.comboBox_plot.setCurrentText("Plot")

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
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, capsize=.5, ci='sd', ax=axs[0, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, size=3, color='orange',
                                  ax=axs[0, 1])
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, capsize=.5, ci='sd', ax=axs[1, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, size=3, color='orange',
                                  ax=axs[1, 0])
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, capsize=.5, ci='sd', ax=axs[1, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, size=3, color='orange',
                                  ax=axs[1, 1])
                    plt.xticks(rotation=40, size=10)
                    plt.show()

                if len(header) == 2:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.5, ci='sd')
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange')
                    plt.xticks(rotation=40, size=10)
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
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, capsize=.0, ci=False, ax=axs[0, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis2], data=df_1, size=3, color='orange',
                                  ax=axs[0, 1])
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, capsize=.0, ci=False, ax=axs[1, 0])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis3], data=df_1, size=3, color='orange',
                                  ax=axs[1, 0])
                    plt.xticks(rotation=40, size=10)
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, capsize=.0, ci=False, ax=axs[1, 1])
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis4], data=df_1, size=3, color='orange',
                                  ax=axs[1, 1])
                    plt.xticks(rotation=40, size=7)
                    plt.show()

                if len(header) == 2:
                    header_xaxis = header[0]
                    header_yaxis1 = header[1]
                    sns.barplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, capsize=.5, ci='sd')
                    sns.swarmplot(x=header_xaxis, y=df_1[header_yaxis1], data=df_1, size=3, color='orange')
                    plt.xticks(rotation=40, size=10)
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
                QMessageBox.information(None, "Error",
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
                QMessageBox.information(None, "Error",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                file = self.lineEdit_filepath.text()
                df = pd.read_csv(file)
                fileName_cpds, _ = QFileDialog.getOpenFileName(None, "Load File with Plate_WELL and CPD_ID",
                                                               "",
                                                               "CSV Files (*.csv)")
                if fileName_cpds:
                    df = pd.read_csv(file, index_col=['PlateSanofi_Well'])
                    df_withcpds = pd.read_csv(fileName_cpds, low_memory=False)
                    self.lineEdit_filepath.setText(fileName_cpds)
                    model = PandasModel(df_withcpds.head(1000))
                    self.tableView_dataframe.setModel(model)
                    df_withcpds = pd.read_csv(fileName_cpds, low_memory=False)
                    self.lineEdit_filepath.setText(fileName_cpds)
                    model = PandasModel(df_withcpds.head(1000))
                    self.tableView_dataframe.setModel(model)
                    df_withcpds = pd.read_csv(fileName_cpds, index_col=['Plate_Well'], low_memory=False)
                    df['CPD_ID'] = df_withcpds['X_CPD_ID']
                    df['BATCH_ID'] = df_withcpds['X_BATCH_ID']
                    df['CPDid_BATCHid'] = df_withcpds['X_CPD_ID'] + '_' + df_withcpds['X_BATCH_ID']
                    if 'Concentration' in df_withcpds:
                        df['Concentration'] = df_withcpds['Concentration']
                    if 'Concentration' not in df_withcpds:
                        df['Concentration'] = '3'
                    if 'Concentration (uM)' not in df_withcpds:
                        df['Concentration'] = '3'
                    if 'Concentration (uM)' in df_withcpds:
                        df['Concentration'] = df_withcpds['Concentration (uM)']
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                    self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                    QMessageBox.information(None, "File linked",
                                            "Successfully linked and saved the files!",
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
                                            "Column 'Well' does not exist in the file\nYou cannot link your file.",
                                            QMessageBox.Ok)
                if 'Well' in df.columns:
                    fileName_cpds, _ = QFileDialog.getOpenFileName(None,
                                                                   "Load File with Platebarcode, CPD_ID and BATCH_ID and Concentration (uM)",
                                                                   "",
                                                                   "CSV Files (*.csv)")
                    if fileName_cpds:
                        df_cpds = pd.read_csv(fileName_cpds)
                        if 'Well' not in df_cpds.columns and 'WELL' not in df_cpds.columns:
                            QMessageBox.information(None, "Error",
                                                    "Column 'Well' or 'WELL does not exist in the file.\nNo file to link.",
                                                    QMessageBox.Ok)
                        if 'Well' in df_cpds.columns and 'WELL' not in df_cpds.columns:
                            if ((len(df_cpds) - df_cpds['Well'].nunique()) != 0):
                                QMessageBox.information(None, 'Error', "Values in column 'Well' are not unique.\nYou cannot link the file.",
                                                                   QMessageBox.Ok)
                            if ((len(df_cpds) - df_cpds['Well'].nunique()) ==0):
                                df = pd.read_csv(file, index_col=['Well'])
                                if 'X_CPD_ID' in df_cpds.columns and 'X_BATCH_ID' in df_cpds.columns:
                                    df_cpds = pd.read_csv(fileName_cpds, index_col=['Well'])
                                    df['CPD_ID'] = df_cpds['X_CPD_ID']
                                    df['BATCH_ID'] = df_cpds['X_BATCH_ID']
                                    df['CPDid_BATCHid'] = df_cpds['X_CPD_ID'] + '_' + df_cpds['X_BATCH_ID']
                                    if 'Concentration' not in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = '0'
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration' in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration (uM)' in df_cpds.columns and 'Concentration' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration (uM)']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                if 'CPD_ID' in df_cpds.columns and 'BATCH_ID' in df_cpds.columns:
                                    df_cpds = pd.read_csv(fileName_cpds, index_col=['Well'])
                                    df['CPD_ID'] = df_cpds['CPD_ID']
                                    df['BATCH_ID'] = df_cpds['BATCH_ID']
                                    df['CPDid_BATCHid'] = df_cpds['CPD_ID'] + '_' + df_cpds['BATCH_ID']
                                    if 'Concentration' not in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = '0'
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration' in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration (uM)' in df_cpds.columns and 'Concentration' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration (uM)']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)


                        if 'WELL' in df_cpds.columns and 'Well' not in df_cpds.columns:
                            if ((len(df_cpds) - df_cpds['WELL'].nunique())!= 0):
                                QMessageBox.information(None, 'Error',
                                                        "Values in column 'WELL' are not unique.\nYou cannot link the file.",
                                                        QMessageBox.Ok)
                            if ((len(df_cpds) - df_cpds['WELL'].nunique()) ==0):
                                df = pd.read_csv(file, index_col=['Well'])
                                if 'X_CPD_ID' in df_cpds.columns and 'X_BATCH_ID' in df_cpds.columns:
                                    df_cpds = pd.read_csv(fileName_cpds, index_col=['Well'])
                                    df['CPD_ID'] = df_cpds['X_CPD_ID']
                                    df['BATCH_ID'] = df_cpds['X_BATCH_ID']
                                    df['CPDid_BATCHid'] = df_cpds['X_CPD_ID'] + '_' + df_cpds['X_BATCH_ID']
                                    if 'Concentration' not in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = '0'
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration' in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration (uM)' in df_cpds.columns and 'Concentration' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration (uM)']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)

                                if 'CPD_ID' in df_cpds.columns and 'BATCH_ID' in df_cpds.columns:
                                    df_cpds = pd.read_csv(fileName_cpds, index_col=['Well'])
                                    df['CPD_ID'] = df_cpds['CPD_ID']
                                    df['BATCH_ID'] = df_cpds['BATCH_ID']
                                    df['CPDid_BATCHid'] = df_cpds['CPD_ID'] + '_' + df_cpds['BATCH_ID']
                                    if 'Concentration' not in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = '0'
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration' in df_cpds.columns and 'Concentration (uM)' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)
                                    if 'Concentration (uM)' in df_cpds.columns and 'Concentration' not in df_cpds.columns:
                                        df['Concentration'] = df_cpds['Concentration (uM)']
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                        QMessageBox.information(None, "File linked",
                                                                "Successfully linked and saved the files!",
                                                                QMessageBox.Ok)

                        if 'WELL' in df_cpds.columns and 'Well' in df_cpds.columns:
                            QMessageBox.information(None, 'Error',
                                                    "You cannot have columns 'WELL' and 'Well' in the same file.\nNo file to link.",
                                                    QMessageBox.Ok)

            self.comboBox_linkfileby.setCurrentText('Link file by')

        if (value_ == 'PLATEBARCODE'):
            file_PLATEBARCODE = self.lineEdit_filepath.text()
            if file_PLATEBARCODE == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df_PLATEBARCODE = pd.read_csv(file_PLATEBARCODE)
                if 'PLATEBARCODE' not in df_PLATEBARCODE.columns :
                    QMessageBox.information(None, "Error ",
                                            "Column 'PLATEBARCODE' does not exist in the file\nYou cannot link your file.",
                                            QMessageBox.Ok)
                if 'PLATEBARCODE' in df_PLATEBARCODE.columns:
                    df_PLATEBARCODE = pd.read_csv(file_PLATEBARCODE, index_col=['PLATEBARCODE'])
                    fileName_Barcode_CompoundPlate, _ = QFileDialog.getOpenFileName(None,
                                                                   "Load File with Barcode_CompoundPlate",
                                                                   "",
                                                                   "CSV Files (*.csv)")
                    if fileName_Barcode_CompoundPlate:
                        df_Barcode_CompoundPlate = pd.read_csv(fileName_Barcode_CompoundPlate)
                        if 'Barcode_CompoundPlate' not in df_Barcode_CompoundPlate.columns:
                            QMessageBox.information(None, "Error ",
                                                    "Column 'Barcode_CompoundPlate' does not exist in the file\nYou cannot link your file.",
                                                    QMessageBox.Ok)
                        if 'Barcode_CompoundPlate' in df_Barcode_CompoundPlate.columns:
                            df_Barcode_CompoundPlate = pd.read_csv(fileName_Barcode_CompoundPlate,
                                                                   index_col='Barcode_CompoundPlate')
                            df_PLATEBARCODE['Barcode_AssayPlate'] = df_Barcode_CompoundPlate['Barcode_AssayPlate']
                            t1 = os.path.dirname(file_PLATEBARCODE)
                            file_name1 = os.path.splitext(os.path.basename(file_PLATEBARCODE))[0]
                            df_PLATEBARCODE.to_csv(t1 + '\\' + 'CPDs_file_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'CPDs_file_' + file_name1 + '.csv')
                            self.lineEdit_filepath.setText(t1 + '/' + 'CPDs_file_' + file_name1 + '.csv')
                            QMessageBox.information(None, "File linked",
                                                    "Successfully linked and saved the file!",
                                                    QMessageBox.Ok)
            self.comboBox_linkfileby.setCurrentText('Link file by')

    def on_comboboxaddcolumn_changed(self, _value):
        file = self.lineEdit_filepath.text()
        if (_value == 'New column'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                df = pd.read_csv(file)
                value_entered_column, okPressed = QInputDialog.getText(None, "Enter column name to add", "Column name ",
                                                            QLineEdit.Normal, "")

                if value_entered_column in df.columns:
                    value_entered_rowval, okPressed = QInputDialog.getText(None,
                                                                           "Enter value to add to the column " + str(
                                                                               value_entered_column), "Value: ",
                                                                           QLineEdit.Normal, "")
                    new_column = str(value_entered_column)
                    if new_column in df.columns:
                        buttonReply = QMessageBox.question(None, 'Error',
                                                                           "The column " + new_column + " already exists in the file.\n"
                                                                           "Press Yes if you want to overwrite the column.\n"
                                                                           "Press No to ignore.",
                                                                           QMessageBox.Yes | QMessageBox.No,
                                                                           QMessageBox.Yes)
                        if buttonReply == QMessageBox.Yes:
                            df[new_column] = '' + value_entered_rowval + ''
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            df.to_csv(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv', index=None)
                            self.reloaddata_fromfilepath(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv')
                            self.lineEdit_filepath.setText(t1 + '/' + 'newcolumn_' + file_name1 + '.csv')
                            QMessageBox.information(None, "Column added",
                                                    "The column " + str(
                                                        value_entered_column) + " has been added to the file.",
                                                    QMessageBox.Ok)

                    if new_column not in df.columns:
                        df[new_column] = '' + value_entered_rowval + ''
                        t1 = os.path.dirname(file)
                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                        df.to_csv(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv', index=None)
                        self.reloaddata_fromfilepath(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv')
                        self.lineEdit_filepath.setText(t1 + '/' + 'newcolumn_' + file_name1 + '.csv')
                        QMessageBox.information(None, "Column added",
                                                "The column " + str(value_entered_column) + " has been added to the file.",
                                                QMessageBox.Ok)

        self.comboBox_addcolumn.setCurrentText('Add column')

    def on_comboboxdropfrom_changed(self, val):
        file = self.lineEdit_filepath.text()
        if (val == 'Order columns'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                exists = os.path.isfile(file)
                if exists:
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    header = self.select_multicolumns()
                    if len(header) == 0:
                        QMessageBox.information(None, "Error ",
                                                "You must select at least 1 column.\nNo file to save!",
                                                QMessageBox.Ok)
                    if len(header) > 0:
                        df = pd.read_csv(file)
                        df =  df[header]
                        df.to_csv(t1 + '\\' + 'ordered_' + file_name1 + '.csv', index=None)
                        self.reloaddata_fromfilepath(t1 + '\\' + 'ordered_' + file_name1 + '.csv')
                        self.lineEdit_filepath.setText(t1 + '/' + 'ordered_' + file_name1 + '.csv')
                else:
                    QMessageBox.information(None, "Error",
                                            "The loaded file does not exist.\n",
                                            QMessageBox.Ok)
        self.comboBox_dropfrom.setCurrentText('Edit rows columns')

        if (val == 'Merge 2 columns'):
            if file == "File path":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "File path":
                exists = os.path.isfile(file)
                if exists:
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    header = self.select_multicolumns()
                    if len(header) == 0:
                        QMessageBox.information(None, "Error ",
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
                            df1 = pd.read_csv(file)
                            if value_entered_column not in df1.columns:
                                if df1[header[0]].dtypes != str or df1[header[1]].dtypes != str:
                                    df1 = pd.read_csv(file, dtype={header[0]: str, header[1]: str})
                                    df1[value_entered_column] = df1[header[0]] + '_' + df1[header[1]]
                                    df1.to_csv(t1 + '\\' + 'merged_' + file_name1 + '.csv', index=None)
                                    self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + file_name1 + '.csv')
                                    self.lineEdit_filepath.setText(t1 + '/' + 'merged_' + file_name1 + '.csv')
                                if df1[header[0]].dtypes == str and df1[header[1]].dtypes == str:
                                    df1[value_entered_column] = df1[header[0]] + '_' + df1[header[1]]
                                    df1.to_csv(t1 + '\\' + 'merged_' + file_name1 + '.csv', index=None)
                                    self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + file_name1 + '.csv')
                                    self.lineEdit_filepath.setText(t1 + '/' + 'merged_' + file_name1 + '.csv')
                            df2 = pd.read_csv(file)
                            if value_entered_column in df2.columns:
                                if df2[header[0]].dtypes != str or df2[header[1]].dtypes != str:
                                    df2 = pd.read_csv(file, dtype={header[0]: str, header[1]: str})
                                    buttonReply = QMessageBox.question(None, 'Error',
                                                                       "The column " + str(
                                                                           value_entered_column) + " already exists in the file.\n"
                                                                                                   "Press Yes if you want to overwrite the column.\n"
                                                                                                   "Press No to ignore.",
                                                                       QMessageBox.Yes | QMessageBox.No,
                                                                       QMessageBox.Yes)
                                    if buttonReply == QMessageBox.Yes:
                                        df2[value_entered_column] = df2[header[0]] + '_' + df2[header[1]]
                                        t1 = os.path.dirname(file)
                                        file_name1 = os.path.splitext(os.path.basename(file))[0]
                                        df2.to_csv(t1 + '\\' + 'merged_' + file_name1 + '.csv', index=None)
                                        self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + file_name1 + '.csv')
                                        self.lineEdit_filepath.setText(t1 + '/' + 'merged_' + file_name1 + '.csv')
                                if df2[header[0]].dtypes == str and df2[header[1]].dtypes == str:
                                    buttonReply = QMessageBox.question(None, 'Error',
                                                                       "The column " + str(
                                                                           value_entered_column) + " already exists in the file.\n"
                                                                                                   "Press Yes if you want to overwrite the column.\n"
                                                                                                   "Press No to ignore.",
                                                                       QMessageBox.Yes | QMessageBox.No,
                                                                       QMessageBox.Yes)
                                    if buttonReply == QMessageBox.Yes:
                                        df2[value_entered_column] = df2[header[0]] + '_' + df2[header[1]]
                                    t1 = os.path.dirname(file)
                                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                                    df2.to_csv(t1 + '\\' + 'merged_' + file_name1 + '.csv', index=None)
                                    self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + file_name1 + '.csv')
                                    self.lineEdit_filepath.setText(t1 + '/' + 'merge_' + file_name1 + '.csv')
                else:
                    QMessageBox.information(None, "Error",
                                            "The loaded file does not exist.\n",
                                            QMessageBox.Ok)

                self.comboBox_dropfrom.setCurrentText('Edit rows columns')

        if (val == 'Extract value from rows'):
            if file == 'File path':
                QMessageBox.information(None, "Error",
                                        "Please load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                header = self.select_column()
                if not header:
                    QMessageBox.information(None, "Error ",
                                            "You must select a column first.\nTry again",
                                            QMessageBox.Ok)
                if header:
                    df = pd.read_csv(file)
                    df['Plate_Sanofi'] = df['Plate'].str.split('_').str[1]
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'file_PlateWell' + file_name1 + '.csv', index=None)
                    self.reloaddata_fromfilepath(t1 + '\\' + 'file_PlateWell' + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '/' + 'file_PlateWell' + file_name1 + '.csv')

            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

        if (val == 'Rename value in rows'):
            if file == 'File path':
                QMessageBox.information(None, "Error",
                                        "Please load a file first.",
                                        QMessageBox.Ok)
            if file != 'File path':
                self.openwindow_renamevalues()
            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

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
                            t1 = os.path.dirname(file)
                            file_name1 = os.path.splitext(os.path.basename(file))[0]
                            df.to_csv(t1 + '\\' + '_renamedcolumn_' + header + file_name1 + '.csv', index=None)
                            self.lineEdit_filepath.setText(t1 + '//' + '_renamedcolumn_' + header + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + '_renamedcolumn_' + header + file_name1 + '.csv')

            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

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
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    d_dropped = df.drop(header, axis=1)
                    d_dropped.to_csv(t1 + '\\' + 'droppedcol_' + file_name1 + '.csv', index=None)
                    self.reloaddata_fromfilepath(t1 + '//' + 'droppedcol_' + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '//' + 'droppedcol_' + file_name1 + '.csv')
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
            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

        if (val == 'Drop/ Rename/ Keep values in rows'):
            if file == 'File path':
                    QMessageBox.information(None, "Error ",
                                            "No loaded file.\nPlease load a file first.",
                                            QMessageBox.Ok)
            if file != 'File path':
                self.openwindow_form_checkboxes()
            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

    def get_filename_path(self):
        file = self.lineEdit_filepath.text()
        return file

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
                                            "No duplicated values have been detected in the column " + str(
                                                header) + "!\nNo file to save.",
                                            QMessageBox.Ok)
                if (len(df_duplicated) > 1):
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    QMessageBox.information(None, "Duplicated values ",
                                            str(len(
                                                df_duplicated)) + " duplicated values have been detected in the column " + str(
                                                header) +
                                            ".\nSuccessfully saved the file!",
                                            QMessageBox.Ok)
                    df_duplicated.to_csv(t1 + '\\' + 'duplicatedValuesfrom_' + header + file_name1 +'.csv', index=None)
                    self.setPlateWellText_intblview(df_duplicated)
                    # t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv'
                    self.reloaddata_fromfilepath(t1 + '//' +  'duplicatedValuesfrom_' + header + file_name1 +'.csv')
                    self.lineEdit_filepath.setText(t1 + '//' +  'duplicatedValuesfrom_' + header + file_name1 +'.csv')

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
                                            "You have no duplicated values in the column " + str(header),
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
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' +  'afterdropduplicatesfrom_' + header + '_' + file_name1 + '.csv', index=None)
                    self.setPlateWellText_intblview(df)
                    self.lineEdit_filepath.setText(
                        t1 + '/' + 'afterdropduplicatesfrom_' + header + '_' + file_name1 + '.csv')
                    self.reloaddata_fromfilepath(
                        t1 + '//' + 'afterdropduplicatesfrom_' + header + '_' + file_name1 + '.csv')
                    QMessageBox.information(None, "Dropped duplicates",
                                            str(len_init - len(df)) + " value has been dropped from " + str(
                                                header) + "\nYour file has been saved",
                                            QMessageBox.Ok)
            self.comboBox_duplicates.setCurrentText('Duplicates')

    def getncpdsbatches(self, dataframe):
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'X_CPD_ID' not in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'CPD_ID' in dataframe.columns and 'BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['CPD_ID'].nunique()) + ' unique CPD_ID')
            self.label_nbbatchid.setText('No BATCH_ID')
        if 'X_CPD_ID' in dataframe.columns and 'X_BATCH_ID' not in dataframe.columns:
            self.label_nbcpdid.setText(str(dataframe['X_CPD_ID'].nunique()) + ' unique X_CPD_ID')
            self.label_nbbatchid.setText('No X_BATCH_ID')
        if 'CPD_ID' not in dataframe.columns and 'BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['BATCH_ID'].nunique()) + ' unique BATCH_ID')
        if 'X_CPD_ID' not in dataframe.columns and 'X_BATCH_ID' in dataframe.columns:
            self.label_nbcpdid.setText('No X_CPD_ID')
            self.label_nbbatchid.setText(str(dataframe['X_BATCH_ID'].nunique()) + ' unique X_BATCH_ID')

    def on_addclasses_clicked(self, t):
        self.openwindow_addclasses()

    def on_loadFile_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File",
                                                  "",
                                                  "CSV Files (*.csv)")
        if fileName:
            exists = os.path.isfile(fileName)
            if exists:
                self.lineEdit_filepath.setText(fileName)
                df = pd.read_csv(fileName, low_memory=False)
                model = PandasModel(df.head(1000))
                self.tableView_dataframe.setModel(model)

                if ('Plate' in df.columns and 'Well' in df.columns):
                    self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                    self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                    self.getncpdsbatches(df)

                if ('Plate' in df.columns and 'WELL' in df.columns):
                    self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                    self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
                    self.getncpdsbatches(df)

                if ('Plate' not in df.columns and 'Well' not in df.columns):
                    self.lineEdit_plate.setText('No plate')
                    self.lineEdit_well.setText('No wells')
                    self.getncpdsbatches(df)

                if ('Plate' not in df.columns and 'Well' in df.columns):
                    self.lineEdit_plate.setText('No plate')
                    self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                    self.getncpdsbatches(df)

                if ('Plate' not in df.columns and 'WELL' in df.columns):
                    self.lineEdit_plate.setText('No plate')
                    self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
                    self.getncpdsbatches(df)

                if ('Plate' in df.columns and 'Well' not in df.columns):
                    self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                    self.lineEdit_well.setText('No wells')
                    self.getncpdsbatches(df)
            else:
                QMessageBox.information(None, "Error",
                                        "The loaded file does not exist.\n",
                                        QMessageBox.Ok)
    def on_textedit_clicked(self):
        self.text_path = str(self.lineEdit_filepath.text())
        return self.text_path

    def on_concatenatefiles_clicked(self):
        filter = "CSV (*.csv)"
        filename, _ = QFileDialog.getOpenFileNames(None, "Select CSV files to concatenate",
                                                   "",
                                                   filter)
        if filename:
            t1 = os.path.dirname(filename[0])
            file_name1 = os.path.splitext(os.path.basename(filename[0]))[0]
            list_files = []
            for i in filename:
                df = pd.read_csv(i)
                list_files.append(df)
                b = pd.DataFrame(pd.concat(list_files, axis=0))
                b.to_csv(t1 + '\\' + 'Concatenated_File.csv', index=None)
                self.reloaddata_fromfilepath(t1 + '\\'  + 'Concatenated_File.csv')
                self.lineEdit_filepath.setText(t1 + '/' + 'Concatenated_File.csv')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_loadDataframe = QtWidgets.QWidget()
    ui = Ui_Form_loadDataframe()
    ui.setupUi(Form_loadDataframe)
    Form_loadDataframe.show()
    sys.exit(app.exec_())

