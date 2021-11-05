import random
numero = random.randint(0, 100)
print("Introduzca el numero a adivinar")
while True:
    numero = input("Introduzca un numero entre 0 y 99 incluidos:")
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
