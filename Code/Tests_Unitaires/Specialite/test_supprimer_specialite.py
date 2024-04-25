from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest

specialite1 = Specialite("Viande", "celui qui gère les Viande")
specialite2 = Specialite("Fruits", "celui qui gère les  Fruits")
specialite3 = Specialite("Legumes", "celui qui gère les Legumes")


@pytest.mark.parametrize("specialite_a_supprimer, resultat_attendu", [
    ("Viande", [specialite2, specialite3]),
    ("legumes", [specialite1, specialite2]),
    ("leg2mes", [specialite1, specialite2, specialite3]),
    ("rie2n", [specialite1, specialite2, specialite3])
])
def test_supprimer_specialite(specialite_a_supprimer, resultat_attendu):
    """
    Un test unitaire qui test si la méthode **supprimer_specialite** qui supprime une spécialité.
    :param specialite_a_supprimer: Le nom de la spécialité à enlever
    :param resultat_attendu: Le résultat attendu
    """
    liste_avant_supprime = Specialite.list_des_specialites[::]

    Specialite.supprimer_specialite(specialite_a_supprimer)

    resultat = Specialite.list_des_specialites

    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)
    Specialite.list_des_specialites = liste_avant_supprime

