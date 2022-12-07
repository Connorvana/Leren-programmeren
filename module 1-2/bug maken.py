repeat=True
while repeat == True:
    leeftijd= input('goedenavond, wat is je leeftijd? ')

    if leeftijd > 18:
        naam=  input('wat is uw naam?: ')
        repeat= True
    else: 
        print('ga weg')
        repeat = False
  
    gummy=  input('\nwat voor gummybears wil je?  \n1. rood\n2. zwart\n3. geel\n')

    if gummy == '1':
        print("slechte keuze, je gaat dood")
    elif gummy == '2':
        print('waarom zou je zwart snoep kiezen? ')
    elif gummy == '3':
        print('fijn dat je voor mij kiest')



