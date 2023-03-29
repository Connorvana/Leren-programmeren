def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

while True:
    keuze = input("Wat wilt u doen? \n(A) Getallen Optellen \n(B) Getallen Aftrekken \n(C) Getallen Vermenigvuldigen \n(D) Getallen Delen \n(E) Getal Ophogen \n(F) Getal Verlagen \n(G) Getal Verdubbelen \n(H) Getal Halveren \n(I) Helemaal Stoppen\n").lower()

    if keuze == 'a':
        n1= float(input('welk getal optellen: '))
        n2= float(input(f'Welk getal optellen bij {n1}: '))
        uitkomst = addition(n1, n2)
        print(f'{n1} + {n2} = {uitkomst}\n')
    
    elif keuze == "b":
        n1 = float(input("Welk getal aftrekken: "))
        n2 = float(input(f"Welk getal aftrekken bij {n1}: "))
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}\n")

    elif keuze == "c":
        n1 = float(input("Welk getal vermenigvuldigen: "))
        n2 = float(input(f"Welk getal vermenigvuldigen bij {n1}: "))
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}\n")

    elif keuze == "d":
        n1 = float(input("Welk getal delen: "))
        n2 = float(input(f"Welk getal delen bij {n1}: "))
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}\n")

    elif keuze == "e":
        n1 = float(input("Getal ophogen: "))
        n2 = 1
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}\n")

    elif keuze == "f":
        n1 = float(input("Getal verlagen: "))
        n2 = 1
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}\n")

    elif keuze == "g":
        n1 = float(input("Getal verdubbelen: "))
        n2 = 2
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}\n")

    elif keuze == "h":
        n1 = float(input("Getal halveren: "))
        n2 = 2
        uitkomst = division(n1, n2)
        print(f'{n1} : {n2} = {uitkomst}')
    
    elif keuze == 'i':
        print('Dan stoppen we hier.')
        break   




