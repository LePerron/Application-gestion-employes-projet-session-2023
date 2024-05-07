from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
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

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_ajouter_employe.Ui_DialogAjouterEmploye
        """
        super(AjouterEmploye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un Employé")
        self.labelDatePromotion.hide()
        self.dateEditDatePromotion.hide()
        self.labelErreurDatePromotion.hide()
        self.dateEditDatePromotion.setMaximumDate(datetime.now())
        self.dateEditDateEngagement.setMaximumDate(datetime.now())
        self.comboBoxSpecialite.addItem("Commis")
        self.comboBoxPoste.activated.connect(self.index_combobox_change)
        self.reset_label_erreur()

    def reset_label_erreur(self):
        self.labelErreurNom.clear()
        self.labelErreurPrenom.clear()
        self.labelErreurDateEngagement.clear()
        self.labelErreurDatePromotion.clear()
        self.labelErreurIdentifiant.clear()

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        AjouterEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        self.reset_label_erreur()
        poste = self.comboBoxPoste.currentText()

        employe_temporaire = eval(poste)()

        identifiant = self.lineEditIdentifiant.text()
        employe_temporaire.identifiant = identifiant
        if employe_temporaire.identifiant != identifiant or not identifiant:
            self.labelErreurIdentifiant.setText("Erreur")
            self.lineEditIdentifiant.clear()

        nom = self.lineEditNom.text().capitalize()
        employe_temporaire.nom = nom
        if employe_temporaire.nom != nom or not nom:
            self.labelErreurNom.setText("Erreur")
            self.lineEditNom.clear()

        prenom = self.lineEditPrenom.text().capitalize()
        if prenom:
            employe_temporaire.prenom = prenom
            if employe_temporaire.prenom != prenom or not prenom:
                self.labelErreurPrenom.setText("Erreur")
                self.lineEditPrenom.clear()

        specialite = self.comboBoxSpecialite.currentText()
        employe_temporaire.specialite = specialite

        date_engagement = self.dateEditDateEngagement.text()
        employe_temporaire.date_engagement = date_engagement

        if poste == "Gerant" or "Gestionnnaire":
            date_promotion = self.dateEditDatePromotion.text()
            employe_temporaire.date_promotion = date_promotion

        if employe_temporaire.nom and employe_temporaire.prenom and employe_temporaire.identifiant:
            if employe_temporaire.identifiant == identifiant and employe_temporaire.nom == nom and employe_temporaire.prenom == prenom:
                fenetre_ajouter_contrat = AjouterContrat(employe_temporaire.identifiant)
                fenetre_ajouter_contrat.show()
                fenetre_ajouter_contrat.exec()
                self.close()

    def index_combobox_change(self, index):
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
