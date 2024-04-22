from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
import pytest

gestionnaire1 = Gestionnaire()
gestionnaire1.identifiant = "2371875"

gestionnaire2 = Gestionnaire()
gestionnaire2.identifiant = "2371875"

gestionnaire2 = Gestionnaire()
gestionnaire2.identifiant = "3456789"

gerant1 = Gerant()

liste2_gestionnaire_attendu = gerant1.liste_gestionnaire

gerant3 = Gerant()
liste3_gestionnaire_attendu = gerant3.liste_gestionnaire

liste1_gestionnaire_attendu = gerant1.liste_gestionnaire
liste1_gestionnaire_attendu.append(gestionnaire1)

@pytest.mark.parametrize("gerant, identifiant_gestionnaire_a_supprimer, resultat_attendu", [
    (gerant3, "2371875", []),
    (gerant1, gestionnaire2.identifiant, [gestionnaire1]),
    (gerant1, gestionnaire1.identifiant, [])
])
def test_identifiant_gestionnaire_a_supprimer(gerant, identifiant_gestionnaire_a_supprimer, resultat_attendu):
    gerant.supprimer_gestionnaire_a_liste(identifiant_gestionnaire_a_supprimer)
    assert gerant.liste_gestionnaire == resultat_attendu