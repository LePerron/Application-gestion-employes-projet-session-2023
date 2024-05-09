from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSpecialite import MenuSpecialite
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuContrats import MenuContrats
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuEmploye import MenuEmploye
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_principal
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuPaye import MenuPaye
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import jsonpickle
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSuperviseur import MenuSuperviseur


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
        self.setWindowTitle("Menu Principal")

    @pyqtSlot()
    def on_pushButtonMenuEmploye_clicked(self):
        dialog_menu_employe = MenuEmploye()
        dialog_menu_employe.show()
        self.hide()
        dialog_menu_employe.exec()
        #   ici  #
        self.show()

    @pyqtSlot()
    def on_pushButtonSuperviseur_clicked(self):
        dialogue_menu_superviseur = MenuSuperviseur()
        dialogue_menu_superviseur.show()
        self.hide()
        dialogue_menu_superviseur.exec()
        #   ici  #
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuContrat_clicked(self):
        dialog_menu_contrat = MenuContrats()
        dialog_menu_contrat.show()
        self.hide()
        dialog_menu_contrat.exec()
        #   ici  #
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuPaye_clicked(self):
        dialog_menu_paye = MenuPaye()
        dialog_menu_paye.show()
        self.hide()
        dialog_menu_paye.exec()
        #   ici  #
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuSpecialite_clicked(self):
        dialog_menu_specialite = MenuSpecialite()
        dialog_menu_specialite.show()
        self.hide()
        dialog_menu_specialite.exec()
        #   ici  #
        self.show()

    @pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        sys.exit(self)
        #   ici  #


def serialisation():
    """
    Une fonction qui s'occupe de sérialiser les données afin de pouvoir les sauvegarder.
    :return:
    """


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
