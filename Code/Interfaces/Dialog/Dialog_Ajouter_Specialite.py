from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_creer_specialite
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class AjouterSpecialite(QtWidgets.QDialog, genere_creer_specialite.Ui_DialogCreerSpecialite):
    """
    Nome de la classe : AjouterSpecialite
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_creer_specialite.Ui_DialogCreerSpecialite : Ma classe générée avec QtDesigner
    """

    def __init__(self, specialite_modification=None, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_creer_specialite.Ui_DialogCreerSpecialite
        :param specialite_modification: La spécialité à modifier sinon rien
        """
        super(AjouterSpecialite, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter une spécialité")
        self.specialite_modification = specialite_modification

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        """
        Ferme la fenêtre AjouterSpecialite lorsque l'utilisateur clique sur le bouton Annuler
        """
        AjouterSpecialite.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterSpecialite_clicked(self):
        """
        Ajoute une nouvelle specialite lorsque l'utilisateur clique sur le bouton Ajouter une specialite
        """
        nom = self.lineEditNom.text().capitalize()
        description = self.textEditDescription.toPlainText()

        if self.specialite_modification:
            specialite_temporaire = Specialite.list_des_specialites[self.specialite_modification.row()]

        else:
            specialite_temporaire = Specialite()

        specialite_temporaire.nom = nom

        if specialite_temporaire.nom != nom or not nom:
            Specialite.list_des_specialites.remove(specialite_temporaire)
            self.labelErreurNom.setText("Nom incorrect")
            self.lineEditNom.clear()
        else:
            specialite_temporaire.description = description
            self.close()


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_specialite = AjouterSpecialite()
    fenetre_ajouter_specialite.show()
    app.exec()


if __name__ == "__main__":
    main()
