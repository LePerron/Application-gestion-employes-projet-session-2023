from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_contrats
from PyQt5 import QtWidgets
import sys


class MenuContrats(QtWidgets.QWidget, genere_menu_contrats.Ui_MainsWindowIntra):
    """
    Nome de la classe : MenuContrats
    H�ritages :
    - QtWidgets.Ui_MainsWindowIntra : Type d'interface cr�� par QtDesigner
    - genere_menu_contrats.Ui_MainWindow : Ma classe g�n�r�e avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et genere_menu_contrats.Ui_MainsWindowIntra
        """
        super(MenuContrats, self).__init__(parent)
        self.setupUi(self)

    def on_pushButtonQuitter_clicked(self):
        # *** � FAIRE *** SAUVEGARDE A LIEU L� #
        sys.exit()

    def on_pushButtonQuitter_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        sys.exit()



def main():
    """
    M�thode main : Point d'entr� du programme.
    Ex�cution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_principale = MenuContrats()
    fenetre_principale.show()
    app.exec()


if __name__ == "__main__":
    main()
