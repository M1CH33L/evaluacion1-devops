# Relleno para el repositorio porque se me hizo mas facil que usar la 


def funcion_relleno(nada: int = 0):
    """
    Esta funcion esta creada por mi, no hace nada util ademas de rellenar este .py para el repo
    igualmente puedes pasarle un argumento tipo int que no aporta en mucho a nada
    """

    if nada == 0:
        print("Tu pusiste el 0 como argumento?")
        eleccion = input("(y/n)")
        eleccion = eleccion.lower().strip()
        if eleccion == "y":
            print("Por que, de toda la infinidad de numeros, tenias que elegir el 0? no te gusta mas el 3? o que se yo, el 4 incluso, pero noooo, tenias que poner el 0.")
        elif eleccion == "n":
            print("Bueno, gracias por no poner ningun argumento, hubiera simplemente dejado una funcion vacia.")
        else: 
            print(f"{eleccion} no estaba entre las opciones, preferire ignorar este error ;)") #El hotfix fue que originalmente trataba un poco mal al usuario xd
            print(f"Claramente el input te daba DOS opciones, y para si, n para no, pero claro, el listillo tenia que poner {eleccion} para ver si pense en esa posibilidad.")
    elif nada == 3:
        print("El 3 no es particularmente el mejor numero que hay, claro, tiene las mejores multiplicaciones, pero siento que intenta ser mas importante de lo que es")
        print("como castigo, un bucle infinito")
        while True:
            print("Nunca podras salir\n")
    elif nada == 42:
        print("Por que todos los programadores estan obsesionados con el 42?")
    elif abs(nada) < 100:
        print("""Muchas gracias por poner un argumento (que no sea el 0)
realmente se agradece que alguien se tome el tiempo con mi funcion
como regalo (y por que el numero no es tan grande) imprimire gracias una cantidad de veces equivalente al valor absoluto de tu argumento
        """)
        print("gracias "*abs(nada))
    else:
        print("Gracias por poner un argumento, pero al ser su valor absoluto mayor a 100 pues solo te dire gracias UNA vez, no hay que ser avariciosos en esta vida")
        print("Gracias.")

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if args:
        try:
            numero = int(args[0])
            funcion_relleno(numero)
        except ValueError:
            print("Error: El argumento debe ser un número entero.")
    else:
        funcion_relleno(0)
