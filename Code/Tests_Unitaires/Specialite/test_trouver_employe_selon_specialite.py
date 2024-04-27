from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest


specialite_viande = Specialite("Viande", "celui qui gère les Viande")
specialite_fruits = Specialite("Fruits", "celui qui gère les  Fruits")
specialite_legumes = Specialite("Legumes", "celui qui gère les Legumes")

employe1 = Employe(p_specialite=specialite_viande)
employe2 = Employe(p_specialite=specialite_viande)
employe3 = Employe(p_specialite=specialite_fruits)
employe4 = Employe(p_specialite=specialite_legumes)


@pytest.mark.parametrize("specialite_demandee, resultat_attendu", [
    ("Viande", [employe1, employe2]),
    ("Fruits", [employe3]),
    ("Legumes", [employe4]),
    ("Reinsda", []),
])
def test_trouve_employe_selon_specialite(specialite_demandee: str, resultat_attendu: list):
    """
    Un test unitaire qui test la methode trouver employé selon une spécialité.
    :param specialite_demandee: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    resultat = Specialite.trouve_employe_selon_specialite(specialite_demandee)
    assert resultat == resultat_attendu
    assert len(resultat) == len(resultat_attendu)
