from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_creer_specialite
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class AjouterSpecialite(QtWidgets.QDialog, genere_creer_specialite.Ui_DialogCreerSpecialite):
    """
    Nome de la classe : AjouterSpecialite
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_creer_specialite.Ui_DialogCreerSpecialite : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_creer_specialite.Ui_DialogCreerSpecialite
        """
        super(AjouterSpecialite, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        AjouterSpecialite.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterSpecialite_clicked(self):
        pass


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_specialite = AjouterSpecialite()
    fenetre_ajouter_specialite.show()
    app.exec()


if __name__ == "__main__":
    main()
