from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
from datetime import datetime
import pytest


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("1234567", "1234567"),
    ("345asd6", ""),
    ("usafhljent", ""),
    ("-204824", ""),
    ("0192824", "0192824"),
    ("0192824", ""),
])
def test_set_identifiant(valeur, resultat_attendu):
    """
    Un test unitaire qui test le setter de l'identifiant de l'employe.
    :param valeur: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    employe1 = Employe()
    employe1.identifiant = valeur
    assert employe1.identifiant == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("marc-antoine", "Marc-antoine"),
    ("marc-23antoine", ""),
    ("24234", ""),
    ("benno", "Benno"),
    ("0192583794", ""),
    (".,`l^.", ""),
    ("élodie", "Élodie"),
])
def test_set_nom(valeur, resultat_attendu):
    """
    Un test unitaire qui test le setter du nom de l'employe
    :param valeur: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    employe1 = Employe()
    employe1.nom = valeur
    assert employe1.nom == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("perron", "Perron"),
    ("lemoyne", "Lemoyne"),
    ("24234", ""),
    ("23", ""),
    (".,`l^.", ""),
    ("pérron", "Pérron"),
])
def test_set_prenom(valeur, resultat_attendu):
    """
    Un test unitaire qui test le setter du prenom de l'employe.
    :param valeur: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    employe1 = Employe()
    employe1.prenom = valeur
    assert employe1.prenom == resultat_attendu


@pytest.mark.parametrize("valeur, resultat_attendu", [
    ("02/05/2022", datetime.strptime("02/05/2022", "%d/%m/%Y")),
    ("22/05/2020", None),
    ("02/05/2025", None),
])
def test_set_date_engagement(valeur, resultat_attendu):
    """
    Un test unitaire qui test le setter de la date d'engagement de l'employe.
    :param valeur: La valeur qu'on souhaite setter
    :param resultat_attendu: La valeur belle et bien setter avec les bonne modifications ou la valeur de remplacement.
    :return:
    """
    employe1 = Employe()
    employe1.date_engagement = valeur
    assert employe1.date_engagement == resultat_attendu
