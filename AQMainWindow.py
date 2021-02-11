# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AQMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftVLayout = QtWidgets.QVBoxLayout()
        self.leftVLayout.setObjectName("leftVLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseDirLabel.setObjectName("chooseDirLabel")
        self.horizontalLayout_2.addWidget(self.chooseDirLabel)
        self.chooseDirToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.chooseDirToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.chooseDirToolButton.setObjectName("chooseDirToolButton")
        self.horizontalLayout_2.addWidget(self.chooseDirToolButton)
        self.leftVLayout.addLayout(self.horizontalLayout_2)
        self.dirPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.dirPathLabel.setObjectName("dirPathLabel")
        self.leftVLayout.addWidget(self.dirPathLabel)
        self.fileListView = QtWidgets.QListView(self.centralwidget)
        self.fileListView.setObjectName("fileListView")
        self.leftVLayout.addWidget(self.fileListView)
        self.lodefilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lodefilePushButton.setObjectName("lodefilePushButton")
        self.leftVLayout.addWidget(self.lodefilePushButton)
        self.horizontalLayout.addLayout(self.leftVLayout)
        self.middleVLayout = QtWidgets.QVBoxLayout()
        self.middleVLayout.setObjectName("middleVLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.middleVLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.middleVLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.middleVLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.middleVLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.middleVLayout.addWidget(self.widget_5)
        self.horizontalLayout.addLayout(self.middleVLayout)
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.dataFilter = QtWidgets.QWidget()
        self.dataFilter.setObjectName("dataFilter")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dataFilter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkGroupBox = QtWidgets.QGroupBox(self.dataFilter)
        self.checkGroupBox.setObjectName("checkGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.checkGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.sWordCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.sWordCheckBox.setChecked(True)
        self.sWordCheckBox.setObjectName("sWordCheckBox")
        self.gridLayout.addWidget(self.sWordCheckBox, 0, 0, 1, 1)
        self.clickPopularityCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.clickPopularityCheckBox.setChecked(True)
        self.clickPopularityCheckBox.setObjectName("clickPopularityCheckBox")
        self.gridLayout.addWidget(self.clickPopularityCheckBox, 1, 0, 1, 1)
        self.recPriceCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.recPriceCheckBox.setChecked(True)
        self.recPriceCheckBox.setObjectName("recPriceCheckBox")
        self.gridLayout.addWidget(self.recPriceCheckBox, 1, 3, 1, 1)
        self.clickRatioCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.clickRatioCheckBox.setChecked(False)
        self.clickRatioCheckBox.setObjectName("clickRatioCheckBox")
        self.gridLayout.addWidget(self.clickRatioCheckBox, 0, 3, 1, 1)
        self.tradingIndexCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.tradingIndexCheckBox.setObjectName("tradingIndexCheckBox")
        self.gridLayout.addWidget(self.tradingIndexCheckBox, 0, 4, 1, 1)
        self.clickHotCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.clickHotCheckBox.setObjectName("clickHotCheckBox")
        self.gridLayout.addWidget(self.clickHotCheckBox, 1, 2, 1, 1)
        self.tradingNumbersCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.tradingNumbersCheckBox.setObjectName("tradingNumbersCheckBox")
        self.gridLayout.addWidget(self.tradingNumbersCheckBox, 0, 5, 1, 1)
        self.payRatioCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.payRatioCheckBox.setChecked(True)
        self.payRatioCheckBox.setObjectName("payRatioCheckBox")
        self.gridLayout.addWidget(self.payRatioCheckBox, 1, 4, 1, 1)
        self.mallClickRatioCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.mallClickRatioCheckBox.setChecked(True)
        self.mallClickRatioCheckBox.setObjectName("mallClickRatioCheckBox")
        self.gridLayout.addWidget(self.mallClickRatioCheckBox, 1, 5, 1, 1)
        self.sPopularityCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.sPopularityCheckBox.setChecked(True)
        self.sPopularityCheckBox.setObjectName("sPopularityCheckBox")
        self.gridLayout.addWidget(self.sPopularityCheckBox, 0, 1, 1, 1)
        self.clickNumbersCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.clickNumbersCheckBox.setObjectName("clickNumbersCheckBox")
        self.gridLayout.addWidget(self.clickNumbersCheckBox, 1, 1, 1, 1)
        self.sNumbersCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.sNumbersCheckBox.setObjectName("sNumbersCheckBox")
        self.gridLayout.addWidget(self.sNumbersCheckBox, 0, 2, 1, 1)
        self.itemNumbersCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.itemNumbersCheckBox.setChecked(True)
        self.itemNumbersCheckBox.setObjectName("itemNumbersCheckBox")
        self.gridLayout.addWidget(self.itemNumbersCheckBox, 1, 6, 1, 1)
        self.competitiveCheckBox = QtWidgets.QCheckBox(self.checkGroupBox)
        self.competitiveCheckBox.setObjectName("competitiveCheckBox")
        self.gridLayout.addWidget(self.competitiveCheckBox, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.checkGroupBox)
        self.dataTableView = QtWidgets.QTableView(self.dataFilter)
        self.dataTableView.setObjectName("dataTableView")
        self.verticalLayout.addWidget(self.dataTableView)
        self.mainTabWidget.addTab(self.dataFilter, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.mainTabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.mainTabWidget.addTab(self.tab3, "")
        self.horizontalLayout.addWidget(self.mainTabWidget)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseDirLabel.setText(_translate("MainWindow", "文件列表"))
        self.chooseDirToolButton.setText(_translate("MainWindow", "选择文件夹..."))
        self.dirPathLabel.setText(_translate("MainWindow", "path"))
        self.lodefilePushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.checkGroupBox.setTitle(_translate("MainWindow", "选择显示列"))
        self.sWordCheckBox.setText(_translate("MainWindow", "搜索词"))
        self.clickPopularityCheckBox.setText(_translate("MainWindow", "点击人气"))
        self.recPriceCheckBox.setText(_translate("MainWindow", "直通车参考价"))
        self.clickRatioCheckBox.setText(_translate("MainWindow", "点击率"))
        self.tradingIndexCheckBox.setText(_translate("MainWindow", "交易指数"))
        self.clickHotCheckBox.setText(_translate("MainWindow", "点击热度"))
        self.tradingNumbersCheckBox.setText(_translate("MainWindow", "交易金额"))
        self.payRatioCheckBox.setText(_translate("MainWindow", "支付转换率"))
        self.mallClickRatioCheckBox.setText(_translate("MainWindow", "商城点击占比"))
        self.sPopularityCheckBox.setText(_translate("MainWindow", "搜索人气"))
        self.clickNumbersCheckBox.setText(_translate("MainWindow", "点击人数"))
        self.sNumbersCheckBox.setText(_translate("MainWindow", "搜索人数"))
        self.itemNumbersCheckBox.setText(_translate("MainWindow", "在线商品数"))
        self.competitiveCheckBox.setText(_translate("MainWindow", "竞争度"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.dataFilter), _translate("MainWindow", "数据筛选"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab2), _translate("MainWindow", "页"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab3), _translate("MainWindow", "页"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
