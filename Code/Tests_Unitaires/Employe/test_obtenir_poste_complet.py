from Projet_intra_Entreprise.Code.Classes.classe_Caissier import Caissier

import pytest

from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite

employe1 = Caissier()


@pytest.mark.parametrize("poste, specialite, resultat_attendu", [
    (Caissier, "Viande", "Caissier Viande")
])
def test_obtenir_poste_complet(poste, specialite, resultat_attendu):
    specialite = Specialite(p_nom=specialite)
    employe1.specialite =
    assert employe1.obtenir_poste_complet() == resultat_attendu
