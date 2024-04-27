from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
from datetime import datetime, date
import pytest

paye1 = Paye(p_montant_paye=2.0)
paye1.date_de_paye = "24/04/2024"

paye2 = Paye(p_montant_paye=1.0)
paye2.date_de_paye = "15/01/2022"

paye3 = Paye(p_montant_paye=5.0)
paye3.date_de_paye = "15/01/2022"

paye4 = Paye(p_montant_paye=2.0)
paye4.date_de_paye = "15/01/2018"

paye5 = Paye(p_montant_paye=2.0)
paye5.date_de_paye = "15/01/2025"


@pytest.mark.parametrize("date_de_paye, resultat_attendu", [
    (datetime.strptime("24/04/2024", "%d/%m/%Y"), [paye1]),
    (datetime.strptime("15/01/2022", "%d/%m/%Y"), [paye2, paye3]),
    (datetime.strptime("15/01/2018", "%d/%m/%Y"), []),
    (datetime.strptime("15/01/2025", "%d/%m/%Y"), [])
])
def test_rechercher_payes_par_date(date_de_paye: date, resultat_attendu: list):
    """
    Permet de tester la méthode pour trouver la ou les payes de la date.
    :param resultat_attendu: La valeur attendue après son initialisation.
    """

    resultat = Paye.rechercher_payes_par_date(date_de_paye)
    assert resultat == resultat_attendu
    assert isinstance(resultat, list)
