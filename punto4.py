# declaro las variables 
a: float
b: float
# Pido que ingresen un numero y despues el otro
a = float(input("ingrese el primer número " ))
b = float(input("ingrese el segundo número"))
# Imprime los numeros ingrasados
print("el primer número es "+ str(a))
print("el segundo número es "+str(b) )
# Si el residuo de a entre b es cero se imprime que el primero es multiplo
# del sugundo sino se imprime el primero no es multiplo del segundo
if a%b==0:
  print("El primer numero es multiplo del segundo")
else:
  print("El primer numero no es multiplo del segundo")