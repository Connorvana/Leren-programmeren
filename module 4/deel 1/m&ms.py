import random
choco= ('Oranje' , 'Blauw', 'Groen', 'Bruin')
Extra= []
aantal = input('Hoeveel M & Ms wilt u?')

for x in range(int(aantal)):
    m= random.choice(choco)
    Extra.append(m)

print(aantal)
print(Extra)


