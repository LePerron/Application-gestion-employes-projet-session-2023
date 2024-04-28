import pytest

from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

caissier1 = Caissier()
caissier1.identifiant = "2371875"

caissier2 = Caissier()
caissier2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()

gestionnaire2 = Gestionnaire()
gestionnaire2.liste_caissier.append(caissier1)

gestionnaire3 = Gestionnaire()

@pytest.mark.parametrize("gestionnaire, identifiant_du_caissier, resultat_attendu", [
    (gestionnaire1, "2371875", [caissier1]),
    (gestionnaire2, "3456789", [caissier1, caissier2]),
    (gestionnaire3, "1234567", [])
])
def test_ajouter_caissier_a_liste(gestionnaire, identifiant_du_caissier: str, resultat_attendu: list):
    """
    Un test unitaire qui test la methode identifiant caissier à supprimer.
    :param identifiant_du_caissier: L'une des valeur qu'on souhaite setter.
    :param gestionnaire: L'une des valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    gestionnaire.ajouter_caissier_a_liste(identifiant_du_caissier)

    resultat = gestionnaire.liste_caissier
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)






