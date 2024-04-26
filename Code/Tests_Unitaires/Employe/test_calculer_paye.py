from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest

employe1 = Employe()
employe1.contrat.salaire_horaire = 16.50
employe1.contrat.facteur_salaire = 0.2
employe1.contrat.nb_heures_semaine = 20

employe2 = Employe()
employe2.contrat.salaire_horaire = 15.75
employe2.contrat.facteur_salaire = 0
employe2.contrat.nb_heures_semaine = 0

employe3 = Employe()
employe3.contrat.salaire_horaire = -12
employe3.contrat.facteur_salaire = 0.02
employe3.contrat.nb_heures_semaine = 1000

@pytest.mark.parametrize("employe, resultat_attendu", [
    (employe1, 396),
    (employe2, 0),
    (employe3, 0)
])
def test_calculer_paye(employe, resultat_attendu: int):
    """
    Un test unitaire qui test la methode calculer paye.
    :param employe: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    resultat = employe.calculer_paye()
    assert resultat == resultat_attendu
    assert isinstance(resultat, float)
