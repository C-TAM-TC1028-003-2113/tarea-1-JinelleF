def main():
    # escribe tu código abajo de esta línea
    harina = float(input("Dame la harina en gramos: "))
    levadura = (harina / 1000) * 50
    print("Necesitas estos gramos de levadura:", round(levadura , 2))


if __name__ == '__main__':
    main()
