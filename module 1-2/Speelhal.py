from ast import Num
from multiprocessing.sharedctypes import Value
from optparse import Values
from re import X
from tkinter.tix import INTEGER


personen=input('hoeveel personen zijn er?:')
print(7.45* int(personen))

minuten=input('hoeveel minuten zijn ze bezig?:')
print(0.074* int(minuten))

totaalbedrag= ((7.45* int(personen)) +  (0.074* int(minuten)))
algemeen= ( int(totaalbedrag) *  int(personen ))

print (' het bedrag is '+ str(algemeen) + ' euro ' )











