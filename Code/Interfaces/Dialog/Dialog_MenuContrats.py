from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_contrats
from PyQt5 import QtWidgets
import sys


class MenuContrats(QtWidgets.QWidget, genere_menu_contrats.Ui_MainsWindowIntra):
    """
    Nome de la classe : MenuContrats
    Héritages :
    - QtWidgets.Ui_MainsWindowIntra : Type d'interface créé par QtDesigner
    - genere_menu_contrats.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et genere_menu_contrats.Ui_MainsWindowIntra
        """
        super(MenuContrats, self).__init__(parent)
        self.setupUi(self)

    def on_pushButtonQuitter_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        sys.exit()

    def on_pushButtonQuitter_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        sys.exit()



def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_principale = MenuContrats()
    fenetre_principale.show()
    app.exec()


if __name__ == "__main__":
    main()
