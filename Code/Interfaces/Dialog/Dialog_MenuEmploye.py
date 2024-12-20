import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Employe import AjouterEmploye
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_employe
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSuperviseur import MenuSuperviseur
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_confirmation import Confirmation


class MenuEmploye(QtWidgets.QDialog, genere_menu_employe.Ui_DialogMenuEmploye):
    """
    Nome de la classe : MenuEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_employe.Ui_DialogMenuEmploye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_employe.Ui_DialogMenuEmploye
        """
        super(MenuEmploye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Employés")
        self.checkBoxIdentifiant.stateChanged.connect(self.mettre_a_jour_listview)
        self.checkBoxNomComplet.stateChanged.connect(self.mettre_a_jour_listview)
        self.checkBoxPosteComplet.stateChanged.connect(self.mettre_a_jour_listview)
        self.checkBoxSalaire.stateChanged.connect(self.salaire_checkbox_change)
        self.checkBoxAnciennete.stateChanged.connect(self.anciennete_checkbox_change)
        self.checkBoxContrat.stateChanged.connect(self.mettre_a_jour_listview)
        self.checkBoxDateEngagement.stateChanged.connect(self.mettre_a_jour_listview)
        self.comboBoxTrierEmploye.currentIndexChanged.connect(self.mettre_a_jour_listview)
        self.lineEditRechercherEmploye.textChanged.connect(self.mettre_a_jour_listview)

        self.mettre_a_jour_listview()

    # def obtenir_type_de_donnees_pour_maj(self, type_donnees):
    #     if type_donnees == "liste_employe"

    def mettre_a_jour_listview(self):
        """
        Modifie la listview lorsque l'utilisateur ajoute ou modifie un employe
        """
        liste_employe = self.rechercher_par_lettre()

        model = QStandardItemModel()
        self.listViewEmploye.setModel(model)
        current_index = self.comboBoxTrierEmploye.currentIndex()

        if liste_employe is None:
            liste_employe = Employe.list_employe

        if current_index == 0:
            employe_tries = sorted(liste_employe, key=lambda x: x.nom)

        elif current_index == 1:
            employe_tries = sorted(liste_employe, key=lambda x: x.nom, reverse=True)

        elif current_index == 2:
            employe_tries = sorted(liste_employe, key=lambda x: x.contrat.salaire_horaire)

        elif current_index == 3:
            employe_tries = sorted(liste_employe, key=lambda x: x.contrat.salaire_horaire, reverse=True)

        elif current_index == 4:
            employe_tries = sorted(liste_employe, key=lambda x: x.obtenir_anciennete)

        elif current_index == 5:
            list_tries_croissant = sorted(liste_employe, key=lambda x: x.obtenir_anciennete)
            employe_tries = list_tries_croissant[::-1]

        if current_index in range(5):
            for employe in employe_tries:
                item = QStandardItem(employe.afficher_informations_employe(self.checkBoxIdentifiant.isChecked(),
                                                                           self.checkBoxNomComplet.isChecked(),
                                                                           self.checkBoxPosteComplet.isChecked(),
                                                                           self.checkBoxContrat.isChecked(),
                                                                           self.checkBoxSalaire.isChecked(),
                                                                           self.checkBoxAnciennete.isChecked(),
                                                                           self.checkBoxDateEngagement.isChecked()))
                model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuEmploye lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        """
        Ouvre la fenêtre AjouterEmploye lorsque l'utilisateur click sur le bouton Ajouter un employe
        """

        dialog_ajouter_employe = AjouterEmploye()
        dialog_ajouter_employe.show()
        dialog_ajouter_employe.exec()
        self.mettre_a_jour_listview()

    @pyqtSlot()
    def on_pushButtonModifierEmploye_clicked(self):
        """
        Modifie l'employé lorsque l'utilisateur click sur le bouton Modifier l'employe
        """
        self.labelErreurSelection.clear()
        index_actuel = self.listViewEmploye.currentIndex()

        if index_actuel.isValid():
            employe_a_modifier = Employe.list_employe[index_actuel.row()]

            fenetre_modifier_employe = AjouterEmploye(modification_employe=employe_a_modifier)
            fenetre_modifier_employe.show()
            fenetre_modifier_employe.labelTitreAjouterEmploye.setText("Modifier l'employé")
            fenetre_modifier_employe.pushButtonAjouterEmploye.setText("Modifier")
            fenetre_modifier_employe.setWindowTitle("Modification d'un employé")

            fenetre_modifier_employe.dateEditDateEngagement.setMinimumDate(employe_a_modifier.date_engagement)
            fenetre_modifier_employe.dateEditDatePromotion.setMinimumDate(employe_a_modifier.date_engagement)
            fenetre_modifier_employe.comboBoxSpecialite.setCurrentText(employe_a_modifier.specialite.nom)
            fenetre_modifier_employe.lineEditIdentifiant.setText(employe_a_modifier.identifiant)
            fenetre_modifier_employe.comboBoxPoste.setCurrentText(employe_a_modifier.poste)
            fenetre_modifier_employe.lineEditPrenom.setText(employe_a_modifier.prenom)
            fenetre_modifier_employe.lineEditNom.setText(employe_a_modifier.nom)
            fenetre_modifier_employe.dateEditDateEngagement.setReadOnly(True)
            fenetre_modifier_employe.lineEditIdentifiant.setReadOnly(True)

            fenetre_modifier_employe.exec()
            self.mettre_a_jour_listview()
        else:
            self.labelErreurSelection.setText("Veuillez sélectionner l'employé que vous souhaitez modifier")

    @pyqtSlot()
    def on_pushButtonSupprimerEmploye_clicked(self):
        """
        Supprime l'employé lorsque l'utilisateur click sur le bouton Supprimer l'employer
        """
        index_actuel = self.listViewEmploye.currentIndex()
        if index_actuel.isValid():
            fenetre_confirmation = Confirmation()
            fenetre_confirmation.show()
            fenetre_confirmation.exec()
            if Confirmation.confirme:
                self.listViewEmploye.model().removeRow(index_actuel.row())
                Employe.list_employe.pop(index_actuel.row())
        else:
            self.labelErreurSelection.setText("Veuillez sélectionner l'employé que vous souhaitez supprimer")

    def salaire_checkbox_change(self, status):
        """
        affiche le salaire quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        """
        self.mettre_a_jour_listview()
        if status == 2:
            self.comboBoxTrierEmploye.addItem("Croissant ($)")
            self.comboBoxTrierEmploye.addItem("Décroissant ($)")
        else:
            self.comboBoxTrierEmploye.findText(
                self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant ($)")))
            self.comboBoxTrierEmploye.findText(
                self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant ($)")))

    def rechercher_par_lettre(self):
        """
        Rechercher un employe selon un groupe de lettre
        """
        lettres_a_rechercher = self.lineEditRechercherEmploye.text()
        if lettres_a_rechercher is not None:
            if len(lettres_a_rechercher) > 0:
                liste_employe_valide = []
                index = len(lettres_a_rechercher)
                for employe in Employe.list_employe:

                    prenom_employe = employe.prenom[:index]
                    if prenom_employe.lower() == lettres_a_rechercher.lower():
                        liste_employe_valide.append(employe)
                return liste_employe_valide

    def anciennete_checkbox_change(self, status):
        """
        affiche l'ancienneté quand le checkbox est coché
        :param status: le status de la checkbox (coché ou non)
        """
        self.mettre_a_jour_listview()
        if status == 2:
            self.comboBoxTrierEmploye.addItem("Croissant (anciennté)")
            self.comboBoxTrierEmploye.addItem("Décroissant (anciennté)")
        else:
            self.comboBoxTrierEmploye.findText(
                self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant (anciennté)")))
            self.comboBoxTrierEmploye.findText(
                self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant (anciennté)")))


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_employe = MenuEmploye()
    fenetre_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
