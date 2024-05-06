from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class ModifierEmploye(QtWidgets.QDialog, genere_ajouter_employe.Ui_DialogAjouterEmploye):
    """
    Nome de la classe : ModifierEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_ajouter_employe.Ui_DialogAjouterEmployer : Ma classe générée avec QtDesigner
    """

    def __init__(self, identifiant_employe, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_ajouter_employe.Ui_DialogAjouterEmploye
        """
        super(ModifierEmploye, self).__init__(parent)
        self.setupUi(self)
        self.labelTitreAjouterEmploye.setText("Modifier l'employé")
        self.pushButtonAjouterEmploye.setText("Modifier")
        self.setWindowTitle("Modification d'un employé")
        self.lineEditIdentifiant.setReadOnly(True)
        self.labelIdentifiantEmploye.setText(identifiant_employe)


    @pyqtSlot()
    def on_pushButtonModifierEmploye_clicked(self):
        if not self.comboBoxPoste.currentText():
            post = Employe()
        else:
            poste = self.comboBoxPoste.currentText()

        employe_temporaire = eval(poste())

        nom = self.lineEditNom.text().capitalize()
        employe_temporaire.nom = nom
        if employe_temporaire.nom != nom:
            self.labelErreurNom.setText("Erreur")
            self.lineEditNom.clear()

        prenom = self.lineEditPrenom.text().capitalize()
        employe_temporaire.prenom = prenom
        if employe_temporaire.prenom != prenom:
            self.labelErreurPrenom.setText("Erreur")
            self.lineEditPrenom.clear()

        specialite = self.comboBoxSpecialite.itemText()
        employe_temporaire.specialite = specialite

        date_engagement = self.dateEditDateEngagement.text()
        employe_temporaire.date_engagement = date_engagement

        if poste == "Gerant" or "Gestionnnaire":
            date_promotion = self.dateEditDatePromotion.text()
            employe_temporaire.date_promotion = date_promotion

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        ModifierEmploye.close(self)


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_employe = ModifierEmploye()
    fenetre_ajouter_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
