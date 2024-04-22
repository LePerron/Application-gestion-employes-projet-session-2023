from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier
from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
import pytest


@pytest.mark.parametrize("poste, specialite, resultat_attendu", [
    (Caissier, "Viande", "Caissier Viande")
])
def test_obtenir_poste_complet(poste, specialite, resultat_attendu):
    employe1 = poste(p_specialite=Specialite(specialite))
    assert employe1.obtenir_poste_complet() == resultat_attendu