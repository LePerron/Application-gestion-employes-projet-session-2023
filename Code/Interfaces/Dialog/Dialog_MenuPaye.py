from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_paye
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
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

        self.lcdNumberMaximum.hide()
        self.lcdNumberMinimum.hide()
        self.lcdNumberMoyenne.hide()
        self.lcdNumberMedianne.hide()

        self.checkBoxMax.stateChanged.connect(self.max_checkbox_change)
        self.checkBoxMin.stateChanged.connect(self.min_checkbox_change)
        self.checkBoxMoyenne.stateChanged.connect(self.moyenne_checkbox_change)
        self.checkBoxMedianne.stateChanged.connect(self.medianne_checkbox_change)

        self.calculer_toute_les_payes()
        self.mettre_a_jour_listview()

    @staticmethod
    def calculer_toute_les_payes():
        for employe in Employe.list_employe:
            paye = Paye()
            date_paye = datetime.now().strftime("%d/%m/%Y")
            paye.date_de_paye = datetime.strptime(str(date_paye), "%d/%m/%Y")
            paye.employe = employe.identifiant
            paye.montant_paye = float(employe.calculer_paye())

    def mettre_a_jour_listview(self):
        self.listViewPaye.reset()
        model = QStandardItemModel()
        self.listViewPaye.setModel(model)
        for paye in Paye.list_payes:
            item = QStandardItem(str(paye))
            model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuPaye lorsque l'utilisateur clique sur le bouton Retourner au menu
        """
        MenuPaye.close(self)

    @pyqtSlot()
    def on_pushButtonModifierContrat_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        """
        Ouvre la fenêtre AjouterContrat lorsque l'utilisateur clique sur le bouton Modifier le contrat
        """
        fenetre_modifier_contrat = AjouterContrat()
        fenetre_modifier_contrat.show()
        fenetre_modifier_contrat.exec()
        pass

    def max_checkbox_change(self, status):
        """
        affiche la valeur maximum quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        :return:
        """
        if status == 2:
            self.lcdNumberMaximum.show()
            self.lcdNumberMaximum.display(float(Paye.obtenir_paye_max()))
        else:
            self.lcdNumberMaximum.hide()

    def min_checkbox_change(self, status):
        """
        affiche la valeur minimum quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        """
        if status == 2:
            self.lcdNumberMinimum.show()
            self.lcdNumberMinimum.display(float(Paye.obtenir_paye_min()))

        else:
            self.lcdNumberMinimum.hide()

    def moyenne_checkbox_change(self, status):
        """
        affiche la moyenne quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        """
        if status == 2:
            self.lcdNumberMoyenne.show()
            self.lcdNumberMoyenne.display(float(Paye.calculer_moyenne_payes()))
        else:
            self.lcdNumberMoyenne.hide()

    def medianne_checkbox_change(self, status):
        """
        affiche la medianne quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        """
        if status == 2:
            self.lcdNumberMedianne.show()
            self.lcdNumberMedianne.display(float(Paye.calculer_mediane_payes()))
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
