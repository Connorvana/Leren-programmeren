#mijn game idee: 
#mijn idee is een 1 speler spel, waarbij je moet raden op welke plek de bom verstopt is
import random

repeat=True

while repeat == True:
   
    nummer = input('Welkom bij deze game| \nKies een nummer: \n A: 1 \n B: 2 \n ')
   
    if nummer == 'a':
        print('Goed geraden! \nWe gaan nu door naar level 2. \n ')
        level2=input('Level 2| \nKies nu een nummer tussen 1 en 5: \n')
              
              #Eerste win

        #win
        if level2== '2':
            win = input('Gewonnen! \nWil je opnieuw spelen of stoppen? quit/restart: \n')
            
            if win == 'quit':
                print('bedankt voor het spelen!')
                quit()
            
            if win == 'restart':
                repeat=True
        else:
             win = input('OH dat was fout! \nWil je opnieuw spelen of stoppen? quit/restart: \n')
             
             if win == 'quit':
                print('bedankt voor het spelen!')
                quit()
             
             if win == 'restart':
                repeat=True
            

 #joker ja / nee
    if nummer == 'b':
       joker = input('OH! dat was fout :( \nWil je een joker gebruiken? ja/nee \n ')

       if joker == 'nee':
           opnieuw = input('bedankt voor het spelen! | \nWil je opnieuw spelen of stoppen?  Restart/Quit| \n')

           if opnieuw == 'restart':
            repeat = True
            
           if opnieuw == 'quit':
            print('bedankt voor het spelen')
            quit()
       
       
       #joker is ja
       if joker == 'ja':
            level3 = input('Je hebt nu gekozen om door te gaan naar |LEVEL 3| \nKies nu een nummer tussen 1 en 10 \n ')
#tweede win
            
            
            if level3 > str(6):
                win2 = input('Goedzo je hebt gewonnen! \nwil je opnieuw beginnen of wil je stoppen?\n Restart/Quit\n')

                if win2 == 'restart':
                    repeat=True
               
               
                if win2 == 'quit':
                    quit()
           
           
            else:
                 win2 = input('OH dat is fout! \nwil je opnieuw beginnen of wil je stoppen?\n  Restart/Quit\n')
                 
                 if win2 == 'restart':
                    repeat=True
                 
                 if win2 == 'quit':
                    print('bedankt voor het spelen misschien tot de volgende keer! \n')
                    quit()

                    

    
        
    



    

