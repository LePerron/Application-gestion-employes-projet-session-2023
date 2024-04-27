import pytest
from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe

employe1 = Employe()
employe1.identifiant = "2371875"


@pytest.mark.parametrize("identifiant_employe, resultat_attendu", [
    ("2371875", [employe1.contrat]),
    ("2222222", []),
    ("", [])
])
def test_rechercher_contrat_par_employe(identifiant_employe: str, resultat_attendu: list):
    """
    Un test unitaire qui test le methode rechercher contrat par employe.
    :param identifiant_employe: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    resultat = ContratEmploi.rechercher_contrat_par_employe(identifiant_employe)
    assert resultat == resultat_attendu
    assert isinstance(resultat, list)

