from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_principal
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSpecialite import MenuSpecialites
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuContrats import MenuContrats
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuEmploye import MenuEmployes
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuPayes import MenuPayes
from PyQt5 import QtWidgets
import sys


class MenuPrincipal(QtWidgets.QMainWindow, genere_menu_principal.Ui_MainsWindowIntra):
    """
    Nome de la classe : MenuPrincipal
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - genere_menu_principal.Ui_MainsWindowIntra : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et genere_menu_principal.Ui_MainsWindowIntra
        """
        super(MenuPrincipal, self).__init__(parent)
        self.setupUi(self)

    def on_pushButtonQuitter_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        sys.exit()

    def on_pushButtonMenuEmployer_clicked(self):
        Dialog_MenuEmploye.M




def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_principale = MenuPrincipal()
    fenetre_principale.show()
    app.exec()


if __name__ == "__main__":
    main()
