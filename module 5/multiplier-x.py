def multi(num):
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')


num = int(input('Van welk getal wil je de tafel zien?:\n'))

multi(num)
