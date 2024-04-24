from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
import pytest

caissier1 = Caissier()
caissier1.identifiant = "2371875"

caissier2 = Caissier()
caissier2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()
list_caissier_attendu1 = gestionnaire1.liste_caissier
list_caissier_attendu1.append(caissier1)

gestionnaire2 = Gestionnaire()
list_caissier_attendu2 = gestionnaire2.liste_caissier

gestionnaire3 = Gestionnaire()
list_caissier_attendu3 = gestionnaire3.liste_caissier


@pytest.mark.parametrize("gestionnaire, identifiant_caissier_a_supprimer, resultat_attendu", [
    (gestionnaire2, caissier1.identifiant, []),
    (gestionnaire1, caissier2.identifiant, [caissier1]),
    (gestionnaire3, "2371875", [])
])
def test_identifiant_caissier_a_supprimer(gestionnaire, identifiant_caissier_a_supprimer, resultat_attendu):
    gestionnaire.supprimer_caissier_a_liste(identifiant_caissier_a_supprimer)
    assert gestionnaire.liste_caissier == resultat_attendu
