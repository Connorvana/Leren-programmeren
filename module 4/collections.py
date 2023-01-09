Alle_dagen = ['maandag', 'Dinsdag', 'Woensdag' , 'Donderdag' , 'Vrijdag' , 'Zaterdag' , 'Zondag']

Alles= reversed(Alle_dagen)
Alles= tuple(Alles)
Werkdagen= reversed(Alle_dagen[0:5])
Werkdagen=tuple(Werkdagen)
weekend= reversed(Alle_dagen[5:7])
weekend= tuple(weekend)

print(Alle_dagen)
print(Alle_dagen[0:5])
print(Alle_dagen [5:7])
print(Alles)
print(Werkdagen)
print(weekend)
