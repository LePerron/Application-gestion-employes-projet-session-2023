from Code.Classes.classe_Employe import Employe


class ContratEmploi:
    """
    Classes Equipe
    """

    list_contrat = []

    # Attribut de classe
    def __init__(self, p_identifiant_contrat: str = "", p_employe: Employe = None, p_facteur_salaire: float = 0.0, p_nb_heures_semaine: int = 0,
                 p_salaire_de_base: float = 0.0, p_termes_embauche: str = ""):
        """
        :param p_identifiant_contrat:
        :param p_employe:
        :param p_facteur_salaire:
        :param p_nb_heures_semaine:
        :param p_salaire_de_base:
        :param p_termes_embauche:
        """
        self.identifiant_contrat = p_identifiant_contrat
        self.facteur_salaire = p_facteur_salaire
        self.nb_heures_semaine = p_nb_heures_semaine
        self.salaire_de_base = p_salaire_de_base
        self.termes_embauche = p_termes_embauche

    def get_nb_heures_semaine(self):
        return self.nb_heures_semaine

    def set_nb_heures_semaine(self, nb_heures_semaine):
        self.nb_heures_semaine = nb_heures_semaine

    def get_salaire_de_base(self):
        return self.salaire_de_base

    def set_salaire_de_base(self, salaire_de_base):
        self.salaire_de_base = salaire_de_base

    def get_termes_embauche(self):
        return self

    def set_termes_embauche(self, termes_embauche):
        self.termes_embauche = termes_embauche

    def get_facteur_salaire(self):
        return self.facteur_salaire

    def set_facteur_salaire(self, facteur_salaire):
        self.facteur_salaire = facteur_salaire

    def __str__(self):
        return f"Le joueur"
