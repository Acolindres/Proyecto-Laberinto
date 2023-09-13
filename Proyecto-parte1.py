import readchar
print("Proyecto Inntegrador parte 1")
print("Bienvenido al laberinto")
nombre = "J"
print(f'Hola jugador, {nombre}! Estas listo para esta aventura?')

# Proyecto integrador parte 2


def main():
    while True:
        char = readchar.readkey()
        print(f"Tecla Pulsada: {char}")
        if char == "\x1b[A":  # Codigo de la tecla (↑)
            print("Pulsaste UP")
            print("Saliendo del bucle")
            break


if __name__ == "_main_":
    main()

