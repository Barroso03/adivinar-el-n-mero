if __name__ == '__main__':
    jugar()
def jugar():
    minimo, maximo = decidir_limites()
    while True:
        numero = pedir_numero_incognita()
        jugar_una_partida(numero,minimo,maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

