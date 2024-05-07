from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_paye
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys



class MenuPaye(QtWidgets.QDialog, genere_menu_paye.Ui_DialogMenuPaye):
    """
    Nome de la classe : MenuPaye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_paye.Ui_DialogMenuPaye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_paye.Ui_DialogMenuPaye
        """
        super(MenuPaye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Payes")
        self.checkBoxMax.stateChanged.connect(self.max_checkbox_change)
        self.lcdNumberMaximum.hide()
        self.checkBoxMin.stateChanged.connect(self.min_checkbox_change)
        self.lcdNumberMinimum.hide()
        self.checkBoxMoyenne.stateChanged.connect(self.moyenne_checkbox_change)
        self.lcdNumberMoyenne.hide()
        self.checkBoxMedianne.stateChanged.connect(self.medianne_checkbox_change)
        self.lcdNumberMedianne.hide()
        model = QStandardItemModel()
        self.listViewPaye.setModel(model)
        for employe in Employe.list_employe:
            paye = Employe.calculer_paye(employe)
            item = QStandardItem(str(paye))
            model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuPaye lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuPaye.close(self)

    @pyqtSlot()
    def on_pushButtonModifierContrat_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        """
        Ouvre la fenêtre AjouterContrat lorsque l'utilisateur click sur le bouton Modifier le contrat
        """
        fenetre_modifier_contrat = AjouterContrat()
        fenetre_modifier_contrat.show()
        fenetre_modifier_contrat.exec()
        pass

    def max_checkbox_change(self, status):
        """

        :param status:
        :return:
        """
        if status == 2:
            self.lcdNumberMaximum.show()
        else:
            self.lcdNumberMaximum.hide()

    def min_checkbox_change(self, status):
        """

        :param status:
        :return:
        """
        if status == 2:
            self.lcdNumberMinimum.show()
        else:
            self.lcdNumberMinimum.hide()

    def moyenne_checkbox_change(self, status):
        """

        :param status:
        :return:
        """
        if status == 2:
            self.lcdNumberMoyenne.show()
        else:
            self.lcdNumberMoyenne.hide()

    def medianne_checkbox_change(self, status):
        """

        :param status:
        :return:
        """
        if status == 2:
            self.lcdNumberMedianne.show()
        else:
            self.lcdNumberMedianne.hide()


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_paye = MenuPaye()
    fenetre_paye.show()
    app.exec()


if __name__ == "__main__":
    main()
