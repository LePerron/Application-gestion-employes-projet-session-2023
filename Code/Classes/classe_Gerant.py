from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date, datetime

from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

DATE_FONDATION_ENTREPRISE = datetime(2020, 5, 23)

class Gerant(Employe):
    """
    Classe enfant Gerant de la classe mère Employe.
    """

    def __init__(self, p_specialite=None, p_liste_gestionnaire=None,
                 p_identifiant: str = "", p_nom: str = "", p_prenom: str = "", p_date_engagement: date = None,
                 p_contrat=None, p_date_gerant: date = None):
        """
        Constructeur de la classe Gerant qui fait app   el à sa classe mère Employe.
        :param p_liste_gestionnaire: La liste des gestionnaires que le gérant gère.
        """
        if p_liste_gestionnaire is None:
            p_liste_gestionnaire = []

        p_poste = self.__class__.__name__
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat, p_specialite)

        self.liste_gestionnaire = p_liste_gestionnaire
        self._date_gerant = p_date_gerant

    @property
    def date_gerant(self):
        return self._date_gerant

    @date_gerant.setter
    def date_gerant(self, v_date_gerant: str):
        if isinstance(v_date_gerant, str):
            if v_date_gerant[:2].isdigit() and v_date_gerant[2] == "/" and v_date_gerant[3:5].isdigit() and v_date_gerant[5] == "/" and v_date_gerant[6:].isdigit():
                date_formatee = datetime.strptime(v_date_gerant, "%d/%m/%Y")
                if DATE_FONDATION_ENTREPRISE <= date_formatee <= datetime.now():
                    self._date_gerant = date_formatee
                else:
                    return

    def ajouter_gestionnaire_a_liste(self, identifiant_gestionnaire_a_ajouter: str) -> None:
        """
        Ajouter un gestionnaire dans la liste_gestionnaire que le gérant gère
        :param identifiant_gestionnaire_a_ajouter: L'identifiant du Gestionnaire à ajouter
        """
        for gestionnaire in Gestionnaire.list_gestionnaire:
            if gestionnaire.identifiant == identifiant_gestionnaire_a_ajouter:
                if gestionnaire in self.liste_gestionnaire:
                    return
                else:
                    self.liste_gestionnaire.append(gestionnaire)

    def supprimer_gestionnaire_a_liste(self, identifiant_gestionnaire_a_supprimer: str) -> None:
        """
        Supprimer un gestionnaire dans la liste_gestionnaire
        :param identifiant_gestionnaire_a_supprimer: L'identifiant du Gestionnaire à supprimer
        """
        for gestionnaire in Gestionnaire.list_gestionnaire:
            if gestionnaire.identifiant == identifiant_gestionnaire_a_supprimer:
                self.liste_gestionnaire.remove(gestionnaire)

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du gérant.
        :return: Les informations du gérant dans un beau format d'affichage.
        """
        return self.afficher_informations_employe()
