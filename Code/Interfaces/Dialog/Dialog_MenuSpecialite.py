from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Specialite import AjouterSpecialite
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_specialite
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_confirmation import Confirmation


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
        """
        Modifie la listview lorsque l'utilisateur ajoute ou modifie une specialité
        """
        model = QStandardItemModel()
        self.listViewSpecialite.setModel(model)

        for specialite in Specialite.list_des_specialites:
            item = QStandardItem(specialite.afficher_specialite_dans_list_view())
            model.appendRow(item)


    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        """
        Ferme la fenêtre MenuSpecialite lorsque l'utilisateur clique sur le bouton Retourner au menu
        """
        MenuSpecialite.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterSpecialite_clicked(self):
        """
        Ouvre la fenêtre AjouterSpecialité lorsque l'utilisateur clique sur le bouton Ajouter un employe
        """
        fenetre_ajouter_specialite = AjouterSpecialite()
        fenetre_ajouter_specialite.show()
        self.hide()
        fenetre_ajouter_specialite.exec()
        self.show()
        self.mettre_a_jour_listview()

    @pyqtSlot()
    def on_pushButtonModifierSpecialite_clicked(self):
        """
        Modifie la spécialité lorsque l'utilisateur clique sur le bouton Modifier la spécialité
        """

        index_actuel = self.listViewSpecialite.currentIndex()
        if index_actuel.isValid():
            fenetre_modifier_specialite = AjouterSpecialite(specialite_modification=index_actuel)
            fenetre_modifier_specialite.setWindowTitle("Modifier Spécialité")
            fenetre_modifier_specialite.labelTitreAjouterSpecialite.setText("Modifier Spécialité")
            fenetre_modifier_specialite.lineEditNom.setText(Specialite.list_des_specialites[index_actuel.row()].nom)
            fenetre_modifier_specialite.textEditDescription.setText(Specialite.list_des_specialites[index_actuel.row()].description)
            fenetre_modifier_specialite.show()
            self.hide()
            fenetre_modifier_specialite.exec()
            self.show()
            self.mettre_a_jour_listview()
        else:
            self.labelErreurSelection.setText("Veuillez sélectionner une spécialité d'abord.")

    @pyqtSlot()
    def on_pushButtonSupprimerSpecialite_clicked(self):
        """
        Supprime la specialite lorsque l'utilisateur clique sur le bouton Supprimer la specialité
        """
        index_actuel = self.listViewSpecialite.currentIndex()
        if index_actuel.isValid():
            fenetre_confirmation = Confirmation()
            fenetre_confirmation.show()
            fenetre_confirmation.exec()
            if Confirmation.confirme:
                Specialite.list_des_specialites.pop(index_actuel.row())
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
