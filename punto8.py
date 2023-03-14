a : float
a = float(input("Ingrese la frecuencia en Hz sin notación científica: "))
if a < 30 * 10**3 :
    print('La frecuencia que ingreso se encuentra en la región "Muy Baja Frecuencia"')
elif a >= 30 * 10**3 and a < 650 * 10**3 :
    print('La frecuencia que ingreso se encuentra en la región "Onda Larga"')
elif a >= 650 * 10**3 and a <  1.7 * 10**6 :
    print('La frecuencia que ingreso se encuentra en la región "Onda Media"')
elif a >=  1.7 * 10**6 and a < 30 * 10**6:
    print('La frecuencia que ingreso se encuentra en la región "Onda Corta"')
elif a >= 30 * 10**6 and a < 300 * 10**6 :
    print('La frecuencia que ingreso se encuentra en la región "Muy Alta Frecuencia"')
elif  a >= 300 * 10**6 and a < 3 * 10**8 :
    print('La frecuencia que ingreso se encuentra en la región "Ultra Alta Frecuencia"')
elif a >= 3 * 10**8 and a < 300 * 10**9 :
    print('La frecuencia que ingreso se encuentra en la región "Microondas"')
elif a >= 300 * 10**9 and a < 6 * 10**12 :
     print('La frecuencia que ingreso se encuentra en la región "Infrarrojo lejano/submilimétrico"')
elif a >= 6 * 10**12 and a < 120 * 10**12 :
    print('La frecuencia que ingreso se encuentra en la región "Infrarrojo medio"')
elif a >= 120 * 10**12 and a < 384 * 10**12 :
    print('La frecuencia que ingreso se encuentra en la región "Infrarrojo cercano"')
elif a >= 384 * 10**12 and a < 7.89 * 10**14 :
    print('La frecuencia que ingreso se encuentra en la región "Espectro Visible"')
elif a >= 7.89 * 10**14 and a < 1.5 * 10**15 :
    print('La frecuencia que ingreso se encuentra en la región "Ultravioleta cercano"')
elif a >= 1.5 * 10**15 and a < 30 * 10**15 :
    print('La frecuencia que ingreso se encuentra en la región "Ultravioleta extremo"')
elif a >= 30 * 10**15 and a < 30 * 10**18 :
    print('La frecuencia que ingreso se encuentra en la región "Rayos X"')
elif a >= 30 * 10**18 :
    print('La frecuencia que ingreso se encuentra en la región "Rayos gamma"')
else:
    print("la onda ingresada esta mal")