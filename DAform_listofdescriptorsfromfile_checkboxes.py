import pandas as pd
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zeina\Documents\QT_Pandas\form_listofdescriptorsfromfile_checkboxes.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# toto
class Ui_form_listofdescriptorsfromfile_checkboxes(object):
    def setupUi(self, form_listofdescriptorsfromfile_checkboxes):
        form_listofdescriptorsfromfile_checkboxes.setObjectName("form_listofdescriptorsfromfile_checkboxes")
        form_listofdescriptorsfromfile_checkboxes.resize(836, 611)
        self.pushButto_apply = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButto_apply.setGeometry(QtCore.QRect(620, 560, 80, 31))
        self.pushButto_apply.setObjectName("pushButto_apply")
        self.pushButton_ADD = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButton_ADD.setGeometry(QtCore.QRect(380, 240, 71, 31))
        self.pushButton_ADD.setObjectName("pushButton_ADD")
        self.pushButton_REMOVE = QtWidgets.QPushButton(form_listofdescriptorsfromfile_checkboxes)
        self.pushButton_REMOVE.setGeometry(QtCore.QRect(380, 290, 71, 31))
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
        self.pushButton_ADD.clicked.connect(self.on_add_clicked)
        self.pushButton_REMOVE.clicked.connect(self.on_remove_clicked)

        self.retranslateUi(form_listofdescriptorsfromfile_checkboxes)
        QtCore.QMetaObject.connectSlotsByName(form_listofdescriptorsfromfile_checkboxes)

    def retranslateUi(self, form_listofdescriptorsfromfile_checkboxes):
        _translate = QtCore.QCoreApplication.translate
        form_listofdescriptorsfromfile_checkboxes.setWindowTitle(_translate("form_listofdescriptorsfromfile_checkboxes", "Select the list of the descriptors"))
        self.pushButto_apply.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "Apply"))
        self.pushButton_ADD.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "ADD"))
        self.pushButton_REMOVE.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "REMOVE"))
        self.pushButton_cancel.setText(_translate("form_listofdescriptorsfromfile_checkboxes", "Cancel"))

    def on_remove_clicked(self):
        model = QtGui.QStandardItemModel()
        row_number = model.row()
        self.listWidget_selecteddescriptors.takeItem(row_number)

    def on_listView_selectdesciptors_clicked(self, item):
        self.l = self.listWidget_selectdesciptors.selectedItems()
        print('1')
        x = []
        for i in range(len(self.l)):
            x.append(str(self.listWidget_selectdesciptors.selectedItems()[i].text()))
            print(x)
            self.selected_list = x
        return self.x

    def on_add_clicked(self, entries):
        # for i in range(len(10)):
        #     item = self.lisQListWidgetItem("Item %i" % i)
        # listWidget.addItem(item)
        # entries = ['one', 'two', 'three']
        # self.entries1 = entries
        # model = QtGui.QStandardItemModel()
        # df = pd.read_csv(self.lineedit_file_path_tochooselist)
        # entries = self.listWidget_selectdesciptors.selectionModel().selectedIndexes()

        model = QtGui.QStandardItemModel()
        print('1')
        self.listWidget_selecteddescriptors.setModel(model)
        print('1')
        print(len(self.selected_list))
        if len(self.selected_list) != 0:
            print('44')
            for i in self.selected_list:
                print('3')
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        if len(self.selected_list) == 0:
            print('no entries')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_listofdescriptorsfromfile_checkboxes = QtWidgets.QWidget()
    ui = Ui_form_listofdescriptorsfromfile_checkboxes()
    ui.setupUi(form_listofdescriptorsfromfile_checkboxes)
    form_listofdescriptorsfromfile_checkboxes.show()
    sys.exit(app.exec_())
