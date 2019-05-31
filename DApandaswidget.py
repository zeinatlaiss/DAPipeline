import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df = pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

    def Load_pandas(self):
        path = self.lineEdit.text()
        df = pd.read_csv(path)
        model = PandasModel(df)
        self.tableView.setModel(model)

class Matplotlib_qt(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Pandas_Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.pathLE = QtWidgets.QLineEdit(self)
        self.labelplate = QtWidgets.QLineEdit(self)
        self.labelwell = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        hLayout.addWidget(self.labelplate)
        hLayout.addWidget(self.labelwell)
        self.loadBtn = QtWidgets.QPushButton("Select File", self)
        self.addclassesBtn = QtWidgets.QPushButton("Add classes", self)
        self.dropclasses = QtWidgets.QPushButton("Drop Classes", self)
        self.combobox_plot = QtWidgets.QComboBox()
        self.combobox_plot.addItem("Plot")
        self.combobox_plot.addItem("Scatter Plot")
        self.combobox_plot.addItem("Swarm Plot")
        # self.plotBtn = QtWidgets.QPushButton("Plot File", self)

        hLayout.addWidget(self.loadBtn)
        hLayout.addWidget(self.addclassesBtn)
        hLayout.addWidget(self.dropclasses)
        hLayout.addWidget(self.combobox_plot)
        # hLayout.addWidget(self.plotBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.addclassesBtn.clicked.connect(self.AddDataframeToTable)
        self.dropclasses.clicked.connect(self.dropClasses)
        self.combobox_plot.currentIndexChanged.connect(self.selectionchange_plot)
        # self.plotBtn.clicked.connect(PlotCanvas.plotFile)
        self.pandasTv.setSortingEnabled(True)


    def AddDataframeToTable(self):
        print('Not imp yet')

        # sys.exit(win.exec_())
    def selectionchange_plot(self, i):
        # for count in range(self.combobox_plot.count()):
            # print(self.combobox_plot.itemText(count))
        data_pd = Pandas_Widget.loadFile
        if (self.combobox_plot.currentText() == "Scatter Plot"):
            print("Current index", i, "selection changed ", self.combobox_plot.currentText())
            print(data_pd)
            plotFie(data_pd)
            print(data_pd)
            print('\n')

        elif(self.combobox_plot.currentText() == "Swarm Plot"):
            print("Current index", i, "selection changed ", self.combobox_plot.currentText())
        else:
            print('you should choose a plot')

    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "D:\\", "CSV Files (*.csv)")
        self.pathLE.setText(fileName)
        df = pd.read_csv(fileName)
        self.labelplate.setText(str(df['Plate'].nunique())+ ' plates')
        self.labelwell.setText(str(df['Well'].nunique())+ ' wells')
        model = PandasModel(df)
        self.pandasTv.setModel(model)
        print(fileName)
        return df

    def dropClasses(self):
        print('dropped')

    def plotGraphs(self):
        print('plotted')

    def loadFile_subf(self):
        subapp = QtWidgets.QApplication(sys.argv)
        pdmodel = PandasModel()
        w = Pandas_Widget(pdmodel)
        w.loadFile()
        # w.setFocus(QtCore.Qt.PopupFocusReason)
        w.show()
        sys.exit(subapp.exec_())

# # if __name__ == "__main__":
# # #
#     app = QtWidgets.QApplication(sys.argv)
#     w = PandasModel()
#     # w = Pandas_Widget(pdmodel)
#     # w.loadFile()
#     # w.show()
#     sys.exit(app.exec_())
#     # app = QtWidgets.QApplication(sys.argv)
#     # pdmodel = PandasModel()
#     # w = Pandas_Widget(pdmodel)
#     # w.loadFile()
#     # w.show()
#     # sys.exit(app.exec_())