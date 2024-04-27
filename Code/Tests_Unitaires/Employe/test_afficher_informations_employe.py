from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import pytest

employe1 = Employe()
employe1.identifiant = "1234567"
employe1.nom = "lemoyne"
employe1.prenom = "benno"
employe1.poste = "Caissier"

employe2 = Employe()
employe2.identifiant = "12345678"
employe2.nom = "lemoyne"
employe2.prenom = "benno"
employe2.poste = "Caissier"


@pytest.mark.parametrize("employe, resultat_attendu", [
    (employe1, (f"IDENTIFIANT : 1234567 - NOM COMPLET : Benno Lemoyne - "
                f"POSTE : Caissier - NUM CONTRAT : 1")),
    (employe2, (f"IDENTIFIANT :  - NOM COMPLET : Benno Lemoyne - "
                f"POSTE : Caissier - NUM CONTRAT : 2"))
])
def test_afficher_informations_employe(employe, resultat_attendu: str):
    """
    Un test unitaire qui test la methode affocher information employe.
    :param employe: La valeur qu'on souhaite setter.
    :param resultat_attendu: La valeur qui est belle et bien setter avec les bonnes modifications ou la valeur de remplacement.
    :return:
    """
    resultat = employe.afficher_informations_employe()
    assert resultat == resultat_attendu
    assert isinstance(resultat, str)
