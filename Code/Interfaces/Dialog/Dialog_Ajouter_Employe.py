from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_ajouter_employe
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Contrat import AjouterContrat
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
from PyQt5 import QtWidgets
import sys





class AjouterEmploye(QtWidgets.QDialog, genere_ajouter_employe.Ui_DialogAjouterEmploye):
    """
    Nome de la classe : AjouterEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_ajouter_employe.Ui_DialogAjouterEmployer : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_ajouter_employe.Ui_DialogAjouterEmploye
        """
        super(AjouterEmploye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un Employé")
        self.labelDatePromotion.hide()
        self.dateEditDatePromotion.hide()
        self.labelErreurDatePromotion.hide()
        self.dateEditDatePromotion.setMaximumDate(datetime.now())
        self.dateEditDateEngagement.setMaximumDate(datetime.now())

        self.comboBoxPoste.activated.connect(self.index_combobox_change)

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        AjouterEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        fenetre_ajouter_contrat = AjouterContrat()
        fenetre_ajouter_contrat.show()
        fenetre_ajouter_contrat.exec()

    def index_combobox_change(self, index):
        if index >= 2:
            self.labelDatePromotion.show()
            self.dateEditDatePromotion.show()
            self.labelErreurDatePromotion.show()
        else:
            self.labelDatePromotion.hide()
            self.dateEditDatePromotion.hide()
            self.labelErreurDatePromotion.hide()


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_ajouter_employe = AjouterEmploye()
    fenetre_ajouter_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
