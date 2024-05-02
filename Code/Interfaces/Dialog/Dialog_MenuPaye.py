from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_paye
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class MenuPaye(QtWidgets.QDialog, genere_menu_paye.Ui_DialogMenuPaye):
    """
    Nome de la classe : MenuPaye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_paye.Ui_DialogMenuPaye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_paye.Ui_DialogMenuPaye
        """
        super(MenuPaye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Payes")

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuPaye.close(self)

    @pyqtSlot()
    def on_pushButtonModifierContrat_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        pass


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_paye = MenuPaye()
    fenetre_paye.show()
    app.exec()


if __name__ == "__main__":
    main()
