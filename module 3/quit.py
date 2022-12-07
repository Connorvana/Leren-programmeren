vraag= 1

repeat= True

while repeat == True:
    antwoord= input('Wil je stoppen?  yes/no | \n')

    if antwoord == 'yes':
        print('Houdoe! de vraag is', vraag, ' keer gesteld')
        repeat= False
    elif antwoord == 'no':
        print('daar gaan we nog een keer! ')
        vraag = vraag + 1 
        repeat=True