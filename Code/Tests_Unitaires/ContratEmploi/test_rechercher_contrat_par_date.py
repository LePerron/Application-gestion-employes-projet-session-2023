from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest
import datetime

employe1 = Employe()
employe1.contrat.date_du_contrat = "12/04/2022"

employe2 = Employe()
employe2.contrat.date_du_contrat = "12/05/2022"

employe3 = Employe()
employe3.contrat.date_du_contrat = "12/05/2022"

@pytest.mark.parametrize("date_du_contrat, resultat_attendu", [
    ("12/04/2022", [employe1.contrat]),
    ("12/05/2022", [employe2.contrat, employe3.contrat]),
    ("16/06/2022", [])
])
def test_rechercher_contrat_par_date(date_du_contrat: str, resultat_attendu):
    """
    Pytest pour tester la classmethod rechercher_contrat_par_date.
    :param date_du_contrat: date du contrat donner.
    :param resultat_attendu: liste des dates de contrat demmander.
    """
    resultat = ContratEmploi.rechercher_contrat_par_date(datetime.datetime.strptime(date_du_contrat, "%d/%m/%Y"))
    assert resultat == resultat_attendu
    assert isinstance(resultat, list)

