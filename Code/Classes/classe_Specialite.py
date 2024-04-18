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
            self._nom = nom_specialite
    @staticmethod
    def trouve_specialite():


    @staticmethod
    def