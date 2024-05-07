from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from statistics import median
from datetime import date, datetime

DATE_FONDATION_ENTREPRISE = datetime(2020, 5, 23)


class Paye:
    """
    Classe Paye
    """
    list_payes = []

    def __init__(self, p_identifiant_paye: int = 0, p_employe: Employe = None, p_montant_paye: float = 0.0,
                 p_date_de_paye: date = None):
        """
        Le constructeur de la classe Paye.
        :param p_identifiant_paye: Identifiant unique de la Paye
        :param p_montant_paye: Montant de la Paye
        :param p_employe: L'employé qui reçoit la Paye
        :param p_date_de_paye: Date de la Paye
        """
        self.identifiant_paye = p_identifiant_paye
        self._montant_paye = p_montant_paye
        self._date_de_paye = p_date_de_paye
        self._employe = p_employe

        Paye.list_payes.append(self)

        if len(self.list_payes) < 1:
            self.identifiant_paye = 1
        else:
            self.identifiant_paye = len(Paye.list_payes) + 1

    @property
    def montant_paye(self):
        return self._montant_paye

    @montant_paye.setter
    def montant_paye(self, v_montant_paye):
        if isinstance(v_montant_paye, float) and v_montant_paye >= 0:
            self._montant_paye = v_montant_paye

    @property
    def employe(self):
        return self._employe

    @employe.setter
    def employe(self, v_identifiant_employe):
        for employe in Employe.list_employe:
            if employe.identifiant != v_identifiant_employe:
                continue
            else:
                self._employe = employe

    @property
    def date_de_paye(self):
        return self._date_de_paye

    @date_de_paye.setter
    def date_de_paye(self, v_date_de_paye):
        if DATE_FONDATION_ENTREPRISE <= v_date_de_paye <= datetime.now():
            self._date_de_paye = v_date_de_paye

    @classmethod
    def calculer_moyenne_payes(cls) -> float:
        """
        Calcul la moyenne de toutes les payes
        :return: La moyenne de toutes les payes
        """
        montants = 0
        for paye in cls.list_payes:
            montants += paye.montant_paye
        moyenne = montants / len(cls.list_payes)
        return moyenne

    @classmethod
    def calculer_mediane_payes(cls) -> float:
        """
        Calcul la médiane de toutes les payes
        :return: La médiane de toute les payes
        """
        montant_total = []
        for paye in cls.list_payes:
            montant_total.append(paye.montant_paye)
        mediane = median(montant_total)
        return mediane

    @classmethod
    def obtenir_paye_min(cls) -> float:
        """
        Trouve Le montant de la Paye la plus petite de toutes les payes
        :return: Le montant de la Paye la plus petite
        """
        return min(paye.montant_paye for paye in cls.list_payes)

    @classmethod
    def obtenir_paye_max(cls) -> float:
        """
        Trouve Le montant de la Paye la plus grosse de toutes les payes
        :return: Le montant de la Paye la plus haute
        """
        return max(paye.montant_paye for paye in cls.list_payes) or 0

    @classmethod
    def rechercher_payes_par_date(cls, date_de_paye: date) -> list:
        """
        Trouve les paiements effectués selon une date.
        :param date_de_paye: La date de recherche
        :return: Une liste des paiements effectués à la date spécifiée
        """
        list_payes_a_date = []
        for paye in cls.list_payes:
            if paye.date_de_paye == date_de_paye:
                list_payes_a_date.append(paye)
        return list_payes_a_date

    @classmethod
    def rechercher_payes_par_employe(cls, identifiant_employe: str) -> list:
        """
        Trouve toutes les payes d'un employé.
        :param identifiant_employe: L'identifiant de l'employé de recherche.
        :return: Une liste des toutes les payes de l'employé.
        """
        paye_a_employe = []
        for paye in cls.list_payes:
            if paye.employe.identifiant == identifiant_employe:
                paye_a_employe.append(paye)
        return paye_a_employe

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations de la Paye.
        :return: Les informations de la Paye dans un beau format d'affichage.
        """
        return (f"IDENTIFIANT DE LA PAYE : {self.identifiant_paye} - MONTANT DE LA PAYE : {self._montant_paye}"
                f" DATE DE LA PAYE : {self._date_de_paye} - EMPLOYÉ QUI REÇOIS LA PAYE : {self._employe}")
