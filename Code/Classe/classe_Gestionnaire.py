# Importation de la classe Caissier
from Code.Classe.classe_Caissier import Caissier
# Importation de la classe Commis
from Code.Classe.classe_Commis import Commis
# Imporation de la classe Gerant
from Code.Classe.classe_Gerant import Gerant


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
        self.gerant = p_gerant
        self._specialite = p_specialite
        self.liste_commis = p_liste_commis
        self.liste_caissier = p_liste_caissier

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, specialite):
        self._specialite = specialite

