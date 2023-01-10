import random


print('Welkom bij dit spel!')
print('Regels: \n1. \nJe moet in 10 rondes proberen een getal te raden \ntussen de 1 en 1000')
print('2. \nals je in 10 rondes niet het getal raad dan ben je af en\n stopt het spel\n ')
print('Dus beginnen maar!')

score = 0
ronde = 0
repeat = True
repeat1 = True

while repeat1 == True:
    getal = random.randint(1,1000) 
    print(getal)
    x = 0
    ronde = ronde + 1
    repeat = True

    while repeat == True:
             
        try:
            geraden_getal = int(input("Wat denk je dat het getal is? : "))
            x = x + 1
            geraden_getal
            repeat = False
            roundtwintig = geraden_getal - getal

            if int(geraden_getal) > 1000 :
                repeat = True
                print("Heb je geluisterd? het getal moet binnen de duizend zijn!!!")

            elif geraden_getal > getal:
                print("Lager!")
                repeat = True
                
               
            elif geraden_getal < getal:
                print("Hoger!")
                repeat = True
            
            if abs(int(roundtwintig)) <= 20:
                    print("Je bent heel warm!")
                    repeat = True
            elif abs(int(roundtwintig)) <= 50:
                    print("Je bent warm!")
                    repeat = True
                
            elif geraden_getal == getal:
                score = score + 1 
                print("Dat is juist!\n" +"Jouw score : "+ str(score))
                opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
                
                if opnieuw == "ja":
                    repeat1 = True
                    if int(ronde) == 5:
                        print("Helaas zijn je ronde's voorbij\nGame Over!\n" + "Jouw score: " + str(score))
                        quit()
                    
                elif opnieuw == "nee":
                    print("Bedankt voor spelen!\nLatersss! ")
                    quit()
             
            if int(x) == 10:
                repeat = False
                print("Helaas zijn je pogingen voorbij\n" + "Jouw score : " + str(score))
            
                opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
                if opnieuw == "ja":
                    repeat1 = True
                    if int(ronde) == 5:
                        print("Helaas zijn je ronde's voorbij\nGame Over!\n" + "Jouw score: " + str(score))
                        quit()
    
                elif opnieuw == "nee":
                    print("Bedankt voor spelen!\nTot latersss!")
                    quit()

            

        except Exception as error:
            print("Dat is geen getal! ")  



    
    
    
    
   

        










    