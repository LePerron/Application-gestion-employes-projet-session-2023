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
def test_obtenir_poste_complet(poste, specialite, resultat_attendu):
    employe1 = poste()
    employe1.specialite = Specialite(p_nom=specialite)
    resultat = employe1.obtenir_poste_complet()
    assert resultat == resultat_attendu
    assert isinstance(resultat, str)
