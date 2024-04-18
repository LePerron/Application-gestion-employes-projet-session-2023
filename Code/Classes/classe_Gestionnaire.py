from classe_Caissier import Caissier
from classe_Commis import Commis
from classe_Gerant import Gerant
from classe_Specialite import Specialite


class Gestionnaire:
    """
    Classes Gestionnaire
    """

    # Création de list_gestionnaire
    list_gestionnaire = []

    def __init__(self, p_gerant: Gerant = None, p_specialite: Specialite = None, p_liste_commis=None,
                 p_liste_caissier=None):
        """
        Constructeur de la classe Gestionnaire
        :param p_gerant: Le gérant du gestionnaire.
        :param p_specialite: La spécialité du gestionnaire.
        :param p_liste_commis: La liste des commis que le gestionnaire gère.
        :param p_liste_caissier: La liste des caissiers que le gestionnaire gère.
        """
        if p_liste_commis is None:
            p_liste_commis = [Commis]
        if p_liste_caissier is None:
            p_liste_caissier = [Caissier]

        self.gerant = p_gerant
        self.specialite = p_specialite
        self.liste_commis = p_liste_commis
        self.liste_caissier = p_liste_caissier

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
