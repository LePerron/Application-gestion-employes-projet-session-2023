from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import datetime
import pytest


@pytest.mark.parametrize("date_engagement, resultat_attendu", [
    ("03/05/2022", 1),
    ("02/09/2000", 23),
    ("03/01/1900", 124)
])
def test_obtenir_anciennete(date_engagement, resultat_attendu):
    date_formatee = datetime.datetime.strptime(date_engagement, "%d/%m/%Y")

    employe1 = Employe(p_identifiant="12345678", p_prenom="lemoyne", p_nom="benno", p_poste="Caissier",
                       p_specialite=None, p_date_engagement=date_formatee)

    resultat = employe1.obtenir_anciennete()
    assert resultat == resultat_attendu
    assert isinstance(resultat, int)
