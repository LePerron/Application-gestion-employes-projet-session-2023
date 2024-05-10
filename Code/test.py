import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QAbstractListModel, Qt

from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

# Cette classe permet au programme d'avoir une listview personnalisée avec des évènements de sélection.
class ListModeleSelectionnable(QAbstractListModel):
    def __init__(self, donnees=None, parent=None):
        super().__init__(parent)
        if donnees is None:
            donnees = []
        self._donnees = donnees

    def rowCount(self, parent):
        return len(self._donnees)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._donnees[index.row()].nom


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.list_view = QListView()
        self.list_view.setSelectionMode(QListView.SingleSelection)
        self.layout.addWidget(self.list_view)

        self.populate_list()
        self.list_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def peupler_la_liste_de_list(self):
        # donnees = [gestionnaire1, gestionnaire2]
        modele = ListModeleSelectionnable(donnees)
        self.list_view.setModel(modele)

    def on_selection_changed(self, selected, deselected):
        index_selectionnes = selected.indexes()
        if index_selectionnes:
            rangee_selectionnee = index_selectionnes[0].row()
            selected_gestionnaire = self.list_view.model().data(index_selectionnes[0], Qt.DisplayRole)
            self.label.setText(f"Gestionnaire sélectionné: {selected_gestionnaire}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
    from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
    from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
    from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
    from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_superviseur
    from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
    from PyQt5.QtGui import QStandardItemModel, QStandardItem
    from PyQt5.QtCore import pyqtSlot, QAbstractListModel, Qt
    from PyQt5 import QtWidgets
    import sys


    # Cette classe permet au programme d'avoir une listview personnalisée avec des évènements de sélection.
    class ListModeleSelectionnable(QAbstractListModel):
        def __init__(self, donnees=None, parent=None):
            super().__init__(parent)
            if donnees is None:
                donnees = []
            self._donnees = donnees

        def rowCount(self, parent):
            return len(self._donnees)

        def data(self, index, role):
            if role == Qt.DisplayRole:
                return not self._donnees[index.row()].prenom


    class MenuSuperviseur(QtWidgets.QDialog, genere_menu_superviseur.Ui_MenuSuperviseur):
        """
        Nome de la classe : MenuSuperviseur
        Héritages :
        - QtWidgets.QDialog : Type d'interface créé par QtDesigner
        - genere_menu_superviseur.Ui_MenuSuperviseur : Ma classe générée avec QtDesigner
        """

        def __init__(self, parent=None):
            """
            Constructeur de la classe
            :param parent: QtWidgets.QDialog et genere_menu_superviseur.Ui_MenuSuperviseur
            """
            super(MenuSuperviseur, self).__init__(parent)
            self.setupUi(self)
            self.setWindowTitle("Gestionnaire des superviseurs")
            self.checkBoxCaissier.stateChanged.connect(self.caissier_change)
            self.checkBoxCommis.stateChanged.connect(self.commis_change)
            self.checkBoxGestionnaire.stateChanged.connect(self.gestionnaire_change)
            self.checkBoxGerant.stateChanged.connect(self.gerant_change)

            self.peupler_liste_superviseur()

            self.listViewGerantGestionnaire.selectionModel().selectionChanged.connect(
                self.changement_selection_superviseur)

        def peupler_liste_superviseur(self):
            liste_superviseur = []
            if len(Employe.list_employe) > 0:
                for employe in Employe.list_employe:
                    if employe.poste == "Gerant" or "Gestion":
                        liste_superviseur.append(employe)

            modele = ListModeleSelectionnable(liste_superviseur)
            self.listViewGerantGestionnaire.setModel(modele)

        def peupler_liste_caissier_commis(self, superviseur_selectionne):

            modele = ListModeleSelectionnable(donnees)
            self.list_view.setModel(modele)


        @pyqtSlot()
        def on_pushButtonRetournerMenu_clicked(self):
            # *** À FAIRE *** SAUVEGARDE A LIEU LÀ #
            """
            Ferme la fenêtre MenuSuperviseur lorsque l'utilisateur click sur le bouton Retourner au menu
            """
            MenuSuperviseur.close(self)

        def changement_selection_superviseur(self, selected, deselected):
            index_selectionnes = selected.indexes()
            if index_selectionnes:
                rangee_selectionnee = index_selectionnes[0].row()
                superviseur_selectionne = self.listViewGerantGestionnaire.model().data(index_selectionnes[0],
                                                                                       Qt.DisplayRole)

                return superviseur_selectionne

        def caissier_change(self, status):
            """
            Affiche les caissiers si coché
            :param status: le status de la checkbox (coché ou non)
            """
            nom_superviseur_actuel = self.tableWidget.currentIndex()
            if nom_superviseur_actuel.isValid():
                self.mettre_a_jour_listview("employe", nom_superviseur_actuel)
                for employe in Employe.list_employe:
                    if nom_superviseur_actuel == employe.gestionnaire:
                        if status == 2:
                            return
                        else:
                            employe.hide()

        def commis_change(self, status):
            """
            Affiche les commis si coché
            :param status: le status de checkbox (coché ou non)
            """
            nom_superviseur_actuel = self.tableWidget.currentIndex()
            if nom_superviseur_actuel.isValid():
                self.mettre_a_jour_listview("employe", nom_superviseur_actuel)
                for employe in Employe.list_employe:
                    if nom_superviseur_actuel == employe.gestionnaire:
                        if status == 2:
                            return
                        else:
                            employe.hide()

        def gerant_change(self, status):
            """
            Affiche les gerants si coché
            :param status: le status de checkbox (coché ou non)
            """
            self.mettre_a_jour_listview_superviseur()
            for employe in Employe.list_employe:
                if employe.poste == "Gerant":
                    if status == 2:
                        return
                    else:
                        employe.hide()

        def gestionnaire_change(self, status):
            """
            Affiche les gestionnaires si coché
            :param status: le status de checkbox (coché ou non)
            """
            self.mettre_a_jour_listview_superviseur()
            for employe in Employe.list_employe:
                if employe.poste == "Gestionnaire":
                    if status == 2:
                        return
                    else:
                        employe.hide()


    def main():
        """
        Méthode main : Point d'entré du programme.
        Exécution de l'application avec l'interface graphique.
        """
        app = QtWidgets.QApplication(sys.argv)
        fenetre_superviseur = MenuSuperviseur()
        fenetre_superviseur.show()
        app.exec()


    if __name__ == "__main__":
        main()
