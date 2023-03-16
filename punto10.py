a = float
b = float
c = float
d = float
e = float
a = 299792458 # Velocidad de la luz
c = 343 # Velocidad del sonido en el aire
d = 141.111 # Velocidad vehículo comercial más veloz
e = 10.44 # Velocidad Usain Bolt
b = float(input("ingrese el valor de la distancia en m: "))
tiempo1 = b / a
tiempo2 = b / c
tiempo3 = b / d
tiempo4 = b / e
print("la luz tarda "+str(tiempo1)+" segundos en recorrer "+str(b)+" metros")
print("El sonido tarda "+str(tiempo2)+" segundos en recorrer "+str(b)+" metros en el aire")
print("El vehículo comercial más rápido tardaría "+str(tiempo3)+" segundos en recorrer "+str(b)+" metros")
print("Usain Bolt tardaría "+str(tiempo4)+" segundos en recorrer "+str(b)+" metros")