# Importation de la classe Gestionnaire
from classe_Gestionnaire import Gestionnaire
# Importation de la class Specialite
from classe_Specialite import Specialite
from datetime import date
from classe_Employe import Employe
from classe_ContratEmploi import ContratEmploi


class Commis(Employe):
    """
    Classe enfant Commis de la classe mère Employe
    """

    # Création de list_commis
    list_commis = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: Specialite = None, p_identifiant: str = "",
                 p_nom: str = "", p_prenom: str = "", p_poste: any = "", p_date_engagement: date = None,
                 p_contrat: ContratEmploi = None):
        """
        Constructeur de la classe Commis
        :param p_gestionnaire: Le gestionnaire du commis
        :param p_specialite: La spécialité du commis
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)
        self.gestionnaire = p_gestionnaire
        self.specialite = p_specialite
