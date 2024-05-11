from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_superviseur
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot, QAbstractListModel, Qt
from PyQt5 import QtWidgets
import sys

# Dans ce Menu Superviseur, c'est le seul endroit qui n'est pas complet au niveau des fonctionnalités
# C'est donc pas 100 % finis pour cette Fenetre de Dialog.
# CRASHs et BUGs possible.


# Cette classe permet au programme d'avoir une listview personnalisée avec des évènements de sélection.
class ListModeleSelectionnable(QAbstractListModel):
    def __init__(self, donnees=None, parent=None):
        super().__init__(parent)
        if donnees is None:
            donnees = []
        self._donnees = donnees

    def rowCount(self, parent):
        return len(self._donnees)

    def data(self, index , role):
        if role == Qt.DisplayRole:
            return self._donnees[index.row()].obtenir_nom_complet()


class MenuSuperviseur(QtWidgets.QDialog, genere_menu_superviseur.Ui_MenuSuperviseur):
    """
    Nome de la classe : MenuSuperviseur
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_superviseur.Ui_MenuSuperviseur : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_superviseur.Ui_MenuSuperviseur
        """
        super(MenuSuperviseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des superviseurs")
        self.checkBoxCaissier.stateChanged.connect(self.caissier_change)
        self.checkBoxCommis.stateChanged.connect(self.commis_change)
        self.checkBoxGestionnaire.stateChanged.connect(self.gestionnaire_change)
        self.checkBoxGerant.stateChanged.connect(self.gerant_change)

        self.peupler_liste_superviseur()
        self.listViewGerantGestionnaire.selectionModel().selectionChanged.connect(self.changement_selection_superviseur)

    def peupler_liste_superviseur(self):
        liste_superviseur = []
        if len(Employe.list_employe) > 0:
            for employe in Employe.list_employe:
                if employe.poste in ["Gerant", "Gestionnaire"]:
                    liste_superviseur.append(employe)

        modele = ListModeleSelectionnable(liste_superviseur)
        self.listViewGerantGestionnaire.setModel(modele)

    def peupler_liste_caissier_commis(self, superviseur_selectionne: str):
        for employe in Employe.list_employe:
            if employe.obtenir_nom_complet() != superviseur_selectionne:
                continue
            else:
                superviseur_selectionne = employe
                if superviseur_selectionne.poste == "Gestionnaire":
                    liste_donnees = []
                    if self.checkBoxCommis.isChecked():

                        for commis in Commis.list_commis:
                            if commis.gestionnaire == superviseur_selectionne.prenom:
                                liste_donnees.append(commis)


                    if self.checkBoxCaissier.isChecked():
                        for caissier in Caissier.liste_caissier:
                            if caissier.gestionnaire == superviseur_selectionne.prenom:
                                liste_donnees.append(caissier)

                    modele = ListModeleSelectionnable(liste_donnees)
                    self.listViewCommisCaissier.setModel(modele)
                else:
                    liste_donnees = superviseur_selectionne.liste_gestionnaire

                modele = ListModeleSelectionnable(liste_donnees)
                self.listViewCommisCaissier.setModel(modele)


    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuSuperviseur lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuSuperviseur.close(self)

    def changement_selection_superviseur(self, selected, deselected):
        index_selectionnes = selected.indexes()
        if index_selectionnes:
            superviseur_selectionne = self.listViewGerantGestionnaire.model().data(index_selectionnes[0],
                                                                                   Qt.DisplayRole)
            self.peupler_liste_caissier_commis(superviseur_selectionne)

            return superviseur_selectionne

    def caissier_change(self, status):
        """
        Affiche les caissiers si coché
        :param status: le status de la checkbox (coché ou non)
        """
        nom_superviseur_actuel = self.listViewCommisCaissier.currentIndex()
        if nom_superviseur_actuel.isValid():
            self.peupler_liste_caissier_commis(nom_superviseur_actuel)
            for employe in Employe.list_employe:
                if nom_superviseur_actuel == employe.gestionnaire:
                    if status == 2:
                        return
                    else:
                        employe.hide()

    def commis_change(self, status):
        """
        Affiche les commis si coché
        :param status: le status de checkbox (coché ou non)
        """
        nom_superviseur_actuel = self.listViewCommisCaissier.currentIndex()
        if nom_superviseur_actuel.isValid():
            self.peupler_liste_caissier_commis(nom_superviseur_actuel)
            for employe in Employe.list_employe:
                if nom_superviseur_actuel == employe.gestionnaire:
                    if status == 2:
                        return
                    else:
                        employe.hide()

    def gerant_change(self, status):
        """
        Affiche les gerants si coché
        :param status: le status de checkbox (coché ou non)
        """
        self.peupler_liste_superviseur()
        for employe in Employe.list_employe:
            if employe.poste == "Gerant":
                if status == 2:
                    return
                else:
                    employe.hide()

    def gestionnaire_change(self, status):
        """
        Affiche les gestionnaires si coché
        :param status: le status de checkbox (coché ou non)
        """
        self.peupler_liste_superviseur()
        for employe in Employe.list_employe:
            if employe.poste == "Gestionnaire":
                if status == 2:
                    return
                else:
                    employe.hide()


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_superviseur = MenuSuperviseur()
    fenetre_superviseur.show()
    app.exec()


if __name__ == "__main__":
    main()
