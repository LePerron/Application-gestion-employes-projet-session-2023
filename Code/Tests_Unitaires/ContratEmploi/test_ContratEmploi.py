from Projet_intra_Entreprise.Code.Classes.classe_ContratEmploi import ContratEmploi
from datetime import datetime
import pytest


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("23", 0),
    (29, 29),
    (-29, 0),
    (60, 0),
    (41, 0),
    (40, 40),
    (39, 39),
    (0, 0),
    (2.23, 0),
    ("20", 0),
])
def test_set_nb_heures_semaine(valeur, resultat_attendu):
    contrat1 = ContratEmploi()
    contrat1.nb_heures_semaine = valeur
    assert contrat1.nb_heures_semaine == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("55", 15.75),
    ("zsd", 15.75),
    (12, 15.75),
    (23.23, 23.23),
    ("0192583794", 15.75),
    (-23, 15.75),
    (9, 15.75),
    (0, 15.75),
    (-264.23, 15.75),
    (55.0, 55.0),
    (56, 15.75),
])
def test_salaire_horaire(valeur, resultat_attendu):
    contrat1 = ContratEmploi()
    contrat1.salaire_horaire = valeur
    assert contrat1.salaire_horaire == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("asdasd", 0.0),
    (10.0, 10.0),
    (20.4, 20.4),
    ("23", 0.0),
    (".35.3.", 0.0),
    ("p4ér2n", 0.0),
])
def test_set_facteur_salaire(valeur, resultat_attendu):
    contrat1 = ContratEmploi()
    contrat1.facteur_salaire = valeur
    assert contrat1.facteur_salaire == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("02/05/2022", datetime.strptime("02/05/2022", "%d/%m/%Y")),
    ("22/05/2020", None),
    ("02/05/2025", None),
])
def test_set_date_engagement(valeur, resultat_attendu):
    contrat1 = ContratEmploi()
    contrat1.date_du_contrat = valeur
    assert contrat1.date_du_contrat == resultat_attendu
