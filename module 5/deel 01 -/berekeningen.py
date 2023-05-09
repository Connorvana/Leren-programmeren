def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication( n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
repeat = True
while repeat == True:
    
    choice = input('Wat wilt u doen?: \nA) getallen optellen \nB) getallen aftrekken \nC) getallen vermenigvuldigen \nD) getallen delen \nE) getal ophogen \nF) getal verlagen \nG) getal verdubbelen \nH) getal halveren\n ').lower() 
    try:
        if choice == 'a':
            n1= float(input('Welk getal wil je optellen?: \n'))
            n2= float(input(f'Welk getal wil je optellen bij {n1}?\n '))
            uitkomst = addition(n1, n2)
            print(f'{n1} + {n2} = {uitkomst}\n')
            
            
        
#aftrekken  
        elif choice == 'b':
            n1= float(input('Welk getal wil je aftrekken?: \n'))
            n2= float(input(f'Welk getal wil je aftrekken bij {n1}?\n '))
            uitkomst = subtraction(n1, n2)
            print(f'{n1} - {n2} = {uitkomst}\n')
            

#vermeningvuldigen
        elif choice == 'c':
            n1= float(input('Welk getal wil je vermenigvuldigen?: \n'))
            n2= float(input(f'Welk getal wil je vermenigvuldigen bij {n1}?\n '))
            uitkomst = multiplication(n1, n2)
            print(f'{n1} x {n2} = {uitkomst}\n')
            
#getal delen
        elif choice == 'd':
            n1= float(input('Welk getal wil je delen?: \n'))
            n2= float(input(f'Welk getal wil je delen bij {n1}?\n '))
            uitkomst = division(n1, n2)
            print(f'{n1} : {n2} = {uitkomst}\n')
            
        
    
#getal ophogen
        elif choice == 'e':
            n1= float(input('Welk getal wil je ophogen?: \n'))
            uitkomst = n1 + 1
            print(f'{n1} + 1.0 = {uitkomst}\n')
            
    
#getal verlagen
        elif choice == 'f':
            n1= float(input('Welk getal wil je verlagen?: \n'))
            uitkomst = n1 - 1
            print(f'{n1} - 1.0 = {uitkomst}\n')
            
    
#getal verdubbelen
        elif choice == 'g':
            n1= float(input('Welk getal wil je verdubbelen?: \n'))
            uitkomst = n1 * 2
            print(f'{n1} x 2.0 = {uitkomst}\n')
            
    
#getal halveren
        elif choice == 'h':
            n1= float(input('Welk getal wil je Halveren?: \n'))
            uitkomst = n1 / 2
            print(f'{n1} : 2.0 = {uitkomst}\n')
            
  
    except:
        print('Sorry, dit kan niet!')
    
    uitkomst2 = uitkomst
    while repeat == True:
        choice = input(f'Wat wilt u doen met de uitkomst? ({uitkomst2}): \nA) Getallen optellen \nB) Getallen aftrekken \nC) Getallen vermenigvuldigen \nD) Getallen delen \nE) Getal ophogen \nF) Getal verlagen \nG) Getal verdubbelen \nH) Getal halveren\nI) Stoppen\n ').lower()
    
        while repeat == True:
            try:
         #optellen
                if choice == 'a':
                    n2a = float(input(f'Welk getal wil je optellen bij {uitkomst2}?: \n'))
                    uitkomst2 = uitkomst2 + n2a
                    print( f'| {uitkomst} + {n2a} = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
         #getallen aftrekken
           
                elif choice == 'b':
                    n2a = float(input(f'Welk getal wil je aftrekken bij {uitkomst2}?: \n'))
                    uitkomst2 = uitkomst2 - n2a
                    print( f'| {uitkomst} - {n2a} = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
            #vermenigvuldigen
            
                elif choice == 'c':
                    n2a = float(input(f'Welk getal wil je vermenigvuldigen met {uitkomst2}?: \n'))
                    uitkomst2 = uitkomst2 * n2a
                    print( f'| {uitkomst} x {n2a} = {uitkomst2} |\n')
                    print('-----------------------------------------')
                
                    break
            #delen
           
                elif choice == 'd':
                    n2a = float(input(f'Welk getal wil je delen met {uitkomst2}?: \n'))
                    uitkomst2 = uitkomst2 / n2a
                    print( f'| {uitkomst} : {n2a} = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
            #ophogen
           
                elif choice == 'e':
                    n2a = print('laden... \n')
                    uitkomst2 = uitkomst2 + 1
                    print( f'| {uitkomst} + 1.0 = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
            #verlagen
           
                elif choice == 'f':
                    n2a = print('Laden... \n')
                    uitkomst2 = uitkomst2 - 1
                    print( f'| {uitkomst} - 1.0 = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
            #verdubbelen
           
                elif choice == 'g':
                    n2a = print('Laden... \n')
                    uitkomst2 = uitkomst2 * 2
                    print( f'| {uitkomst} x 2 = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
            #halveren
            
                elif choice == 'h':
                    n2a = print('Laden... \n')
                    uitkomst2 = uitkomst2 / 2
                    print( f'| {uitkomst} : 2  = {uitkomst2} |\n')
                    print('-----------------------------------------')
                    break
           
                elif choice == 'i':
                    print('-----------------------------------------')
                    print('Fijn dat je op mij kon REKENEN.\nTot de volgende keer!')
                    print('-----------------------------------------')
                    repeat = False
            except:
                print('Sorry, dit kan niet!\n')

            

        
          

    
    
    

        






