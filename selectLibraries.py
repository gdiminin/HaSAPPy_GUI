# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectLibraries.ui'
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

class Ui_Libraries(object):
    def setupUi(self, Libraries):
        Libraries.setObjectName(_fromUtf8("Libraries"))
        Libraries.resize(408, 272)
        Libraries.setMinimumSize(QtCore.QSize(408, 272))
        Libraries.setMaximumSize(QtCore.QSize(408, 272))
        self.buttonBox = QtGui.QDialogButtonBox(Libraries)
        self.buttonBox.setGeometry(QtCore.QRect(243, 230, 131, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Libraries)
        self.label.setGeometry(QtCore.QRect(60, 10, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Libraries)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget = QtGui.QWidget(Libraries)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.available = QtGui.QListWidget(self.layoutWidget)
        self.available.setObjectName(_fromUtf8("available"))
        self.horizontalLayout.addWidget(self.available)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.add = QtGui.QPushButton(self.layoutWidget)
        self.add.setObjectName(_fromUtf8("add"))
        self.verticalLayout.addWidget(self.add)
        self.up = QtGui.QPushButton(self.layoutWidget)
        self.up.setObjectName(_fromUtf8("up"))
        self.verticalLayout.addWidget(self.up)
        self.down = QtGui.QPushButton(self.layoutWidget)
        self.down.setObjectName(_fromUtf8("down"))
        self.verticalLayout.addWidget(self.down)
        self.remove = QtGui.QPushButton(self.layoutWidget)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.verticalLayout.addWidget(self.remove)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.selected = QtGui.QListWidget(self.layoutWidget)
        self.selected.setObjectName(_fromUtf8("selected"))
        self.horizontalLayout.addWidget(self.selected)

        self.retranslateUi(Libraries)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Libraries.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Libraries.reject)
        QtCore.QMetaObject.connectSlotsByName(Libraries)

    def retranslateUi(self, Libraries):
        Libraries.setWindowTitle(_translate("Libraries", "Dialog", None))
        self.label.setText(_translate("Libraries", "Available", None))
        self.label_2.setText(_translate("Libraries", "Selected", None))
        self.add.setText(_translate("Libraries", "Add", None))
        self.up.setText(_translate("Libraries", "Up", None))
        self.down.setText(_translate("Libraries", "Down", None))
        self.remove.setText(_translate("Libraries", "Remove", None))

