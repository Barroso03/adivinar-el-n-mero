import random
numero = random.randint(0, 100)
print("Introduzca el número a adivinar")
while True:
    numero = input("Introduzca un número entre 0 y 99 incluidos:")
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
print("intente encontrar el número a adivinar")
while True:
    numero = input("Introduzca el número a adivinar") 
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
    while True:
        intento = input("Introduzca un número entre 0 y 99 incluidos:")
        try:
            numero = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
if intento < numero:
   print("Demasiado pequeño")
elif intento > numero:
   print("Demasiado grande")
else:
   print("Victoria!")
