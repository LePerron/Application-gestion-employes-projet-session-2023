from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_confirmation
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
from PyQt5 import QtWidgets
import sys


class Confirmation(QtWidgets.QDialog, genere_confirmation.Ui_DialogConfirmation):
    """
    Nome de la classe : Confirmation
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_confirmation.Ui_DialogConfirmation : Ma classe générée avec QtDesigner
    """

    def __init__(self, modification_employe=None, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_confirmation.Ui_DialogConfirmation
        """
        super(Confirmation, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Confirmer la suppression")

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre Confirmation lorsque l'utilisateur clique sur le bouton Annuler
        """
        Confirmation.close(self)

    @pyqtSlot()
    def on_pushButtonConfirmation_clicked(self):
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

        employe_temporaire = eval(poste)()

        if self.modification_employe:
            Employe.list_employe.remove(self.modification_employe)
            employe_temporaire.identifiant = identifiant
        else:
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
                    fenetre_ajouter_contrat.show()
                    fenetre_ajouter_contrat.exec()
                self.close()
        else:
            Employe.list_employe.remove(employe_temporaire)


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_confirmation = Confirmation()
    fenetre_confirmation.show()
    app.exec()


if __name__ == "__main__":
    main()
