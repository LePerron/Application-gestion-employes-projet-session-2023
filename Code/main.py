git from Projet_intra_Entreprise.Code.Interfaces.Dialog.Dialog_MenuSpecialite import MenuSpecialite
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
<<<<<<< HEAD
        self.serialisation()
=======
        dialog_menu_employe.mettre_a_jour_listview()
#        self.serialisation()
>>>>>>> ed448fb50ceb2ea0b7b0db752a8f9d9582e58647
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
#        self.serialisation()
        self.show()

    @pyqtSlot()
    def on_pushButtonMenuPaye_clicked(self):
        dialog_menu_paye = MenuPaye()
        dialog_menu_paye.show()
        self.hide()
        dialog_menu_paye.exec()
#        self.serialisation()
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

        dict_serialise = {
            "contrat.json": ContratEmploi.list_contrat,
             "paye.json": Paye.list_payes,
             "specialite.json": Specialite.list_des_specialites,
             "employe.json": Employe.list_employe
         }

        for cle in dict_serialise.keys():
            for objet_a_serialiser in dict_serialise[cle]:
                chemin = f"../Fichiers_sérialisations/{cle}"
                donnes_serialise = jsonpickle.encode(objet_a_serialiser)

                with open(chemin, 'a') as file:
                    file.write(donnes_serialise)


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

        dict_a_deserialise = {
            "contrat.json": ContratEmploi.list_contrat,
            "paye.json": Paye.list_payes,
            "specialite.json": Specialite.list_des_specialites,
            "employe.json": Employe.list_employe

        }

        for cle in dict_a_deserialise.keys():
            chemin = f"../Fichiers_sérialisations/{cle}"
            with open(chemin, 'r') as fichier:
                donnes_a_deserialiser = fichier.readlines()

                for object_a_deserialiser in donnes_a_deserialiser:
                    if object_a_deserialiser == "":
                        fichier.close()
                    else:
                        object_deserialise = jsonpickle.decode(object_a_deserialiser)
                        dict_a_deserialise[cle].append(object_deserialise)



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
    # MenuPrincipal.deserialisation()
    main()
