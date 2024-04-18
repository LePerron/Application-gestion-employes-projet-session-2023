# Importation de la classe Gestionnaire
from Code.Classes.classe_Gestionnaire import Gestionnaire
# Importation de la class Specialite
from Code.Classes.classe_Specialite import Specialite


class Commis:
    """
    Classe enfant Commis de la classe mère Employe
    """

    # Création de list_commis
    list_commis = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: Specialite = None):
        """
        Constructeur de la classe Commis
        :param p_gestionnaire: Le gestionnaire du commis
        :param p_specialite: La spécialité du commis
        """
        self.gestionnaire = p_gestionnaire
        self.specialite = p_specialite
