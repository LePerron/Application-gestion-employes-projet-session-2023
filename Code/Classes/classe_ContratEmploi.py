from classe_Employe import Employe


class ContratEmploi:
    """
    Classes ContratEmploi
    """

    list_contrat = []

    # Attribut de classe
    def __init__(self, p_identifiant_contrat: int = 0, p_employe: Employe = None, p_facteur_salaire: float = 0.0,
                 p_nb_heures_semaine: int = 0, p_salaire_de_base: float = 0.0, p_termes_embauche: str = ""):
        """
        :param p_identifiant_contrat: L'identifiant du contrat de l'employé
        :param p_employe: Le numéro de l'employé associé à ce contrat
        :param p_facteur_salaire: Facteur qui affecte le salaire de l'employé
        :param p_nb_heures_semaine: Nombre d'heure fait par l'employé
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

    def _get_nb_heures_semaine(self):
        return self._nb_heures_semaine

    def _set_nb_heures_semaine(self, v_nb_heures_semaine):
        if isinstance(v_nb_heures_semaine, int) and 40 > v_nb_heures_semaine > 0:
            self._nb_heures_semaine = v_nb_heures_semaine

    nb_heures_semaine = property(_get_nb_heures_semaine, _set_nb_heures_semaine)

    def _get_salaire_de_base(self):
        return self._salaire_de_base

    def _set_salaire_de_base(self, v_salaire_de_base):
        if isinstance(v_salaire_de_base, float) and v_salaire_de_base > 0:
            self._salaire_de_base = v_salaire_de_base

    salaire_de_base = property(_get_salaire_de_base, _set_salaire_de_base)

    def _get_termes_embauche(self):
        return self._termes_embauche

    def _set_termes_embauche(self, v_termes_embauche):
        if isinstance(v_termes_embauche, str):
            self._termes_embauche = v_termes_embauche

    termes_embauche = property(_get_termes_embauche, _set_termes_embauche)

    def _get_facteur_salaire(self):
        return self._facteur_salaire

    def _set_facteur_salaire(self, v_facteur_salaire):
        if isinstance(v_facteur_salaire, float) and 100 > v_facteur_salaire > 0:
            self._facteur_salaire = v_facteur_salaire

    facteur_salaire = property(_get_facteur_salaire, _set_facteur_salaire)

    def _get_employe(self):
        return self._employe

    def _set_employe(self, v_employe):
        self._employe = v_employe

    employe = property(_get_employe, _set_employe)

    def __str__(self):
        return (f"- IDENTIFIANT DU CONTRAT : {self.identifiant_contrat} - SALAIRE DE BASE : {self.salaire_de_base} $"
                f"- TERMES D'EMBAUCHE : {self.termes_embauche} - NOMBRE D'HEURE PAR SEMAINE : {self.nb_heures_semaine} h"
                f"- FACTEUR DU SALAIRE : {self.facteur_salaire} % - NOM DE L'EMPLOYÉ : {self.employe.nom}")



