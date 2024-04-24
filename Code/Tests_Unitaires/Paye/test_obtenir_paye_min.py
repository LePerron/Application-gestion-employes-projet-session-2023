import pytest
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye


paye3 = Paye(p_montant_paye=3)
paye_negatif = Paye(p_montant_paye=-1)
paye_decimal = Paye(p_montant_paye=2.5)
paye_str = Paye(p_montant_paye="wdaf")


@pytest.mark.parametrize("list_paye,resultat_attendu", [
    ([paye3, paye_decimal], 2.5),
    ([paye_negatif, paye3], -1),
    ([paye_str], 'wdaf')
])
def test_obtenir_paye_min(list_paye, resultat_attendu):
    """
    Permet de tester la méthode pour trouver la paye minimum
    :param list_paye: la liste utilisé pour initialiser la méthode
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """
    Paye.list_payes = list_paye
    assert Paye.obtenir_paye_min() == resultat_attendu