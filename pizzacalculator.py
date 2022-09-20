import math


small=6
medium=7.99
large=9.99

keuze = input('wilt u small, medium of large pizza?: ')
aantal= input('hoeveel pizzas zou u willen?: ')

prijs= 0 

if keuze == 'small' : 
    prijs= int(aantal) * small
if keuze == 'medium' : 
    prijs= int (aantal) * medium
if keuze == 'large' : 
    prijs= int(aantal) * large

print(' __________________________________')
print('|                                   |')
print('|', aantal , 'X', keuze ,'pizza     |' )
print('| U komt op een totaal van ''€', prijs,'|' )
print('------------------------------------')















