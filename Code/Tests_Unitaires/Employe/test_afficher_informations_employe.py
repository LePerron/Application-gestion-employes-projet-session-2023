from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import datetime
import pytest

employe1 = Employe(p_identifiant="12345678", p_prenom="lemoyne", p_nom="benno", p_poste="Caissier", p_specialite=Specialite(p_nom="Viande"), p_date_engagement=datetime.datetime.now())
employe2 = Employe(p_identifiant="1234523", p_prenom="landry", p_nom="maël", p_specialite=Specialite("Legume"))
employe3 = Employe(p_identifiant="12d34a8", p_prenom="perron", p_nom="marc", p_date_engagement=datetime.datetime.now())


@pytest.mark.parametrize("employe, resultat_attendu", [
    (employe1, (f"IDENTIFIANT : 12345678 - NOM COMPLET : benno lemoyne - "
                f"POSTE : Caissier - NUM CONTRAT : "))
])
def test_afficher_informations_employe(employe, resultat_attendu):
    employe.afficher_informations_employe()
