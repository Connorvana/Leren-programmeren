from fruitmand import fruitmand 
kleuren = {
    
     'yellow' : 'gele',
    'green'  : 'groene', 
    'orange' : 'oranje',
    'red' : 'rode', 
    'brown': 'bruine', 
   
}


naam = []

for x in range(len(fruitmand)):
    naam.append(fruitmand[x]['name'])
naam.sort(key=len)
naam.reverse()

langste_naam = naam[0]
aantal_letters = len(langste_naam)

for y in range(len(fruitmand)): 
    if fruitmand[y]['name']== langste_naam:
        gewicht = fruitmand[y]['weight']
        kleur = fruitmand[y]['color']



print('De', langste_naam, '(' ,aantal_letters, 'letters ) heeft een' ,kleuren[kleur], 'kleur en een gewicht van' ,gewicht/1000,'kg')