from datetime import date


class Employe:
    """
    Classe M�re Employe
    """

    def __init__(self, p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: str = "", p_date_engagement: date = None):
        """
        Le constructeur de la classe m�re Employe
        :param p_identifiant: L'identifiant unique de l'employ�. (7 digits, str)
        :param p_nom: Le nom de l'employ�.
        :param p_prenom: Le pr�nom de l'employ�.
        :param p_poste: Le poste qu'occupe l'employ�.
        :param p_date_engagement: La date d'engagement de l'employ� dans l'entreprise.
        """

        self._identifiant = p_identifiant
        self._nom = p_nom
        self._prenom = p_prenom
        self._poste = p_poste
        self._date_engagement = p_date_engagement



