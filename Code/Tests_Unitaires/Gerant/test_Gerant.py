import pytest
from datetime import datetime

from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("20/06/2006", None),
    ("20/05/2021", datetime.strptime("20/05/2021", "%d/%m/%Y")),
    (14, None),
    ("", None)
])

def test_set_date_gerant(valeur, resultat_attendu):
    """
    Un test unitaire qui test le setter de la date du gerant.
    :param valeur: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonn modifications ou la valeur de remplacement.
    """
    gerant1 = Gerant()
    gerant1.date_gerant = valeur
    assert gerant1.date_gerant == resultat_attendu
