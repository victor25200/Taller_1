# Taller_1
## Punto 1:
Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).
[![image.png](https://i.postimg.cc/0Ns0V0cx/image.png)](https://postimg.cc/nX3mz7yw)
## Punto 4:
Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
## Codigo:
```python
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
```
## Programa Funcionando:
[![image.png](https://i.postimg.cc/d1xrzkMQ/image.png)](https://postimg.cc/HcbrMLsF)

[![image.png](https://i.postimg.cc/cLBDPmFs/image.png)](https://postimg.cc/87sB6h83)
## Punto 7:
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

- El promedio
- La mediana
- El promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operadores)
- Ordenar los números de forma ascendente
- Ordenar los numeros de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

## Codigo:
```python
a:float
b:float 
c:float
d:float
e:float
m1:float
m2:float
m3:float
m4:float
m5:float
promedio : float
potencia : float
promult : float 
raizm : float 
a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese el segundo número real: "))
c = float(input("Ingrese el tercer número real: "))
d = float(input("Ingrese el cuarto número real: "))
e = float(input("Ingrese el quinto número real: "))
print ("los números ingresados son ("+ str(a)+ ", "+ str(b)+", "+ str(c)+ ", "+str(d)+ ", "+str(e) +")" )
promedio = (a+b+c+d+e)/5
print("El promedio es "+ str(promedio))
if a<b and a<c and a<d and a<e:
    m1=a
    if b<c and b<d and b<e:
       m2=b
       if c<d and c<e:
          m3=c
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif c<b and c<d and c<e:
       m2=c
       if b<d and b<e:
          m3=b
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<b and d<c and d<e:
       m2=d
       if b<c and b<e:
          m3=b
          if c<e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<b and e<c and e<d:
       m2=e
       if b<c and b<d:
          m3=b
          if b<d:
              m4=b ; m5=d
          else : 
             m4=d ; m5=b 
elif b<a and b<c and b<d and b<e:
    m1=b
    if a<c and a<d and a<e:
       m2=a 
       if c<d and c<e:
          m3=c
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif c<a and c<d and c<e:
       m2=c
       if a<d and a<e:
          m3=a
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<a and d<c and d<e:
       m2=d
       if a<c and a<e:
          m3=a
          if c<e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<a and e<c and e<d:
       m2=e
       if a<c and a<d:
          m3=a
          if a<d:
              m4=a ; m5=d 
          else : 
             m4=d ; m5=a
if c<b and c<a and c<d and c<e:
    m1=c
    if b<a and b<d and b<e:
       m2=b 
       if a<d and a<e:
          m3=a
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif a<b and a<d and a<e:
       m2=a
       if b<d and b<e:
          m3=b
          if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<b and d<a and d<e:
       m2=d
       if b<a and b<e:
          m3=b
          if a<e:
              m4=a ; m5=e 
          else : 
             m4=e ; m5=a 
    elif e<b and e<a and e<d:
       m2=e
       if b<a and b<d:
          m3=b
          if b<d:
              m4=b ; m5=d 
          else : 
             m4=d ; m5=b
if d<b and d<c and d<a and d<e:
    m1=d
    if b<c and b<a and b<e:
       m2=b 
       if c<a and c<e:
          m3=c
          if a<e:
              m4=a ; m5=e 
          else : 
             m4=e ; m5=a 
    elif c<b and c<a and c<e:
       m2=c
       if b<a and b<e:
          m3=b
          if d<e:
            if d<e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif a<b and a<c and a<e:
       m2=a
       if b<c and b<e:
          m3=b
          if c<e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<b and e<c and e<a:
       m2=e
       if b<c and b<a:
          m3=b
          if b<a:
              m4=b ; m5=a 
          else : 
             m4=a ; m5=b
if e<b and e<c and e<d and e<a:
    m1=e
    if b<c and b<d and b<a:
       m2=b 
       if c<d and c<a:
          m3=c
          if d<a:
              m4=d ; m5=a 
          else : 
             m4=a ; m5=d 
    elif c<b and c<d and c<a:
       m2=c
       if b<d and b<a:
          m3=b
          if d<a:
              m4=d ; m5=a 
          else : 
             m4=a ; m5=d 
    elif d<b and d<c and d<a:
       m2=d
       if b<c and b<a:
          m3=b
          if c<a:
              m4=c ; m5=a 
          else : 
             m4=a ; m5=c 
    elif a<b and a<c and a<d:
       m2=a
       if b<c and b<d:
          m3=b
          if b<d:
              m4=b ; m5=d 
          else : 
             m4=d ; m5=b  
potencia = m5**m1
promult= (m1*m2*m3*m4*m5)**(1/5)
raizm = (m1)**(1/2)
print("la mediana es "+ str(m3))
print("El promedio multilpicativo es "+ str(promult))
print("los numeros en orden descendente son ("+ str(m5)+ ", "+ str(m4)+", "+ str(m3)+ ", "+str(m2)+ ", "+str(m1) +")") 
print("los numeros en orden ascendente son ("+ str(m1)+ ", "+ str(m2)+", "+ str(m3)+ ", "+str(m4)+ ", "+str(m5) +")") 
print("la potencia del mayor numero elvado el menor numero  es "+ str(potencia))
print("la raiz del menor número es " + str (raizm)) 
```
## Programa Funcionando:
[![image.png](https://i.postimg.cc/fWPVZQVL/image.png)](https://postimg.cc/14pmcTch)
## Punto 9:
Escriba un programa que reciba el nombre en minúsculas de un país de America y devuelva la ciudad capital, si el país no pertenece al continente debe arrojar pais no identificado
## Codigo:
```python
pais = input("ingrese un país de america en minisculas ")
char1 = "antigua y barbuda"; char2 = "argentina"; char3 = "bahamas "
char4 = "barbados "; char5 = "belice"; char6 = "bolivia"
char7 = "brasil"; char8 = "canada"; char9 = "chile"
char10 = "colombia"; char11 = "costa rica"; char12 = "cuba "
char13 = "dominica"; char14 = "ecuador"; char15 = "el salvador"
char16 = "estados unidos "; char17 = "granada"; char18 = "guatemala"
char19 = "guyana"; char20 = "haiti"; char21 = "honduras"
char22 = "jamaica"; char23 = "mexico "; char24 = "nicaragua"
char25 = "panama"; char26 = "paraguay"; char27 = "peru"
char28 = "republica dominicana"; char29 = "san cristibal y nieves"
char30 = "san vicente y las granadinas "; char31 = "santa lucia"
char32 = "surinam"; char33 = "trinidad y tovago "
char34 = "uruguay"; char35 = "venezuela"
if pais == char1 :
    print("la capital de "  + str(pais)+ " es saint john")
elif pais == char2 :
    print("la capital de "  + str(pais)+ " es buenos aires ")
elif pais == char3 :
    print("la capital de "  + str(pais)+ " es nasau")
elif pais == char4 :
    print("la capital de "  + str(pais)+ " es bridgertown")
elif pais == char5 :
    print("la capital de "  + str(pais)+ " es belmopan")
elif pais == char6 :
    print("la capital de "  + str(pais)+ " es sucre")
elif pais == char7 :
    print("la capital de "  + str(pais)+ " es brasilia")
elif pais == char8 :
    print("la capital de "  + str(pais)+ " es ottawa")
elif pais == char9 :
    print("la capital de "  + str(pais)+ " es santiago")
elif pais == char10 :
    print("la capital de "  + str(pais)+ " es bogota")
elif pais == char11 :
    print("la capital de "  + str(pais)+ " es san jose")
elif pais == char12 :
    print("la capital de "  + str(pais)+ " es la habana")
elif pais == char13 :
    print("la capital de "  + str(pais)+ " es roseau")
elif pais == char14 :
    print("la capital de "  + str(pais)+ " es quito")
elif pais == char15 :
    print("la capital de "  + str(pais)+ " es san salvador")
elif pais == char16 :
    print("la capital de "  + str(pais)+ " es washintown")
elif pais == char17 :
    print("la capital de "  + str(pais)+ " es saint george")
elif pais == char18 :
    print("la capital de "  + str(pais)+ " es ciudad de guatemala")
elif pais == char19 :
    print("la capital de "  + str(pais)+ " es georgetown")
elif pais == char20 :
    print("la capital de "  + str(pais)+ " es puerto principe")
elif pais == char21 :
    print("la capital de "  + str(pais)+ " es tegucigalpa")
elif pais == char22 :
    print("la capital de "  + str(pais)+ " es kinston")
elif pais == char23 :
    print("la capital de "  + str(pais)+ " es ciudad de mexico")
elif pais == char24 :
    print("la capital de "  + str(pais)+ " es managua")
elif pais == char25 :
    print("la capital de "  + str(pais)+ " es ciudad de panama")
elif pais == char26 :
    print("la capital de "  + str(pais)+ " es asunción ")
elif pais == char27 :
    print("la capital de "  + str(pais)+ " es lima")
elif pais == char28 :
    print("la capital de "  + str(pais)+ " es santo domingo")
elif pais == char29 :
    print("la capital de "  + str(pais)+ " es basseterre")
elif pais == char30 :
    print("la capital de "  + str(pais)+ " es kingstown")
elif pais == char31 :
    print("la capital de "  + str(pais)+ " es castris")
elif pais == char32 :
    print("la capital de "  + str(pais)+ " es paramaribo")
elif pais == char33 :
    print("la capital de "  + str(pais)+ " es purto españa")
elif pais == char34 :
    print("la capital de "  + str(pais)+ " es montevideo ")
elif pais == char35 :
    print("la capital de "  + str(pais)+ " es caracas")
else:
    print("país no identificado")
```
## Programa Funcionando:
[![image.png](https://i.postimg.cc/FKZ4CGgQ/image.png)](https://postimg.cc/Y4hZh6sX)
## Diagrama de flujo .
[![image.png](https://i.postimg.cc/5NhgDVnw/image.png)](https://postimg.cc/YhxQmJc9)
