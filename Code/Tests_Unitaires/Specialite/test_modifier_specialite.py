from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest

specialite1 = Specialite("Viandes", "ancienne description de Viande")
specialite2 = Specialite("Legumes", "ancienne description de legume")
specialite3 = Specialite("Fruits", "ancienne description de fruits")

liste_initiale = [Specialite("Legumes", "celui qui gère les légumes"),
                   Specialite("Legume", "ancienne description de legume"),
                   Specialite("Fruits", "ancienne description de fruits")]



liste_attendu_1 = [Specialite("Legumes", "celui qui gère les légumes"),
                   Specialite("Legume", "ancienne description de legume"),
                   Specialite("Fruits", "ancienne description de fruits")]

liste_attendu_2 = [Specialite("Viandes", "ancienne description de Viande"),
                   Specialite("Legume", "celui qui gère les Fruits"),
                   Specialite("Fruits", "celui qui gère les legumes")]

liste_attendu_3 = [Specialite("Viande", "celui qui gère les légumes"),
                   Specialite("Fruits", "celui qui gère les Fruits"),
                   Specialite("Fruits", "ancienne description de fruits")]


@pytest.mark.parametrize("specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu", [
    ("Viandes", "legumes", "celui qui gère les légumes", liste_attendu_1),
    ("legumes", "Fruits", "celui qui gère les Fruits", liste_attendu_2),
    ("rien", "legumes", "celui qui gère les legumes", liste_attendu_3),
])
def test_modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu):
    """
    Un test unitaire que test si la méthode **modifier_specialite** modifie le nom et la description d'une spécialité.
    :param specialite_a_modifier: Le nom actuel de la spécialité
    :param nouvelle_specialite: Le nouveau nom de la spécialité
    :param nouvelle_description: La nouvelle description de la spécialité
    :param resultat_attendu: Le résultat attendu
    """
    Specialite.modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description)
    assert Specialite.list_des_specialites == resultat_attendu
