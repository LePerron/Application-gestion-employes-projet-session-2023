from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant

from PyQt5.QtCore import pyqtSlot
from datetime import datetime
from PyQt5 import QtWidgets
import sys


class AjouterEmploye(QtWidgets.QDialog, genere_ajouter_employe.Ui_DialogAjouterEmploye):
    """
    Nome de la classe : AjouterEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_ajouter_employe.Ui_DialogAjouterEmployer : Ma classe générée avec QtDesigner
    """

    def __init__(self, modification_employe=None, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_ajouter_employe.Ui_DialogAjouterEmploye
        :param modification_employe: L'employé à modifier sinon rien
        """
        super(AjouterEmploye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un Employé")
        self.labelDatePromotion.hide()
        self.dateEditDatePromotion.hide()
        self.labelErreurDatePromotion.hide()
        self.dateEditDatePromotion.setMaximumDate(datetime.now())
        self.dateEditDateEngagement.setMaximumDate(datetime.now())
        self.comboBoxPoste.activated.connect(self.index_combobox_change)
        self.reset_label_erreur()
        self.modification_employe = modification_employe

        for specialite in Specialite.list_des_specialites:
            self.comboBoxSpecialite.addItem(specialite.nom)

    def reset_label_erreur(self):
        """
        Retire les messages d'erreurs
        """
        self.labelErreurNom.clear()
        self.labelErreurPrenom.clear()
        self.labelErreurDateEngagement.clear()
        self.labelErreurDatePromotion.clear()
        self.labelErreurIdentifiant.clear()

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre AjouterEmploye lorsque l'utilisateur clique sur le bouton Annuler
        """
        AjouterEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        """
        Ajoute un nouveau employé lorsque l'utilisateur clique sur le bouton Ajouter un employe
        """
        self.reset_label_erreur()

        specialite = self.comboBoxSpecialite.currentText()
        prenom = self.lineEditPrenom.text().capitalize()
        identifiant = self.lineEditIdentifiant.text()
        nom = self.lineEditNom.text().capitalize()
        date_engagement = self.dateEditDateEngagement.text()
        poste = self.comboBoxPoste.currentText()

        if self.modification_employe:
            employe_temporaire = eval(poste)(p_contrat=self.modification_employe.contrat)
            Employe.list_employe.remove(self.modification_employe)

        else:
            employe_temporaire = eval(poste)()

            employe_temporaire.identifiant = identifiant
            if employe_temporaire.identifiant != identifiant or not identifiant:
                self.labelErreurIdentifiant.setText("Veuillez entrer un identifiant valide de 7 chiffre")
                self.lineEditIdentifiant.clear()

        employe_temporaire.nom = nom
        if employe_temporaire.nom != nom or not nom:
            self.labelErreurNom.setText("Veuillez entrer un nom valide (peut contenir '-').")
            self.lineEditNom.clear()

        employe_temporaire.prenom = prenom
        if employe_temporaire.prenom != prenom or not prenom:
            self.labelErreurPrenom.setText("Veuillez entrer un prénom valide (peut contenir '-').")
            self.lineEditPrenom.clear()

        employe_temporaire.specialite = specialite
        if employe_temporaire.specialite != specialite or not specialite:
            self.labelErreurSpecialite.setText("Veuillez d'abord créer une spécialité dans le menu spécialité")

        employe_temporaire.date_engagement = date_engagement

        if poste == "Gerant" or "Gestionnnaire":
            date_promotion = self.dateEditDatePromotion.text()
            employe_temporaire.date_promotion = date_promotion

        if nom and prenom and identifiant and specialite:
            if employe_temporaire.identifiant == identifiant and employe_temporaire.nom == nom and employe_temporaire.prenom == prenom:
                if not self.modification_employe:
                    fenetre_ajouter_contrat = AjouterContrat(employe_temporaire)
                    fenetre_ajouter_contrat.lineEditIdentifiant.setText(employe_temporaire.identifiant)
                    fenetre_ajouter_contrat.show()
                    fenetre_ajouter_contrat.exec()
                self.close()
        else:
            Employe.list_employe.remove(employe_temporaire)

    def index_combobox_change(self, index):
        """

        :param index:
        :return:
        """
        if index >= 2:
            self.labelDatePromotion.show()
            self.dateEditDatePromotion.show()
            self.labelErreurDatePromotion.show()
        else:
            self.labelDatePromotion.hide()
            self.dateEditDatePromotion.hide()
            self.labelErreurDatePromotion.hide()


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_employe = AjouterEmploye()
    fenetre_ajouter_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
