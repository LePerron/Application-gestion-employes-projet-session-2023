import pytest
from datetime import date
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye

paye1 = Paye()
paye1.montant_paye = 2
paye1.date_de_paye = "24/04/2024"

paye2 = Paye()
paye2.montant_paye = "aaaa"
paye2.date_de_paye = "15/01/2022"

paye3 = Paye()
paye3.montant_paye = 2.5
paye3.date_de_paye = "11111111"

paye4 = Paye()
paye4.montant_paye = "aaa"
paye4.date_de_paye = "adfasf"


@pytest.mark.parametrize("date_de_paye, resultat_attendu", [
    ([paye1.date_de_paye], "24/04/2024"),
    ([paye2.date_de_paye], "15/01/2022"),
    ([paye3.date_de_paye], "11111111"),
    ([paye4.date_de_paye], "adfasf")
])
def test_rechercher_payes_par_date(date_de_paye, resultat_attendu):
    """
    Permet de tester la méthode pour trouver la paye maximum
    :param list_paye: la liste utilisé pour initialiser la méthode
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """
    Paye.date_de_paye = date_de_paye
    assert Paye.rechercher_payes_par_date() == resultat_attendu
