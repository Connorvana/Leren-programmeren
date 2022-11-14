#mijn game idee: 
#mijn idee is een 1 speler spel, waarbij je moet raden op welke plek de bom verstopt is
import random

repeat= True
random= random.randint(1,1)

while repeat == True: 
   
    nummer= input('kies een nummer tussen 1 en 2 ' )
   
    if int(nummer) == int(random) : 
        print( 'goedzo! je kan doorgaan. ')
        repeat=True
   
    else:
        print('BOOM! je bent opgeblazen toen je naar een snoepje zocht, maar je hebt nog een leven. ')
        repeat=True
   
    nummer2= input('je bent nu bij level 2| kies een nummer tussen 1 en 2 ')

    if int(nummer) == int(random):
         print('goedzo je hebt gewonnen! ')
         quit()
         
    else:
        joker=input('nee dat is fout. Wil je een joker gebruiken?  ja / nee ')
        repeat=True
        
        if joker == 'ja':
            repeat= True
       
        if joker == 'nee':
            quit()
    
    nummer3= input('kies een nummer tussen 1 en 2 ')
    
    if int(nummer3) ==int(random):
        print('Goed gespeeld, je hebt gewonnen. ')
        repeat=False
    else:
        print('jeetje wat ben jij slecht zeg!')
        repeat=False

        exit()
        
    
    
            

    
        
    



    

