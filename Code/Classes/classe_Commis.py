# Importation de la classe Gestionnaire
from Code.Classes.classe_Gestionnaire import Gestionnaire


class Commis:
    """
    Classe enfant Commis de la classe mère Employe
    """

    # Création de list_commis
    list_commis = []

    # Création de liste_specialite
    list_specialite = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: str = ""):
        """
        Constructeur de la classe Commis
        :param p_gestionnaire: Le gestionnaire du commis
        :param p_specialite: La spécialité du commis
        """
        self.gestionnaire = p_gestionnaire
        self._specialite = p_specialite

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, v_specialite: str):
        if v_specialite in Commis.list_specialite:
            self._specialite = v_specialite

    # | MÉTHODE À AJOUTER | #
    # créer une nouvelle specialité (ajouter un "nom" à la liste des spécialités de la classe
    # enlever une spécialité (supprimer de la liste des spécialités)
    # modifier une spécialité (changer le "nom" de la spécialité dans la liste des spécialités)
