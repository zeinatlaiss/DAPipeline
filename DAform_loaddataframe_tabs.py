from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PyQt5.QtWidgets import *
import pandas as pd
from DAform_checkboxes_dropfromrows import Ui_Form_CheckBoxes
from DAform_table_addclasses import Ui_form_table_addclasses
from DAform_checkboxes_editincolumns import Ui_Form_editcolumns
from DApandaswidget import PandasModel
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_loaddataframe_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_loadDataframe_tabs(object):
    def openwindow_form_checkboxes(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_CheckBoxes()
        self.ui.setupUi(self.window)
        # Form_loadDataframe.hide()
        self.ui.lineEdit_filepath_checkboxes.setText(self.lineEdit_filepath.text())
        self.load_ddf()
        self.ui.loadFile()
        self.window.show()

    def openwindow_addclasses(self):
        self.window = QtWidgets.QMainWindow()
        self.ui1 = Ui_form_table_addclasses()
        self.ui1.setupUi(self.window)
        self.ui1.lineEdit_filepathfromdataframe.setText(self.lineEdit_filepath.text())
        self.ui1.loadFile()
        # Form_loadDataframe.hide()
        self.window.show()

    def openwindow_form_checkboxes_editincolumns(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_Form_editcolumns()
        self.ui2.setupUi(self.window)
        self.ui2.lineedit_file_path_to_edit = self.lineEdit_filepath.text()
        self.ui2.tableView_dataframe_to_edit = self.tableView_dataframe
        self.ui2.t1_new = os.path.dirname(self.lineEdit_filepath.text())
        self.ui2.file_name1_new = os.path.splitext(os.path.basename(self.ui2.lineedit_file_path_to_edit))[0]
        # self.ui2.lineedit_to_read = self.lineEdit_filepath.text()
        self.ui2.lineEdit_plate_new = self.lineEdit_plate
        self.ui2.lineEdit_well_new = self.lineEdit_well
        self.ui2.label_nbcpdid_new = self.label_nbcpdid
        self.ui2.label_nbbatchid_new = self.label_nbbatchid
        self.lineEdit_filepath.setText(self.ui2.t1_new + '/' + self.ui2.file_name1_new + '.csv')
        # self.ui.loadFile()
        self.window.show()

    def openwindow_form_checkboxes_editinrows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui3 = Ui_Form_CheckBoxes()
        self.ui3.setupUi(self.window)
        self.ui3.lineedit_file_path_to_edit = self.lineEdit_filepath.text()
        self.ui3.tableView_dataframe_to_edit = self.tableView_dataframe
        self.ui3.t1_rows = os.path.dirname(self.lineEdit_filepath.text())
        self.ui3.file_name1_rows = os.path.splitext(os.path.basename(self.ui3.lineedit_file_path_to_edit))[0]
        # self.ui3.lineedit_to_read = self.lineEdit_filepath.text()
        self.ui3.lineEdit_plate_rows = self.lineEdit_plate
        self.ui3.lineEdit_well_rows = self.lineEdit_well
        self.ui3.label_nbcpdid_rows = self.label_nbcpdid
        self.ui3.label_nbbatchid_rows = self.label_nbbatchid
        self.lineEdit_filepath.setText(self.ui3.t1_rows + '/' + self.ui3.file_name1_rows + '.csv')
        # self.ui.loadFile()
        self.window.show()

    def setupUi(self, Form_loadDataframe_tabs):
        Form_loadDataframe_tabs.setObjectName("Form_loadDataframe_tabs")
        Form_loadDataframe_tabs.setWindowModality(QtCore.Qt.WindowModal)
        Form_loadDataframe_tabs.setEnabled(True)
        Form_loadDataframe_tabs.resize(1524, 1066)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_loadDataframe_tabs.sizePolicy().hasHeightForWidth())
        Form_loadDataframe_tabs.setSizePolicy(sizePolicy)
        Form_loadDataframe_tabs.setSizeIncrement(QtCore.QSize(25, 25))
        Form_loadDataframe_tabs.setStyleSheet("background-color: rgb(222, 241, 255);")
        self.tabWidget_filestatistics = QtWidgets.QTabWidget(Form_loadDataframe_tabs)
        self.tabWidget_filestatistics.setGeometry(QtCore.QRect(30, 30, 1481, 1031))
        self.tabWidget_filestatistics.setStyleSheet("background-color: rgb(229, 241, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";")
        self.tabWidget_filestatistics.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_filestatistics.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_filestatistics.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget_filestatistics.setMovable(True)
        self.tabWidget_filestatistics.setObjectName("tabWidget_filestatistics")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")
        self.pushButton_addclasses = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_addclasses.setGeometry(QtCore.QRect(1210, 900, 101, 31))
        self.pushButton_addclasses.setStyleSheet("background-color: rgb(220, 236, 255);")
        self.pushButton_addclasses.setObjectName("pushButton_addclasses")
        self.pushButton_onlinkfiles = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_onlinkfiles.setGeometry(QtCore.QRect(1080, 900, 111, 31))
        self.pushButton_onlinkfiles.setStyleSheet("background-color: rgb(220, 236, 255);")
        self.pushButton_onlinkfiles.setObjectName("pushButton_onlinkfiles")
        self.pushButton_concatfiles = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_concatfiles.setGeometry(QtCore.QRect(920, 900, 141, 31))
        self.pushButton_concatfiles.setStyleSheet("background-color: rgb(220, 236, 255);")
        self.pushButton_concatfiles.setObjectName("pushButton_concatfiles")
        self.pushButton_loadfile = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_loadfile.setGeometry(QtCore.QRect(1350, 900, 111, 31))
        self.pushButton_loadfile.setMouseTracking(False)
        self.pushButton_loadfile.setAutoFillBackground(False)
        self.pushButton_loadfile.setStyleSheet("background-color: rgb(220, 236, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"")
        self.pushButton_loadfile.setObjectName("pushButton_loadfile")
        self.tabWidget_filestatistics.addTab(self.tab_file, "")
        self.tab_edit = QtWidgets.QWidget()
        self.tab_edit.setObjectName("tab_edit")
        self.pushButton_editinrows = QtWidgets.QPushButton(self.tab_edit)
        self.pushButton_editinrows.setGeometry(QtCore.QRect(1230, 900, 100, 31))
        self.pushButton_editinrows.setObjectName("pushButton_editinrows")
        self.pushButton_editincolumns = QtWidgets.QPushButton(self.tab_edit)
        self.pushButton_editincolumns.setGeometry(QtCore.QRect(1350, 900, 111, 31))
        self.pushButton_editincolumns.setObjectName("pushButton_editincolumns")
        self.comboBox_duplicates = QtWidgets.QComboBox(self.tab_edit)
        self.comboBox_duplicates.setGeometry(QtCore.QRect(1230, 940, 231, 31))
        self.comboBox_duplicates.setObjectName("comboBox_duplicates")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.comboBox_duplicates.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_edit, "")
        self.tab_normalisation = QtWidgets.QWidget()
        self.tab_normalisation.setObjectName("tab_normalisation")
        self.comboBox_normalize = QtWidgets.QComboBox(self.tab_normalisation)
        self.comboBox_normalize.setGeometry(QtCore.QRect(1270, 900, 191, 31))
        self.comboBox_normalize.setObjectName("comboBox_normalize")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_normalisation, "")
        self.tab_statistics = QtWidgets.QWidget()
        self.tab_statistics.setObjectName("tab_statistics")
        self.comboBox_statistics = QtWidgets.QComboBox(self.tab_statistics)
        self.comboBox_statistics.setGeometry(QtCore.QRect(890, 900, 271, 41))
        self.comboBox_statistics.setObjectName("comboBox_statistics")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_statistics.addItem("")
        self.comboBox_aggregate = QtWidgets.QComboBox(self.tab_statistics)
        self.comboBox_aggregate.setGeometry(QtCore.QRect(1190, 900, 271, 41))
        self.comboBox_aggregate.setObjectName("comboBox_aggregate")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.comboBox_aggregate.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_statistics, "")
        self.tab_detectvalues = QtWidgets.QWidget()
        self.tab_detectvalues.setObjectName("tab_detectvalues")
        self.comboBox_extracthits = QtWidgets.QComboBox(self.tab_detectvalues)
        self.comboBox_extracthits.setGeometry(QtCore.QRect(1190, 900, 271, 31))
        self.comboBox_extracthits.setObjectName("comboBox_extracthits")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.comboBox_extracthits.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_detectvalues, "")
        self.tab_detectoutliers = QtWidgets.QWidget()
        self.tab_detectoutliers.setObjectName("tab_detectoutliers")
        self.comboBox_removeoutliers = QtWidgets.QComboBox(self.tab_detectoutliers)
        self.comboBox_removeoutliers.setGeometry(QtCore.QRect(1190, 900, 271, 31))
        self.comboBox_removeoutliers.setObjectName("comboBox_removeoutliers")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.comboBox_removeoutliers.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_detectoutliers, "")
        self.tab_machinelearning = QtWidgets.QWidget()
        self.tab_machinelearning.setObjectName("tab_machinelearning")
        self.comboBox_machinelearning = QtWidgets.QComboBox(self.tab_machinelearning)
        self.comboBox_machinelearning.setGeometry(QtCore.QRect(1290, 900, 171, 31))
        self.comboBox_machinelearning.setObjectName("comboBox_machinelearning")
        self.comboBox_machinelearning.addItem("")
        self.comboBox_machinelearning.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_machinelearning, "")
        self.tab_deeplearning = QtWidgets.QWidget()
        self.tab_deeplearning.setEnabled(False)
        self.tab_deeplearning.setObjectName("tab_deeplearning")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 900, 80, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton_3.setGeometry(QtCore.QRect(980, 900, 80, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton_4.setGeometry(QtCore.QRect(1080, 900, 80, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton.setGeometry(QtCore.QRect(1180, 900, 80, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton_5.setGeometry(QtCore.QRect(1280, 900, 80, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_deeplearning)
        self.pushButton_6.setGeometry(QtCore.QRect(1380, 900, 80, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_filestatistics.addTab(self.tab_deeplearning, "")
        self.tab_plot = QtWidgets.QWidget()
        self.tab_plot.setObjectName("tab_plot")
        self.comboBox_plot = QtWidgets.QComboBox(self.tab_plot)
        self.comboBox_plot.setGeometry(QtCore.QRect(1290, 900, 171, 31))
        self.comboBox_plot.setObjectName("comboBox_plot")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.tabWidget_filestatistics.addTab(self.tab_plot, "")
        self.label_nbcpdid = QtWidgets.QLabel(Form_loadDataframe_tabs)
        self.label_nbcpdid.setGeometry(QtCore.QRect(1200, 70, 141, 20))
        self.label_nbcpdid.setAutoFillBackground(False)
        self.label_nbcpdid.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(229, 241, 255);")
        self.label_nbcpdid.setText("")
        self.label_nbcpdid.setObjectName("label_nbcpdid")
        self.label_nbbatchid = QtWidgets.QLabel(Form_loadDataframe_tabs)
        self.label_nbbatchid.setGeometry(QtCore.QRect(1350, 70, 141, 20))
        self.label_nbbatchid.setAutoFillBackground(False)
        self.label_nbbatchid.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(229, 241, 255);")
        self.label_nbbatchid.setText("")
        self.label_nbbatchid.setObjectName("label_nbbatchid")
        self.lineEdit_well = QtWidgets.QLabel(Form_loadDataframe_tabs)
        self.lineEdit_well.setGeometry(QtCore.QRect(1050, 70, 141, 20))
        self.lineEdit_well.setAutoFillBackground(False)
        self.lineEdit_well.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(229, 241, 255);")
        self.lineEdit_well.setText("")
        self.lineEdit_well.setObjectName("lineEdit_well")
        self.lineEdit_filepath = QtWidgets.QLineEdit(Form_loadDataframe_tabs)
        self.lineEdit_filepath.setEnabled(True)
        self.lineEdit_filepath.setGeometry(QtCore.QRect(40, 70, 821, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lineEdit_filepath.setFont(font)
        self.lineEdit_filepath.setAutoFillBackground(False)
        self.lineEdit_filepath.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(229, 241, 255);")
        self.lineEdit_filepath.setFrame(False)
        self.lineEdit_filepath.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_filepath.setReadOnly(True)
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.lineEdit_plate = QtWidgets.QLabel(Form_loadDataframe_tabs)
        self.lineEdit_plate.setGeometry(QtCore.QRect(900, 70, 141, 21))
        self.lineEdit_plate.setAutoFillBackground(False)
        self.lineEdit_plate.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(229, 241, 255);")
        self.lineEdit_plate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineEdit_plate.setText("")
        self.lineEdit_plate.setObjectName("lineEdit_plate")
        self.tableView_dataframe = QtWidgets.QTableView(Form_loadDataframe_tabs)
        self.tableView_dataframe.setGeometry(QtCore.QRect(40, 120, 1460, 800))
        self.tableView_dataframe.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(157, 157, 157);\n"
"color: rgb(24, 32, 177);\n"
"background-color: rgb(220, 236, 255);")
        self.tableView_dataframe.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_dataframe.setDragEnabled(True)
        self.tableView_dataframe.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableView_dataframe.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView_dataframe.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_dataframe.setSortingEnabled(True)
        self.tableView_dataframe.setObjectName("tableView_dataframe")

        self.lineEdit_filepath.setText('  ')
        self.pushButton_loadfile.clicked.connect(self.on_loadFile_clicked)
        self.pushButton_onlinkfiles.clicked.connect(self.on_linkfiles_clicked)
        self.pushButton_concatfiles.clicked.connect(self.on_concatenatefiles_clicked)
        self.pushButton_addclasses.clicked.connect(self.on_addclasses_clicked)
        self.pushButton_editincolumns.clicked.connect(self.on_editcolumns_clicked)
        self.pushButton_editinrows.clicked.connect(self.on_editrows_clicked)
        self.comboBox_duplicates.currentTextChanged.connect(self.on_comboboxduplicates_changed)
        self.comboBox_extracthits.currentTextChanged.connect(self.on_comboboxactivecompounds_changed)
        self.comboBox_removeoutliers.currentTextChanged.connect(self.on_comboboxremoveoutliers_changed)
        self.comboBox_machinelearning.currentTextChanged.connect(self.on_machinelearning_changed)
        self.comboBox_statistics.currentTextChanged.connect(self.on_statistics_changed)
        self.comboBox_normalize.currentTextChanged.connect(self.on_comboboxnormalize_changed)
        self.comboBox_plot.currentTextChanged.connect(self.on_plot_changed)
        self.comboBox_aggregate.currentTextChanged.connect(self.on_comboboxaggregate_changed)

        self.retranslateUi(Form_loadDataframe_tabs)
        self.tabWidget_filestatistics.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_loadDataframe_tabs)

    def retranslateUi(self, Form_loadDataframe_tabs):
        _translate = QtCore.QCoreApplication.translate
        Form_loadDataframe_tabs.setWindowTitle(_translate("Form_loadDataframe_tabs", "DAPipeline"))
        self.pushButton_addclasses.setText(_translate("Form_loadDataframe_tabs", "Add classes"))
        self.pushButton_onlinkfiles.setText(_translate("Form_loadDataframe_tabs", "Link 2 files"))
        self.pushButton_concatfiles.setText(_translate("Form_loadDataframe_tabs", "Concatenate Files"))
        self.pushButton_loadfile.setText(_translate("Form_loadDataframe_tabs", "Load File"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_file), _translate("Form_loadDataframe_tabs", "File"))
        self.pushButton_editinrows.setText(_translate("Form_loadDataframe_tabs", "Edit in rows"))
        self.pushButton_editincolumns.setText(_translate("Form_loadDataframe_tabs", "Edit in columns"))
        self.comboBox_duplicates.setItemText(0, _translate("Form_loadDataframe_tabs", "Duplicates"))
        self.comboBox_duplicates.setItemText(1, _translate("Form_loadDataframe_tabs", "Get duplicated values"))
        self.comboBox_duplicates.setItemText(2, _translate("Form_loadDataframe_tabs", "Number of duplicates"))
        self.comboBox_duplicates.setItemText(3, _translate("Form_loadDataframe_tabs", "Drop duplicated values"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_edit), _translate("Form_loadDataframe_tabs", "Edit"))
        self.comboBox_normalize.setItemText(0, _translate("Form_loadDataframe_tabs", "Normalise"))
        self.comboBox_normalize.setItemText(1, _translate("Form_loadDataframe_tabs", "Median"))
        self.comboBox_normalize.setItemText(2, _translate("Form_loadDataframe_tabs", "Mean"))
        self.comboBox_normalize.setItemText(3, _translate("Form_loadDataframe_tabs", "Min-Max"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_normalisation), _translate("Form_loadDataframe_tabs", "Normalise"))
        self.comboBox_statistics.setItemText(0, _translate("Form_loadDataframe_tabs", "Statistics"))
        self.comboBox_statistics.setItemText(1, _translate("Form_loadDataframe_tabs", "Z factor & Robust Z factor"))
        self.comboBox_statistics.setItemText(2, _translate("Form_loadDataframe_tabs", "Mean and STD"))
        self.comboBox_statistics.setItemText(3, _translate("Form_loadDataframe_tabs", "Intersection"))
        self.comboBox_statistics.setItemText(4, _translate("Form_loadDataframe_tabs", "Union"))
        self.comboBox_statistics.setItemText(5, _translate("Form_loadDataframe_tabs", "Merge 2 files"))
        self.comboBox_aggregate.setItemText(0, _translate("Form_loadDataframe_tabs", "Aggregate"))
        self.comboBox_aggregate.setItemText(1, _translate("Form_loadDataframe_tabs", "Aggregate - Min Max Mean Sum STD"))
        self.comboBox_aggregate.setItemText(2, _translate("Form_loadDataframe_tabs", "Aggregate grouping by"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_statistics), _translate("Form_loadDataframe_tabs", "Statistics"))
        self.comboBox_extracthits.setItemText(0, _translate("Form_loadDataframe_tabs", "Detect values"))
        self.comboBox_extracthits.setItemText(1, _translate("Form_loadDataframe_tabs", "> mean + value * sigma"))
        self.comboBox_extracthits.setItemText(2, _translate("Form_loadDataframe_tabs", "> mean - value * sigma"))
        self.comboBox_extracthits.setItemText(3, _translate("Form_loadDataframe_tabs", "< mean - value * sigma"))
        self.comboBox_extracthits.setItemText(4, _translate("Form_loadDataframe_tabs", "> mean"))
        self.comboBox_extracthits.setItemText(5, _translate("Form_loadDataframe_tabs", "< mean"))
        self.comboBox_extracthits.setItemText(6, _translate("Form_loadDataframe_tabs", "> value"))
        self.comboBox_extracthits.setItemText(7, _translate("Form_loadDataframe_tabs", "< value"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_detectvalues), _translate("Form_loadDataframe_tabs", "Detect values"))
        self.comboBox_removeoutliers.setItemText(0, _translate("Form_loadDataframe_tabs", "Remove outliers"))
        self.comboBox_removeoutliers.setItemText(1, _translate("Form_loadDataframe_tabs", "Mean-value*sigma <value< Mean+value*sigma"))
        self.comboBox_removeoutliers.setItemText(2, _translate("Form_loadDataframe_tabs", "> mean"))
        self.comboBox_removeoutliers.setItemText(3, _translate("Form_loadDataframe_tabs", "> value"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_detectoutliers), _translate("Form_loadDataframe_tabs", "Detect outliers"))
        self.comboBox_machinelearning.setItemText(0, _translate("Form_loadDataframe_tabs", "Machine learning"))
        self.comboBox_machinelearning.setItemText(1, _translate("Form_loadDataframe_tabs", "LDA"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_machinelearning), _translate("Form_loadDataframe_tabs", "Machine Learning"))
        self.pushButton_2.setText(_translate("Form_loadDataframe_tabs", "Label"))
        self.pushButton_3.setText(_translate("Form_loadDataframe_tabs", "Pickle"))
        self.pushButton_4.setText(_translate("Form_loadDataframe_tabs", "Load pickle"))
        self.pushButton.setText(_translate("Form_loadDataframe_tabs", "Train"))
        self.pushButton_5.setText(_translate("Form_loadDataframe_tabs", "Predict"))
        self.pushButton_6.setText(_translate("Form_loadDataframe_tabs", "Validate"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_deeplearning), _translate("Form_loadDataframe_tabs", "Deep learning"))
        self.comboBox_plot.setItemText(0, _translate("Form_loadDataframe_tabs", "Plot"))
        self.comboBox_plot.setItemText(1, _translate("Form_loadDataframe_tabs", "Correlation"))
        self.comboBox_plot.setItemText(2, _translate("Form_loadDataframe_tabs", "Swarm plot with error bar"))
        self.comboBox_plot.setItemText(3, _translate("Form_loadDataframe_tabs", "Swarm plot without error bar"))
        self.comboBox_plot.setItemText(4, _translate("Form_loadDataframe_tabs", "Error bar"))
        self.tabWidget_filestatistics.setTabText(self.tabWidget_filestatistics.indexOf(self.tab_plot), _translate("Form_loadDataframe_tabs", "Plot"))


    def get_linedit(self):
        line_edit_main = self.lineEdit_filepath.text()
        return line_edit_main

    def on_comboboxnormalize_changed(self, value_nor):
        file = self.lineEdit_filepath.text()
        if (value_nor == "Mean"):
            if file == '  ':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != '  ':
                df2 = pd.read_csv(file)
                t1 = os.path.dirname(file)
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
                                if column != 'Class' and column != 'Concentration':
                                    max_a = np.max(grp[1].query('Class == 2')[column])
                                    max_b = np.max(grp[1].query('Class == 1')[column])
                                    if max_a < max_b:
                                        max_cp = np.mean(grp[1].query('Class == 1')[column])
                                    else:
                                        max_cp = np.mean(grp[1].query('Class == 2')[column])
                                    coeff = grp[1][column] / max_cp
                                    grp[1][column] = coeff
                                    grp[1].to_csv(t1 + '\\' + grp[0] + '.csv', index=None)
                        QMessageBox.information(None, "Mean normalisation",
                                                str(len(df2_grp[
                                                            'Plate'].nunique())) + " plates have been normalised.\nSaved files.",
                                                QMessageBox.Ok)
        self.comboBox_normalize.setCurrentText("Normalise")

        if (value_nor == "Median"):
            df2 = pd.read_csv(file)
            t1 = os.path.dirname(file)
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
            df1 = pd.read_csv(file)
            header = self.select_multicolumns()
            if (len(header)) == 0:
                QMessageBox.information(None, "Error",
                                        "You must select a column to apply the merge." + "\nNo file to save.",
                                        QMessageBox.Ok)
            if (len(header)) > 0:
                fileName2, _ = QFileDialog.getOpenFileName(None, "Load 2nd file to apply the merge",
                                                           "",
                                                           "CSV Files (*.csv)")
                if fileName2:
                    df2 = pd.read_csv(fileName2)
                    if header not in df2.columns:
                        QMessageBox.information(None, "Error",
                                                "Cannot merge the 2 files. The column " + str(
                                                    header) + " does not exist in the 2nd file." + "\nNo file to save.",
                                                QMessageBox.Ok)
                    if header in df2.columns:
                        df2 = pd.read_csv(fileName2)
                        mergedStuff = pd.merge(df1, df2, on=[header], how='inner')
                        if len(mergedStuff) == 0:
                            QMessageBox.information(None, "No merge",
                                                    "You have no values in common between the 2 files.\nNo file to save.",
                                                    QMessageBox.Ok)
                        if len(mergedStuff) > 0:
                            mergedStuff.to_csv(t1 + '\\' + 'merged_' + header + '_' + file_name1 + '.csv', index=None)
                            self.reloaddata_fromfilepath(t1 + '\\' + 'merged_' + header + '_' + file_name1 + '.csv')
                            self.lineEdit_filepath.setText(t1 + '/' + 'merged_' + header + '_' + file_name1 + '.csv')
                            QMessageBox.information(None, "Merge",
                                                    "Successfully merged the 2 files" + "\nSaved file.",
                                                    QMessageBox.Ok)

        if value_st == "Mean and STD":
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
                columnname = self.select_column()
                df = pd.read_csv(file)
                df['Check_if_String'] = [isinstance(x, str) for x in df[columnname]]
                if df['Check_if_String'].any() == True:
                    QMessageBox.information(None, "Error",
                                            "The column " + columnname + " selected contains string.\nPlease select another column.",
                                            QMessageBox.Ok)
                if df['Check_if_String'].any() == False:
                    if df[columnname].isna().any() == True or df[columnname].isnull().any() == True:
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
            if file == '  ':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != '  ':
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
                                Z_factor = 1 - ((3 * (np.std(neg_data) + np.std(pos_data))) / (
                                    np.abs(np.mean(neg_data) - np.mean(pos_data))))
                                QMessageBox.information(None, "Z factor",
                                                        "Z factor " + str(header) + " = " + str(Z_factor[header]),
                                                        QMessageBox.Ok)
                            if (df['Plate'].nunique() > 1):
                                QMessageBox.information(None, "Error ",
                                                        "The Plate is not unique.\nPlease group your data first.",
                                                        QMessageBox.Ok)
        if value_st == "Intersection":
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file:
                fileName1 = file
                file1 = pd.read_csv(fileName1)
                header1 = self.select_multicolumns()
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
                                                        "The number of intersected data = " + str(
                                                            len(inter)) + "\nSaved file.",
                                                        QMessageBox.Ok)
            self.comboBox_statistics.setCurrentText("Statistics")

        if value_st == "Union":
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file:
                fileName1 = file
                file1 = pd.read_csv(fileName1)
                header = self.select_multicolumns()
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
        # file = self.lineEdit_filepath.text()
        if value_ch == "LDA":
            QMessageBox.information(None, "Not imp",
                                    "Not implemented yet..",
                                    QMessageBox.Ok)

    def on_comboboxactivecompounds_changed(self, value_c):
        file = self.lineEdit_filepath.text()
        if (value_c == "> mean + value * sigma"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
                df_toremoveout = pd.read_csv(file)
                columnname = self.select_multicolumns()
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
                            data_dropped.to_csv(t1 + '\\' + 'Activecpds_' + file_name1 + '.csv', index=None)
                            QMessageBox.information(None, "Active coumpounds",
                                                    str(len(data_dropped)) +
                                                    " active compounds were detected using the column '" + str(
                                                        columnname) + "' when value > " + str(
                                                        meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '/' + 'Activecpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'Activecpds_' + file_name1 + '.csv')
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> mean - value * sigma"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                                                        columnname) + "' when value > " + str(
                                                        meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '/' + 'ToxCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv')
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "< mean - value * sigma"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                        df_toremoveout['Toxic_compounds'][
                            (df_toremoveout[columnname] <= meanval - value_sigma1 * stdval)] = \
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
                                                        columnname) + " when value < " + str(
                                                        meanval) + ' ' + ' + ' + str(
                                                        value_sigma1) + ' ' + ' * ' + ' ' + str(stdval)
                                                    + "\nSuccessfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(t1 + '/' + 'ToxCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + 'ToxCpds_' + file_name1 + '.csv')

            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "> mean"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                        if len(df_toremoveout) < 1:
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
                                                        columnname) + 'when value > ' + str() + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                t1 + '/' + 'ActiveCpds_' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(
                                t1 + '\\' + 'ActiveCpds_' + file_name1 + '.csv')
            self.comboBox_extracthits.setCurrentText("Detect compounds")

        if (value_c == "< mean"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
                columnname = self.select_column()
                print(columnname)
                df_toremoveout = pd.read_csv(file)
                if df_toremoveout[columnname].dtypes == str or df_toremoveout[columnname].dtypes == bool or df_toremoveout[columnname].dtypes == object:
                    print('fmjfkkd')
                if df_toremoveout[columnname].dtypes != str or df_toremoveout[columnname].dtypes != bool or df_toremoveout[columnname].dtypes != object:
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
                                df_toremoveout['Outliers'][
                                    (df_toremoveout[columnname] >= meanval + value_sigma1 * stdval) |
                                    (df_toremoveout[columnname] <= meanval - value_sigma1 * stdval)] = \
                                    df_toremoveout['Plate'] + '_' + df_toremoveout['Well']
                                data_dropped = df_toremoveout.drop(
                                    df_toremoveout[(df_toremoveout['Outliers'].str.contains('outlier'))].index)
                                if len(data_dropped) < 1:
                                    QMessageBox.information(None, "No Outliers",
                                                            "You have no outliers"
                                                            + " \nNo file to save",
                                                            QMessageBox.Ok)
                                if len(data_dropped) >= 1:
                                    t1 = os.path.dirname(file)
                                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                                    outfile = t1 + '\\' + '_WithoutOutliers_' + str(
                                        value_sigma1) + 'sigma' + file_name1 + '.csv'
                                    data_dropped.to_csv(outfile, index=None)
                                    self.lineEdit_filepath.setText(
                                        t1 + '/' + '_WithoutOutliers_' + str(
                                            value_sigma1) + 'sigma' + file_name1 + '.csv')
                                    QMessageBox.information(None, "Outliers",
                                                            str(len(df_toremoveout) - len(data_dropped)) +
                                                            " outliers have been removed using the column " + str(
                                                                columnname) + '.\n'
                                                            + "Successfully saved the file!",
                                                            QMessageBox.Ok)
                                    self.reloaddata_fromfilepath(t1 + '\\' + '_WithoutOutliers_' + str(
                                        value_sigma1) + 'sigma' + file_name1 + '.csv')
            self.comboBox_removeoutliers.setCurrentText("Remove outliers")

        if (value_cb == "> mean"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                            outfile = t1 + '\\' + '_WithoutOutliers' + file_name1 + '.csv'
                            data_dropped.to_csv(outfile, index=None)
                            QMessageBox.information(None, "Outliers",
                                                    str(len(df_toremoveout) - len(data_dropped)) +
                                                    " outliers have been removed using the column " + str(
                                                        columnname) + '.\n'
                                                    + "Successfully saved the file!",
                                                    QMessageBox.Ok)
                            self.lineEdit_filepath.setText(
                                t1 + '/' + '_WithoutOutliers' + file_name1 + '.csv')
                            self.reloaddata_fromfilepath(t1 + '\\' + '_WithoutOutliers' + file_name1 + '.csv')
            self.comboBox_removeoutliers.setCurrentText("Remove outliers")

        if (value_cb == "> value"):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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

    def load_ddf(self):
        file = self.lineEdit_filepath.text()
        df = pd.read_csv(file)
        model = PandasModel(df.head(100))
        self.tableView_dataframe.setModel(model)

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
        if 'Plate' in df.columns and 'Well' in df.columns:
            self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' unique plate')
            self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')

    def reloaddata_fromfilepath(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df.head(500))
        self.tableView_dataframe.setModel(model)
        if 'Plate' in df.columns:
            if 'Well' not in df.columns:
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText('No wells')
                self.getncpdsbatches(df)
            if 'Well' in df.columns:
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)
            if 'WELL' in df.columns:
                self.lineEdit_plate.setText(str(df['Plate'].nunique()) + ' plates')
                self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
                self.getncpdsbatches(df)

        if 'Plate' not in df.columns:
            if 'Well' not in df.columns:
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText('No wells')
                self.getncpdsbatches(df)
            if 'Well' in df.columns:
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText(str(len(df['Well'])) + ' wells')
                self.getncpdsbatches(df)
            if 'WELL' in df.columns:
                self.lineEdit_plate.setText('No plate')
                self.lineEdit_well.setText(str(len(df['WELL'])) + ' WELLs')
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
            if file == '  ':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != '  ':
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
                                            plt.scatter(df_data1['Perc_SenescentCells'].values,
                                                        df_data2['Perc_SenescentCells'].values)
                                            plt.ylim([0, 2])
                                            plt.xlim([0, 2])
                                            plt.show()
                                            QMessageBox.information(None, "Correlation ",
                                                                    "Correlation = " + str(
                                                                        np.corrcoef(df_data1[header1].values,
                                                                                    df_data2[header1])),
                                                                    QMessageBox.Ok)

        self.comboBox_plot.setCurrentText("Plot")

        if (vl == 'Swarm plot with error bar'):
            file = self.lineEdit_filepath.text()
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
            if file == "  ":
                QMessageBox.information(None, "Error",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                        self.lineEdit_filepath.setText(t2 + '/' + t3 + '/' + t1 + '/' + t1 + '_agg.csv')
                        self.reloaddata_fromfilepath(outfile)
                        QMessageBox.information(None, "Aggregate",
                                                "File has been successfully saved!",
                                                QMessageBox.Ok)
            self.comboBox_aggregate.setCurrentText("Aggregate")

    def on_linkfiles_clicked(self):
        file = self.lineEdit_filepath.text()
        if file == "  ":
            QMessageBox.information(None, "Error",
                                    "No loaded file.\nPlease load a file first.",
                                    QMessageBox.Ok)
        if file != "  ":
            file = self.lineEdit_filepath.text()
            df = pd.read_csv(file)
            header = self.select_multicolumns()
            if len(header) == 0 or len(header) > 1:
                QMessageBox.information(None, "Error",
                                        "You must select one column to link the 2 files.",
                                        QMessageBox.Ok)
            if len(header) == 1:
                boolk = df.duplicated(subset=header[0], keep=False)
                df_duplicated = df[boolk]
                if (len(df_duplicated) > 0):
                    buttonReply = QMessageBox.question(None, 'Error',
                                                       "Duplicated index in the column " + str(header) + "\n"
                                                                                                         "Press Yes if you want to continue.\n"
                                                                                                         "Press No to ignore.",
                                                       QMessageBox.Yes | QMessageBox.No,
                                                       QMessageBox.Yes)
                    if buttonReply == QMessageBox.Yes:
                        fileName_cpds, _ = QFileDialog.getOpenFileName(None, "Load File to link from",
                                                                       "",
                                                                       "CSV Files (*.csv)")
                        if fileName_cpds:
                            df = pd.read_csv(file, index_col=header)
                            self.reloaddata_fromfilepath(fileName_cpds)
                            self.lineEdit_filepath.setText(fileName_cpds)
                            df_withcpds = pd.read_csv(fileName_cpds)
                            if header[0] not in df_withcpds.columns:
                                print('s')
                            if header[0] in df_withcpds.columns:
                                boolk = df_withcpds.duplicated(subset=header[0], keep=False)
                                df_duplicated1 = df_withcpds[boolk]
                                if len(df_duplicated1) > 0:
                                    QMessageBox.information(None, "Error",
                                                            "Duplicated index. You cannot link the file.\nNo file to save.",
                                                            QMessageBox.Ok)
                                if len(df_duplicated1) == 0:
                                    df_withcpds = pd.read_csv(fileName_cpds, index_col=header)
                                    d_merged = df.merge(df_withcpds, on=header[0])
                                    # d_merged =
                                    t1 = os.path.dirname(file)
                                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                                    d_merged.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                    self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                    self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                    QMessageBox.information(None, "File linked",
                                                            "Successfully linked and saved the files!",
                                                            QMessageBox.Ok)

                if (len(df_duplicated) == 0):
                    fileName_cpds, _ = QFileDialog.getOpenFileName(None, "Load File to link from",
                                                                   "",
                                                                   "CSV Files (*.csv)")
                    if fileName_cpds:
                        df = pd.read_csv(file, index_col=header)
                        self.reloaddata_fromfilepath(fileName_cpds)
                        self.lineEdit_filepath.setText(fileName_cpds)
                        df_withcpds = pd.read_csv(fileName_cpds)
                        if header[0] not in df_withcpds.columns:
                            QMessageBox.information(None, "Error",
                                                    "The key " + str(
                                                        header) + " does not exist in the 2nd file.\nPlease select another column to link the 2 files.",
                                                    QMessageBox.Ok)
                        if header[0] in df_withcpds.columns:
                            boolk = df_withcpds.duplicated(subset=header[0], keep=False)
                            df_duplicated = df_withcpds[boolk]
                            if len(df_duplicated) > 0:
                                QMessageBox.information(None, "Error",
                                                        "You cannot link the file.\nDuplicated index in column " + str(
                                                            header),
                                                        QMessageBox.Ok)
                            if len(df_duplicated) == 0:
                                df_withcpds = pd.read_csv(fileName_cpds, index_col=header)
                                d_merged = df.merge(df_withcpds, on=header[0])
                                t1 = os.path.dirname(file)
                                file_name1 = os.path.splitext(os.path.basename(file))[0]
                                d_merged.to_csv(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                self.reloaddata_fromfilepath(t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv')
                                self.lineEdit_filepath.setText(t1 + '/' + 'LinkedFile_' + file_name1 + '.csv')
                                QMessageBox.information(None, "File linked",
                                                        "Successfully linked and saved the files!",
                                                        QMessageBox.Ok)

    def on_comboboxdropfrom_changed(self, val):
        file = self.lineEdit_filepath.text()
        if (val == 'Extract value from rows'):
            if file == '  ':
                QMessageBox.information(None, "Error",
                                        "Please load a file first.",
                                        QMessageBox.Ok)
            if file != '  ':
                header = self.select_column()
                if not header:
                    QMessageBox.information(None, "Error ",
                                            "You must select a column first.\nTry again",
                                            QMessageBox.Ok)
                if header:
                    df = pd.read_csv(file)
                    df['newcol'] = df[header].str.split('_').str[1] + '_' + df[header].str.split('_').str[
                        2]  # + '_' + df['Plate'].str.split('_').str[3]
                    t1 = os.path.dirname(file)
                    file_name1 = os.path.splitext(os.path.basename(file))[0]
                    df.to_csv(t1 + '\\' + 'PlateWell' + file_name1 + '.csv', index=None)
                    self.reloaddata_fromfilepath(t1 + '\\' + 'PlateWell' + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '/' + 'PlateWell' + file_name1 + '.csv')

            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

        if (val == 'Rename value in rows'):
            file = self.lineEdit_filepath.text()
            t1 = os.path.dirname(file)
            file_name1 = os.path.splitext(os.path.basename(file))[0]
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
                df = pd.read_csv(file)
                value_entered_column, okPressed = QInputDialog.getText(None, "Enter column name to add", "Column name ",
                                                                       QLineEdit.Normal, "")

                if value_entered_column in df.columns:
                    df2 = df
                    new_column = str(value_entered_column)
                    buttonReply = QMessageBox.question(None, 'Error',
                                                       "The column " + new_column + " already exists in the file.\n"
                                                                                    "Press Yes if you want to overwrite values on the column.\n"
                                                                                    "Press No to ignore.",
                                                       QMessageBox.Yes | QMessageBox.No,
                                                       QMessageBox.Yes)
                    if buttonReply == QMessageBox.Yes:
                        value_entered_rowval1, okPressed = QInputDialog.getText(None,
                                                                                "Enter value to overwrite to the column " + str(
                                                                                    value_entered_column), "Value: ",
                                                                                QLineEdit.Normal, "")

                        df2[new_column] = str(value_entered_rowval1)
                        df2.to_csv(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv', index=None)
                        self.reloaddata_fromfilepath(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv')
                        self.lineEdit_filepath.setText(t1 + '/' + 'newcolumn_' + file_name1 + '.csv')
                        QMessageBox.information(None, "Value ovewriten",
                                                "The value " + value_entered_rowval1 + " has been added to the column " + str(
                                                    new_column),
                                                QMessageBox.Ok)
                if value_entered_column not in df.columns:
                    df1 = df
                    value_entered_rowval, okPressed = QInputDialog.getText(None,
                                                                           "Enter value to add in the column " + str(
                                                                               value_entered_column), "Value: ",
                                                                           QLineEdit.Normal, "")
                    val_to_add = str(value_entered_rowval)
                    df1[value_entered_column] = value_entered_rowval
                    df1.to_csv(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv')
                    self.reloaddata_fromfilepath(t1 + '\\' + 'newcolumn_' + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '/' + 'newcolumn_' + file_name1 + '.csv')
                    QMessageBox.information(None, "Column added",
                                            "The column " + str(
                                                value_entered_column) + " has been added to the file.\nFile saved.",
                                            QMessageBox.Ok)

        if (val == 'Drop/ Rename/ Keep values in rows'):
            if file == '  ':
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != '  ':
                self.openwindow_form_checkboxes()
            self.comboBox_dropfrom.setCurrentText('Edit rows columns')

    def get_filename_path(self):
        file = self.lineEdit_filepath.text()
        return file

    def on_comboboxduplicates_changed(self, value):
        file = self.lineEdit_filepath.text()
        if (value == 'Get duplicated values'):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                    df_duplicated.to_csv(t1 + '\\' + 'duplicatedValuesfrom_' + header + file_name1 + '.csv', index=None)
                    self.setPlateWellText_intblview(df_duplicated)
                    # t1 + '\\' + 'LinkedFile_' + file_name1 + '.csv'
                    self.reloaddata_fromfilepath(t1 + '//' + 'duplicatedValuesfrom_' + header + file_name1 + '.csv')
                    self.lineEdit_filepath.setText(t1 + '/' + 'duplicatedValuesfrom_' + header + file_name1 + '.csv')

            self.comboBox_duplicates.setCurrentText('Duplicates')

        if (value == 'Number of duplicates'):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
                df = pd.read_csv(file, low_memory=False)
                header = self.select_column()
                nb_unique_header = df[header].nunique()
                if (len(df[header]) - nb_unique_header == 0):
                    QMessageBox.information(None, "Number of duplicates",
                                            "You have no duplicated values in the column " + str(header),
                                            QMessageBox.Ok)
                if (len(df[header]) - nb_unique_header > 0):
                    QMessageBox.information(None, "Number of duplicates",
                                            "You have no duplicated values.\n" + str(nb_unique_header) + " unique values in column" + str(header) + '\n' + "",
                                            QMessageBox.Ok)
            self.comboBox_duplicates.setCurrentText('Duplicates')

        if (value == 'Drop duplicated values'):
            if file == "  ":
                QMessageBox.information(None, "Error ",
                                        "No loaded file.\nPlease load a file first.",
                                        QMessageBox.Ok)
            if file != "  ":
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
                    df.to_csv(t1 + '\\' + 'afterdropduplicatesfrom_' + header + '_' + file_name1 + '.csv', index=None)
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

    def on_editrows_clicked(self):
        self.openwindow_form_checkboxes_editinrows()

    def on_editcolumns_clicked(self):
        self.openwindow_form_checkboxes_editincolumns()

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
                                        "The loaded file does not exist anymore.\n",
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
                self.reloaddata_fromfilepath(t1 + '\\' + 'Concatenated_File.csv')
                self.lineEdit_filepath.setText(t1 + '/' + 'Concatenated_File.csv')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_loadDataframe_tabs = QtWidgets.QWidget()
    ui = Ui_Form_loadDataframe_tabs()
    ui.setupUi(Form_loadDataframe_tabs)
    Form_loadDataframe_tabs.show()
    sys.exit(app.exec_())

