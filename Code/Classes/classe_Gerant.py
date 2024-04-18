from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import date


class Gerant(Employe):
    """
    Classes enfant Gerant de la classe mère Employe.
    """

    def __init__(self, p_specialite: Specialite = None, p_liste_gestionnaire=None,
                 p_identifiant: str = "", p_nom: str = "", p_prenom: str = "",
                 p_poste: any = None, p_date_engagement: date = None, p_contrat=None):
        """
        Constructeur de la classe Gerant qui fait appel à sa classe mère Employe.
        :param p_specialite: Spécialité du gerant
        :param p_liste_gestionnaire: La liste des gestionnaires que le gérant gère.
        """
        Employe.__init__(self, p_identifiant, p_nom, p_prenom, p_poste, p_date_engagement, p_contrat)

        self.specialite = p_specialite
        self.liste_gestionnaire = p_liste_gestionnaire

<<<<<<< HEAD
    def ajouter_gestionnaire_a_liste(self, gestionnaire_a_ajouter: Gestionnaire) -> None:
=======

    def ajouter_gestionnaire_a_liste(self, nom_gestionnaire_a_ajouter: str) -> None:
>>>>>>> 697a3238b4faa1c88dd8f93ef8f81c44bc90465f
        """
        Ajouter un gestionnaire dans liste_gestionnaire
        :param nom_gestionnaire_a_ajouter: Gestionnaire à ajouter
        :return: La liste des gestionnaires avec le gestionnaire ajouté
        """
        for gestionnaire in self.liste_gestionnaire:
            if gestionnaire.nom == nom_gestionnaire_a_ajouter:
                return
        self.liste_gestionnaire.append(nom_gestionnaire_a_ajouter)

<<<<<<< HEAD
    def supprimer_gestionnaire_a_liste(self, gestionnaire_a_supprimer: Gestionnaire) -> None:
=======

    def supprimer_gestionnaire_a_liste(self, nom_gestionnaire_a_supprimer: str) -> None:
>>>>>>> 697a3238b4faa1c88dd8f93ef8f81c44bc90465f
        """
        Supprimer un gestionnaire dans la liste_gestionnaire
        :param nom_gestionnaire_a_supprimer: Gestionnaire à supprimer
        """
        for gestionnaire in self.liste_gestionnaire:
            if gestionnaire.nom == nom_gestionnaire_a_supprimer:
                self.liste_gestionnaire.remove(nom_gestionnaire_a_supprimer)

    def __str__(self):
        return "AAAAAAA faire"
