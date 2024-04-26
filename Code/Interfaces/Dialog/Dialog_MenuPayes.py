from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_payes
from PyQt5 import QtWidgets
import sys


class MenuPayes(QtWidgets.QDialog, genere_menu_payes.Ui_DialogMainPaye):
    """
    Nome de la classe : MenuPayes
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_payes.Ui_DialogMainPaye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_payes.Ui_DialogMainPaye
        """
        super(MenuPayes, self).__init__(parent)
        self.setupUi(self)

    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuPayes.close(self)

    def on_pushButtonModifierContrat_clicked(self):
        # SAUVEGARDE A LIEU LAAAAAAAAAA #
        pass


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_paye = MenuPayes()
    fenetre_paye.show()
    app.exec()


if __name__ == "__main__":
    main()
