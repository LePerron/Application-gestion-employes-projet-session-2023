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
def test_ajouter_caissier_a_liste(gestionnaire, identifiant_du_caissier, resultat_attendu):
    gestionnaire.ajouter_caissier_a_liste(identifiant_du_caissier)

    resultat = gestionnaire.liste_caissier
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)






