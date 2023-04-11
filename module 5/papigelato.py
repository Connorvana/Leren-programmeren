def papi_gelato():
    print("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")
    while True:
        bolletjes = input("Hoeveel bolletjes wilt u? ")
        try:
            bolletjes = int(bolletjes)
        except :
            print("Sorry, dat snap ik niet...")
            continue
       
        if bolletjes >= 1 and bolletjes <= 3:
             bakje_hoorntje = input(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? ")
             
             if bakje_hoorntje == "bakje" or bakje_hoorntje == "hoorntje":
                 print(f"Hier is uw {bakje_hoorntje} met {bolletjes} bolletje(s).")
                 break
        
        else:
            print("Sorry, dat snap ik niet...")
            break
        
        if bolletjes >= 4 and bolletjes <= 8:
            print(f"Dank u wel, dan krijgt u van mij een bakje met {bolletjes} bolletjes.")
            break
        
        elif bolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet.")
       
        else:
            print("Sorry, dat snap ik niet...")
            break

    while True:
        meer_bestellen = input("Wilt u nog meer bestellen? ")
       
        if meer_bestellen == "ja":
            papi_gelato()
            break
       
        elif meer_bestellen == "nee":
            print("Bedankt en tot ziens!")
            break
        
        else:
            print("Sorry, dat snap ik niet...")

