from PyQt5.QtWidgets import *
import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_listofdescriptorsfromfile_checkboxes.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_listofdescriptorsfromfile_checkboxes(object):
    def setupUi(self, form_listofdescriptorsfromfile_checkboxes):
        form_listofdescriptorsfromfile_checkboxes.setObjectName("form_listofdescriptorsfromfile_checkboxes")
        form_listofdescriptorsfromfile_checkboxes.resize(836, 611)
        self.pushButto_apply = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButto_apply.setGeometry(QtCore.QRect(620, 560, 80, 31))
        self.pushButto_apply.setObjectName("pushButto_apply")
        self.pushButton_REMOVE = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButton_REMOVE.setGeometry(QtCore.QRect(380, 260, 71, 31))
        self.pushButton_REMOVE.setObjectName("pushButton_REMOVE")
        self.pushButton_cancel = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButton_cancel.setGeometry(QtCore.QRect(720, 560, 80, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.listWidget_selectdesciptors = QtWidgets.QListWidget(form_listofdescriptorsfromfile_checkboxes)
        self.listWidget_selectdesciptors.setGeometry(QtCore.QRect(30, 40, 311, 491))
        self.listWidget_selectdesciptors.setObjectName("listWidget_selectdesciptors")
        self.listWidget_selecteddescriptors = QtWidgets.QListWidget(form_listofdescriptorsfromfile_checkboxes)
        self.listWidget_selecteddescriptors.setGeometry(QtCore.QRect(490, 40, 311, 491))
        self.listWidget_selecteddescriptors.setObjectName("listWidget_selecteddescriptors")

        self.listWidget_selectdesciptors.clicked.connect(self.on_listView_selectdesciptors_clicked)
        self.pushButton_REMOVE.clicked.connect(self.on_remove_clicked)
        self.pushButto_apply.clicked.connect(self.on_apply_clicked)
        self.pushButton_cancel.clicked.connect(self.on_cancel_clicked)

        self.retranslateUi(form_listofdescriptorsfromfile_checkboxes)
        QtCore.QMetaObject.connectSlotsByName(form_listofdescriptorsfromfile_checkboxes)

    def retranslateUi(self, form_listofdescriptorsfromfile_checkboxes):
        _translate = QtCore.QCoreApplication.translate
        form_listofdescriptorsfromfile_checkboxes.setWindowTitle(_translate("form_listofdescriptorsfromfile_checkboxes", "Select the list of the descriptors"))
        self.pushButto_apply.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "Apply"))
        self.pushButton_REMOVE.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "REMOVE"))
        self.pushButton_cancel.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "Cancel"))


    def on_remove_clicked(self):
        for item in self.listWidget_selecteddescriptors.selectedItems():
            self.listWidget_selectdesciptors.addItem(item.text())
            self.listWidget_selecteddescriptors.takeItem(self.listWidget_selecteddescriptors.row(item))

    def on_apply_clicked(self):
        list_descriptors =  self.get_items_fromlist()
        if len(list_descriptors) == 0:
            QMessageBox.information(None, "Error ",
                                    "You have no descriptor in your list.\nPlease load descriptors first",
                                    QMessageBox.Ok)

        if len(list_descriptors) > 0:
            # print(list_descriptors)
            df = pd.read_csv('D:\RESULTS\Plates_DM1\DM1_6000cells\\ag1d9bbd1b60fc2dddd431c7101e53a507_wt_6000.csv')
            # for i in range(len(list_descriptors)):
            df = df.assign(list_descriptors)
            print(df)
            # dd.to_csv('D:\RESULTS\Plates_DM1\DM1_6000cells\\out.csv')

    def on_listView_selectdesciptors_clicked(self, item):
        for item in self.listWidget_selectdesciptors.selectedItems():
            self.listWidget_selecteddescriptors.addItem(item.text())
            self.listWidget_selectdesciptors.takeItem(self.listWidget_selectdesciptors.row(item))

    def get_items_fromlist(self):
        # for i in self.listWidget_selecteddescriptors.count():
        itemsTextList = [str(self.listWidget_selecteddescriptors.item(i).text()) for i in range(self.listWidget_selecteddescriptors.count())]
        return itemsTextList

    def on_cancel_clicked(self):
        print('w')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_listofdescriptorsfromfile_checkboxes = QtWidgets.QWidget()
    ui = Ui_form_listofdescriptorsfromfile_checkboxes()
    ui.setupUi(form_listofdescriptorsfromfile_checkboxes)
    form_listofdescriptorsfromfile_checkboxes.show()
    sys.exit(app.exec_())
