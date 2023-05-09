from schoenen_data import *


# opdracht 3:
# Vraag een merk en print vervolgens alle witte schoenen mits duurder dan €100.

merk = input("Geef het merk op: ")

for schoen in schoenen_lijst:
    if schoen["merk"] == merk and schoen["kleur"] == "wit" and schoen["prijs"] > 100:
        print(schoen['merk'], '-', schoen['model'],'-', schoen['kleur'] ,'-', schoen['prijs'])