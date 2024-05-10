import os

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSpecialite import MenuSpecialite
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuContrats import MenuContrats
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuEmploye import MenuEmploye
from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_principal
from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuPaye import MenuPaye
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import jsonpickle
import sys

from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSuperviseur import MenuSuperviseur


class MenuPrincipal(QtWidgets.QMainWindow, genere_menu_principal.Ui_MainWindowMenuPrincipal):
    """
    Nome de la classe : MenuPrincipal
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - genere_menu_principal.Ui_MainsWindowIntra : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et genere_menu_principal.Ui_MainsWindowIntra
        """
        super(MenuPrincipal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Menu Principal")

    @pyqtSlot()
    def on_pushButtonMenuEmploye_clicked(self):
        dialog_menu_employe = MenuEmploye()
        dialog_menu_employe.show()
        self.hide()
        dialog_menu_employe.exec()
        self.serialisation()
        dialog_menu_employe.mettre_a_jour_listview()
        self.show()

    @pyqtSlot()
    def on_pushButtonSuperviseur_clicked(self):
        dialogue_menu_superviseur = MenuSuperviseur()
        dialogue_menu_superviseur.show()
        self.hide()
        dialogue_menu_superviseur.exec()
        self.serialisation()
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuContrat_clicked(self):
        dialog_menu_contrat = MenuContrats()
        dialog_menu_contrat.show()
        self.hide()
        dialog_menu_contrat.exec()
        self.serialisation()
        dialog_menu_contrat.mettre_a_jour_listview()
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuPaye_clicked(self):
        dialog_menu_paye = MenuPaye()
        dialog_menu_paye.show()
        self.hide()
        dialog_menu_paye.exec()
        self.serialisation()
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuSpecialite_clicked(self):
        dialog_menu_specialite = MenuSpecialite()
        dialog_menu_specialite.show()
        self.hide()
        dialog_menu_specialite.exec()
        self.serialisation()
        self.show()

    @pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        self.serialisation()
        sys.exit(self)


    @staticmethod
    def serialisation():
        """
        Une fonction qui s'occupe de sérialiser les données afin de pouvoir les sauvegarder.
        :return:
        """
        from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
        from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
        from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
        from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye

        if len(ContratEmploi.list_contrat) > 0:
            for contrat in ContratEmploi.list_contrat:
                chemin = f"../Fichiers_sérialisations/contrat/{contrat.identifiant_contrat}.json"
                with open(chemin, 'w') as file:
                    file.writelines(jsonpickle.encode(contrat))

        if len(Employe.list_employe) > 0:
            for employe in Employe.list_employe:
                chemin = f"../Fichiers_sérialisations/employe/{employe.identifiant}.json"
                with open(chemin, 'w') as file:
                    file.writelines(jsonpickle.encode(employe))

        if len(Paye.list_payes) > 0:
            for paye in Paye.list_payes:
                chemin = f"../Fichiers_sérialisations/paye/{paye.identifiant_paye}.json"
                donnes_serialise = jsonpickle.encode(paye)
                with open(chemin, 'w') as file:
                    file.writelines(donnes_serialise)

        if len(Specialite.list_des_specialites) > 0:
            for specialite in Specialite.list_des_specialites:
                chemin = f"../Fichiers_sérialisations/specialite/{specialite.nom}.json"
                donnes_serialise = jsonpickle.encode(specialite)
                with open(chemin, 'w') as file:
                    file.writelines(donnes_serialise)

    @staticmethod
    def deserialisation():
        """
        Une fonction qui s'occupe de sérialiser les données afin de pouvoir les sauvegarder.
        :return:
        """
        from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
        from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
        from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
        from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite

        chemin = "../Fichiers_sérialisations/contrat"
        for fichier_contrat in os.listdir(chemin):
            chemin_fichier = os.path.join(chemin, fichier_contrat)
            with open(chemin_fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readline()
                ContratEmploi.list_contrat.append(jsonpickle.decode(donnes_a_deserialiser))
            os.remove(chemin_fichier)

        chemin = "../Fichiers_sérialisations/employe"
        for fichier_employe in os.listdir(chemin):
            chemin_fichier = os.path.join(chemin, fichier_employe)
            with open(chemin_fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readline()
                Employe.list_employe.append(jsonpickle.decode(donnes_a_deserialiser))
            os.remove(chemin_fichier)

        chemin = "../Fichiers_sérialisations/paye"
        for fichier_paye in os.listdir(chemin):
            chemin_fichier = os.path.join(chemin, fichier_paye)
            with open(chemin_fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readline()
                Paye.list_payes.append(jsonpickle.decode(donnes_a_deserialiser))
            os.remove(chemin_fichier)

        chemin = "../Fichiers_sérialisations/specialite/"
        for fichier_specialite in os.listdir(chemin):
            chemin_fichier = os.path.join(chemin, fichier_specialite)
            with open(chemin_fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readline()
                Specialite.list_des_specialites.append(jsonpickle.decode(donnes_a_deserialiser))
            os.remove(chemin_fichier)



def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_principale = MenuPrincipal()
    fenetre_principale.show()
    app.exec()


if __name__ == "__main__":
    MenuPrincipal.deserialisation()
    main()
