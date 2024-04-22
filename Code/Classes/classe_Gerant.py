from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date


class Gerant(Employe):
    """
    Classe enfant Gerant de la classe mère Employe.
    """

    def __init__(self, p_specialite=None, p_liste_gestionnaire=None,
                 p_identifiant: str = "", p_nom: str = "", p_prenom: str = "", p_date_engagement: date = None,
                 p_contrat=None):
        """
        Constructeur de la classe Gerant qui fait app   el à sa classe mère Employe.
        :param p_liste_gestionnaire: La liste des gestionnaires que le gérant gère.
        """
        p_poste = self.__class__.__name__
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat, p_specialite)

        self.liste_gestionnaire = p_liste_gestionnaire

    def ajouter_gestionnaire_de_liste(self, identifiant_gestionnaire_a_ajouter: str) -> None:
        """
        Ajouter un gestionnaire dans la liste_gestionnaire que le gérant gère
        :param identifiant_gestionnaire_a_ajouter: L'identifiant du Gestionnaire à ajouter
        """
        for gestionnaire in self.liste_gestionnaire:
            if gestionnaire.identifiant != identifiant_gestionnaire_a_ajouter:
                continue
            else:
                if gestionnaire not in self.liste_gestionnaire:
                    self.liste_gestionnaire.append(gestionnaire)

    def supprimer_gestionnaire_de_liste(self, identifiant_gestionnaire_a_supprimer: str) -> None:
        """
        Supprimer un gestionnaire dans la liste_gestionnaire
        :param identifiant_gestionnaire_a_supprimer: L'identifiant du Gestionnaire à supprimer
        """
        for gestionnaire in self.liste_gestionnaire:
            if gestionnaire.identifiant == identifiant_gestionnaire_a_supprimer:
                self.liste_gestionnaire.remove(gestionnaire)

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du gérant.
        :return: Les informations du gérant dans un beau format d'affichage.
        """
        return self.afficher_informations_employe()
