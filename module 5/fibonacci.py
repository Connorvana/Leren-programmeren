def fibonacci(getal):
 a,b= 0, 1
 lijst=[]
 
 for i in range(getal):
   lijst.append(a)
   a, b = b, a + b
 return lijst

print(fibonacci(25))