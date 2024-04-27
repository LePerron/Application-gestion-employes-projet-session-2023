from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
import pytest

commis1 = Commis()
commis1.identifiant = "2371875"

commis2 = Commis()
commis2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()
gestionnaire1.liste_commis.append(commis1)

gestionnaire2 = Gestionnaire()
gestionnaire2.liste_commis.append(commis1)
gestionnaire2.liste_commis.append(commis2)

gestionnaire3 = Gestionnaire()


@pytest.mark.parametrize("gestionnaire, identifiant_commis_a_supprimer, resultat_attendu", [
    (gestionnaire1, "2371875", []),
    (gestionnaire2, "3456789", [commis1]),
    (gestionnaire3, "1234567", [])
])
def test_commis_a_supprimer(gestionnaire, identifiant_commis_a_supprimer: str, resultat_attendu: list):
    """
    Un test unitaire qui test la methode commis à supprimer.
    :param identifiant_commis_a_supprimer: L'une des valeurs qu'on souhaite setter.
    :param gestionnaire: L'une des valeurs qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    :return:
    """
    gestionnaire.supprimer_commis_a_liste(identifiant_commis_a_supprimer)

    resultat = gestionnaire.liste_commis
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)
