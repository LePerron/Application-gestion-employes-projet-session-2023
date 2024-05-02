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
    ("16/06/2022", []),
    (0, []),
    (-9, []),
    (2.0, [])
])
def test_rechercher_contrat_par_date(date_du_contrat: str, resultat_attendu: list):
    """
    Un test unitaire qui test le methode rechercher contrat par date.
    :param date_du_contrat: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    resultat = ContratEmploi.rechercher_contrat_par_date(datetime.datetime.strptime(date_du_contrat, "%d/%m/%Y"))
    assert resultat == resultat_attendu
    assert isinstance(resultat, list)
