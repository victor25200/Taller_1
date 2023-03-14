x : float
y : float
g : float
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
g = float(input("Ingrese el tercer número: "))
if x > y and x > g :
    print(""+ str(x) +" es el número mayor de los 3 ingresados.")
elif y > x and y > g :
    print(""+ str(y) +" es el número mayor de los 3 ingresados.")
elif g > x and g > y : 
    print(""+ str(g) +" es el número mayor de los 3 ingresados.")