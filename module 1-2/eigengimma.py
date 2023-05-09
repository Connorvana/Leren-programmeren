#mijn game idee: 
#mijn idee is een 1 speler spel, waarbij je moet raden op welke plek de bom verstopt is
import random

def restart_win():
    win = input('wil je opnieuw spelen of stoppen?  Restart/Quit \n').lower()
    if win == 'quit':
        print('bedankt voor het spelen!')
        quit()
    if win == 'restart':
        repeat == True

repeat=True

while repeat == True:
   
    nummer = input('Welkom bij deze game| \nKies een nummer: \n A: 1 \n B: 2 \n ')
   
    if nummer == 'a':
        print('Goed geraden! \nWe gaan nu door naar level 2. \n ')
        level2=input('Level 2| \nKies nu een nummer tussen 1 en 5: \n')
              
#win
        if level2== '2':
            print('Gewonnen!')
            restart_win()
        else:
            print('Jammer, dat is fout!')
            restart_win()
             
#joker ja / nee
    if nummer == 'b':
       joker = input('OH! dat was fout :( \nWil je een joker gebruiken? ja/nee \n ')

       if joker == 'nee':
           restart_win()
           
#joker is ja
       if joker == 'ja':
            level3 = input('Je hebt nu gekozen om door te gaan naar |LEVEL 3| \nKies nu een nummer tussen 1 en 10 \n ')
#tweede win
            
            
            if level3 > str(6):
                print('Goedzo je hebt gewonnen!')
                restart_win()
                
            else:
                print('OH dat is fout!')
                restart_win()
                    

    
        
    



    

