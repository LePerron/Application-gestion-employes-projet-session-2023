from Code.Classe.classe_Caissier import Caissier
from Code.Classe.classe_Commis import Commis


class Gestionnaire:
    """
    Classe Gestionnaire
    """

    # Création de list_gestionnaire
    list_gestionnaire = []

    def __init__(self, p_gerant: Gerant = None, p_specialite: str = "", p_liste_commis: list = [Commis],
                 p_liste_caissier: list = [Caissier]):
        """
        Constructeur de la classe Gestionnaire
        :param p_gerant: Base de données des gerants
        :param p_specialite: Spécialiter du gestionnaire
        :param p_liste_commis: Base de données des commis
        :param p_liste_caissier: Base de données des caissier
        """
        self._gerant = p_gerant
        self._specialite = p_specialite
        self._liste_commis = p_liste_commis
        self._liste_caissier = p_liste_caissier

    # Get/Set gerant
    @property
    def gerant(self):
        return self._gerant

    @gerant.setter
    def gerant(self, gerant):
        self._gerant = gerant

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, specialite):
        self._specialite = specialite

