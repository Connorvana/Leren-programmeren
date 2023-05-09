def namen():
    naam = input('Wat is je naam? \n')
    leeftijd = input('Wat is je leeftijd? \n')
    return {'name' : naam , 'age' : leeftijd}

lijst = []
repeat = True

while repeat == True:
    persoon = namen()
    lijst.append(persoon)
    doorgaan = input('Wil je nog doorgaan? (ja/nee) \n').lower()
    
    if doorgaan == 'nee':
        repeat = False
    
for persoon in lijst:
    print(persoon['name'], 'is' , persoon['age'],'Jaar.')

