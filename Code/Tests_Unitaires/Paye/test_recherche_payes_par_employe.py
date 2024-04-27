from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
import pytest

employe1 = Employe(p_identifiant="1234567")
paye1 = Paye(p_montant_paye=21.0, p_employe=employe1)

employe2 = Employe(p_identifiant="1324569")
paye2 = Paye(p_montant_paye=2.0, p_employe=employe2)
paye3 = Paye(p_montant_paye=6.0, p_employe=employe2)


@pytest.mark.parametrize("identifiant_employe_recherche, resultat_attendu", [
    ("1234567", [paye1]),
    ("1324569", [paye2, paye3]),
    ("RIEN", []),
    ("saljhnbxvs;l", []),
])
def test_rechercher_payes_par_employe(identifiant_employe_recherche: str, resultat_attendu: list):
    """
    Permet de tester la méthode pour trouver la ou les payes qu'un employé a reçu.
    :param resultat_attendu: La valeur attendue après son initialisation.
    """
    resultat = Paye.rechercher_payes_par_employe(identifiant_employe_recherche)
    assert resultat == resultat_attendu
    assert isinstance(resultat, list)
