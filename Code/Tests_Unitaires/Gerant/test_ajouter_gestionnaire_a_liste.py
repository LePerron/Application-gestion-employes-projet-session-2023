from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
import pytest

gestionnaire1 = Gestionnaire()
gestionnaire1.identifiant = "2371875"

gestionnaire2 = Gestionnaire()
gestionnaire2.identifiant = "3456789"


gerant1 = Gerant()

gerant2 = Gerant()
gerant2.liste_gestionnaire.append(gestionnaire1)

gerant3 = Gerant()



@pytest.mark.parametrize("gerant, identifiant_gestionnaire_a_ajouter, resultat_attendu",[
    (gerant1, "2371875", [gestionnaire1]),
    (gerant2, "3456789", [gestionnaire1, gestionnaire2]),
    (gerant3, "1234567", [])
])
def test_ajouter_gestionnaire_a_liste(gerant, identifiant_gestionnaire_a_ajouter: str, resultat_attendu: list):
    """
    Un test unitaire qui test la methode identifiant gestionnaire à supprimer.
    :param identifiant_gestionnaire_a_ajouter: La valeur qu'on souhaite setter
    :param gerant: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    gerant.ajouter_gestionnaire_a_liste(identifiant_gestionnaire_a_ajouter)

    resultat = gerant.liste_gestionnaire
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)

