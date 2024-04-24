from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
import pytest

commis1 = Commis()
commis1.identifiant = "2371875"

commis2 = Commis()
commis2.identifiant = "3456789"

gestionnaire1 = Gestionnaire()
list_commis_attendu1 = gestionnaire1.liste_commis
list_commis_attendu1.append(commis1)

gestionnaire2 = Gestionnaire()
list_commis_attendu2 = gestionnaire2.liste_commis

gestionnaire3 = Gestionnaire()
list_commis_attendu3 = gestionnaire3.liste_commis


@pytest.mark.parametrize("gestionnaire, identifiant_commis_a_supprimer, resultat_attendu", [
    (gestionnaire2, commis1.identifiant, []),
    (gestionnaire1, commis2.identifiant, [commis1]),
    (gestionnaire3, "2371875", [])
])
def test_identifiant_commis_a_supprimer(gestionnaire, identifiant_commis_a_supprimer, resultat_attendu):
    gestionnaire.supprimer_commis_a_liste(identifiant_commis_a_supprimer)
    assert gestionnaire.liste_commis == resultat_attendu
