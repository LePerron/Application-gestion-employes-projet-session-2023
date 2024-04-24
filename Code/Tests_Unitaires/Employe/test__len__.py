import pytest
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe


@pytest.mark.parametrize("liste_employe, resultat_attendu", [
    (3),
    (2),
    (0),
    (None, 0)
])
def test__len__(liste_employe, resultat_attendu):
    assert len(Employe) == resultat_attendu
