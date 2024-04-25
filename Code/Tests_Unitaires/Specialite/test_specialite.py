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
def test_set_nom(valeur, resultat_attendu):
    specialite1 = Specialite()
    specialite1.nom = valeur
    assert specialite1.nom == resultat_attendu
