import math
repeat = True
while repeat == True:
    keuze = input('wilt u small, medium of large pizza?: ')
  
    
    if keuze == 'small':
        repeat= False
        prijs= 5,99
    
    elif keuze == 'medium':
        repeat= False
        prijs= 7,99
    
    elif keuze == 'large': 
        repeat= False
        prijs= 8,99
    else: 
     print(keuze)

    aantal= input('hoeveel pizzas wilt u? ')

    try: 
        totaal= int(keuze)* prijs
    except: 
        print('dit is geen cijfer')
        exit()


    

    

print(' __________________________________')
print('|                                   |')
print('|', aantal , 'X', keuze ,'pizza     |' )
print('| U komt op een totaal van ''€', prijs,'|' )
print('------------------------------------')















