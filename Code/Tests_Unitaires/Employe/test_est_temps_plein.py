from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest


employe1 = Employe(p_identifiant="12345678", p_prenom="lemoyne", p_nom="benno", p_poste="Caissier", p_specialite=None, p_date_engagement=None)


@pytest.mark.parametrize("nb_heures_semaine, resultat_attendu", [
    (23, False),
    (12, False),
    (-12, False),
    (40, True),
    (55, True),
    (39, False),
    (20.3, False),
    ("a", False),
    ("0", False),
    (0, False)
])
def test_est_temps_plein(nb_heures_semaine: int, resultat_attendu: bool):
    """
    Un test unitaire qui test la methode est temps plein.
    :param nb_heures_semaine: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    :return:
    """
    employe1.contrat.nb_heures_semaine = nb_heures_semaine
    resultat = employe1.est_temps_plein()
    assert resultat == resultat_attendu
    assert isinstance(resultat, bool)
