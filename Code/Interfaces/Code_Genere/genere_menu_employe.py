# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tout\Prog\Projet_intra_Entreprise\UI\MenuEmploye.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMenuEmploye(object):
    def setupUi(self, DialogMenuEmploye):
        DialogMenuEmploye.setObjectName("DialogMenuEmploye")
        DialogMenuEmploye.resize(824, 583)
        font = QtGui.QFont()
        font.setPointSize(13)
        DialogMenuEmploye.setFont(font)
        self.labelTitreEmploye = QtWidgets.QLabel(DialogMenuEmploye)
        self.labelTitreEmploye.setGeometry(QtCore.QRect(20, 12, 788, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitreEmploye.setFont(font)
        self.labelTitreEmploye.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreEmploye.setObjectName("labelTitreEmploye")
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogMenuEmploye)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 80, 361, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonRechercherEmploye = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonRechercherEmploye.setObjectName("pushButtonRechercherEmploye")
        self.verticalLayout.addWidget(self.pushButtonRechercherEmploye)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEditRechercherEmploye = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditRechercherEmploye.setObjectName("lineEditRechercherEmploye")
        self.verticalLayout.addWidget(self.lineEditRechercherEmploye)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(DialogMenuEmploye)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 361, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTrierEmploye = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTrierEmploye.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTrierEmploye.setObjectName("labelTrierEmploye")
        self.verticalLayout_2.addWidget(self.labelTrierEmploye)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.comboBoxTrierEmploye = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBoxTrierEmploye.setObjectName("comboBoxTrierEmploye")
        self.comboBoxTrierEmploye.addItem("")
        self.comboBoxTrierEmploye.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxTrierEmploye)
        self.listViewEmploye = QtWidgets.QListView(DialogMenuEmploye)
        self.listViewEmploye.setGeometry(QtCore.QRect(20, 180, 621, 341))
        self.listViewEmploye.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listViewEmploye.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewEmploye.setObjectName("listViewEmploye")
        self.pushButtonAjouterEmploye = QtWidgets.QPushButton(DialogMenuEmploye)
        self.pushButtonAjouterEmploye.setGeometry(QtCore.QRect(30, 530, 191, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButtonAjouterEmploye.sizePolicy().hasHeightForWidth())
        self.pushButtonAjouterEmploye.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonAjouterEmploye.setFont(font)
        self.pushButtonAjouterEmploye.setObjectName("pushButtonAjouterEmploye")
        self.pushButtonModifierEmploye = QtWidgets.QPushButton(DialogMenuEmploye)
        self.pushButtonModifierEmploye.setGeometry(QtCore.QRect(430, 530, 191, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.pushButtonModifierEmploye.sizePolicy().hasHeightForWidth())
        self.pushButtonModifierEmploye.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonModifierEmploye.setFont(font)
        self.pushButtonModifierEmploye.setObjectName("pushButtonModifierEmploye")
        self.pushButtonSupprimerEmploye = QtWidgets.QPushButton(DialogMenuEmploye)
        self.pushButtonSupprimerEmploye.setGeometry(QtCore.QRect(230, 530, 191, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.pushButtonSupprimerEmploye.sizePolicy().hasHeightForWidth())
        self.pushButtonSupprimerEmploye.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonSupprimerEmploye.setFont(font)
        self.pushButtonSupprimerEmploye.setObjectName("pushButtonSupprimerEmploye")
        self.pushButtonRetournerMenu = QtWidgets.QPushButton(DialogMenuEmploye)
        self.pushButtonRetournerMenu.setGeometry(QtCore.QRect(650, 530, 161, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.pushButtonRetournerMenu.sizePolicy().hasHeightForWidth())
        self.pushButtonRetournerMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonRetournerMenu.setFont(font)
        self.pushButtonRetournerMenu.setObjectName("pushButtonRetournerMenu")
        self.line = QtWidgets.QFrame(DialogMenuEmploye)
        self.line.setGeometry(QtCore.QRect(20, 50, 791, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(DialogMenuEmploye)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 180, 151, 291))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxIdentifiant = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxIdentifiant.setFont(font)
        self.checkBoxIdentifiant.setCheckable(True)
        self.checkBoxIdentifiant.setChecked(True)
        self.checkBoxIdentifiant.setAutoExclusive(False)
        self.checkBoxIdentifiant.setTristate(False)
        self.checkBoxIdentifiant.setObjectName("checkBoxIdentifiant")
        self.verticalLayout_3.addWidget(self.checkBoxIdentifiant)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.checkBoxPrenom = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxPrenom.setFont(font)
        self.checkBoxPrenom.setChecked(True)
        self.checkBoxPrenom.setObjectName("checkBoxPrenom")
        self.verticalLayout_3.addWidget(self.checkBoxPrenom)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.checkBoxNom = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxNom.setFont(font)
        self.checkBoxNom.setChecked(True)
        self.checkBoxNom.setObjectName("checkBoxNom")
        self.verticalLayout_3.addWidget(self.checkBoxNom)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.checkBoxSalaire = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxSalaire.setFont(font)
        self.checkBoxSalaire.setObjectName("checkBoxSalaire")
        self.verticalLayout_3.addWidget(self.checkBoxSalaire)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.checkBoxAnciennete = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxAnciennete.setFont(font)
        self.checkBoxAnciennete.setObjectName("checkBoxAnciennete")
        self.verticalLayout_3.addWidget(self.checkBoxAnciennete)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.checkBoxNbHeure = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxNbHeure.setFont(font)
        self.checkBoxNbHeure.setObjectName("checkBoxNbHeure")
        self.verticalLayout_3.addWidget(self.checkBoxNbHeure)
        self.labelErreurSelection = QtWidgets.QLabel(DialogMenuEmploye)
        self.labelErreurSelection.setGeometry(QtCore.QRect(660, 470, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.labelErreurSelection.sizePolicy().hasHeightForWidth())
        self.labelErreurSelection.setSizePolicy(sizePolicy)
        self.labelErreurSelection.setMinimumSize(QtCore.QSize(0, 5))
        self.labelErreurSelection.setSizeIncrement(QtCore.QSize(0, 5))
        self.labelErreurSelection.setBaseSize(QtCore.QSize(0, 5))
        self.labelErreurSelection.setText("")
        self.labelErreurSelection.setObjectName("labelErreurSelection")
        self.line_2 = QtWidgets.QFrame(DialogMenuEmploye)
        self.line_2.setGeometry(QtCore.QRect(640, 520, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(DialogMenuEmploye)
        self.line_3.setGeometry(QtCore.QRect(640, 513, 180, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(DialogMenuEmploye)
        QtCore.QMetaObject.connectSlotsByName(DialogMenuEmploye)

    def retranslateUi(self, DialogMenuEmploye):
        _translate = QtCore.QCoreApplication.translate
        DialogMenuEmploye.setWindowTitle(_translate("DialogMenuEmploye", "Dialog"))
        self.labelTitreEmploye.setText(_translate("DialogMenuEmploye", "Gestionnaire des employés"))
        self.pushButtonRechercherEmploye.setText(_translate("DialogMenuEmploye", "Rechercher un employé:"))
        self.labelTrierEmploye.setText(_translate("DialogMenuEmploye", "Trier employé selon:"))
        self.comboBoxTrierEmploye.setItemText(0, _translate("DialogMenuEmploye", "A-Z"))
        self.comboBoxTrierEmploye.setItemText(1, _translate("DialogMenuEmploye", "Z-A"))
        self.pushButtonAjouterEmploye.setText(_translate("DialogMenuEmploye", "Ajouter"))
        self.pushButtonModifierEmploye.setText(_translate("DialogMenuEmploye", "Modifier"))
        self.pushButtonSupprimerEmploye.setText(_translate("DialogMenuEmploye", "Supprimer"))
        self.pushButtonRetournerMenu.setText(_translate("DialogMenuEmploye", "Menu"))
        self.checkBoxIdentifiant.setText(_translate("DialogMenuEmploye", "Identifiant"))
        self.checkBoxPrenom.setText(_translate("DialogMenuEmploye", "Prénom"))
        self.checkBoxNom.setText(_translate("DialogMenuEmploye", "Nom"))
        self.checkBoxSalaire.setText(_translate("DialogMenuEmploye", "Salaire"))
        self.checkBoxAnciennete.setText(_translate("DialogMenuEmploye", "Ancienneté"))
        self.checkBoxNbHeure.setText(_translate("DialogMenuEmploye", "Nombre d\'heure"))
