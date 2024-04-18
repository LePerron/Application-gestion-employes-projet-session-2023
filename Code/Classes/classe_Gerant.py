from classe_Gestionnaire import Gestionnaire
from classe_Specialite import Specialite
from classe_Employe import Employe
from datetime import date


class Gerant(Employe):
    """
    Classes enfant Gerant de la classe mère Employe.
    """

    def __init__(self, p_specialite: Specialite = None, p_liste_gestionnaire: list = [Gestionnaire],
                 p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: any = "", p_date_engagement: date = None, p_contrat=None):
        """
        Constructeur de la classe Gerant qui fait appel à sa classe mère Employe.
        :param p_specialite: Spécialité du gerant
        :param p_liste_gestionnaire: La liste des gestionnaires que le gérant gère.
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)

        self.specialite = p_specialite
        self.liste_gestionnaire = p_liste_gestionnaire

    # Ajouter un gestionnaire dans liste_gestionnaire à gérer

    def ajouter_gestionnaire_a_liste(self, gestionnaire_a_ajouter: Gestionnaire) -> None:
        """
        Ajouter un gestionnaire dans liste_gestionnaire
        :param gestionnaire_a_ajouter: Gestionnaire à ajouter
        :return: La liste des gestionnaires avec le gestionnaire ajouté
        """
        self.liste_gestionnaire.append(gestionnaire_a_ajouter)

    # Supprimer un gestionnaire dans liste_gestionnaire à gérer

    def supprimer_gestionnaire_a_liste(self, gestionnaire_a_supprimer: Gestionnaire) -> None:
        """
        Supprimer un gestionnaire dans la liste_gestionnaire
        :param gestionnaire_a_supprimer: Gestionnaire à supprimer
        """
        self.liste_gestionnaire.remove(gestionnaire_a_supprimer)


    def __str__(self):
        return
