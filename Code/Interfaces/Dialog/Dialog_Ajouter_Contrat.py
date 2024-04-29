from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_creer_contrat
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class AjouterContrat(QtWidgets.QDialog, genere_creer_contrat.Ui_DialogCreerContrat):
    """
    Nome de la classe : AjouterContrat
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_creer_contrat.Ui_DialogCreerContrat : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_creer_contrat.Ui_DialogCreerContrat
        """
        super(AjouterContrat, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un Contrat")

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        pass

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        AjouterContrat.close(self)


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_contrat = AjouterContrat()
    fenetre_contrat.show()
    app.exec()


if __name__ == "__main__":
    main()
