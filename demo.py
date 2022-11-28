#2 getallen invoeren grootste getal geprint
a=input('voer een getal in: ')
 
b=input('voer een getal in: ')

if int(a) > int(b):
    max=a
    min=b
    print (max)
elif int(a) < int(b):
    max= b
    min= a
    print (max)