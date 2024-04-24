import pytest

from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire

commis1 = Commis()
commis1.identifiant = "2371875"

commis2 = Commis()
commis2.identifiant = "1234567"

gestionnaire1 = Gestionnaire()
list_commis_attendu1 = gestionnaire1.liste_commis
list_commis_attendu1.append(commis1)

list_commis_attendu2 = gestionnaire1.liste_commis

list_commis_attendu3 = gestionnaire1.liste_commis

@pytest.mark.parametrize("gestionnaire, identifiant_du_commis, resultat_attendu", [
    (gestionnaire1, commis1.identifiant, [commis1]),
    (gestionnaire1, commis2.identifiant, [commis1]),
    (gestionnaire1, "2371875", [commis1])
])
def test_ajouter_caissier_a_liste(gestionnaire, identifiant_du_commis, resultat_attendu):
    gestionnaire.ajouter_commis_a_liste(identifiant_du_commis)
    assert gestionnaire.liste_commis == resultat_attendu



