def main():
    # escribe tu código abajo de esta línea
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    costo = 0.8 * (mensajes + megas + minutos)
    print("El costo mensual es:",costo)


if __name__ == '__main__':
    main()
