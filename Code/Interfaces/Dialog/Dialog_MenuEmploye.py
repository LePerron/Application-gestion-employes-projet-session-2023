import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
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
        self.comboBoxTrierEmploye.currentIndexChanged.connect(self.mettre_a_jour_listview(self.comboBoxTrierEmploye.currentIndex()))
        self.mettre_a_jour_listview()

    def mettre_a_jour_listview(self, current_index=None):
        """
        Modifie la listview lorsque l'utilisateur ajoute ou modifie un employe
        """
        model = QStandardItemModel()
        self.listViewEmploye.setModel(model)

<<<<<<< HEAD
        if current_index == 0
=======
>>>>>>> 03be817f80c941544f9e8e4d7c90b1882bc1bd0b
        dictionnaire_triage = {}
        for employe in Employe.list_employe:
            dictionnaire_triage[employe.nom] = employe

        if current_index == 0:
            dictionnaire_triage = sorted(dictionnaire_triage.keys())
        elif current_index == 1:
            dictionnaire_triage = sorted(dictionnaire_triage.keys()).reverse()
        for nom_employe in dictionnaire_triage:
            employe = dictionnaire_triage[nom_employe]
            item = QStandardItem(str(employe.afficher_informations_employe(self.checkBoxIdentifiant.isChecked(), self.checkBoxNomComplet.isChecked(), self.checkBoxPosteComplet.isChecked(), self.checkBoxContrat.isChecked(), self.checkBoxSalaire.isChecked(), self.checkBoxAnciennete.isChecked(), self.checkBoxDateEngagement.isChecked())))
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
            fenetre_modifier_employe.comboBoxSpecialite.setCurrentText(employe_a_modifier.specialite)
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
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant ($)")))
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant ($)")))

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
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant (anciennté)")))
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant (anciennté)")))

    def trier_a_z_list_view(self):
        ifn
    def trier_z_a_list_view(self):
    def trier_croissant_salaire_list_view(self):
    def trier_decroissant_salaire_list_view(self):
    def trier_croissant_anciennete_list_view(self):

    def trier_decroissant_anciennete_list_view(self):

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
