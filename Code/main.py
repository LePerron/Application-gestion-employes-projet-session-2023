from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_menu_principal
from PyQt5 import QtWidgets
import sys


class MenuPrincipal(QtWidgets.QMainWindow, genere_menu_principal.Ui_MainsWindowIntra):
    """
    Nome de la classe : MenuPrincipal
    Héritages :
    - QtWidgets.Ui_MainsWindowIntra : Type d'interface créé par QtDesigner
    - genere_menu_principal.Ui_MainWindow : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):
        '''
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et code_interface_genere.Ui_MainWindow
        '''
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(demoQt, self).__init__(parent)
        self.setupUi(self) #Préparer l'interface utilisateur.

# Créer le main qui lance la fenêtre de Qt
def main():
    '''
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = demoQt() #Nom de ma classe
    form.show()
    app.exec()

if __name__ == "__main__":
    main()

