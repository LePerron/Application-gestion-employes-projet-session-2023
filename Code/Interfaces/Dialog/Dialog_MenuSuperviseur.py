from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_superviseur
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class MenuSuperviseur(QtWidgets.QDialog, genere_menu_superviseur.Ui_MenuSuperviseur):
    """
    Nome de la classe : MenuSuperviseur
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_superviseur.Ui_MenuSuperviseur : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_superviseur.Ui_MenuSuperviseur
        """
        super(MenuSuperviseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des superviseurs")
        self.checkBoxCaissier.stateChanged.connect(self.caissier_change)
        # self.checkBoxCommis.stateChanged.connect(self.commis_change)
        # self.checkBoxGestionnaire.stateChanged.connect(self.Gestionnaire_change)
        # self.checkBoxGerant.stateChanged.connect(self.gerant_change)

    @pyqtSlot()
    def on_pushButtonRetournerEmploye_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuSuperviseur lorsque l'utilisateur click sur le bouton Retourner au menu
        """
        MenuSuperviseur.close(self)

    def caissier_change(self, status):
        """
        Affiche les caissier si coché
        :param status: le status de la checkbox (coché ou non)
        """
        nom_superviseur_actuel = self.listViewGerantGestionnaire.currentIndex()
        if nom_superviseur_actuel.isValid():
            for employe in Employe.list_employe:
                if nom_superviseur_actuel == employe.nom:
                    if employe.poste == "Gerant":
                        return
                    # else:
                    #    if status == 2:
                    #         print(caissier for caissier in employe.liste_caissier)
#
def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_superviseur = MenuSuperviseur()
    fenetre_superviseur.show()
    app.exec()


if __name__ == "__main__":
    main()
