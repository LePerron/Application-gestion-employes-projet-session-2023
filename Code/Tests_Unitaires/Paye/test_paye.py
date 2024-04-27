from Projet_intra_Entreprise.Code.Classes.classe_Paye import Paye
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import datetime, date
import pytest

employe1 = Employe(p_identifiant="1234567")
employe2 = Employe(p_identifiant="7654321")
employe3 = Employe(p_identifiant="5647839")


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("55", 0),
    ("zsd", 0),
    (12.0, 12.0),
    (23.23, 23.23),
    ("0192583794", 0),
    (-23.0, 0),
    (9.0, 9),
    (0.0, 0),
    (-264.23, 0),
    (55.0, 55.0),
    (56.0, 56.0),
    (2, 0),
])
def test_set_montant_paye(valeur: str, resultat_attendu: str):
    """
    Un test unitaire qui test le setter du montant de la paye.
    :param valeur: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    paye1 = Paye()
    paye1.montant_paye = valeur
    assert paye1.montant_paye == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("1234567", employe1),
    ("7654321", employe2),
    ("5647839", employe3),
    ("1324569", None),
    (".35.3.", None),
    ("-132452", None),
])
def test_set_employe(valeur: str, resultat_attendu: str):
    """
    Un test unitaire qui test le setter de l'employe a qui appartient la paye.
    :param valeur: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    paye1 = Paye()
    paye1.employe = valeur
    assert paye1.employe == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("02/05/2022", datetime.strptime("02/05/2022", "%d/%m/%Y")),
    ("22/05/2020", None),
    ("02/05/2025", None),
])
def test_set_date_de_paye(valeur: str, resultat_attendu: date):
    """
    Un test unitaire qui test le setter de la date de paye.
    :param valeur: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    """
    paye1 = Paye()
    paye1.date_de_paye = valeur
    assert paye1.date_de_paye == resultat_attendu
