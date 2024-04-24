import pytest
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye

paye1 = Paye()
paye1.employe.contrat.salaire_de_horraire =


employe1 = Employe()
employe1.contrat.salaire_de_horraire = 16.50
employe1.contrat.facteur_salaire = 0.2
employe1.contrat.nb_heures_semaine = 20

@pytest.mark.parametrize("employe, resultat_attendu", [
    (Paye, 396)
])
def test_calculer_paye(employe, resultat_attendu):
    assert employe.calculer_paye(employe1) == resultat_attendu
