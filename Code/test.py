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
