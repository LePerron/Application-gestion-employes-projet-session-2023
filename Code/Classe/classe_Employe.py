from datetime import date, datetime


class Employe:
    """
    Classe Mère Employe
    """
    list_employe = []

    def __init__(self, p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: str = "", p_date_engagement: date = None):
        """
        Le constructeur de la classe mère Employe
        :param p_identifiant: L'identifiant unique de l'employé. (7 digits, str)
        :param p_nom: Le nom de l'employé.
        :param p_prenom: Le prénom de l'employé.
        :param p_poste: Le poste qu'occupe l'employé.
        :param p_date_engagement: La date d'engagement de l'employé dans l'entreprise.
        """

        self._identifiant = p_identifiant
        self._nom = p_nom
        self._prenom = p_prenom
        self._poste = p_poste
        self._date_engagement = p_date_engagement

        Employe.list_employe.append(self)

    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, v_identifiant):
        if len(v_identifiant) == 7 and isinstance(v_identifiant, str) and v_identifiant.isdigit:
            self._identifiant = v_identifiant

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, v_nom):
        if isinstance(v_nom, str) and v_nom.isalpha():
            self._nom = v_nom

    @property
    def prenom(self):
        return self._nom

    @prenom.setter
    def prenom(self, v_prenom):
        if isinstance(v_prenom, str) and v_prenom.isalpha():
            self._prenom = v_prenom

    @property
    def date_engagement(self):
        return self._date_engagement

    @date_engagement.setter
    def date_engagement(self, v_date_engagement):
        date_naissance_formatee = datetime.strptime(v_date_engagement, "%d/%m/%Y")
        self._date_engagement = date_naissance_formatee

    def obtenir_anciennete(self):

        return self._date_engagement
