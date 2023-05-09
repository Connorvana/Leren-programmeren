from schoenen_data import *

# opdracht 4:
# vraag de maat van de klant en print vervolgens:
# "fonetische_kleuren Merknaam Modelnaam, prijs"
# uiteraard alleen de schoenen die beschikbaar zijn in betreffende maat.

klant_maat = int(input('Welke maat heb je? '))


for schoen in schoenen_lijst:
    if klant_maat in schoen['maten']:
        print(fonetische_kleuren[schoen['kleur']] ,schoen['merk'], schoen['model'], schoen['prijs'])

        
    
  
