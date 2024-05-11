from datetime import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_contrat
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat


class MenuContrats(QtWidgets.QDialog, genere_menu_contrat.Ui_DialogContratEmploye):
    """
    Nome de la classe : MenuContrats
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_contrat.Ui_DialogContratEmploye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_contrat.Ui_DialogContratEmploye
        """
        super(MenuContrats, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Contrats")
        self.dateEditContratSelonDate.setMaximumDate(datetime.now())
        self.lineEditAfficherContratSelonEmploye.textChanged.connect(self.mettre_a_jour_listview)
        self.mettre_a_jour_listview()


    def mettre_a_jour_listview(self):
        """
        Modifie la listview lorsque l'utilisateur ajoute ou modifie un contrat
        """
        liste_contrat = self.rechercher_par_lettre()
        model = QStandardItemModel()
        self.listViewContrat.setModel(model)
        if liste_contrat is None:
            liste_contrat = ContratEmploi.list_contrat
        for contrat in liste_contrat:
            item = QStandardItem(contrat.afficher_informations_contrat())
            model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuContrats lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuContrats.close(self)

    @pyqtSlot()
    def on_pushButtonModifierContrat_clicked(self):
        """
        Ouvre la fenêtre ModifierContrat lorsque l'utilisateur clique sur le bouton Modifier le contrat
        """
        index_actuel = self.listViewContrat.currentIndex()
        if index_actuel.isValid():
            self.listViewContrat.model().removeRow(index_actuel.row())
            employe = Employe.list_employe[index_actuel.row()]
            ContratEmploi.list_contrat.pop(index_actuel.row())
            fenetre_ajouter_contrat = AjouterContrat(employe)
            fenetre_ajouter_contrat.pushButtonAjouterEmploye.setText("Modifier")
            fenetre_ajouter_contrat.labelTitreAjouterContrat.setText("Modifier Contrat")
            fenetre_ajouter_contrat.setWindowTitle("Modifier Contrat")
            fenetre_ajouter_contrat.lineEditIdentifiant.setReadOnly(True)
            fenetre_ajouter_contrat.lineEditIdentifiant.setText(employe.identifiant)
            fenetre_ajouter_contrat.show()
            fenetre_ajouter_contrat.exec()
            self.mettre_a_jour_listview()
        else:
            self.labelErreurSelection.setText("Erreur.")

    def rechercher_par_lettre(self):
        """
        Rechercher un employe selon un groupe de lettre
        """
        lettres_a_rechercher = self.lineEditAfficherContratSelonEmploye.text()
        if lettres_a_rechercher is not None:
            if len(lettres_a_rechercher) > 0:
                liste_contrat_valide = []
                index = len(lettres_a_rechercher)
                for contrat in ContratEmploi.list_contrat:

                    prenom_employe = contrat.employe[:index]
                    if prenom_employe.lower() == lettres_a_rechercher.lower():
                        liste_contrat_valide.append(contrat)
                return liste_contrat_valide



def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_contrat = MenuContrats()
    fenetre_contrat.show()
    app.exec()


if __name__ == "__main__":
    main()
