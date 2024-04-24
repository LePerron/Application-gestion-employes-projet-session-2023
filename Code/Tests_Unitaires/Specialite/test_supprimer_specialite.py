from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest

specialite1 = Specialite("Viande", "ancienne description")


@pytest.mark.parametrize("specialite_a_modifier, nouvelle_specialite, nouvelle_description, resultat_attendu", [
    ("Viande", "legumes", "celui qui gère les légumes", []),
    ("legumes", "Fruits", "celui qui gère les Fruits", []),
    ("rien", "legumes", "celui qui gère les legumes", [])
])
def test_modifier_specialite(nom_specialite, resultat_attendu):
    """
    Un test unitaire qui test si la méthode **modifier_specialite** modifie le nom et la description d'une spécialité.
    :param nom_specialite: Le nom de la spécialité à enlever
    :param resultat_attendu: Le résultat attendu
    """
    Specialite.modifier_specialite(specialite_a_modifier, nouvelle_specialite, nouvelle_description)
    for specialite in Specialite.list_des_specialites:
        if specialite_a_modifier != specialite.nom:
            continue
        else:
            break

    for specialite in Specialite.list_des_specialites:
        assert specialite.nom != specialite_a_modifier
        if specialite.nom == nouvelle_specialite:
            assert specialite.description == nouvelle_description
