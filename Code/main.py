from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSpecialite import MenuSpecialites
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuContrats import MenuContrats
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuEmploye import MenuEmployes
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_principal
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuPayes import MenuPayes
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class MenuPrincipal(QtWidgets.QMainWindow, genere_menu_principal.Ui_MainWindowMenuPrincipal):
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

    @pyqtSlot()
    def on_pushButtonMenuEmploye_clicked(self):
        dialog_menu_employe = MenuEmployes()
        dialog_menu_employe.show()
        dialog_menu_employe.exec()

    @pyqtSlot()
    def on_pushButtonMenuContrat_clicked(self):
        dialog_menu_contrat = MenuContrats()
        dialog_menu_contrat.show()
        dialog_menu_contrat.exec()

    @pyqtSlot()
    def on_pushButtonMenuPaye_clicked(self):
        dialog_menu_paye = MenuPayes()
        dialog_menu_paye.show()
        dialog_menu_paye.exec()

    @pyqtSlot()
    def on_pushButtonMenuSpecialite_clicked(self):
        dialog_menu_specialite = MenuSpecialites()
        dialog_menu_specialite.show()
        dialog_menu_specialite.exec()

    @pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        sys.exit(self)


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
