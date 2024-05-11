from datetime import datetime

from Projet_intra_Entreprise.Code.Interfaces.Code_Genere import genere_creer_contrat
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import sys


class AjouterContrat(QtWidgets.QDialog, genere_creer_contrat.Ui_DialogCreerContrat):
    """
    Nome de la classe : AjouterContrat
    Héritages :
    - QtWidgets.QDialog : Type d'interface créé par QtDesigner
    - genere_creer_contrat.Ui_DialogCreerContrat : Ma classe générée avec QtDesigner
    """

    def __init__(self, employe_modification=None, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QDialog et genere_creer_contrat.Ui_DialogCreerContrat
        :param employe_modification: L'employé a qui appartient le contrat
        """

        super(AjouterContrat, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un Contrat")
        self.employe_modification = employe_modification

        if employe_modification:
            contrat = employe_modification.contrat
            self.doubleSpinBoxFacteur.setValue(contrat.facteur_salaire)
            self.horizontalSliderNbHeure.setValue(contrat.nb_heures_semaine)
            self.doubleSpinBoxSalaireHoraire.setValue(contrat.salaire_horaire)
            self.textEditTermeContrat.setText(contrat.termes_embauche)

    @pyqtSlot()
    def on_pushButtonAjouterEmploye_clicked(self):
        """
        Ajoute un nouveau contrat lorsque l'utilisateur clique sur le bouton Ajouter un employe
        """

        salaire_horaire = float(self.doubleSpinBoxSalaireHoraire.value())
        facteur_salaire = float(self.doubleSpinBoxFacteur.value())
        autres_termes = self.textEditTermeContrat.toPlainText()
        nb_heures = int(self.lcdNumberNbHeure.value())

        for employe in Employe.list_employe:
            if employe.identifiant == self.employe_modification.identifiant:
                contrat_temporaire = employe.contrat
                contrat_temporaire.facteur_salaire = facteur_salaire
                contrat_temporaire.nb_heures_semaine = nb_heures
                contrat_temporaire.salaire_horaire = salaire_horaire
                contrat_temporaire.termes_embauche = autres_termes
                contrat_temporaire.date_du_contrat = datetime.now().strftime("%d/%m/%Y")
                AjouterContrat.close(self)
                break
            else:
                continue
        else:
            AjouterContrat.close(self)

    @pyqtSlot()
    def on_pushButtonAnnuler_clicked(self):
        """
        Ferme la fenêtre AjouterContrat lorsque l'utilisateur clique sur le bouton Annuler
        """
        from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
        from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi

        try:
            if not self.employe_modification.contrat:
                ContratEmploi.list_contrat.remove(self.employe_modification.contrat)
            Employe.list_employe.remove(self.employe_modification)
        finally:
            AjouterContrat.close(self)


def main():
    """
    Méthode main : Point d'entré du programme.
    Exécution de l'application avec l'interface graphique.
    """
    app = QtWidgets.QApplication(sys.argv)
    fenetre_contrat = AjouterContrat()
    fenetre_contrat.show()
    app.exec()


if __name__ == "__main__":
    main()
