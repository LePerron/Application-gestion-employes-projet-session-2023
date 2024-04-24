# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Mains.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainsWindowIntra(object):
    def setupUi(self, MainsWindowIntra):
        MainsWindowIntra.setObjectName("MainsWindowIntra")
        MainsWindowIntra.resize(372, 417)
        self.centralwidget = QtWidgets.QWidget(MainsWindowIntra)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 291, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LayoutMenu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutMenu.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.LayoutMenu.setContentsMargins(0, 0, 0, 0)
        self.LayoutMenu.setSpacing(0)
        self.LayoutMenu.setObjectName("LayoutMenu")
        self.labelNomEntreprise = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelNomEntreprise.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNomEntreprise.sizePolicy().hasHeightForWidth())
        self.labelNomEntreprise.setSizePolicy(sizePolicy)
        self.labelNomEntreprise.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.labelNomEntreprise.setFont(font)
        self.labelNomEntreprise.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNomEntreprise.setObjectName("labelNomEntreprise")
        self.LayoutMenu.addWidget(self.labelNomEntreprise)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LayoutMenu.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LayoutMenu.addWidget(self.line)
        self.pushButtonContrat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonContrat.sizePolicy().hasHeightForWidth())
        self.pushButtonContrat.setSizePolicy(sizePolicy)
        self.pushButtonContrat.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonContrat.setFont(font)
        self.pushButtonContrat.setObjectName("pushButtonContrat")
        self.LayoutMenu.addWidget(self.pushButtonContrat)
        self.pushButtonPaye = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPaye.sizePolicy().hasHeightForWidth())
        self.pushButtonPaye.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonPaye.setFont(font)
        self.pushButtonPaye.setObjectName("pushButtonPaye")
        self.LayoutMenu.addWidget(self.pushButtonPaye)
        self.pushButtonEmployer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEmployer.sizePolicy().hasHeightForWidth())
        self.pushButtonEmployer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonEmployer.setFont(font)
        self.pushButtonEmployer.setCheckable(False)
        self.pushButtonEmployer.setAutoRepeat(False)
        self.pushButtonEmployer.setAutoExclusive(False)
        self.pushButtonEmployer.setObjectName("pushButtonEmployer")
        self.LayoutMenu.addWidget(self.pushButtonEmployer)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.LayoutMenu.addWidget(self.line_2)
        self.pushButtonQuitter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonQuitter.sizePolicy().hasHeightForWidth())
        self.pushButtonQuitter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonQuitter.setFont(font)
        self.pushButtonQuitter.setObjectName("pushButtonQuitter")
        self.LayoutMenu.addWidget(self.pushButtonQuitter)
        self.LayoutMenu.setStretch(0, 4)
        self.LayoutMenu.setStretch(1, 4)
        self.LayoutMenu.setStretch(2, 2)
        self.LayoutMenu.setStretch(3, 2)
        self.LayoutMenu.setStretch(4, 2)
        self.LayoutMenu.setStretch(5, 2)
        self.LayoutMenu.setStretch(6, 2)
        self.LayoutMenu.setStretch(7, 2)
        MainsWindowIntra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainsWindowIntra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 22))
        self.menubar.setObjectName("menubar")
        MainsWindowIntra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainsWindowIntra)
        self.statusbar.setObjectName("statusbar")
        MainsWindowIntra.setStatusBar(self.statusbar)

        self.retranslateUi(MainsWindowIntra)
        QtCore.QMetaObject.connectSlotsByName(MainsWindowIntra)

    def retranslateUi(self, MainsWindowIntra):
        _translate = QtCore.QCoreApplication.translate
        MainsWindowIntra.setWindowTitle(_translate("MainsWindowIntra", "MainWindow"))
        self.labelNomEntreprise.setText(_translate("MainsWindowIntra", "Menu De L\'entreprise"))
        self.pushButtonContrat.setText(_translate("MainsWindowIntra", "Gérer les Contrats"))
        self.pushButtonPaye.setText(_translate("MainsWindowIntra", "Gérer les Payes"))
        self.pushButtonEmployer.setText(_translate("MainsWindowIntra", "Gérer les Employés"))
        self.pushButtonQuitter.setText(_translate("MainsWindowIntra", "Quitter"))