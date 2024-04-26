from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
import pytest

caissier1 = Caissier()
caissier1.nom = "benjamin"

caissier2 = Caissier()
caissier2.nom = "samuel"

commis1 = Commis()
commis1.nom = "marc"

gestionnaire1 = Gestionnaire()
liste1_caissier_attendu = gestionnaire1.liste_caissier
liste1_caissier_attendu.append(caissier1)
liste1_commis_attendu = gestionnaire1.liste_commis
liste1_commis_attendu.append(commis1)

gestionnaire2 = Gestionnaire()
liste2_caissier_attendu = gestionnaire2.liste_caissier
liste2_caissier_attendu.append(caissier1)
liste2_caissier_attendu.append(caissier2)


@pytest.mark.parametrize("liste_a_parcourir, resultat_attendu", [
    (gestionnaire1.liste_caissier, f"{caissier1.nom} | "),
    (gestionnaire2.liste_caissier, f"{caissier1.nom} | {caissier2.nom} | "),
    (gestionnaire1.liste_commis, f"{commis1.nom} | ")
])
def test_parcourir_liste(liste_a_parcourir: list, resultat_attendu: str):
    """
    Un test unitaire qui test la methode parcourir liste.
    :param liste_a_parcourir: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    chaine_str = Gestionnaire.parcourir_liste(liste_a_parcourir)
    assert chaine_str == resultat_attendu
    assert isinstance(chaine_str, str)
