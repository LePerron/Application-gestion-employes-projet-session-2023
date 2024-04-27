import pytest

from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

commis1 = Commis()
commis1.identifiant = "2371875"

commis2 = Commis()
commis2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()

gestionnaire2 = Gestionnaire()
gestionnaire2.liste_commis.append(commis1)

gestionnaire3 = Gestionnaire()


@pytest.mark.parametrize("gestionnaire, identifiant_du_commis, resultat_attendu", [
    (gestionnaire1, "2371875", [commis1]),
    (gestionnaire2, "3456789", [commis1, commis2]),
    (gestionnaire3, "1234567", [])
])
def test_ajouter_commis_a_liste(gestionnaire, identifiant_du_commis: str, resultat_attendu: list):
    """
    Un test unitaire qui test la methode commis à ajouter.
    :param identifiant_du_commis: L'une des valeurs qu'on souhaite setter.
    :param gestionnaire: L'une des valeurs qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    gestionnaire.ajouter_commis_a_liste(identifiant_du_commis)

    resultat = gestionnaire.liste_commis
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)


