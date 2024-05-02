from datetime import datetime

from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_contrat
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat


class MenuContrats(QtWidgets.QDialog, genere_menu_contrat.Ui_DialogContratEmploye):
    """
    Nome de la classe : MenuContrats
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_contrat.Ui_DialogContratEmploye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_contrat.Ui_DialogContratEmploye
        """
        super(MenuContrats, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Contrats")
        self.dateEditContratSelonDate.setMaximumDate(datetime.now())

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuContrats.close(self)

    @pyqtSlot()
    def on_pushButtonModifierContrat_clicked(self):
        fenetre_ajouter_contrat = AjouterContrat()
        fenetre_ajouter_contrat.pushButtonAjouterEmploye.setText("Modifier")
        fenetre_ajouter_contrat.show()
        fenetre_ajouter_contrat.exec()

def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_contrat = MenuContrats()
    fenetre_contrat.show()
    app.exec()


if __name__ == "__main__":
    main()
