import sys
import os
# pandas
import pandas as pd

# qt lib
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QFileSystemModel, QTableView, QCheckBox
from PyQt5.QtCore import Qt, QAbstractTableModel, QDir, QStringListModel, QMetaObject
from PyQt5.Qt import QObject

import AQMainWindow


class DataAnalysisWindows(QMainWindow, AQMainWindow.Ui_MainWindow):
    opendir = ''
    csvDataFrame = ''
    checkMap = {}

    def __init__(self, parent=None):
        super(DataAnalysisWindows, self).__init__(parent)
        self.setupUi(self)
        self.chooseDirToolButton.clicked.connect(self.openWindow)
        self.lodefilePushButton.clicked.connect(self.loadfile)

        children = self.checkGroupBox.children()
        count = len(self.checkGroupBox.children())
        print('check box count {0}'.format(count))
        for child in children:
            if child.staticMetaObject.className() == 'QCheckBox':
                self.checkMap[child.text()] = child.isChecked()

        print('checkMap {0}'.format(self.checkMap))

    def openWindow(self):
        dirpath = QFileDialog.getExistingDirectory(self, self.tr(u'打开目录'),
                                                   "~/",
                                                   QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.dirPathLabel.setText(dirpath)

        filters = ['*.csv']

        self.opendir = QDir(dirpath)
        self.opendir.setNameFilters(filters)
        print('open dir is {0}, dirpath is {1}'.format(self.opendir.path(), dirpath))


        model = QStringListModel()
        model.setStringList(self.opendir.entryList())

        self.fileListView.setModel(model)

    # 读取csv文件，到主窗口显示
    def loadfile(self):
        path = os.path.join(self.opendir.path(), self.fileListView.currentIndex().data())
        print('file path is {0}'.format(path))
        self.csvDataFrame = CSVFilter.readCsv(path)
        self.updateCVSDisplay()


    def updateCVSDisplay(self):
        role = {u'搜索人气': [1000, 10000000], u'在线商品数': [1, 5000]}
        dataframe = CSVFilter.filtterRow(self.csvDataFrame, role)

        list = []
        for key in self.checkMap:
            if self.checkMap[key]:
                list.append(key)

        data_frame_column_by_name = dataframe.loc[:, list]
        print('display list {0}'.format(list))

        self.dataTableView.setModel(PandasModel(data_frame_column_by_name))


class CSVFilter:
    @staticmethod
    def readCsv(input_file):
        data_frame = pd.read_csv(input_file)
        # data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
        # print(data_frame['Cost'])

        # data_frame_value_meets_condition = \
        #     data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

        return data_frame

    @staticmethod
    def filtterRow(dataframe, filterrole):
        for fitter in filterrole:
            print('filter role {0}, min = {1}, max = {2}'.format(fitter, filterrole[fitter][0], filterrole[fitter][1]))
        return dataframe

class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    aqWidget = DataAnalysisWindows()
    aqWidget.show()
    sys.exit(myapp.exec_())


