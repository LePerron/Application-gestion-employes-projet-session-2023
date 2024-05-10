from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_superviseur
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


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
        self.mettre_a_jour_listview_superviseur()

        self.listViewGerantGestionnaire.clicked.connect(self.mettre_a_jour_listview_superviseur)

    def mettre_a_jour_listview_superviseur(self):
        model_superviseur = QStandardItemModel()
        self.listViewGerantGestionnaire.setModel(model_superviseur)

        dict_superviseur = {}


        if self.checkBoxGestionnaire.isChecked():
            for gestionnaire in Gestionnaire.list_gestionnaire:
                dict_superviseur[gestionnaire.nom] = gestionnaire

        if self.checkBoxGerant.isChecked():
            for gerant in Gerant.list_gerant:
                dict_superviseur[gerant.nom] = gerant

        for superviseur in dict_superviseur.keys():
            item = QStandardItem(superviseur)
            model_superviseur.appendRow(item)

    def mettre_a_jour_listview_employe_gere(self):
        superviseur_actuel = self.listViewGerantGestionnaire.currentIndex().data()
        model_employe_gere = QStandardItemModel()
        dict_employe_gere = {}

        if superviseur_actuel.poste != "Gerant":
            if self.checkBoxCommis.isChecked():
                for commis in superviseur_actuel.list_commis:
                    dict_employe_gere[commis.nom] = commis

            if self.checkBoxCaissier.isChecked():
                for caissier in superviseur_actuel.list_caissier:
                    dict_employe_gere[caissier.nom] = caissier
        else:
            if self.checkBoxGestionnaire.isChecked():
                for gestionnaire in superviseur_actuel.liste_gestionnaire:
                    dict_employe_gere[gestionnaire.nom] = gestionnaire

        for employe_gere in dict_employe_gere.keys():
            item = QStandardItem(employe_gere)
            model_employe_gere.appendRow(item)

    def mettre_a_jour_listview(self, listview):
        """
        Modifie la listview lorsque l'utilisateur ajoute ou modifie un contrat
        """
        if listview == "superviseur":
            model_superviseur = QStandardItemModel()

            if self.checkBoxGerant.isChecked():
                for gerant in Gerant.list_gerant:
                    item = QStandardItem(gerant.nom)
                    model_superviseur.appendRow(item)

            if self.checkBoxGestionnaire.isChecked():
                for gestionnaire in Gestionnaire.list_gestionnaire:
                    item = QStandardItem(gestionnaire.nom)
                    model_superviseur.appendRow(item)
            self.listViewGerantGestionnaire.setModel(model_superviseur)

        else:
            superviseur_selectionne = self.listViewGerantGestionnaire.selectionModel().currentIndex()
            if superviseur_selectionne:
                model_commis_caissier = QStandardItemModel()
                if self.checkBoxCaissier.isChecked():
                    for employe in Employe.list_employe:
                        if employe.nom == superviseur_selectionne:
                            for caissier in employe.liste_caissier:
                                item = QStandardItem(caissier.nom)
                                model_commis_caissier.appendRow(item)

                if self.checkBoxCommis.isChecked():
                    for employe in Employe.list_employe:
                        if employe.nom == superviseur_selectionne:
                            for commis in employe.dict_commis.values():
                                item = QStandardItem(commis.nom)
                                model_commis_caissier.appendRow(item)

                self.listViewCommisCaissier.setModel(model_commis_caissier)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuSuperviseur lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuSuperviseur.close(self)

    def caissier_change(self, status):
        """
        Affiche les caissiers si coché
        :param status: le status de la checkbox (coché ou non)
        """
        nom_superviseur_actuel = self.listViewGerantGestionnaire.currentIndex()
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
        nom_superviseur_actuel = self.listViewGerantGestionnaire.currentIndex()
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
