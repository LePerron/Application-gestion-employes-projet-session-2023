# Importation de la classe Gestionnaire
from classe_Gestionnaire import Gestionnaire
from classe_Specialite import Specialite



class Gerant:
    """
    Classes Gerant
    """

    def __init__(self, p_specialite: Specialite = None, p_liste_gestionnaire: list = [Gestionnaire]):
        """
        Constructeur de la classe Gerant
        :param p_specialite: Spécialité du gerant
        :param p_liste_gestionnaire: La liste des gestionnaires que le gérant gère.
        """
        self.specialite = p_specialite
        self.liste_gestionnaire = p_liste_gestionnaire

    # Ajouter un gestionnaire dans liste_gestionnaire à gérer

    def ajouter_gestionnaire_a_liste(self, gestionnaire_a_ajouter: Gestionnaire) -> list:
        """
        Ajouter un gestionnaire dans liste_gestionnaire
        :param gestionnaire_a_ajouter: Gestionnaire à ajouter
        :return: La liste des gestionnaires avec le gestionnaire ajouté
        """
        self.liste_gestionnaire.append(gestionnaire_a_ajouter)

    # Supprimer un gestionnaire dans liste_gestionnaire à gérer

    def supprimer_gestionnaire_a_liste(self, gestionnaire_a_supprimer: Gestionnaire) -> list:
        """
        Supprimer un gestionnaire dans la liste_gestionnaire
        :param gestionnaire_a_supprimer: Gestionnaire à supprimer
        :return: La liste des gestionnaires avec le gestionnaire supprimé
        """
        self.liste_gestionnaire.remove(gestionnaire_a_supprimer)



