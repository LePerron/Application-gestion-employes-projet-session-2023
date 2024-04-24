from Projet_intra_Entreprise.Code.Classes.classe_Specialite import Specialite
from Projet_intra_Entreprise.Code.Classes.classe_Employe import Employe
import datetime
import pytest

employe1 = Employe(p_poste="Caissier", p_specialite=Specialite(p_nom="Viande"), p_date_engagement=datetime.datetime.now())
employe1.identifiant = "12345678"
employe1.prenom = "lemoyne"
employe1.nom = "benno"
employe1.poste = "C"



@pytest.mark.parametrize("employe, resultat_attendu", [
    (employe1, (f"IDENTIFIANT : 12345678 - NOM COMPLET : benno lemoyne - "
                f"POSTE : Caissier - NUM CONTRAT : "))
])
def test_afficher_informations_employe(employe, resultat_attendu):
    employe.afficher_informations_employe()
