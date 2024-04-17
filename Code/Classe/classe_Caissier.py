# Importation de la classe Gestionnaire
from Code.Classe.classe_Gestionnaire import Gestionnaire


class Caissier:
    """
    Classe employer caissier
    """

    # Création de la liste_caissier.
    liste_caissier = []

    # Création de la liste_specialite
    list_specialite = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: str = ""):
        """
        Constructeur de la classe Caissier
        :param p_gestionnaire: Base de donner des gestionnaires
        :param p_specialite: Spécialiter du caissier
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