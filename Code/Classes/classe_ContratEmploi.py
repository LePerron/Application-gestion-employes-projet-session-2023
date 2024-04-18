class ContratEmploi:
    """
    Classes Equipe
    """

    list_contrat = []

    # Attribut de classe
    def __init__(self, p_identifiant_contrat: str = "", p_employe=None, p_facteur_salaire: float = 0.0,
                 p_nb_heures_semaine: int = 0, p_salaire_de_base: float = 0.0, p_termes_embauche: str = ""):
        """
        :param p_identifiant_contrat:
        :param p_employe: Le numéro de l'employé associé à ce contrat
        :param p_facteur_salaire:
        :param p_nb_heures_semaine:
        :param p_salaire_de_base:
        :param p_termes_embauche:
        """
        self.identifiant_contrat = p_identifiant_contrat
        self._facteur_salaire = p_facteur_salaire
        self._nb_heures_semaine = p_nb_heures_semaine
        self._salaire_de_base = p_salaire_de_base
        self._termes_embauche = p_termes_embauche
        self._employe = p_employe

    def get_nb_heures_semaine(self):
        return self._nb_heures_semaine

    def set_nb_heures_semaine(self, v_nb_heures_semaine):
        if isinstance(v_nb_heures_semaine, int):
            self._nb_heures_semaine = v_nb_heures_semaine

    nb_heures_semaine = property(get_nb_heures_semaine, set_nb_heures_semaine)

    def get_salaire_de_base(self):
        return self._salaire_de_base

    def set_salaire_de_base(self, v_salaire_de_base):
        if isinstance(v_salaire_de_base, float):
            self._salaire_de_base = v_salaire_de_base

    salaire_de_base = property(get_salaire_de_base, set_salaire_de_base)

    def get_termes_embauche(self):
        return self._termes_embauche

    def set_termes_embauche(self, v_termes_embauche):
        if isinstance(v_termes_embauche, str):
            self._termes_embauche = v_termes_embauche

    termes_embauche = property(get_termes_embauche, set_termes_embauche)

    def get_facteur_salaire(self):
        return self._facteur_salaire

    def set_facteur_salaire(self, v_facteur_salaire):
        if isinstance(v_facteur_salaire, float):
            self._facteur_salaire = v_facteur_salaire

    facteur_salaire = property(get_facteur_salaire, set_facteur_salaire)

    def get_employe(self):
        return self._employe

    def set_employe(self, v_employe):
        if isinstance(v_employe, Employe):
            self._employe = v_employe

    employe = property(get_employe, set_employe)

    def __str__(self):
        return (f"{self.identifiant_contrat} {self.nb_heures_semaine} {self.salaire_de_base} {self.termes_embauche} "
                f"{self.facteur_salaire} {self.employe}")
