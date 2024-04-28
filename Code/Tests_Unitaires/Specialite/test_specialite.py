from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("Viande", "Viande"),
    ("boulangerie", "Boulangerie"),
    ("légume", "Légume"),
    ("sd-dg", ""),
    ("09328fjds", ""),
    (".,`l^.", ""),
    ("Fruits2", ""),
])
def test_set_nom(valeur: str, resultat_attendu: str):
    """
    Un test unitaire qui test le setter du nom de la specialite.
    :param valeur: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    specialite1 = Specialite()
    specialite1.nom = valeur
    assert specialite1.nom == resultat_attendu
