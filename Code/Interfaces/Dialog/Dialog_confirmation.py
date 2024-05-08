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

    def __init__(self, confirme=False, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_confirmation.Ui_DialogConfirmation
        :param confirme: La confirmation que l'annulation ou non doit avoir lieu (True ou False)
        """
        super(Confirmation, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Confirmer la suppression")
        self.confirme = confirme


    @pyqtSlot()
    def on_pushButtonNon_clicked(self):
        """
        Ferme la fenêtre Confirmation lorsque l'utilisateur clique sur le bouton Annuler
        """
        Confirmation.close(self)

    @pyqtSlot()
    def on_pushButtonOui_clicked(self):
        """
        Ajoute un nouveau employé lorsque l'utilisateur clique sur le bouton Ajouter un employe
        """
        Confirmation.confirme = True
        Confirmation.close(self)


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
