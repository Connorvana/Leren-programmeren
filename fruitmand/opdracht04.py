from fruitmand import fruitmand
import random

getal=int(input('Voer een getal in:'))

random = random.choice(fruitmand)

for x in range(getal):
    print(random['name'])


