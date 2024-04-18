# Importation de la classe Gestionnaire
from Code.Classes.classe_Gestionnaire import Gestionnaire


class Caissier:
    """
    Classe Caissier enfant de la classe Employe.
    """

    # Création de la liste_caissier.
    liste_caissier = []

    # Création de la liste_specialite
    list_specialite = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: str = ""):
        """
        Constructeur de la classe Caissier
        :param p_gestionnaire: Le gestionnaire du caissier.
        :param p_specialite: La spécialité du caissier
        """
        self.gestionnaire = p_gestionnaire
        self._specialite = p_specialite

    # Get/Set specialite
    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, v_specialite: str):
        if v_specialite in Caissier.list_specialite:
            self._specialite = v_specialite

    # créer une nouvelle specialité (ajouter un "nom" à la liste des spécialités de la classe
    # enlever une spécialité (supprimer de la liste des spécialités)
    # modifier une spécialité (changer le "nom" de la spécialité dans la liste des spécialités)
