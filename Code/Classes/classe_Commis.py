from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date


class Commis(Employe):
    """
    Classe enfant Commis de la classe mère Employe
    """

    list_commis = []

    def __init__(self, p_gestionnaire=None, p_specialite=None, p_identifiant: str = "",
                 p_nom: str = "", p_prenom: str = "", p_date_engagement: date = None,
                 p_contrat=None):
        """
        Constructeur de la classe Commis avec les attributs de sa mère.
        :param p_gestionnaire: Le gestionnaire du commis.
        """
        p_poste = self.__class__.__name__
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat, p_specialite)

        self.gestionnaire = p_gestionnaire

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un bon format les informations du commis.
        :return: Les informations du commis dans un beau format d'affichage.
        """
        return f"{self.afficher_informations_employe()} - GESTIONNAIRE : {self.gestionnaire}"
