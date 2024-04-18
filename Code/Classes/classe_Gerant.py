# Importation de la classe Gestionnaire
from Code.Classes.classe_Gestionnaire import Gestionnaire


class Gerant:
    """
    Classes Gerant
    """

    # Création de liste_specialite
    list_specialite = []

    def __init__(self, p_specialite: str = "", p_liste_gestionnaire: list = [Gestionnaire]):
        """
        Constructeur de la classe Gerant
        :param p_specialite: Spécialité du gerant
        :param p_liste_gestionnaire: Base de données des gestionnaires
        """
        self._specialite = p_specialite
        self.liste_gestionnaire = p_liste_gestionnaire

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, specialite: str):
        if specialite in Gerant.list_specialite:
            self._specialite = specialite

    # Ajouter un gestionnaire dans liste_gestionnaire à gérer

    def ajouter_gestionnaire_a_liste(self, gestionnaire_a_ajouter: Gestionnaire) -> list:
        """
        Ajouter un gestionnaire dans liste_gestionnaire
        :param gestionnaire_a_ajouter: Gestionnaire à ajouter
        :return: La liste des gestionnaires avec le gestionnaire ajouter
        """
        self.liste_gestionnaire.append(gestionnaire_a_ajouter)

    # Supprimer un gestionnaire dans liste_gestionnaire à gérer

    def supprimer_gestionnaire_a_liste(self, gestionnaire_a_supprimer: Gestionnaire) -> list:
        """
        Supprimer un gestionnaire dans liste_gestionnaire
        :param gestionnaire_a_supprimer: Gestionnaire à supprimer
        :return: La liste des gestionnaire avec le gestionnaire supprimer
        """
        self.liste_gestionnaire.remove(gestionnaire_a_supprimer)



