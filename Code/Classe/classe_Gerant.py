# Importation de la classe Gestionnaire
from Code.Classe.classe_Gestionnaire import Gestionnaire


class Gerant:
    """
    Classe Gerant
    """

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
    def specialite(self, specialite):
        self._specialite = specialite

