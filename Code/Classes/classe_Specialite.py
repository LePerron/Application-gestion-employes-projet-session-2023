import jsonpickle

from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe


class Specialite:
    """
    Classe Specialite
    """
    list_des_specialites = []

    def __init__(self, p_nom: str = "", p_description: str = ""):
        """
        Constructeur de la classe Specialite
        :param p_nom: Nom de la spécialité
        :param p_description: Description de la spécialité
        """
        self._nom = p_nom
        self.description = p_description

        Specialite.list_des_specialites.append(self)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom_specialite: str) -> None:
        if isinstance(nom_specialite, str) and nom_specialite.isalpha():
            for specialite in Specialite.list_des_specialites:
                if specialite.nom == nom_specialite:
                    return
            self._nom = nom_specialite.capitalize()

    @classmethod
    def supprimer_specialite(cls, nom_specialite: str) -> None:
        """
        Une méthode de classe qui permet de supprimer une spécialité des spécialité existante.
        :param nom_specialite: Nom de la spécialité à enlever
        """
        for specialite in cls.list_des_specialites:
            if specialite.nom == nom_specialite.capitalize():
                cls.list_des_specialites.remove(specialite)

    @classmethod
    def modifier_specialite(cls, specialite_a_modifier: str, nouvelle_specialite: str,
                            nouvelle_description: str) -> None:
        """
        Modifie le nom et la description d'une spécialité.
        :param specialite_a_modifier: Le nom actuel de la spécialité
        :param nouvelle_specialite: Le nouveau nom de la spécialité
        :param nouvelle_description: La nouvelle description de la spécialité
        """
        for specialite in cls.list_des_specialites:
            if specialite.nom.capitalize() != nouvelle_specialite.capitalize():
                continue
            else:
                return
        else:
            for specialite in cls.list_des_specialites:
                if specialite.nom.capitalize() == specialite_a_modifier.capitalize():
                    specialite.nom = nouvelle_specialite.capitalize()
                    if len(nouvelle_description) > 1:
                        specialite.description = nouvelle_description
                    break

    @staticmethod
    def trouve_employe_selon_specialite(specialite_demandee: str) -> list:
        """
        Une méthode statique qui permet de trouver tous les employés d'une même spécialité.
        :param specialite_demandee: Nom de la spécialitée demandée.
        :return: La liste des employés de la spécialité demandée.
        """
        list_employes_selon_specialite = []

        for employe in Employe.list_employe:
            if specialite_demandee.capitalize() == employe.specialite.nom.capitalize():
                list_employes_selon_specialite.append(employe)
        return list_employes_selon_specialite

    def afficher_specialite_dans_list_view(self, description_=True, nb_employe_=True) -> str:
        """
        Une qui permet de retourner dans un beau format les informations de la spécialité pour être afficher dans la
        listView des spécialité.
        :return: Les informations de la spécialité dans un beau format d'affichage.
        """

        chaine_caracteres = f" ↳ Nom de la spécialitée : {self._nom}\n"

        try:
            if description_ == "":
                chaine_caracteres += f" ↳ Description de la spécialitée : Aucune description\n"
            elif description_:
                chaine_caracteres += f" ↳ Description de la spécialitée : {self.description}\n"
        except NameError:
            pass
        try:
            if nb_employe_:
                chaine_caracteres += f" ↳ Le nombre d'employe : {self.calculer_nb_employe(self._nom)}\n"
        except NameError:
            pass
        return chaine_caracteres

    def calculer_nb_employe(self, specialite) -> int:
        """
        Permet de calculer le nombre d'employe selon une spécialité lier
        :return: le nombre d'employé pour la spécialitée
        """
        return len(Specialite.trouve_employe_selon_specialite(specialite))

    def __str__(self):
        """
        Une fonction magique qui permet de retourner dans un beau format les informations de la spécialité.
        :return: Les informations de la spécialité dans un beau format d'affichage.
        """
        return self.afficher_specialite_dans_list_view()
