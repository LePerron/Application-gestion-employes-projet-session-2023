from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
import pytest

employe1 = Employe(p_identifiant="1234567")
paye1 = Paye(p_montant_paye=2.0, p_employe=employe1)

employe2 = Employe(p_identifiant="1234527")
paye2 = Paye(p_montant_paye=2.0, p_employe=employe2)

employe3 = Employe(p_identifiant="1234562")
paye3 = Paye(p_montant_paye=2.0, p_employe=employe3)


@pytest.mark.parametrize("identifiant_employe_recherche, resultat_attendu", [
    ("1234567", [paye1]),
])
def test_rechercher_payes_par_employe(identifiant_employe_recherche, resultat_attendu, ):
    """
    Permet de tester la méthode pour trouver la ou les payes qu'un employé a reçu
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """
    assert Paye.rechercher_payes_par_employe(identifiant_employe_recherche) == resultat_attendu
