repeat = True
Boodschappenlijstje = {}

while repeat == True:
    toevoegen = (input('Hallo, wat wilt u toevoegen?:\n')).upper()
    aantal = int(input(f'Hoevaak wilt u {toevoegen} aan uw lijstje toevoegen?:\n'))

    if toevoegen not in Boodschappenlijstje:
        Boodschappenlijstje.update({toevoegen: aantal})

    
    else:
        (Boodschappenlijstje)[toevoegen] += aantal
 
    restart = str(input('Wilt u nog iets toevoegen?\n'))

     
    if restart == 'nee':
        break
        
    if restart == 'ja':
        repeat = True
   
print("=[-| BOODSCHAPPENLIJSTJE |-]=")
for aantal, toevoegen in Boodschappenlijstje.items():
    print(f"  {toevoegen}x {aantal}   ")
print("=-------------------------=")