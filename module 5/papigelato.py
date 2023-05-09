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
        
       

