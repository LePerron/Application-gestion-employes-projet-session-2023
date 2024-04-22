import pytest
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye

paye0 = Paye(p_montant_paye=0)
paye1 = Paye(p_montant_paye=1)
paye2 = Paye(p_montant_paye=2)
paye3 = Paye(p_montant_paye=3)
paye4 = Paye(p_montant_paye=4)
paye5 = Paye(p_montant_paye=5)
paye_negatif = Paye(p_montant_paye=-1)
paye_decimal = Paye(p_montant_paye=1.5)
paye_str = Paye(p_montant_paye="wdasifiaf")


@pytest.mark.parametrize("list_paye,resultat_attendu", [
    ([paye1, paye3, paye2, paye4, paye5], 3),
    ([paye1, paye3, paye2, paye4], 2.5),
    ([], 0),
    ([paye_negatif, paye2, paye3, paye4, paye5], 3),
    ([paye_decimal, paye2, paye3, paye4, paye5], 3),
    ([paye_negatif], -1),
    (paye_str, 0),
])
def test_calculer_mediane_payes(list_paye,  resultat_attendu):
    """
    Permet de tester la méthode pour calculer la mediane
    :param list_paye: la liste utilisé pour initialiser la méthode
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """

    Paye.list_payes = list_paye
    assert Paye.calculer_mediane_payes() == resultat_attendu
