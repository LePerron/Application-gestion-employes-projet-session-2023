from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Specialite import AjouterSpecialite
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_specialite
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
        fenetre_modifier_specialite = AjouterSpecialite()
        fenetre_modifier_specialite.setWindowTitle("Modifier Spécialité")
        fenetre_modifier_specialite.labelTitreAjouterSpecialite.setText("Modifier Spécialité")
        fenetre_modifier_specialite.show()
        fenetre_modifier_specialite.exec()
        self.mettre_a_jour_listview()
    @pyqtSlot()
    def on_pushButtonSupprimerSpecialite_clicked(self):
        pass





def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_MenuSpecialite = MenuSpecialite()
    fenetre_MenuSpecialite.show()
    app.exec()


if __name__ == "__main__":
    main()
