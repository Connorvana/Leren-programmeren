from schoenen_data import *


# opdracht 6:
# print van de schoen leverbaar in de grootste maat :
# IN maat ... leverbaar: merk. model en kleur van de schoenen
grootste_maat = 0
for schoen in schoenen_lijst:
    if max(schoen['maten']) >= grootste_maat:
        grootste_maat = max(schoen['maten'])

for schoen in schoenen_lijst:
    if grootste_maat in schoen['maten']:
        merk = schoen['merk']
        model = schoen['model']
        kleur = schoen['kleur']
        print(f'IN maat {grootste_maat} leverbaar: {merk}. {model} {kleur}')
  

 

    