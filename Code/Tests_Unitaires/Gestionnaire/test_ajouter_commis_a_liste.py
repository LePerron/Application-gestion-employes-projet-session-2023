import pytest

from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

caissier1 = Caissier()
caissier1.identifiant = "2371875"

caissier2 = Caissier()
caissier2.identifiant = "1234567"

gestionnaire1 = Gestionnaire()
list_caissier_attendu1 = gestionnaire1.liste_caissier
list_caissier_attendu1.append(caissier1)

list_caissier_attendu2 = gestionnaire1.liste_caissier

list_caissier_attendu3 = gestionnaire1.liste_caissier

@pytest.mark.parametrize("gestionnaire, identifiant_du_caissier, resultat_attendu", [
    (gestionnaire1, caissier1.identifiant, [caissier1]),
    (gestionnaire1, caissier2.identifiant, [caissier1]),
    (gestionnaire1, "2371875", [caissier1])
])
def test_ajouter_caissier_a_liste(gestionnaire, identifiant_du_caissier, resultat_attendu):
    gestionnaire.ajouter_caissier_a_liste(identifiant_du_caissier)
    assert gestionnaire.liste_caissier == resultat_attendu

