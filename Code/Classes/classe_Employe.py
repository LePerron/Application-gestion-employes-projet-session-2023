from datetime import date, datetime
from classe_ContratEmploi import ContratEmploi

#               UMLs            #
# +contrat: ContratEmploi = None
# +contrat = ContratEmploi: ContratEmploi
#
# À FAIRE !!!!
#   → dans le menu, faire "Gestion des contrats des employés"
#        ⇉ créer un contrat
#        ⇉ modifier un contrat
#        ⇉ supprimer un contrat


class Employe:
    """
    Classe mère Employe
    """
    list_employe = []

    def __init__(self, p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: any = "", p_date_engagement: date = None, p_contrat: ContratEmploi = None):
        """
        Le constructeur de la classe mére Employe
        :param p_identifiant: L'identifiant unique de l'employé. (7 digits, str)
        :param p_nom: Le nom de l'employé.
        :param p_prenom: Le prénom de l'employé.
        :param p_poste: Le poste qu'occupe l'employé.
        :param p_date_engagement: La date d'engagement de l'employé dans l'entreprise.
        :param p_contrat: Le contrat d'engagement de l'employé par l'entreprise.
        """

        self._identifiant = p_identifiant
        self._nom = p_nom
        self._prenom = p_prenom
        self._date_engagement = p_date_engagement
        self.poste = p_poste
        self.contrat = p_contrat

        # for contrat in ContratEmploi.list_contrat:
        #     if contrat.employe == self._identifiant:
        #         self.contrat = contrat

        Employe.list_employe.append(self)

    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, v_identifiant: str):
        if len(v_identifiant) == 7 and isinstance(v_identifiant, str) and v_identifiant.isdigit:
            self._identifiant = v_identifiant

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, v_nom: str):
        if isinstance(v_nom, str) and v_nom.isalpha():
            self._nom = v_nom

    @property
    def prenom(self):
        return self._nom

    @prenom.setter
    def prenom(self, v_prenom: str):
        if isinstance(v_prenom, str) and v_prenom.isalpha():
            self._prenom = v_prenom

    @property
    def date_engagement(self):
        return self._date_engagement

    @date_engagement.setter
    def date_engagement(self, v_date_engagement: str):
        date_naissance_formatee = datetime.strptime(v_date_engagement, "%d/%m/%Y")
        self._date_engagement = date_naissance_formatee

    def obtenir_anciennete(self) -> int:
        """
        Une méthode qui permet d'obtenir l'ancienneté d'un employé.
        :return: Le nombre d'années d'ancienneté
        """
        return (datetime.now() - self._date_engagement).days // 365

    def est_temps_plein(self) -> bool:
        """
        Une méthode qui retourne True si l'employé travail plus de 40 heures / semaine.
        :return: True si l'employé est à temps plein sinon False
        """
        return self.contrat.nb_heures_semaine >= 40

    def obtenir_specialite(self) -> str:
        return f"{self.poste.__name__} {self.poste.specialite}"

    def __str__(self) -> str:
        return (f"IDENTIFIANT : {self._identifiant} - NOM COMPLET : {self._nom} "
                f"{self._prenom} - POSTE : {self.poste.nom} - NUM CONTRAT : {self.contrat.identifiant_contrat}")

