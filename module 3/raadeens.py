import  random 


ronde= 0
score = 0 

repeat1= True
repeat= True

print('Welkom bij dit spel!')
print('Regels: \n1. \nJe moet in 10 rondes proberen een getal te raden \ntussen de 1 en 1000')
print('2. \nals je in 10 rondes niet het getal raad dan ben je af en\n stopt het spel\n ')
print('Dus beginnen maar!')

while repeat1 == True:
    getal = random.randint(1,1000)
    x = 0 
    ronde= ronde + 1
    repeat = True
    
    while repeat== True:
     
        try:
         raad_getal=int(input('Welk getal denk je dat het is?\n '))
         x = x + 1 
         raad_getal
         repeat = False
         rondetwintig = raad_getal - getal
         
         if int(raad_getal) > 1000:
                repeat = True
                print('heb je geluisterd? het getal moet binnen de 1000 zijn!')

        #getal is lager

         elif raad_getal > getal:
             print('lager')
             repeat = True
             if  (int(rondetwintig)) <= 20:
                 print('je bent heel warm')
                 repeat = True
            
             elif (int(rondetwintig)) <=50:
                 print('je bent warm')
                 repeat = True
        
         elif raad_getal < getal:
             print('Hoger')
             repeat = True
            
             if abs (int(rondetwintig)) <= 20:
                 print('je bent heel warm')
                 repeat = True
            
             elif abs (int(rondetwintig)) <=50:
                 print('je bent warm')
                 repeat = True
         
         elif raad_getal == getal:
             score = score + 1 
             print('Dat is goed \n'+ 'je score is: ' + str(score))
             opnieuw = input('Nog een getal raden?  ja/nee\n').lower()

             if opnieuw == 'ja':
                repeat1= True
                if (int(ronde)) == 3:
                    print('Balen! je rondes zijn voorbij! \n Game over \n je score is: ' + str(score))
                    quit()
             elif opnieuw == 'nee':
                print('Bedankt voor het spelen!\nLatersss \nJe score was: ' + str(score))
                quit()
        
         if int(x) == 10:
            repeat = False
            print( 'Helaas! Je mag niet meer raden. Je score is: ' + str(score))

            opnieuw = input('Nog een getal raden? Ja/nee \n').lower() 
            
            if opnieuw == 'ja':
                repeat1= True
                if int(ronde) == 20:
                    print('Sorry je rondes zijn voorbij! \nGame over! \n' + str(score))
                    quit()
            elif opnieuw == 'nee': 
                print('Bedankt voor het spelen! \nTot ziens!')
                quit()
        
        except Exception as error:
            print('dat is geen nummer!')

    
    
    
    
   

        










    