from datetime import date

from classe_Employe import Employe
from classe_Specialite import Specialite
from classe_Caissier import Caissier
from classe_Commis import Commis
from classe_Gerant import Gerant


class Gestionnaire(Employe):
    """
    Classes Gestionnaire
    """

    list_gestionnaire = []

    def __init__(self, p_gerant: Gerant = None, p_specialite: Specialite = None, p_liste_commis=None,
                 p_liste_caissier=None,  p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: any = None, p_date_engagement: date = None, p_contrat=None):
        """
        Constructeur de la classe Gestionnaire avec les attributs de sa classe mère Employe
        :param p_gerant: Le gérant du gestionnaire.
        :param p_specialite: La spécialité du gestionnaire.
        :param p_liste_commis: La liste des commis que le gestionnaire gère.
        :param p_liste_caissier: La liste des caissiers que le gestionnaire gère.
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)

        self.gerant = p_gerant
        self.specialite = p_specialite
        self.liste_commis = p_liste_commis
        self.liste_caissier = p_liste_caissier

    def ajouter_commis_a_liste(self, nom_commis_a_ajouter: str) -> None:
        """
        Ajouter un commis dans liste_commis
        :param nom_commis_a_ajouter: Commis à ajouter
        :return: La liste des commis avec le commis ajouté
        """
        for commis in self.liste_commis:
            if commis.nom == nom_commis_a_ajouter:
                return
        self.liste_commis.append(nom_commis_a_ajouter)


    def supprimer_commis_a_liste(self, nom_commis_a_supprimer: str) -> None:
        """
        Supprimer un commis dans liste_commis
        :param nom_commis_a_supprimer: Commis à supprimer
        :return: La liste des commis avec le commis supprimé
        """
        for commis in self.liste_commis:
            if commis.nom == nom_commis_a_supprimer:
                self.liste_commis.remove(nom_commis_a_supprimer)

    def ajouter_caissier_a_liste(self, nom_caissier_a_ajouter: str) -> None:
        """
        Ajouter un caissier dans liste_caissier
        :param nom_caissier_a_ajouter: Caissier à ajouter
        :return: La liste des caissier avec le caissier ajouté
        """
        for caissier in self.liste_caissier:
            if caissier.nom == nom_caissier_a_ajouter:
                return
        self.liste_caissier.append(nom_caissier_a_ajouter)

    def supprimer_caissier_a_liste(self, nom_caissier_a_supprimer: str) -> None:
        """
        Supprimer un caissier dans liste_caissier
        :param nom_caissier_a_supprimer: Caissier à supprimer
        :return: La liste des caissier avec le caissier supprimé
        """
        for caissier in self.liste_caissier:
            if caissier.nom == nom_caissier_a_supprimer:
                self.liste_caissier.remove(nom_caissier_a_supprimer)

