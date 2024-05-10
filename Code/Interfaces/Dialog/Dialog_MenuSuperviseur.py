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


# Cette classe permet au programme d'avoir une listview personnalisée avec des évènements de sélection.
class ListModeleSelectionnable(QAbstractListModel):
    def __init__(self, donnees=None, parent=None):
        super().__init__(parent)
        if donnees is None:
            donnees = []
        self._donnees = donnees

    def rowCount(self, parent):
        return len(self._donnees)

    def data(self, index, role):
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
                    if self.checkBoxCommis.isChecked():
                        employe.mettre_a_jour_dict_de_commis()
                        liste_donnees = []
                        liste_donnees.append(caissier.prenom for caissier in superviseur_selectionne.dict_commis)

                    if self.checkBoxCaissier.isChecked():
                        employe.mettre_a_jour_list_caissier()
                        liste_donnees = [caissier.prenom for caissier in superviseur_selectionne.liste_caissier]
                else:
                    liste_donnees = [gestionnaire.prenom for gestionnaire in superviseur_selectionne.liste_gestionnaire]

                modele = ListModeleSelectionnable(liste_donnees)
                self.listViewCommisCaissier.setModel(modele)

    #
    # def mettre_a_jour_listview_superviseur(self):
    #     model_superviseur = QStandardItem()
    #     self.listViewGerantGestionnaire.selectionModel()
    #
    #     dict_superviseur = {}
    #
    #     if self.checkBoxGestionnaire.isChecked():
    #         for gestionnaire in Gestionnaire.list_gestionnaire:
    #             dict_superviseur[gestionnaire] = gestionnaire.nom
    #
    #     if self.checkBoxGerant.isChecked():
    #         for gerant in Gerant.list_gerant:
    #             dict_superviseur[gerant] = gerant.nom
    #
    #     for superviseur in dict_superviseur.keys():
    #         item = QStandardItem(superviseur)
    #         model_superviseur.appendRow(item)

    # def mettre_a_jour_listview_employe_gere(self):
    #     superviseur_actuel = self.tableWidget.currentIndex().data()
    #     model_employe_gere = QStandardItemModel()
    #     dict_employe_gere = {}
    #
    #     if superviseur_actuel.poste != "Gerant":
    #         if self.checkBoxCommis.isChecked():
    #             for commis in superviseur_actuel.list_commis:
    #                 dict_employe_gere[commis] = commis.nom
    #
    #         if self.checkBoxCaissier.isChecked():
    #             for caissier in superviseur_actuel.list_caissier:
    #                 dict_employe_gere[caissier] = caissier.nom
    #     else:
    #         if self.checkBoxGestionnaire.isChecked():
    #             for gestionnaire in superviseur_actuel.liste_gestionnaire:
    #                 dict_employe_gere[gestionnaire] = gestionnaire.nom
    #
    #     for employe_gere in dict_employe_gere.items():
    #         item = QStandardItem(employe_gere)
    #         model_employe_gere.appendRow(item)

    # def mettre_a_jour_listview(self, listview):
    #     """
    #     Modifie la listview lorsque l'utilisateur ajoute ou modifie un contrat
    #     """
    #     if listview == "superviseur":
    #         model_superviseur = QStandardItemModel()
    #
    #         if self.checkBoxGerant.isChecked():
    #             for gerant in Gerant.list_gerant:
    #                 item = QStandardItem(gerant.nom)
    #                 model_superviseur.appendRow(item)
    #
    #         if self.checkBoxGestionnaire.isChecked():
    #             for gestionnaire in Gestionnaire.list_gestionnaire:
    #                 item = QStandardItem(gestionnaire.nom)
    #                 model_superviseur.appendRow(item)
    #         self.tableWidget.setModel(model_superviseur)
    #
    #     else:
    #         superviseur_selectionne = self.tableWidget.selectionModel().currentIndex()
    #         if superviseur_selectionne:
    #             model_commis_caissier = QStandardItemModel()
    #             if self.checkBoxCaissier.isChecked():
    #                 for employe in Employe.list_employe:
    #                     if employe.nom == superviseur_selectionne:
    #                         for caissier in employe.liste_caissier:
    #                             item = QStandardItem(caissier.nom)
    #                             model_commis_caissier.appendRow(item)
    #
    #             if self.checkBoxCommis.isChecked():
    #                 for employe in Employe.list_employe:
    #                     if employe.nom == superviseur_selectionne:
    #                         for commis in employe.dict_commis.values():
    #                             item = QStringListModel(commis.nom)
    #                             model_commis_caissier.appendRow(item)
    #
    #             self.listViewCommisCaissier.setModel(model_commis_caissier)

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
            # rangee_selectionnee = index_selectionnes[0].row()
            superviseur_selectionne = self.listViewGerantGestionnaire.model().data(index_selectionnes[0],
                                                                                   Qt.DisplayRole)
            self.peupler_liste_caissier_commis(superviseur_selectionne)

            return superviseur_selectionne

    def caissier_change(self, status):
        """
        Affiche les caissiers si coché
        :param status: le status de la checkbox (coché ou non)
        """
        nom_superviseur_actuel = self.tableWidget.currentIndex()
        if nom_superviseur_actuel.isValid():
            self.mettre_a_jour_listview("employe", nom_superviseur_actuel)
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
        nom_superviseur_actuel = self.tableWidget.currentIndex()
        if nom_superviseur_actuel.isValid():
            self.mettre_a_jour_listview("employe", nom_superviseur_actuel)
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
        self.mettre_a_jour_listview_superviseur()
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
        self.mettre_a_jour_listview_superviseur()
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
