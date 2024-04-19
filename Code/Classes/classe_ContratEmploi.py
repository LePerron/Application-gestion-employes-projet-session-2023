from classe_Employe import Employe


class ContratEmploi:
    """
    Classe ContratEmploi
    """

    list_contrat = []

    def __init__(self, p_identifiant_contrat: int = 0, p_employe: Employe = None, p_facteur_salaire: float = 0.0,
                 p_nb_heures_semaine: int = 0, p_salaire_de_base: float = 0.0, p_termes_embauche: str = ""):
        """
        :param p_identifiant_contrat: L'identifiant du contrat de l'employé
        :param p_employe: Le numéro de l'employé associé à ce contrat
        :param p_facteur_salaire: Facteur qui affecte le salaire de l'employé
        :param p_nb_heures_semaine: Nombre d'heures fait par l'employé
        :param p_salaire_de_base: Le salaire de base de l'employé
        :param p_termes_embauche: Termes d'emboche de l'employé
        """
        self.identifiant_contrat = p_identifiant_contrat
        self._facteur_salaire = p_facteur_salaire
        self._nb_heures_semaine = p_nb_heures_semaine
        self._salaire_de_base = p_salaire_de_base
        self._termes_embauche = p_termes_embauche
        self._employe = p_employe

        if len(self.list_contrat) < 1:
            self.identifiant_contrat = 1
        else:
            self.identifiant_contrat = len(ContratEmploi.list_contrat) + 1

    @property
    def nb_heures_semaine(self):
        return self._nb_heures_semaine

    @nb_heures_semaine.setter
    def nb_heures_semaine(self, v_nb_heures_semaine):
        if isinstance(v_nb_heures_semaine, int) and 40 > v_nb_heures_semaine > 0:
            self._nb_heures_semaine = v_nb_heures_semaine

    @property
    def salaire_de_base(self):
        return self._salaire_de_base

    @salaire_de_base.setter
    def salaire_de_base(self, v_salaire_de_base):
        if isinstance(v_salaire_de_base, float) and v_salaire_de_base > 0:
            self._salaire_de_base = v_salaire_de_base

    @property
    def termes_embauche(self):
        return self._termes_embauche

    @termes_embauche.setter
    def termes_embauche(self, v_termes_embauche):
        if isinstance(v_termes_embauche, str):
            self._termes_embauche = v_termes_embauche

    @property
    def facteur_salaire(self):
        return self._facteur_salaire

    @facteur_salaire.setter
    def facteur_salaire(self, v_facteur_salaire):
        if isinstance(v_facteur_salaire, float) and 100 >= v_facteur_salaire > 0:
            self._facteur_salaire = v_facteur_salaire

    @property
    def employe(self):
        return self._employe

    @employe.setter
    def employe(self, v_identifiant_employe):
        for employe in Employe.list_employe:
            if employe.identifiant != v_identifiant_employe:
                continue
            else:
                self._employe = employe

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un bon format les informations du contrat.
        :return: Les informations du contrat dans un beau format d'affichage.
        """
        return (f"- IDENTIFIANT DU CONTRAT : {self.identifiant_contrat} - SALAIRE DE BASE : {self.salaire_de_base} $"
                f"- FACTEUR DU SALAIRE : {self.facteur_salaire * 100} % - NOM DE L'EMPLOYÉ : {self.employe.nom}"
                f"- NOMBRE D'HEURE PAR SEMAINE : {self.nb_heures_semaine} h"
                f"- TERMES D'EMBAUCHE : {self.termes_embauche}")
#####ALLO