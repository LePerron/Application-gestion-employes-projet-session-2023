from classe_Gestionnaire import Gestionnaire
from classe_Specialite import Specialite
from classe_Employe import Employe
from datetime import date


class Commis(Employe):
    """
    Classe enfant Commis de la classe mère Employe
    """

    list_commis = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: Specialite = None, p_identifiant: str = "",
                 p_nom: str = "", p_prenom: str = "", p_poste: any = "", p_date_engagement: date = None,
                 p_contrat=None):
        """
        Constructeur de la classe Commis avec les attributs de sa mère.
        :param p_gestionnaire: Le gestionnaire du commis.
        :param p_specialite: La spécialité du commis.
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)

        self.gestionnaire = p_gestionnaire
        self.specialite = p_specialite

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un bon format les informations du commis.
        :return: Les informations du commis dans un beau format d'affichage.
        """
        return (f"{self.afficher_informations_employe()} - GESTIONNAIRE : {self.gestionnaire}"
                f" - SPÉCIALITÉ : {self.specialite}")
