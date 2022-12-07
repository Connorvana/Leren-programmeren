getal = 50
totaal = 0 
output= ''
nummer = 0 

while totaal < 1000:
    totaal += getal
    getal += 1
    output += f' + {getal}'
    nummer += 1 
    print(f'{nummer}. 50{output} = {totaal}')

