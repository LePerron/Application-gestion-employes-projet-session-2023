from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date, datetime

DATE_FONDATION_ENTREPRISE = datetime(2020, 5, 23)


class ContratEmploi:
    """
    Classe ContratEmploi
    """

    list_contrat = []

    def __init__(self, p_identifiant_contrat: int = 0, p_employe: Employe = None, p_facteur_salaire: float = 0.0,
                 p_nb_heures_semaine: int = 0, p_salaire_horaire: float = 15.75, p_termes_embauche: str = "",
                 p_date_du_contrat: date = None):
        """
        :param p_identifiant_contrat: L'identifiant du contrat de l'employé
        :param p_employe: Le numéro de l'employé associé à ce contrat
        :param p_facteur_salaire: Facteur qui affecte le salaire de l'employé
        :param p_nb_heures_semaine: Nombre d'heures fait par l'employé
        :param p_salaire_horaire: Le salaire de base de l'employé
        :param p_termes_embauche: Termes d'emboche de l'employé
        :param p_date_du_contrat: Date du contrat
        """
        self.identifiant_contrat = p_identifiant_contrat
        self._facteur_salaire = p_facteur_salaire
        self._nb_heures_semaine = p_nb_heures_semaine
        self._salaire_horaire = p_salaire_horaire
        self.termes_embauche = p_termes_embauche
        self._date_du_contrat = p_date_du_contrat
        self.employe = p_employe

        ContratEmploi.list_contrat.append(self)

        self.identifiant_contrat = len(ContratEmploi.list_contrat)

    @property
    def nb_heures_semaine(self):
        return self._nb_heures_semaine

    @nb_heures_semaine.setter
    def nb_heures_semaine(self, v_nb_heures_semaine: int):
        if isinstance(v_nb_heures_semaine, int) and 40 >= v_nb_heures_semaine >= 0:
            self._nb_heures_semaine = v_nb_heures_semaine

    @property
    def salaire_horaire(self):
        return self._salaire_horaire

    @salaire_horaire.setter
    def salaire_horaire(self, v_salaire_horaire: float):
        if isinstance(v_salaire_horaire, float) and 56 >= v_salaire_horaire >= 15.75:
            self._salaire_horaire = v_salaire_horaire

    @property
    def facteur_salaire(self):
        return self._facteur_salaire

    @facteur_salaire.setter
    def facteur_salaire(self, v_facteur_salaire: float):
        if isinstance(v_facteur_salaire, float) and 100 >= v_facteur_salaire > 0:
            self._facteur_salaire = v_facteur_salaire

    @property
    def date_du_contrat(self):
        return self._date_du_contrat

    @date_du_contrat.setter
    def date_du_contrat(self, v_date_du_contrat: str):
        date_formatee = datetime.strptime(v_date_du_contrat, "%d/%m/%Y")
        if DATE_FONDATION_ENTREPRISE <= date_formatee <= datetime.now():
            self._date_du_contrat = date_formatee

    @classmethod
    def rechercher_contrat_par_date(cls, date_du_contrat: date) -> list:
        """
        Rechercher tout les contrats d'une date demandée.
        :param date_du_contrat: La date de recherche des contrats
        :return: La liste des contrats selon la date spécifique.
        """
        list_contrat_a_date = []
        for contrat in cls.list_contrat:
            if contrat.date_du_contrat == date_du_contrat:
                list_contrat_a_date.append(contrat)
        return list_contrat_a_date

    @classmethod
    def rechercher_contrat_par_employe(cls, identifiant_employe: str) -> list:
        """
        Rechercher contrat par employé.
        :param identifiant_employe: Identifiant de l'employé.
        :return: La liste des contrats selon l'employé demandé.
        """
        list_contrat_a_employe = []
        for contrat in cls.list_contrat:
            if contrat.employe.identifiant == identifiant_employe:
                list_contrat_a_employe.append(contrat)
        return list_contrat_a_employe

    @staticmethod
    def modifier_contrat(identifiant_contrat_renouvele: int, nouveau_facteur: float,
                         nouveau_salaire: float, nouveau_nb_heure: int) -> None:
        """
        Metode qui permet de modifier un contrat.
        :param identifiant_contrat_renouvele: L'identifiant du contrat qui doit être modifier.
        :param nouveau_facteur: Le nouveau facteur salaire du contrat.
        :param nouveau_salaire: Le nouveau salaire horaire du contrat.
        :param nouveau_nb_heure: Le nouveau nombre d'heure de travail.
        """
        for contrat in ContratEmploi.list_contrat:
            if contrat.identifiant_contrat == identifiant_contrat_renouvele:
                contrat.salaire_horaire = nouveau_salaire
                contrat.facteur_salaire = nouveau_facteur
                contrat.nb_heures_semaine = nouveau_nb_heure

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations du contrat.
        :return: Les informations du contrat dans un beau format d'affichage.
        """
        return (f"IDENTIFIANT DU CONTRAT : {self.identifiant_contrat} - SALAIRE DE BASE : {self.salaire_horaire} $ - "
                f"FACTEUR DU SALAIRE : {self.facteur_salaire} % - NOM DE L'EMPLOYÉ : {self.employe.nom} - "
                f"NOMBRE D'HEURE PAR SEMAINE : {self.nb_heures_semaine} h - "
                f"TERMES D'EMBAUCHE : {self.termes_embauche}")
