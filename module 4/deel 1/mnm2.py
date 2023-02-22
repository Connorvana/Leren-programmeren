import random


kleuren=('Rood', 'Blauw', 'Groen', 'geel','bruin')
Mnm= int(input('Hoeveel M&Ms moeten er toegevoegd worden? : '))
zak= {}
getal = 1 

for x in range(Mnm):
    keuze = random.choice(kleuren)
    if keuze not in zak:
        zak.update({keuze: getal})
    elif keuze in zak:
        zak [keuze] += 1

print(zak)

