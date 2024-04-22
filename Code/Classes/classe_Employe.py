from datetime import date, datetime


DATE_FONDATION_ENTREPRISE = datetime(2020, 5, 23)

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
                 p_poste: any = None, p_date_engagement: date = None, p_contrat=None, p_specialite=None):
        """
        Le constructeur de la classe mère Employe
        :param p_identifiant: L'identifiant unique de l'employé. | (7 digits, str)
        :param p_nom: Le nom de l'employé.
        :param p_prenom: Le prénom de l'employé.
        :param p_date_engagement: La date d'engagement de l'employé dans l'entreprise.
        :param p_contrat: Le contrat d'engagement de l'employé par l'entreprise.
        :param p_specialite: La spécialisation du poste de l'employé.
        """

        self._identifiant = p_identifiant
        self._nom = p_nom
        self._prenom = p_prenom
        self._date_engagement = p_date_engagement
        self.poste = p_poste
        self.contrat = p_contrat
        self.specialite = p_specialite

        from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
        self.contrat = ContratEmploi(p_employe=self)

        Employe.list_employe.append(self)

    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, v_identifiant: str) -> None:
        if len(v_identifiant) == 7 and isinstance(v_identifiant, str) and v_identifiant.isdigit:
            for employe in Employe.list_employe:
                if employe.identifiant == v_identifiant:
                    return
            self._identifiant = v_identifiant

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, v_nom: str) -> None:
        if isinstance(v_nom, str) and v_nom.isalpha():
            self._nom = v_nom.capitalize()

    @property
    def prenom(self):
        return self._nom

    @prenom.setter
    def prenom(self, v_prenom: str) -> None:
        if isinstance(v_prenom, str) and v_prenom.isalpha():
            self._prenom = v_prenom.capitalize()

    @property
    def date_engagement(self):
        return self._date_engagement

    @date_engagement.setter
    def date_engagement(self, v_date_engagement: str) -> None:
        date_formatee = datetime.strptime(v_date_engagement, "%d/%m/%Y")
        if DATE_FONDATION_ENTREPRISE <= date_formatee <= datetime.now():
            self._date_engagement = date_formatee

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

    def obtenir_poste_complet(self) -> str:
        """
        Une fonction qui permet d'obtenir le poste et la spécialité du poste de l'employé
        :return: Le poste de l'employé avec sa spécialité.. ex: Commis Boucherie
        """
        return f"{self.poste} {self.specialite}"

    def afficher_informations_employe(self) -> str:
        """
        Une fonction qui permet de retourner dans un bon format les informations de l'employé.
        :return: Les informations de l'employé dans un beau format d'affichage.
        """
        return (f"IDENTIFIANT : {self._identifiant} - NOM COMPLET : {self._nom} {self._prenom} - "
                f"POSTE : {self.poste.capitalize()} - NUM CONTRAT : {self.contrat.identifiant_contrat}")

    def __str__(self) -> str:
        """
        Une fonction magique qui permet de retourner dans un beau format les informations de l'employé.
         * La fonction **afficher_informations_employe** est utilisée pour permettre à ses enfants d'avoir leur propre
           fonction magique **__str__()** en plus de celui de la classe mère.

        :return: Les informations de l'employé dans un beau format d'affichage.
        """
        return self.afficher_informations_employe()

    @classmethod
    def __len__(cls) -> int:
        """
        Une méthode magique de classe qui permet de retourner le nombre d'employé total.
        :return: Le nombre d'employé total.
        """
        return len(cls.list_employe)
