# Importation de la classe Gestionnaire
<<<<<<< HEAD
from classe_Gestionnaire import Gestionnaire
# Importation de la class Specialite
from classe_Specialite import Specialite
=======

from classe_Gestionnaire import Gestionnaire
from classe_Specialite import Specialite


>>>>>>> 3f52adaadf531f7280a1369d1799e416be02ad5e


class Caissier:
    """
    Classe Caissier enfant de la classe mère Employe.
    """

    # Création de la liste_caissier.
    liste_caissier = []

    def __init__(self, p_gestionnaire: Gestionnaire = None, p_specialite: Specialite = None):
        """
        Constructeur de la classe Caissier
        :param p_gestionnaire: Le gestionnaire du caissier.
        :param p_specialite: La spécialité du caissier
        """
        self.gestionnaire = p_gestionnaire
        self.specialite = p_specialite
