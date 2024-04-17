from datetime import date
from classe_Employe import Employe


class Paye:
    """
    Classe Paye
    """
    # Attribut de classe
    def __init__(self, identifiant_paye: str = "", p_employe: Employe = None, p_montant_paye: float = 0.0, p_date_de_paye:date = None):
        """
        :param identifiant_paye:
        :param p_montant_paye:
        :param p_employe:
        :param p_date_de_paye:
        """
        self.montant_paye = p_montant_paye
        self.identifiant = identifiant_paye
        self.date_de_paye = p_date_de_paye
        self.employe = p_employe



