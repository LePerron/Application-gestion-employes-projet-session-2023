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
def test_rechercher_contrat_par_employe(identifiant_employe, resultat_attendu):
    assert ContratEmploi.rechercher_contrat_par_employe(identifiant_employe) == resultat_attendu
