# Importation de la classe Caissier
from Code.Classes.classe_Caissier import Caissier
# Importation de la classe Commis
from Code.Classes.classe_Commis import Commis
# Imporation de la classe Gerant
from Code.Classes.classe_Gerant import Gerant


class Gestionnaire:
    """
    Classes Gestionnaire
    """

    # Création de list_gestionnaire
    list_gestionnaire = []

    # Création de liste_specialite
    list_specialite = []

    def __init__(self, p_gerant: Gerant = None, p_specialite: str = "", p_liste_commis: list = [Commis],
                 p_liste_caissier: list = [Caissier]):
        """
        Constructeur de la classe Gestionnaire
        :param p_gerant: Le gérant du gestionnaire.
        :param p_specialite: La spécialité du gestionnaire.
        :param p_liste_commis: La liste des commis que le gestionnaire gère.
        :param p_liste_caissier: La liste des caissiers que le gestionnaire gère.
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
    def specialite(self, specialite: str):
        if specialite in Gestionnaire.list_specialite:
            self._specialite = specialite

    # Ajouter un Commis dans liste_commis à gérer
    def ajouter_commis_a_liste(self, commis_a_ajouter: Commis) -> list:
        """
        Ajouter un commis dans liste_commis
        :param commis_a_ajouter: Commis à ajouter
        :return: La liste des commis avec le commis ajouter
        """
        self.liste_commis.append(commis_a_ajouter)

    # Supprimer un Commis dans liste_commis à gérer
    def supprimer_commis_a_liste(self, commis_a_supprimer: Commis) -> list:
        """
        Supprimer un commis dans liste_commis
        :param commis_a_supprimer: Commis à supprimer
        :return: La liste des commis avec le commis supprimer
        """
        self.liste_commis.remove(commis_a_supprimer)

    # Ajouter un Caissier dans liste_caissier à gérer
    def ajouter_caissier_a_liste(self, caissier_a_ajouter: Caissier) -> list:
        """
        Ajouter un caissier dans liste_caissier
        :param caissier_a_ajouter: Caissier à ajouter
        :return: La liste des caissier avec le caissier ajouter
        """
        self.liste_caissier.append(caissier_a_ajouter)

    # Supprimer un Caissier dans liste_caissier à gérer
    def supprimer_caissier_a_liste(self, caissier_a_supprimer: Caissier) -> list:
        """
        Supprimer un caissier dans liste_caissier
        :param caissier_a_supprimer: Caissier à supprimer
        :return: La liste des caissier avec le caissier supprimer
        """
        self.liste_caissier.remove(caissier_a_supprimer)