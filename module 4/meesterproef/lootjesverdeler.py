import random

repeat = True
repeat2 = True
lijst = []

while repeat == True:
    naam = input("voer de namen in van de spelers:\n").lower()

    if naam in lijst:
        print("Die naam zit al in de lijst.")
        continue

    else:
        lijst.append(naam)     
        if len(lijst) >= 3:
            repeat = False

while repeat2 == True:
    extra = input("Wil je nog extra namen toevoegen?: (ja/nee)\n")

    if extra == "ja":
        toevoegen = input("Wie wil je nog meer toevoegen?:\n").lower()
        if toevoegen in lijst:  
            print("Die naam zit al in de lijst.")
            continue

        else:
            lijst.append(toevoegen)

    else:
        repeat2 = False
        random.shuffle(lijst)
        print(lijst)

        for i in range(len(lijst)-1):
            print(lijst[i],'heeft',lijst[i + 1])
            
        print(lijst[-1],'heeft',lijst[0])


