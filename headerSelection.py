# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'headerSelection.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_Header(object):
    def setupUi(self, Header):
        Header.setObjectName(_fromUtf8("Header"))
        Header.resize(340, 220)
        Header.setMinimumSize(QtCore.QSize(300, 200))
        Header.setMaximumSize(QtCore.QSize(340, 220))
        self.buttonBox = QtGui.QDialogButtonBox(Header)
        self.buttonBox.setGeometry(QtCore.QRect(10, 180, 321, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.selected = QtGui.QListWidget(Header)
        self.selected.setGeometry(QtCore.QRect(220, 30, 111, 141))
        self.selected.setObjectName(_fromUtf8("selected"))
        self.label_4 = QtGui.QLabel(Header)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutWidget = QtGui.QWidget(Header)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 104, 148))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.sample = QtGui.QComboBox(self.layoutWidget)
        self.sample.setObjectName(_fromUtf8("sample"))
        self.verticalLayout.addWidget(self.sample)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.parameter = QtGui.QComboBox(self.layoutWidget)
        self.parameter.setObjectName(_fromUtf8("parameter"))
        self.verticalLayout.addWidget(self.parameter)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.function = QtGui.QComboBox(self.layoutWidget)
        self.function.setObjectName(_fromUtf8("function"))
        self.verticalLayout.addWidget(self.function)
        self.layoutWidget1 = QtGui.QWidget(Header)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 30, 91, 134))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add = QtGui.QPushButton(self.layoutWidget1)
        self.add.setObjectName(_fromUtf8("add"))
        self.verticalLayout_2.addWidget(self.add)
        self.up = QtGui.QPushButton(self.layoutWidget1)
        self.up.setObjectName(_fromUtf8("up"))
        self.verticalLayout_2.addWidget(self.up)
        self.down = QtGui.QPushButton(self.layoutWidget1)
        self.down.setObjectName(_fromUtf8("down"))
        self.verticalLayout_2.addWidget(self.down)
        self.remove = QtGui.QPushButton(self.layoutWidget1)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.verticalLayout_2.addWidget(self.remove)

        self.retranslateUi(Header)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Header.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Header.reject)
        QtCore.QMetaObject.connectSlotsByName(Header)

    def retranslateUi(self, Header):
        Header.setWindowTitle(_translate("Header", "Dialog", None))
        self.label_4.setText(_translate("Header", "Selected Headers", None))
        self.label.setText(_translate("Header", "Sample", None))
        self.label_2.setText(_translate("Header", "Parameter", None))
        self.label_3.setText(_translate("Header", "Function", None))
        self.add.setText(_translate("Header", "Add", None))
        self.up.setText(_translate("Header", "Up", None))
        self.down.setText(_translate("Header", "Down", None))
        self.remove.setText(_translate("Header", "Remove", None))

