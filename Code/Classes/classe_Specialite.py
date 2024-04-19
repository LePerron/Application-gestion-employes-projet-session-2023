class Specialite:
    """
    Class Specialite
    """

    list_specialite = []

    def __init__(self, p_nom: str = "", p_description: str = ""):
        """
        Constructeur de la classe Specialite
        :param p_nom: Nom de la spécialité
        :param p_description: Description de la spécialité
        """
        self._nom = p_nom
        self.description = p_description

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom_specialite):
        if isinstance(nom_specialite, str):
            for specialite in Specialite.list_specialite:
                if specialite == nom_specialite:
                    self._nom = nom_specialite

    @classmethod
    def supprimer_specialite(cls, nom_specialite: str) -> None:
        """
        Une méthode de classe qui permet de supprimer une spécialité.
        :param nom_specialite: Nom de la spécialité à enlever
        """
        for specialite in cls.list_specialite:
            if specialite.nom == nom_specialite:
                cls.list_specialite.remove(specialite)

    @classmethod
    def ajouter_specialite(cls, nouvelle_specialite: str) -> None:
        """
        Ajouter une spécialité dans list_specialite
        :param nouvelle_specialite: Nom de la spécialité à ajouter
        """
        for specialite in cls.list_specialite:
            if specialite.nom == nouvelle_specialite:
                return
        cls.list_specialite.append(nouvelle_specialite)

    @classmethod
    def modifier_specialite(cls, specialite_a_modifier: str, nouvelle_specialite: str, nouvelle_description: str) -> None:
        """
        Modifie le nom et la description d'une spécialité.
        :param specialite_a_modifier: Le nom actuel de la spécialité
        :param nouvelle_specialite: Le nouveau nom de la spécialité
        :param nouvelle_description: La nouvelle description de la spécialité
        """
        for specialite in cls.list_specialite:
            if specialite.nom == specialite_a_modifier:
                specialite.nom = nouvelle_specialite
                specialite.description = nouvelle_description

    @staticmethod
    def trouve_employe_selon_specialite(specialite_demandee: str) -> list:
        """
        Une méthode statique qui permet de trouver tout les employés d'une même spécialité.
        :param specialite_demandee: Nom de la spécialitée demandée.
        :return: La liste des employés de la spécialité demandée.
        """
        list_employes_selon_specialite = []

        for specialite in Specialite.list_specialite:
            if specialite_demandee == specialite.nom:
                list_employes_selon_specialite.append(specialite)

        if len(list_employes_selon_specialite) > 0:
            return list_employes_selon_specialite

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un bon format les informations de la spécialité.
        :return: Les informations de la spécialité dans un beau format d'affichage.
        """
        return f"NOM DE LA SPÉCIALITÉ : {self._nom} - DESCRIPTION : {self.description}"
