# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdcui.ui'
#
# Created: Sun Mar 29 16:44:13 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(1008, 686)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEditMissionStatus = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEditMissionStatus.setGeometry(QtCore.QRect(430, 30, 561, 571))
        self.plainTextEditMissionStatus.setReadOnly(True)
        self.plainTextEditMissionStatus.setPlainText(_fromUtf8(""))
        self.plainTextEditMissionStatus.setObjectName(_fromUtf8("plainTextEditMissionStatus"))
        self.labelMissionStatus = QtGui.QLabel(self.centralwidget)
        self.labelMissionStatus.setGeometry(QtCore.QRect(430, 10, 561, 17))
        self.labelMissionStatus.setObjectName(_fromUtf8("labelMissionStatus"))
        self.labelCommandConsole = QtGui.QLabel(self.centralwidget)
        self.labelCommandConsole.setGeometry(QtCore.QRect(430, 610, 561, 17))
        self.labelCommandConsole.setObjectName(_fromUtf8("labelCommandConsole"))
        self.plainTextEditTelemetry = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEditTelemetry.setGeometry(QtCore.QRect(10, 360, 400, 300))
        self.plainTextEditTelemetry.setObjectName(_fromUtf8("plainTextEditTelemetry"))
        self.labelVideoStream = QtGui.QLabel(self.centralwidget)
        self.labelVideoStream.setGeometry(QtCore.QRect(10, 10, 401, 17))
        self.labelVideoStream.setObjectName(_fromUtf8("labelVideoStream"))
        self.labelTelemetry = QtGui.QLabel(self.centralwidget)
        self.labelTelemetry.setGeometry(QtCore.QRect(10, 340, 401, 17))
        self.labelTelemetry.setObjectName(_fromUtf8("labelTelemetry"))
        self.lineEditCommandConsole = QtGui.QLineEdit(self.centralwidget)
        self.lineEditCommandConsole.setGeometry(QtCore.QRect(430, 630, 561, 29))
        self.lineEditCommandConsole.setText(_fromUtf8(""))
        self.lineEditCommandConsole.setObjectName(_fromUtf8("lineEditCommandConsole"))
        self.widgetVideoStream = QtGui.QWidget(self.centralwidget)
        self.widgetVideoStream.setGeometry(QtCore.QRect(10, 30, 400, 300))
        self.widgetVideoStream.setObjectName(_fromUtf8("widgetVideoStream"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CDC: Command Distribution Center", None))
        self.labelMissionStatus.setText(_translate("MainWindow", "Mission Status", None))
        self.labelCommandConsole.setText(_translate("MainWindow", "Enter Command", None))
        self.labelVideoStream.setText(_translate("MainWindow", "Live Video Stream", None))
        self.labelTelemetry.setText(_translate("MainWindow", "Telemetry", None))

