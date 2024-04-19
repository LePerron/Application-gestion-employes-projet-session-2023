from classe_Employe import Employe
from statistics import median
from datetime import date


class Paye:
    """
    Classe Paye
    """
    list_paye = []

    def __init__(self, p_identifiant_paye: int = 0, p_employe: Employe = None, p_montant_paye: float = 0.0,
                 p_date_de_paye: date = None):
        """
        Le constructeur de la classe Paye.
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
            self.identifiant_paye = len(Paye.list_paye) + 1

    def _get_montant_paye(self):
        return self._montant_paye

    def _set_montant_paye(self, v_montant_paye):
        if isinstance(v_montant_paye, float):
            self._montant_paye = v_montant_paye

    montant_paye = property(_get_montant_paye, _set_montant_paye)

    def get_date_de_paye(self):
        return self._date_de_paye

    def set_date_de_paye(self, v_date_de_paye):
        self._date_de_paye = v_date_de_paye

    date_de_paye = property(get_date_de_paye, set_date_de_paye)

    def get_employe(self):
        return self._employe

    def set_employe(self, v_employe):
        if isinstance(v_employe, Employe):
            self._employe = v_employe

    employe = property(get_employe, set_employe)

    @classmethod
    def calculer_moyenne_payes(cls) -> float:
        """
        Calcul la moyenne de toutes les payes
        :return: La moyenne de toutes les payes
        """
        montants = 0
        for paye in cls.list_paye:
            montants += paye.montant_paye
        return montants / len(cls.list_paye)

    @classmethod
    def calculer_mediane_payes(cls) -> float:
        """
        Calcul la médiane de toutes les payes
        :return: La médiane de toute les payes
        """
        montants = []
        for paye in cls.list_paye:
            montants += paye.montant_paye
        return median(montants)

    @classmethod
    def obtenir_paye_min(cls) -> float:
        """
        Trouve Le montant de la paye la plus petite de toutes les payes
        :return: Le montant de la paye la plus petite
        """
        return min(paye.montant_paye for paye in cls.list_paye)

    @classmethod
    def obtenir_paye_max(cls) -> float:
        """
        Trouve Le montant de la paye la plus grosse de toutes les payes
        :return: Le montant de la paye la plus haute
        """
        return max(paye.montant_paye for paye in cls.list_paye)

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un bon format les informations de la paye.
        :return: Les informations de la paye dans un beau format d'affichage.
        """
        return (f"IDENTIFIANT DE LA PAYE : {self.identifiant_paye} MONTANT DE LA PAYE : {self._montant_paye}"
                f" DATE DE LA PAYE : {self._date_de_paye} EMPLOYÉ QUI REÇOIS LA PAYE : {self._employe}")
