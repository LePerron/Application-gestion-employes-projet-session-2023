from Projet_intra_Entreprise.Code.Classes.classe_Gestionnaire import Gestionnaire
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Commis import Commis
from Projet_intra_Entreprise.Code.Classes.classe_Gerant import Gerant
import pytest


@pytest.mark.parametrize("poste, specialite, resultat_attendu", [
    (Gestionnaire, "Viande", "Gestionnaire Viande"),
    (Caissier, "Legume", "Caissier Legume"),
    (Commis, "caisses", "Commis Caisses"),
    (Gerant, "saucisses", "Gerant Saucisses")
])
def test_obtenir_poste_complet(poste, specialite: str, resultat_attendu: str):
    """
    Un test unitaire qui test la methode pour obtenir l'ancienneté.
    :param poste: L'une des valeurs qu'on souhaite setter.
    :param specialite: L'une des valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    :return:
    """
    employe1 = poste()
    employe1.specialite = Specialite(p_nom=specialite)
    resultat = employe1.obtenir_poste_complet()
    assert resultat == resultat_attendu
    assert isinstance(resultat, str)
