from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Specialite import AjouterSpecialite
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_specialite
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class MenuSpecialite(QtWidgets.QDialog, genere_menu_specialite.Ui_DialogMenuSpecialite):
    """
    Nome de la classe : MenuSpecialite
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_specialite.Dialog_Ajouter_Specialite : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_specialite.Dialog_Ajouter_Specialite
        """
        super(MenuSpecialite, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Spécialités")
        self.mettre_a_jour_listview()


    def mettre_a_jour_listview(self):
        model = QStandardItemModel()
        self.listViewSpecialite.setModel(model)

        for specialite in Specialite.list_des_specialites:
            item = QStandardItem(str(specialite))
            model.appendRow(item)


    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuSpecialite.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterSpecialite_clicked(self):
        fenetre_ajouter_specialite = AjouterSpecialite()
        fenetre_ajouter_specialite.show()
        fenetre_ajouter_specialite.exec()
        self.mettre_a_jour_listview()

    @pyqtSlot()
    def on_pushButtonModifierSpecialite_clicked(self):
        longueur_avant = Specialite.list_des_specialites

        fenetre_modifier_specialite = AjouterSpecialite()
        fenetre_modifier_specialite.setWindowTitle("Modifier Spécialité")
        fenetre_modifier_specialite.labelTitreAjouterSpecialite.setText("Modifier Spécialité")
        fenetre_modifier_specialite.show()
        fenetre_modifier_specialite.exec()
        if len(Specialite.list_des_specialites) != longueur_avant:
            self.mettre_a_jour_listview()

    @pyqtSlot()
    def on_pushButtonSupprimerSpecialite_clicked(self):
        index_actuel = self.listViewSpecialite.currentIndex()
        if index_actuel.isValid():
            self.listViewSpecialite.model().removeRow(index_actuel.row())
        else:
            self.labelErreurSelection.setText("Veuillez sélectionner une spécialité d'abord.")


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_menu_specialite = MenuSpecialite()
    fenetre_menu_specialite.show()
    app.exec()


if __name__ == "__main__":
    main()
