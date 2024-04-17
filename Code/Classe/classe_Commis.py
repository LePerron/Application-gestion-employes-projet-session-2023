# Importation de la classe Gestionnaire
from Code.Classe.classe_Gestionnaire import Gestionnaire


class Commis:
    """
    Classe Commis
    """

    # Création de list_commis
    list_commis = []

    # Création de liste_specialite
    liste_specialite = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: str = ""):
        """
        Constructeur de la classe Commis
        :param p_gestionnaire: Base de donner des gestionnaires
        :param p_specialite: Spécialiter du commis
        """
        self.gestionnaire = p_gestionnaire
        self._specialite = p_specialite

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, specialite):
        self._specialite = specialite
