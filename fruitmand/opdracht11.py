from fruitmand import fruitmand

repeat = True
lijstkleur = []

rond = 0 
niet_rond= 0 

for x in range(len(fruitmand)):
    kleur = (fruitmand[x]['color'])
    if kleur not in lijstkleur:
        lijstkleur.append(kleur)
while repeat == True:
   kleur = str(input('Kies welke kleur je wilt:' + str(lijstkleur) + '.\n')).lower()
   
   if (kleur) not in lijstkleur:
       print('de kleur: ' + kleur + ' zit niet in de fruitmand')
   else: 
       print('De kleur zit in de lijst.')
       repeat = False

for fruit in fruitmand:
    
    if fruit['color'] == kleur: 
        if fruit['round'] == True:
            rond += 1
        else: 
            niet_rond += 1 


verschil = abs(rond - niet_rond)

if rond > niet_rond:
    print(f'er zijn {int(verschil)} meer ronde vruchten, dan niet ronde vruchten in de kleur {str(kleur)}')
if rond < niet_rond:
        print (f"Er zijn {str(verschil)} minder ronde vruchten, dan niet ronde vruchten in de kleur {str(kleur)}")
if rond == niet_rond:
    print (f"Er zijn {str(verschil)} ronde vruchten en {str(niet_rond)} niet ronde vruchten in de kleur {str(kleur)}")






