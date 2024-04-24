from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest

specialite2 = Specialite("Legumes", "ancienne description de legume")
specialite3 = Specialite("Fruits", "ancienne description de fruits")
specialite1 = Specialite("Viandes", "ancienne description de Viande")


@pytest.mark.parametrize("specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu", [
    ("Viandes", "allo", "celui qui gère les Allo", ("Allo", "celui qui gère les Allo")),
])
def test_modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu):
    """
    Un test unitaire qui test si la méthode **modifier_specialite** modifie le nom et la description d'une spécialité.
    :param specialite_a_modifier: Le nom actuel de la spécialité
    :param nouvelle_specialite: Le nouveau nom de la spécialité
    :param nouvelle_description: La nouvelle description de la spécialité
    :param resultat_attendu: Le résultat attendu (nom, description)
    """
    Specialite.modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description)

    for specialite in Specialite.list_des_specialites:
        if specialite.nom != resultat_attendu[0]:
            continue
        else:
            assert specialite.nom == resultat_attendu[0]
            assert specialite.description == resultat_attendu[1]
            return
    else:
        @pytest.raises()




# ("legumes", "Fruits", "celui qui gère les Fruits", ("Fruits", "celui qui gère les Fruits")),
# ("rien", "bonjour", "celui qui gère les Bonjour", ("Bonjour", "celui qui gère les Bonjour")),