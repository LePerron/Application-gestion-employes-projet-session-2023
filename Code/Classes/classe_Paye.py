from datetime import date
from classe_Employe import Employe
from statistics import median


class Paye:
    """
    Classe Paye
    """
    list_paye = []

    def __init__(self, p_identifiant_paye: int = 0, p_employe: Employe = None, p_montant_paye: float = 0.0,
                 p_date_de_paye: date = None):
        """
        :param p_identifiant_paye: Identifiant unique de la paye
        :param p_montant_paye: Montant de la paye
        :param p_employe: L'employé qui reçoit la paye
        :param p_date_de_paye: Date de la paye
        """
        self.identifiant_paye = p_identifiant_paye
        self._montant_paye = p_montant_paye
        self._date_de_paye = p_date_de_paye
        self._employe = p_employe

        Paye.list_paye.append(self)

        if len(self.list_paye) < 1:
            self.identifiant_paye = 1
        else:
            self.identifiant_paye += 1

    def get_montant_paye(self):
        return self._montant_paye

    def set_montant_paye(self, v_montant_paye):
        if isinstance(v_montant_paye, float):
            self._montant_paye = v_montant_paye

    montant_paye = property(get_montant_paye, set_montant_paye)

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
    def mediane(cls):
        """
        Trouve le montant de la paye la plus petite de touts les employés
        :return: le montant de la paye la plus petite
        """
        montants = []
        for paye in cls.liste_paye:
            montants += paye.montant_paye
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
