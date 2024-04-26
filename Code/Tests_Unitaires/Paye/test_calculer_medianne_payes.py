from _pytest.python_api import raises

from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
import pytest


paye3 = Paye(p_montant_paye=3)
paye_negatif = Paye(p_montant_paye=-1)
paye_decimal = Paye(p_montant_paye=1.5)
paye_str = Paye(p_montant_paye="wdaf")


@pytest.mark.parametrize("list_paye, resultat_attendu", [
    ([paye3], 3),
    ([paye_negatif, paye3], 1),
    ([paye_decimal, paye3], 2.25),
    ([paye_str], 0.0)
])
@pytest.mark.xfail()
def test_calculer_mediane_payes(list_paye: list, resultat_attendu: float):
    """
    Permet de tester la méthode pour calculer la mediane
    :param list_paye: la liste utilisé pour initialiser la méthode
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """
    Paye.list_payes = list_paye
    resultat = Paye.calculer_mediane_payes()
    assert resultat == resultat_attendu
    assert isinstance(resultat, float)
