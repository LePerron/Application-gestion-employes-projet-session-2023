# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tout\Prog\Projet_intra_Entreprise\UI\Modifier_Employe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogModifierEmploye(object):
    def setupUi(self, DialogModifierEmploye):
        DialogModifierEmploye.setObjectName("DialogModifierEmploye")
        DialogModifierEmploye.resize(393, 683)
        self.frame = QtWidgets.QFrame(DialogModifierEmploye)
        self.frame.setGeometry(QtCore.QRect(0, 66, 391, 611))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelIdentifiant = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.labelIdentifiant.setFont(font)
        self.labelIdentifiant.setObjectName("labelIdentifiant")
        self.verticalLayout_8.addWidget(self.labelIdentifiant)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditIdentifiant = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditIdentifiant.setAutoFillBackground(False)
        self.lineEditIdentifiant.setFrame(True)
        self.lineEditIdentifiant.setClearButtonEnabled(False)
        self.lineEditIdentifiant.setObjectName("lineEditIdentifiant")
        self.verticalLayout.addWidget(self.lineEditIdentifiant)
        self.labelErreurIdentifiant = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurIdentifiant.setText("")
        self.labelErreurIdentifiant.setObjectName("labelErreurIdentifiant")
        self.verticalLayout.addWidget(self.labelErreurIdentifiant)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.labelNom = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNom.setFont(font)
        self.labelNom.setObjectName("labelNom")
        self.verticalLayout_8.addWidget(self.labelNom)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditNom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNom.setObjectName("lineEditNom")
        self.verticalLayout_2.addWidget(self.lineEditNom)
        self.labelErreurNom = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurNom.setText("")
        self.labelErreurNom.setObjectName("labelErreurNom")
        self.verticalLayout_2.addWidget(self.labelErreurNom)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.labelPrenom = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelPrenom.setFont(font)
        self.labelPrenom.setObjectName("labelPrenom")
        self.verticalLayout_8.addWidget(self.labelPrenom)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditPrenom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.verticalLayout_4.addWidget(self.lineEditPrenom)
        self.labelErreurPrenom = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurPrenom.setText("")
        self.labelErreurPrenom.setObjectName("labelErreurPrenom")
        self.verticalLayout_4.addWidget(self.labelErreurPrenom)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.labelPoste = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelPoste.setFont(font)
        self.labelPoste.setObjectName("labelPoste")
        self.verticalLayout_8.addWidget(self.labelPoste)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comboBoxPoste = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxPoste.setObjectName("comboBoxPoste")
        self.comboBoxPoste.addItem("")
        self.comboBoxPoste.addItem("")
        self.comboBoxPoste.addItem("")
        self.comboBoxPoste.addItem("")
        self.verticalLayout_6.addWidget(self.comboBoxPoste)
        spacerItem = QtWidgets.QSpacerItem(48, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.labelSpecialite = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelSpecialite.setFont(font)
        self.labelSpecialite.setObjectName("labelSpecialite")
        self.verticalLayout_8.addWidget(self.labelSpecialite)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBoxSpecialite = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxSpecialite.setObjectName("comboBoxSpecialite")
        self.verticalLayout_5.addWidget(self.comboBoxSpecialite)
        spacerItem1 = QtWidgets.QSpacerItem(68, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.labelDateEngagement = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelDateEngagement.setFont(font)
        self.labelDateEngagement.setObjectName("labelDateEngagement")
        self.verticalLayout_8.addWidget(self.labelDateEngagement)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dateEditDateEngagement = QtWidgets.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEditDateEngagement.setFont(font)
        self.dateEditDateEngagement.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 5, 23), QtCore.QTime(0, 0, 0)))
        self.dateEditDateEngagement.setCalendarPopup(True)
        self.dateEditDateEngagement.setObjectName("dateEditDateEngagement")
        self.verticalLayout_7.addWidget(self.dateEditDateEngagement)
        self.labelErreurDateEngagement = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurDateEngagement.setText("")
        self.labelErreurDateEngagement.setObjectName("labelErreurDateEngagement")
        self.verticalLayout_7.addWidget(self.labelErreurDateEngagement)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.labelDatePromotion = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelDatePromotion.setFont(font)
        self.labelDatePromotion.setObjectName("labelDatePromotion")
        self.verticalLayout_8.addWidget(self.labelDatePromotion)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.dateEditDatePromotion = QtWidgets.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEditDatePromotion.setFont(font)
        self.dateEditDatePromotion.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 5, 23), QtCore.QTime(0, 0, 0)))
        self.dateEditDatePromotion.setCalendarPopup(True)
        self.dateEditDatePromotion.setObjectName("dateEditDatePromotion")
        self.verticalLayout_11.addWidget(self.dateEditDatePromotion)
        self.labelErreurDatePromotion = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurDatePromotion.setText("")
        self.labelErreurDatePromotion.setObjectName("labelErreurDatePromotion")
        self.verticalLayout_11.addWidget(self.labelErreurDatePromotion)
        self.verticalLayout_8.addLayout(self.verticalLayout_11)
        self.pushButtonModifierEmploye = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonModifierEmploye.setFont(font)
        self.pushButtonModifierEmploye.setObjectName("pushButtonModifierEmploye")
        self.verticalLayout_8.addWidget(self.pushButtonModifierEmploye)
        self.pushButtonAnnuler = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonAnnuler.setFont(font)
        self.pushButtonAnnuler.setObjectName("pushButtonAnnuler")
        self.verticalLayout_8.addWidget(self.pushButtonAnnuler)
        self.line = QtWidgets.QFrame(DialogModifierEmploye)
        self.line.setGeometry(QtCore.QRect(10, 46, 370, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.labelTitreModifierEmploye = QtWidgets.QLabel(DialogModifierEmploye)
        self.labelTitreModifierEmploye.setGeometry(QtCore.QRect(0, 20, 390, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.labelTitreModifierEmploye.setFont(font)
        self.labelTitreModifierEmploye.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTitreModifierEmploye.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreModifierEmploye.setObjectName("labelTitreModifierEmploye")

        self.retranslateUi(DialogModifierEmploye)
        QtCore.QMetaObject.connectSlotsByName(DialogModifierEmploye)

    def retranslateUi(self, DialogModifierEmploye):
        _translate = QtCore.QCoreApplication.translate
        DialogModifierEmploye.setWindowTitle(_translate("DialogModifierEmploye", "Dialog"))
        self.labelIdentifiant.setText(_translate("DialogModifierEmploye", "Identifiant de l\'employé"))
        self.labelNom.setText(_translate("DialogModifierEmploye", "Nom de l\'employé"))
        self.labelPrenom.setText(_translate("DialogModifierEmploye", "Prénom de l\'employé"))
        self.labelPoste.setText(_translate("DialogModifierEmploye", "Poste de l\'employé"))
        self.comboBoxPoste.setItemText(0, _translate("DialogModifierEmploye", "Commis"))
        self.comboBoxPoste.setItemText(1, _translate("DialogModifierEmploye", "Caissier"))
        self.comboBoxPoste.setItemText(2, _translate("DialogModifierEmploye", "Gestionnaire"))
        self.comboBoxPoste.setItemText(3, _translate("DialogModifierEmploye", "Gerant"))
        self.labelSpecialite.setText(_translate("DialogModifierEmploye", "Spécialité de l\'employé"))
        self.labelDateEngagement.setText(_translate("DialogModifierEmploye", "Date d\'engagement de l\'employé"))
        self.labelDatePromotion.setText(_translate("DialogModifierEmploye", "Date de promotion"))
        self.pushButtonModifierEmploye.setText(_translate("DialogModifierEmploye", "Modifier l\'employé"))
        self.pushButtonAnnuler.setText(_translate("DialogModifierEmploye", "Annuler"))
        self.labelTitreModifierEmploye.setText(_translate("DialogModifierEmploye", "Modifier un employé"))
