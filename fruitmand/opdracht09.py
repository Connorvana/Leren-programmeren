from fruitmand import fruitmand

fruitmand.remove(
    {
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True  })


for fruit in fruitmand:
    print(fruit['color'])
    
