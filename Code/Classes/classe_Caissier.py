from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date


class Caissier(Employe):
    """
    Classe Caissier enfant de la classe mère Employe.
    """

    liste_caissier = []

    def __init__(self, p_gestionnaire=None, p_specialite=None, p_identifiant: str = "",
                 p_nom: str = "", p_prenom: str = "", p_poste=None, p_date_engagement: date = None,
                 p_contrat=None):
        """
        Constructeur de la classe Caissier avec les attributs de sa classe mère.
        :param p_gestionnaire: Le gestionnaire du caissier.
        :param p_specialite: La spécialité du caissier
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)

        self.gestionnaire = p_gestionnaire
        self.specialite = p_specialite

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du caissier.
        :return: Les informations du caissier dans un beau format d'affichage.
        """
        return (f"{self.afficher_informations_employe()} - GESTIONNAIRE : {self.gestionnaire} - "
                f"SPÉCIALITÉ : {self.specialite.nom}")
