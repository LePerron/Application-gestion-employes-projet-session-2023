class Specialite:
    """
    Class Specialite
    """

    # Création de la list_specialite
    list_specialite = []
    def __init__(self, p_nom:str = "", p_description:str = ""):
        """
        Constructeur de la classe Specialite
        :param p_nom: Nom de la spécialité
        :param p_description: Description de la spécialité
        """
        self._nom = p_nom
        self.description = p_description

        # Get/Set du param nom
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self,nom_specialite):
        if isinstance(nom_specialite, str):
            for specialite in Specialite.list_specialite:
                if specialite == nom_specialite:
                    self._nom = nom_specialite

    @classmethod
    def supprimer_specialite(cls, nom_specialite: str):
        """
        Une méthode de classe qui permet de supprimer une spécialité.
        :param nom_specialite: Nom de la spécialité à enlever
        """
        for specialite in cls.list_specialite:
            if specialite.nom == nom_specialite:
                cls.list_specialite.remove(specialite)

    @classmethod
    def ajouter_specialite(cls, nouvelle_specialite: str):
        """
        Ajouter une spécialité dans list_specialite
        :param nouvelle_specialite: Nom de la spécialité
        """
        for specialite in cls.list_specialite:
            if specialite.nom == nouvelle_specialite:
                return
        cls.list_specialite.append(nouvelle_specialite)

    @classmethod
    def modifier_specialite(cls, specialite_a_modifier: str, nouveau_nom):
        """
        Modifie le nom d'une spécialité
        :param specialite_a_modifier: Le nom actuel de la spécialité
        """
        for specialite in cls.list_specialite:
            if specialite.nom == specialite_a_modifier:
                specialite.nom = specialite_a_modifier

    @staticmethod
    def trouve_specialite():
        for

