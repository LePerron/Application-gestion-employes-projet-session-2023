from PyQt5.QtCore import pyqtSlot

from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_employes
from PyQt5 import QtWidgets
import sys


class MenuEmployes(QtWidgets.QDialog, genere_menu_employes.Ui_DialogMenuEmploye):
    """
    Nome de la classe : MenuEmployes
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_employes.Ui_DialogMenuEmploye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_employes.Ui_DialogMenuEmploye
        """
        super(MenuEmployes, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuEmployes.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        dialog_ajouter_employe =

    @pyqtSlot()
    def on_pushButtonModifierEmploye_clicked(self):
        pass

    @pyqtSlot()
    def on_pushButtonSupprimerEmploye_clicked(self):
        pass


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_employe = MenuEmployes()
    fenetre_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
