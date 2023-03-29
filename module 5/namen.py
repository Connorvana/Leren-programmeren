def vraag():
    naam = input('Wat is je naam?: \n')
    Leeftijd = input('Wat is je leeftijd?: \n')
    return{ 'naam': naam, 'leeftijd': Leeftijd}
 
lijst = []
repeat = True

while repeat == True: 
    persoon = vraag()
    lijst.append(persoon)
    stoppen= input( 'wil je nog doorgaan?: ja/nee \n').lower()
    
    if stoppen == 'nee':
        break

for persoon in lijst : 
    print(persoon['naam'], 'is', persoon['leeftijd'], 'Jaar oud' )