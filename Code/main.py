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
        #   ici  #
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
        # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
        sys.exit(self)
        #   ici  #

    @staticmethod
    def serialisation():
        """
        Une fonction qui s'occupe de sérialiser les données afin de pouvoir les sauvegarder.
        :return:
        """
        from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
        from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
        from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
        from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite

        if len(ContratEmploi.list_contrat) > 0:
            for contrat in ContratEmploi.list_contrat:
                chemin = f"../Fichiers_sérialisations/contrat/{contrat.identifiant_contrat}.json"
                donnes_serialise = jsonpickle.encode(contrat)
                with open(chemin, 'w') as file:
                    file.writelines(donnes_serialise)

        if len(Employe.list_employe) > 0:
            for employe in Employe.list_employe:
                chemin = f"../Fichiers_sérialisations/employe/{employe.identifiant}.json"
                donnes_serialise = jsonpickle.encode(employe)
                with open(chemin, 'w') as file:
                    file.writelines(donnes_serialise)

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

        chemain = "../Fichiers_sérialisations/contrat"

        for fichier in os.listdir(chemain):
            with open(fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readlines()
                donnes_a_deserialisee = jsonpickle.decode(donnes_a_deserialiser)
                ContratEmploi.list_contrat.append(donnes_a_deserialisee)

        chemain = "../Fichiers_sérialisations/employe"

        for fichier in os.listdir(chemain):
            with open(fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readlines()
                donnes_a_deserialisee = jsonpickle.decode(donnes_a_deserialiser)
                Employe.list_employe.append(donnes_a_deserialisee)

        chemain = "../Fichiers_sérialisations/paye"

<<<<<<< HEAD
        for fichier in os.listdir(chemain):
            with open(fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readlines()
                donnes_a_deserialisee = jsonpickle.decode(donnes_a_deserialiser)
                Paye.list_payes.append(donnes_a_deserialisee)

        chemain = "../Fichiers_sérialisations/specialite"

        for fichier in os.listdir(chemain):
            with open(fichier, "r") as fichier:
                donnes_a_deserialiser = fichier.readlines()
                donnes_a_deserialisee = jsonpickle.decode(donnes_a_deserialiser)
                Specialite.list_des_specialites.append(donnes_a_deserialisee)
=======
        #
        #
        # employe1 = Employe()
        # paye1 = Paye()
        # specialite1 = Specialite()
        # del employe1
        # del paye1
        # del specialite1
        # Employe.list_employe = []
        # Paye.list_payes = []
        # Specialite.list_des_specialites = []
        #
        # for cle in dict_a_deserialise.keys():
        #     chemin = f"../Fichiers_sérialisations/{cle}"
        #     list_serialiser = []
        #     with open(chemin, 'r') as fichier:
        #         donnes_a_deserialiser = fichier.readlines()
        #         list_serialiser.append(donnes_a_deserialiser)
        #
        #     for object_a_deserialiser in list_serialiser:
        #         for donnes in object_a_deserialiser:
        #             if donnes == '\n':
        #                 fichier.close()
        #             else:
        #                 donnes = jsonpickle.decode(donnes)
        #                 for don in donnes:
        #                     dict_a_deserialise[cle].append(don)
        #
        #
>>>>>>> f05bc2acddb384577518aea56d68ed9919c3a3b6

def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_principale = MenuPrincipal()
    fenetre_principale.show()
    MenuPrincipal.deserialisation()
    app.exec()


if __name__ == "__main__":
    main()
