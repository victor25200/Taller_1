a: float
b: float
a = float(input("ingrese el primer número " ))
b = float(input("ingrese el segundo número"))
print("el primer número es "+ str(a))
print("el segundo número es "+str(b) )
if a%b==0:
  print("El primer numero es multiplo del segundo")
else:
  print("El primer numero no es multiplo del segundo")