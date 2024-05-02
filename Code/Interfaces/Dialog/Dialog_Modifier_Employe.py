from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class ModifierEmploye(QtWidgets.QDialog, genere_ajouter_employe.Ui_DialogAjouterEmploye):
    """
    Nome de la classe : ModifierEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_ajouter_employe.Ui_DialogAjouterEmployer : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_ajouter_employe.Ui_DialogAjouterEmploye
        """
        super(ModifierEmploye, self).__init__(parent)
        self.setupUi(self)
        self.labelTitreAjouterEmploye.setText("Modifier l'employé")
        self.pushButtonAjouterEmploye.setText("Modifier")
        self.setWindowTitle("Modification d'un employé")


    @pyqtSlot()
    def on_pushButtonModifierEmploye_clicked(self):
        pass

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        ModifierEmploye.close(self)


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_employe = ModifierEmploye()
    fenetre_ajouter_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
