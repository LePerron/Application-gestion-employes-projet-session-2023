

class Caissier:
    """
    Classe employer caissier
    """

    # Création de la liste_caissier.
    liste_caissier = []

    def __init__(self, gestionnaire: Gestionnaire = None, specialite: str = ""):
        """
        Constructeur de la classe Caissier
        :param gestionnaire: Base de donner des gestionnaires
        :param specialite: Spécialiter du caissier
        """
