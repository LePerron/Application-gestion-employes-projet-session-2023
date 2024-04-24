import pytest
from datetime import datetime
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye

paye1 = Paye()
paye1.date_de_paye = "24/04/2024"
paye1.montant_paye = 2.0

paye2 = Paye()
paye2.date_de_paye = "15/01/2022"
paye2.montant_paye = 1.0

paye3 = Paye()
paye3.date_de_paye = "15/01/2021"
paye3.montant_paye = 2.0
#
# (paye2.date_de_paye, datetime.strptime("15/01/2022", "%d/%m/%Y")),
#     (paye3.date_de_paye, datetime.strptime("15/01/2021", "%d/%m/%Y"))


@pytest.mark.parametrize("date_de_paye, resultat_attendu", [
    (datetime.strptime("15/01/2022", "%d/%m/%Y"), [paye2]),
])
def test_rechercher_payes_par_date(date_de_paye, resultat_attendu):
    """
    Permet de tester la méthode pour trouver la ou les payes de la date
    :param resultat_attendu: La valeur attendue après son initialisation
    :return: None
    """

    assert Paye.rechercher_payes_par_date(date_de_paye) == resultat_attendu
