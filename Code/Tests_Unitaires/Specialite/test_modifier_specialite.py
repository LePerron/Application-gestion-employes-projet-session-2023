from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest

specialite1 = Specialite("Viandes", "ancienne description de Viandes")
specialite2 = Specialite("Legumes", "ancienne description de Légumes")
specialite3 = Specialite("Fruits", "ancienne description de Fruits")
specialite4 = Specialite("Poisson", "ancienne description de Poissons")


@pytest.mark.parametrize("specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu", [
    ("Viandes", "Boulangerie", "celui qui gère les boulangeries", ("Boulangerie", "celui qui gère les boulangeries")),
    ("Fruits", "Caisses", "celui qui gère les caisses", ("Caisses", "celui qui gère les caisses")),
    ("Pam", "Legumes", "celui qui gère le legume", ("", "")),
    ("Poisson", "Boulangerie", "celui qui gère les boulangeries", ("Poisson", "ancienne description de Poissons")),
])
def test_modifier_specialite(specialite_a_modifier: str, nouvelle_specialite: str, nouvelle_description: str,
                             resultat_attendu: tuple):
    """
    Un test unitaire qui test si la méthode **modifier_specialite** modifie le nom et la description d'une spécialité.
    :param specialite_a_modifier: Le nom actuel de la spécialité.
    :param nouvelle_specialite: Le nouveau nom de la spécialité.
    :param nouvelle_description: La nouvelle description de la spécialité.
    :param resultat_attendu: Le résultat attendu (nom, description).
    """
    index_ancienne_specialite = None
    for index, specialite in enumerate(Specialite.list_des_specialites):
        if specialite.nom == specialite_a_modifier:
            index_ancienne_specialite = index
            Specialite.modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description)
            break
        else:
            continue

    if index_ancienne_specialite:
        resultat = Specialite.list_des_specialites[index_ancienne_specialite]
        assert resultat.nom == resultat_attendu[0]
        assert resultat.description == resultat_attendu[1]
        assert isinstance(resultat.nom, str)
        assert isinstance(resultat.description, str)
