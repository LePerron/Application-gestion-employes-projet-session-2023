# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tout\Prog\Projet_intra_Entreprise\UI\Creer_contrat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCreerContrat(object):
    def setupUi(self, DialogCreerContrat):
        DialogCreerContrat.setObjectName("DialogCreerContrat")
        DialogCreerContrat.resize(391, 737)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        DialogCreerContrat.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        DialogCreerContrat.setFont(font)
        DialogCreerContrat.setModal(False)
        self.labelTitreAjouterContrat = QtWidgets.QLabel(DialogCreerContrat)
        self.labelTitreAjouterContrat.setGeometry(QtCore.QRect(0, 21, 381, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.labelTitreAjouterContrat.setFont(font)
        self.labelTitreAjouterContrat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTitreAjouterContrat.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreAjouterContrat.setObjectName("labelTitreAjouterContrat")
        self.line = QtWidgets.QFrame(DialogCreerContrat)
        self.line.setGeometry(QtCore.QRect(10, 50, 370, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(DialogCreerContrat)
        self.frame.setGeometry(QtCore.QRect(0, 70, 391, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 23, 351, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelIdentifiantEmploye = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.labelIdentifiantEmploye.setFont(font)
        self.labelIdentifiantEmploye.setObjectName("labelIdentifiantEmploye")
        self.verticalLayout_8.addWidget(self.labelIdentifiantEmploye)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditIdentifiant = QtWidgets.QLineEdit(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(156, 156, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 156, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.lineEditIdentifiant.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lineEditIdentifiant.setFont(font)
        self.lineEditIdentifiant.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lineEditIdentifiant.setMouseTracking(False)
        self.lineEditIdentifiant.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEditIdentifiant.setAutoFillBackground(False)
        self.lineEditIdentifiant.setFrame(False)
        self.lineEditIdentifiant.setReadOnly(False)
        self.lineEditIdentifiant.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditIdentifiant.setClearButtonEnabled(False)
        self.lineEditIdentifiant.setObjectName("lineEditIdentifiant")
        self.verticalLayout.addWidget(self.lineEditIdentifiant)
        self.labelErreurIdentifiant = QtWidgets.QLabel(self.layoutWidget)
        self.labelErreurIdentifiant.setText("")
        self.labelErreurIdentifiant.setObjectName("labelErreurIdentifiant")
        self.verticalLayout.addWidget(self.labelErreurIdentifiant)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.labelFacteur = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelFacteur.setFont(font)
        self.labelFacteur.setScaledContents(False)
        self.labelFacteur.setObjectName("labelFacteur")
        self.verticalLayout_8.addWidget(self.labelFacteur)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doubleSpinBoxFacteur = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBoxFacteur.setFont(font)
        self.doubleSpinBoxFacteur.setSingleStep(0.5)
        self.doubleSpinBoxFacteur.setObjectName("doubleSpinBoxFacteur")
        self.verticalLayout_2.addWidget(self.doubleSpinBoxFacteur)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.labelNbHeure = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNbHeure.setFont(font)
        self.labelNbHeure.setObjectName("labelNbHeure")
        self.verticalLayout_8.addWidget(self.labelNbHeure)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lcdNumberNbHeure = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumberNbHeure.setGeometry(QtCore.QRect(0, 8, 55, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumberNbHeure.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lcdNumberNbHeure.setFont(font)
        self.lcdNumberNbHeure.setAutoFillBackground(True)
        self.lcdNumberNbHeure.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumberNbHeure.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberNbHeure.setLineWidth(1)
        self.lcdNumberNbHeure.setMidLineWidth(0)
        self.lcdNumberNbHeure.setSmallDecimalPoint(False)
        self.lcdNumberNbHeure.setDigitCount(2)
        self.lcdNumberNbHeure.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumberNbHeure.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberNbHeure.setObjectName("lcdNumberNbHeure")
        self.labelHeure = QtWidgets.QLabel(self.frame_2)
        self.labelHeure.setGeometry(QtCore.QRect(41, 10, 21, 36))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.labelHeure.setFont(font)
        self.labelHeure.setObjectName("labelHeure")
        self.horizontalSliderNbHeure = QtWidgets.QSlider(self.frame_2)
        self.horizontalSliderNbHeure.setGeometry(QtCore.QRect(64, 10, 271, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.horizontalSliderNbHeure.sizePolicy().hasHeightForWidth())
        self.horizontalSliderNbHeure.setSizePolicy(sizePolicy)
        self.horizontalSliderNbHeure.setMinimumSize(QtCore.QSize(4, 0))
        self.horizontalSliderNbHeure.setSizeIncrement(QtCore.QSize(2, 4))
        self.horizontalSliderNbHeure.setBaseSize(QtCore.QSize(4, 0))
        self.horizontalSliderNbHeure.setAutoFillBackground(True)
        self.horizontalSliderNbHeure.setMaximum(40)
        self.horizontalSliderNbHeure.setPageStep(1)
        self.horizontalSliderNbHeure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderNbHeure.setInvertedAppearance(False)
        self.horizontalSliderNbHeure.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSliderNbHeure.setObjectName("horizontalSliderNbHeure")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.labelSalaireHoraire = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelSalaireHoraire.setFont(font)
        self.labelSalaireHoraire.setObjectName("labelSalaireHoraire")
        self.verticalLayout_8.addWidget(self.labelSalaireHoraire)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.doubleSpinBoxSalaireHoraire = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxSalaireHoraire.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxSalaireHoraire.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBoxSalaireHoraire.setFont(font)
        self.doubleSpinBoxSalaireHoraire.setWrapping(False)
        self.doubleSpinBoxSalaireHoraire.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxSalaireHoraire.setDecimals(2)
        self.doubleSpinBoxSalaireHoraire.setMinimum(15.75)
        self.doubleSpinBoxSalaireHoraire.setMaximum(50.0)
        self.doubleSpinBoxSalaireHoraire.setSingleStep(0.25)
        self.doubleSpinBoxSalaireHoraire.setProperty("value", 15.75)
        self.doubleSpinBoxSalaireHoraire.setObjectName("doubleSpinBoxSalaireHoraire")
        self.verticalLayout_6.addWidget(self.doubleSpinBoxSalaireHoraire)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.labelTermeContrat_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTermeContrat_2.sizePolicy().hasHeightForWidth())
        self.labelTermeContrat_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelTermeContrat_2.setFont(font)
        self.labelTermeContrat_2.setObjectName("labelTermeContrat_2")
        self.verticalLayout_8.addWidget(self.labelTermeContrat_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEditTermeContrat = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditTermeContrat.sizePolicy().hasHeightForWidth())
        self.textEditTermeContrat.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.textEditTermeContrat.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textEditTermeContrat.setFont(font)
        self.textEditTermeContrat.setObjectName("textEditTermeContrat")
        self.verticalLayout_5.addWidget(self.textEditTermeContrat)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.pushButtonAjouterEmploye = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonAjouterEmploye.setFont(font)
        self.pushButtonAjouterEmploye.setObjectName("pushButtonAjouterEmploye")
        self.verticalLayout_8.addWidget(self.pushButtonAjouterEmploye)
        self.pushButtonAnnuler = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonAnnuler.setFont(font)
        self.pushButtonAnnuler.setObjectName("pushButtonAnnuler")
        self.verticalLayout_8.addWidget(self.pushButtonAnnuler)

        self.retranslateUi(DialogCreerContrat)
        self.horizontalSliderNbHeure.valueChanged['int'].connect(self.lcdNumberNbHeure.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogCreerContrat)

    def retranslateUi(self, DialogCreerContrat):
        _translate = QtCore.QCoreApplication.translate
        DialogCreerContrat.setWindowTitle(_translate("DialogCreerContrat", "Dialog"))
        self.labelTitreAjouterContrat.setText(_translate("DialogCreerContrat", "Contrat de l\'employé"))
        self.labelIdentifiantEmploye.setText(_translate("DialogCreerContrat", "Identifiant de l\'employé"))
        self.lineEditIdentifiant.setText(_translate("DialogCreerContrat", "1234567"))
        self.labelFacteur.setText(_translate("DialogCreerContrat", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:400;\">Facteur de salaire </span><span style=\" font-size:7pt; font-weight:400;\">(% du salaire minimum)</span></p></body></html>"))
        self.doubleSpinBoxFacteur.setSuffix(_translate("DialogCreerContrat", "%"))
        self.labelNbHeure.setText(_translate("DialogCreerContrat", "Nombre d\'heure par semaine"))
        self.labelHeure.setText(_translate("DialogCreerContrat", "h"))
        self.labelSalaireHoraire.setText(_translate("DialogCreerContrat", "Salaire horaire"))
        self.doubleSpinBoxSalaireHoraire.setSuffix(_translate("DialogCreerContrat", "$ /h"))
        self.labelTermeContrat_2.setText(_translate("DialogCreerContrat", "<html><head/><body><p>Autres termes <span style=\" vertical-align:sub;\">(optionnel)</span></p></body></html>"))
        self.pushButtonAjouterEmploye.setText(_translate("DialogCreerContrat", "Créer l\'employé son contrat"))
        self.pushButtonAnnuler.setText(_translate("DialogCreerContrat", "Annuler"))
