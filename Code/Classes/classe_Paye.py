from datetime import date
from classe_Employe import Employe


class Paye:
    """
    Classes Paye
    """
    # Attribut de classe
    def __init__(self, p_identifiant_paye: str = "", p_employe: Employe = None, p_montant_paye: float = 0.0, p_date_de_paye:date = None):
        """
        :param identifiant_paye:
        :param p_montant_paye:
        :param p_employe:
        :param p_date_de_paye:
        """
        self.identifiant_paye = p_identifiant_paye
        self._montant_paye = p_montant_paye
        self._date_de_paye = p_date_de_paye
        self._employe = p_employe

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

    def __str__(self):
        return f"{self.identifiant_paye}{self.nb_montant_paye} {self.date_de_paye} {self.employe}"
