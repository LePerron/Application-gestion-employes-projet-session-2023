from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest

employe1 = Employe()
employe2 = Employe()
employe3 = Employe()
Employe.list_employe = []


@pytest.mark.parametrize("liste_employe, resultat_attendu", [
    ([employe1, employe2], 2),
    ([employe1], 1),
    ([employe1, employe2, employe3], 3),
])
def test__len__(liste_employe, resultat_attendu):
    Employe.list_employe = liste_employe
    resultat = Employe.__len__()
    assert resultat == resultat_attendu
    assert isinstance(resultat, int)
