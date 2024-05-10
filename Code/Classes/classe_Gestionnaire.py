from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date, datetime

DATE_FONDATION_ENTREPRISE = datetime(2020, 5, 23)


class Gestionnaire(Employe):
    """
    Classe enfant Gestionnaire de la classe mère Employe
    """

    list_gestionnaire = []

    def __init__(self, p_gerant=None, p_specialite=None, p_dict_commis=None,
                 p_liste_caissier=None, p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_date_engagement: date = None, p_contrat=None, p_date_gestionnaire: date = None):
        """
        Constructeur de la classe Gestionnaire avec les attributs de sa classe mère Employe
        :param p_gerant: Le gérant du gestionnaire.
        :param p_dict_commis: Le dictionnaire des commis que le gestionnaire gère.
        :param p_liste_caissier: La liste des caissiers que le gestionnaire gère.
        :param p_date_gestionnaire: La date que ce gestionnaire à eu son titre de gestionnaire.
        """

        if p_liste_caissier is None:
            p_liste_caissier = []

        if p_dict_commis is None:
            p_dict_commis = {}

        p_poste = self.__class__.__name__
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat, p_specialite)

        self.gerant = p_gerant
        self.dict_commis = p_dict_commis
        self.liste_caissier = p_liste_caissier
        self._date_gestionnaire = p_date_gestionnaire

        Gestionnaire.list_gestionnaire.append(self)

    @property
    def date_gestionnaire(self):
        return self._date_gestionnaire

    @date_gestionnaire.setter
    def date_gestionnaire(self, v_date_gestionnaire: str):
        if isinstance(v_date_gestionnaire, str):
            if v_date_gestionnaire[:2].isdigit() and v_date_gestionnaire[2] == "/" and v_date_gestionnaire[
                                                                                       3:5].isdigit() and \
                    v_date_gestionnaire[5] == "/" and v_date_gestionnaire[6:].isdigit():
                date_formatee = datetime.strptime(v_date_gestionnaire, "%d/%m/%Y")
                if DATE_FONDATION_ENTREPRISE <= date_formatee <= datetime.now():
                    self._date_engagement = date_formatee
                else:
                    return

    def mettre_a_jour_dict_de_commis(self, ) -> None:
        """
        Met à jour le dict_commis que le gérant gère.
        """
        for commis in Commis.list_commis:
            if commis.gestionnaire == self.prenom:
                self.dict_commis[commis.identifiant] = commis

    def supprimer_commis_de_dict(self, identifiant_commis_a_supprimer: str) -> None:
        """
        Supprimer un commis dans dict_commis que le gérant gère.
        :param identifiant_commis_a_supprimer: L'identifiant du commis à supprimer
        """
        if identifiant_commis_a_supprimer in self.dict_commis.keys():
            self.dict_commis.pop(identifiant_commis_a_supprimer)

    def mettre_a_jour_list_caissier(self, identifiant_caissier_a_ajouter: str) -> None:
        """
         Met à jour la liste_caissier que le gérant gère.
        """
        for caissier in Caissier.liste_caissier:
            if caissier.gestionnaire == self.prenom:
                self.liste_caissier.append(caissier)

    def supprimer_caissier_de_list(self, identifiant_caissier_a_supprimer: str) -> None:
        """
        Supprimer un caissier dans liste_caissier que le gérant gère.
        :param identifiant_caissier_a_supprimer: L'identifiant du caissier à supprimer
        """
        for caissier in Caissier.liste_caissier:
            if caissier.identifiant == identifiant_caissier_a_supprimer:
                self.liste_caissier.remove(caissier)

    @staticmethod
    def parcourir_liste(liste_a_parcourir: list) -> str:
        """
        Une méthode statique qui permet de parcourir une liste et de retourner son contenus dans une chaîne de str.
        :param liste_a_parcourir: La liste à parcourir. | TYPE: list[Caissier] OU list[Commis]
        :return: La chaine de caractère contenant tout le contenu de la liste séparé pour être facilement affiché.
        """
        chaine_str = ""
        for element in liste_a_parcourir:
            chaine_str += f"{element.nom} | "
        return chaine_str

    def afficher_employe(self, nom_=True) -> str:
        """
        Affichage de superviseur
        :return:
        """
        chaine_caracteres = ""
        try:
            if nom_:
                chaine_caracteres += f"{self._nom}\n"
        except NameError:
            pass
        return chaine_caracteres

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du gestionnaire.
        :return: Les informations du gestionnaire dans un beau format d'affichage.
        """
        return f"{self.afficher_employe()}"
