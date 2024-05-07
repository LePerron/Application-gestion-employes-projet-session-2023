from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Ajouter_Employe import AjouterEmploye
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_employe
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_Modifier_Employe import ModifierEmploye


class MenuEmploye(QtWidgets.QDialog, genere_menu_employe.Ui_DialogMenuEmploye):
    """
    Nome de la classe : MenuEmploye
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_menu_employe.Ui_DialogMenuEmploye : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_menu_employe.Ui_DialogMenuEmploye
        """
        employe1 = Caissier(p_identifiant="2371875", p_nom="Lemoyne", p_prenom="Benjamin",
                            p_date_engagement=None)

        super(MenuEmploye, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestionnaire des Employés")
        self.checkBoxSalaire.stateChanged.connect(self.salaire_checkbox_change)
        self.checkBoxAnciennete.stateChanged.connect(self.anciennete_checkbox_change)
        self.checkBoxNbHeure.stateChanged.connect(self.nbheure_checkbox_change)
        self.mettre_a_jour_listview()

    def mettre_a_jour_listview(self):
        model = QStandardItemModel()
        self.listViewEmploye.setModel(model)

        for employe in Employe.list_employe:
            item = QStandardItem(str(employe))
            model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonRetournerMenu_clicked(self):
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        MenuEmploye.close(self)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        dialog_ajouter_employe = AjouterEmploye()
        dialog_ajouter_employe.show()
        dialog_ajouter_employe.exec()
        self.mettre_a_jour_listview()

    @pyqtSlot()
    def on_pushButtonModifierEmploye_clicked(self):
        index_actuel = self.listViewEmploye.currentIndex()
        if index_actuel.isValid():
            employe_modifier = Employe.list_employe[index_actuel.row()]
            dialog_modifier_employe = AjouterEmploye(employe_modifier)
            dialog_modifier_employe.show()
            dialog_modifier_employe.exec()
            self.mettre_a_jour_listview()
        else:
            self.labelErreurSelection.setText("Erreur")

    @pyqtSlot()
    def on_pushButtonSupprimerEmploye_clicked(self):
        index_actuel = self.listViewEmploye.currentIndex()
        if index_actuel.isValid():
            self.listViewEmploye.model().removeRow(index_actuel.row())
        else:
            self.labelErreurSelection.setText("Erreur.")

    def salaire_checkbox_change(self, status):
        if status == 2:
            self.comboBoxTrierEmploye.addItem("Croissant ($)")
            self.comboBoxTrierEmploye.addItem("Décroissant ($)")
        else:
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant ($)")))
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant ($)")))

    def anciennete_checkbox_change(self, status):
        if status == 2:
            self.comboBoxTrierEmploye.addItem("Croissant (anciennté)")
            self.comboBoxTrierEmploye.addItem("Décroissant (anciennté)")
        else:
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant (anciennté)")))
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant (anciennté)")))

    def nbheure_checkbox_change(self, status):
        if status == 2:
            self.comboBoxTrierEmploye.addItem("Croissant (h)")
            self.comboBoxTrierEmploye.addItem("Décroissant (h)")
        else:
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Croissant (h)")))
            self.comboBoxTrierEmploye.findText(self.comboBoxTrierEmploye.removeItem(self.comboBoxTrierEmploye.findText("Décroissant (h)")))



def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_employe = MenuEmploye()
    fenetre_employe.show()
    app.exec()


if __name__ == "__main__":
    main()
