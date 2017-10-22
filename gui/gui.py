# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LadybugVizzz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1123, 753)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/log")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1121, 691))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tbMain = QtGui.QWidget()
        self.tbMain.setObjectName(_fromUtf8("tbMain"))
        self.linEditSearch = QtGui.QLineEdit(self.tbMain)
        self.linEditSearch.setGeometry(QtCore.QRect(60, 10, 231, 22))
        self.linEditSearch.setObjectName(_fromUtf8("linEditSearch"))
        self.textEdit = QtGui.QTextEdit(self.tbMain)
        self.textEdit.setGeometry(QtCore.QRect(0, 170, 291, 131))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.webView = QtWebKit.QWebView(self.tbMain)
        self.webView.setGeometry(QtCore.QRect(300, 0, 811, 651))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.linEditLatitude = QtGui.QLineEdit(self.tbMain)
        self.linEditLatitude.setGeometry(QtCore.QRect(110, 40, 181, 22))
        self.linEditLatitude.setObjectName(_fromUtf8("linEditLatitude"))
        self.linEditLongitude = QtGui.QLineEdit(self.tbMain)
        self.linEditLongitude.setGeometry(QtCore.QRect(110, 70, 181, 22))
        self.linEditLongitude.setObjectName(_fromUtf8("linEditLongitude"))
        self.lblLatitude = QtGui.QLabel(self.tbMain)
        self.lblLatitude.setGeometry(QtCore.QRect(2, 40, 101, 20))
        self.lblLatitude.setObjectName(_fromUtf8("lblLatitude"))
        self.lblLongitude = QtGui.QLabel(self.tbMain)
        self.lblLongitude.setGeometry(QtCore.QRect(0, 70, 101, 20))
        self.lblLongitude.setObjectName(_fromUtf8("lblLongitude"))
        self.lblSearch = QtGui.QLabel(self.tbMain)
        self.lblSearch.setGeometry(QtCore.QRect(0, 10, 101, 20))
        self.lblSearch.setObjectName(_fromUtf8("lblSearch"))
        self.btnSearch = QtGui.QPushButton(self.tbMain)
        self.btnSearch.setGeometry(QtCore.QRect(0, 100, 291, 28))
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.lblLocation = QtGui.QLabel(self.tbMain)
        self.lblLocation.setGeometry(QtCore.QRect(0, 150, 101, 20))
        self.lblLocation.setObjectName(_fromUtf8("lblLocation"))
        self.lblEPWlocations = QtGui.QLabel(self.tbMain)
        self.lblEPWlocations.setGeometry(QtCore.QRect(0, 320, 101, 20))
        self.lblEPWlocations.setObjectName(_fromUtf8("lblEPWlocations"))
        self.listEPWlocations = QtGui.QListWidget(self.tbMain)
        self.listEPWlocations.setGeometry(QtCore.QRect(0, 340, 291, 271))
        self.listEPWlocations.setObjectName(_fromUtf8("listEPWlocations"))
        self.btnGeneratePlots = QtGui.QPushButton(self.tbMain)
        self.btnGeneratePlots.setGeometry(QtCore.QRect(0, 620, 291, 28))
        self.btnGeneratePlots.setObjectName(_fromUtf8("btnGeneratePlots"))
        self.tabWidget.addTab(self.tbMain, _fromUtf8(""))
        self.tbWindRose = QtGui.QWidget()
        self.tbWindRose.setObjectName(_fromUtf8("tbWindRose"))
        self.lblWindrose = QtGui.QLabel(self.tbWindRose)
        self.lblWindrose.setGeometry(QtCore.QRect(150, 60, 951, 591))
        self.lblWindrose.setText(_fromUtf8(""))
        self.lblWindrose.setObjectName(_fromUtf8("lblWindrose"))
        self.tabWidget.addTab(self.tbWindRose, _fromUtf8(""))
        self.tbChart = QtGui.QWidget()
        self.tbChart.setObjectName(_fromUtf8("tbChart"))
        self.lblCharts = QtGui.QLabel(self.tbChart)
        self.lblCharts.setGeometry(QtCore.QRect(200, 10, 901, 641))
        self.lblCharts.setText(_fromUtf8(""))
        self.lblCharts.setObjectName(_fromUtf8("lblCharts"))
        self.cmbPlotType = QtGui.QComboBox(self.tbChart)
        self.cmbPlotType.setGeometry(QtCore.QRect(0, 20, 201, 22))
        self.cmbPlotType.setObjectName(_fromUtf8("cmbPlotType"))
        self.cmbColorScheme = QtGui.QComboBox(self.tbChart)
        self.cmbColorScheme.setGeometry(QtCore.QRect(0, 70, 201, 22))
        self.cmbColorScheme.setObjectName(_fromUtf8("cmbColorScheme"))
        self.label = QtGui.QLabel(self.tbChart)
        self.label.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tbChart)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tbChart, _fromUtf8(""))
        self.tbSunPath = QtGui.QWidget()
        self.tbSunPath.setObjectName(_fromUtf8("tbSunPath"))
        self.labelSunpath = QtGui.QLabel(self.tbSunPath)
        self.labelSunpath.setGeometry(QtCore.QRect(370, 10, 741, 641))
        self.labelSunpath.setText(_fromUtf8(""))
        self.labelSunpath.setObjectName(_fromUtf8("labelSunpath"))
        self.tabWidget.addTab(self.tbSunPath, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ladybugvizzz !", None))
        self.lblLatitude.setText(_translate("MainWindow", "Latitude", None))
        self.lblLongitude.setText(_translate("MainWindow", "Longitude", None))
        self.lblSearch.setText(_translate("MainWindow", "Search", None))
        self.btnSearch.setText(_translate("MainWindow", "Search!", None))
        self.lblLocation.setText(_translate("MainWindow", "Location", None))
        self.lblEPWlocations.setText(_translate("MainWindow", "EPW Locations", None))
        self.btnGeneratePlots.setText(_translate("MainWindow", "Visualize !", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbMain), _translate("MainWindow", "Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbWindRose), _translate("MainWindow", "Wind Rose", None))
        self.label.setText(_translate("MainWindow", "Plot Type", None))
        self.label_2.setText(_translate("MainWindow", "Color Scheme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbChart), _translate("MainWindow", "Charts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbSunPath), _translate("MainWindow", "SunPath", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from PyQt4 import QtWebKit
import resources
