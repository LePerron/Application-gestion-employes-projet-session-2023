from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
import pytest

caissier1 = Caissier()
caissier1.identifiant = "2371875"

caissier2 = Caissier()
caissier2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()
gestionnaire1.liste_caissier.append(caissier1)

gestionnaire2 = Gestionnaire()
gestionnaire2.liste_caissier.append(caissier1)
gestionnaire2.liste_caissier.append(caissier2)

gestionnaire3 = Gestionnaire()



@pytest.mark.parametrize("gestionnaire, identifiant_caissier_a_supprimer, resultat_attendu", [
    (gestionnaire1, "2371875", []),
    (gestionnaire2, "3456789", [caissier1]),
    (gestionnaire3, "1234567", [])
])
def test_identifiant_caissier_a_supprimer(gestionnaire, identifiant_caissier_a_supprimer, resultat_attendu):
    len_avant_supprimer = len(gestionnaire.liste_caissier)

    gestionnaire.supprimer_caissier_a_liste(identifiant_caissier_a_supprimer)

    resultat = gestionnaire.liste_caissier
    assert gestionnaire.liste_caissier == resultat_attendu
    if len_avant_supprimer == 0:
        assert len(resultat) == len_avant_supprimer
    else:
        assert len(resultat) == len_avant_supprimer - 1
