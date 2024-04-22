from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date


class Gestionnaire(Employe):
    """
    Classe enfant Gestionnaire de la classe mère Employe
    """

    list_gestionnaire = []

    def __init__(self, p_gerant=None, p_specialite=None, p_liste_commis=None,
                 p_liste_caissier=None,  p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_date_engagement: date = None, p_contrat=None):
        """
        Constructeur de la classe Gestionnaire avec les attributs de sa classe mère Employe
        :param p_gerant: Le gérant du gestionnaire.
        :param p_liste_commis: La liste des commis que le gestionnaire gère.
        :param p_liste_caissier: La liste des caissiers que le gestionnaire gère.
        """
        p_poste = self.__class__.__name__
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat, p_specialite)

        self.gerant = p_gerant
        self.liste_commis = p_liste_commis
        self.liste_caissier = p_liste_caissier

    def ajouter_commis_a_liste(self, identifiant_commis_a_ajouter: str) -> None:
        """
        Ajouter un commis dans liste_commis que le gérant gère.
        :param identifiant_commis_a_ajouter: L'identifiant du commis à ajouter
        """
        for commis in self.liste_commis:
            if commis.identifiant != identifiant_commis_a_ajouter:
                continue
            else:
                if commis not in self.liste_commis:
                    self.liste_commis.append(commis)

    def supprimer_commis_a_liste(self, identifiant_commis_a_supprimer: str) -> None:
        """
        Supprimer un commis dans liste_commis que le gérant gère.
        :param identifiant_commis_a_supprimer: L'identifiant du commis à supprimer
        """
        for commis in self.liste_commis:
            if commis.identifiant == identifiant_commis_a_supprimer:
                self.liste_commis.remove(commis)

    def ajouter_caissier_a_liste(self, identifiant_caissier_a_ajouter: str) -> None:
        """
        Ajouter un caissier dans liste_caissier que le gérant gère.
        :param identifiant_caissier_a_ajouter: L'identifiantCaissier du caissier à ajouter
        """
        for caissier in self.liste_caissier:
            if caissier.identifiant != identifiant_caissier_a_ajouter:
                continue
            else:
                if caissier not in self.liste_caissier:
                    self.liste_caissier.append(caissier)

    def supprimer_caissier_a_liste(self, identifiant_caissier_a_supprimer: str) -> None:
        """
        Supprimer un caissier dans liste_caissier que le gérant gère.
        :param identifiant_caissier_a_supprimer: L'identifiant du caissier à supprimer
        """
        for caissier in self.liste_caissier:
            if caissier.identifiant == identifiant_caissier_a_supprimer:
                self.liste_caissier.remove(identifiant_caissier_a_supprimer)

    @staticmethod
    def parcourir_liste(liste_a_parcourir: list) -> str:
        """
        Une méthode statique qui permet de parcourir une liste et de retourner son contenus dans une chaîne de str.
        :param liste_a_parcourir: La liste à parcourir. | TYPE: list[Caissier] OU list[Commis]
        :return: La chaine de caractère contenant toute le contenu de la liste séparé pour être facilement affiché.
        """
        chaine_str = ""
        for element in liste_a_parcourir:
            chaine_str += f"{element.nom} | "
        return chaine_str

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du gestionnaire.
        :return: Les informations du gestionnaire dans un beau format d'affichage.
        """
        return f"{self.afficher_informations_employe()} - GÉRANT : {self.gerant}"
