from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from PyQt5.QtCore import pyqtSlot
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

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        AjouterEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        pass


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
