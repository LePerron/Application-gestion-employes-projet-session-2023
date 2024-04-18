from datetime import date
from classe_Employe import Employe
from statistics import median


class Paye:
    """
    Classes Paye
    """
    liste_paye = []

    def __init__(self, p_identifiant_paye: str = "", p_employe: Employe = None, p_montant_paye: float = 0.0, p_date_de_paye:date = None):
        """
        :param identifiant_paye: Identifiant de la paye
        :param p_montant_paye: montant de la paye la plus récente
        :param p_employe: l'employe qui reçoit la paye
        :param p_date_de_paye: date de la paye la plus récente
        """
        self.identifiant_paye = p_identifiant_paye
        self._montant_paye = p_montant_paye
        self._date_de_paye = p_date_de_paye
        self._employe = p_employe
        Paye.liste_paye.append(self)

    def get_montant_paye(self):
        return self._montant_paye

    def set_montant_paye(self, v_montant_paye):
        if isinstance(v_montant_paye, float):
            self._montant_paye = v_montant_paye

    nb_montant_paye = property(get_montant_paye, set_montant_paye)

    def get_date_de_paye(self):
        return self._date_de_paye

    def set_date_de_paye(self, v_date_de_paye):
        if isinstance(v_date_de_paye, date):
            self._date_de_paye = v_date_de_paye

    date_de_paye = property(get_date_de_paye, set_date_de_paye)

    def get_employe(self):
        return self._employe

    def set_employe(self, v_employe):
        if isinstance(v_employe, Employe):
            self._employe = v_employe

    employe = property(get_employe, set_employe)

    @classmethod
    def rechercher_paye_par_date(cls, date_de_paye: date) -> list:
        """
        Trouve les paiements effectués à une date.
        :param date_de_paye: La date
        :return: Une liste des paiements effectués à la date spécifiée
        """
        paiements_a_date = []
        for paye in cls.liste_paye:
            if paye.date_de_paye == date_de_paye:
                paiements_a_date.append(paye)
        return paiements_a_date

    @classmethod
    def rechercher_paye_par_employe(cls, employe: Employe) -> list:
        """
        Trouve les payes envoyées à un employé.
        :param employe: L'employé
        :return: Une liste des paiements envoyés à l'employé
        """
        paiements_par_employe = []
        for paye in cls.liste_paye:
            if paye.employe == employe:
                paiements_par_employe.append(paye)
        return paiements_par_employe

    @classmethod
    def moyenne(cls):
        """
        Trouve le montant de la paye la plus petite de touts les employés
        :return: le montant de la paye la plus petite
        """
        montants = 0
        for paye in cls.liste_paye:
            montants += paye.montant_paye
        return montants / len(cls.liste_paye)

    @classmethod
    def mediane(cls) -> float:
        """
        Trouve le montant de la paye la plus petite de touts les employés
        :return: le montant de la paye la plus petite
        """
        montants = []
        for paye in cls.liste_paye:
            montants.append(paye.montant_paye)
        return median(montants)

    @classmethod
    def min(cls) -> float:
        """
        Trouve le montant de la paye la plus petite de touts les employés
        :return: le montant de la paye la plus petite
        """
        return min(paye.montant_paye for paye in cls.liste_paye)

    @classmethod
    def max(cls) -> float:
        """
        Trouve le montant de la paye la plus grosse de touts les employés
        :return: le montant de la paye la plus haute
        """
        return max(paye.montant_paye for paye in cls.liste_paye)

    def __str__(self):
        return (f"IDENTIFIANT DE LA PAYE : {self.identifiant_paye} MONTANT DE LA PAYE : {self.nb_montant_paye}"
                f" DATE DE LA PAYE : {self.date_de_paye} EMPLOYÉ QUI REÇOIS LA PAYE : {self.employe}")
