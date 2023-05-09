from schoenen_data import *

# Opdracht 5:
# print van de duurste schoen: merk en model en doe dat ook voor de goedkoopste.

goedkoop = schoenen_lijst[0]
duur = schoenen_lijst[0]

for schoen in schoenen_lijst:
    if schoen['prijs'] > duur['prijs']:
        duur = schoen
    if schoen['prijs'] < goedkoop['prijs']:
        goedkoop = schoen
    
    
print(duur['merk'],'-', duur['model'],'-', duur['prijs'])
print(goedkoop['merk'],'-', goedkoop['model'],'-', goedkoop['prijs'])
    



