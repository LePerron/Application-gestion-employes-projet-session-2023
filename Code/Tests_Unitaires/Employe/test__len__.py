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
def test__len__(liste_employe: list, resultat_attendu: int):
    """
    Un test unitaire qui test le methode magic len.
    :param liste_employe: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    Employe.list_employe = liste_employe
    resultat = Employe.__len__()
    assert resultat == resultat_attendu
    assert isinstance(resultat, int)
