# XYLA - Calculadora de áreas
# Copia este código en Visual Studio Code, guárdalo como main.py y ejecútalo.

def calcular_area(figura, *datos):
    if figura == "cuadrado":
        lado = datos[0]
        return lado ** 2
    elif figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * (radio ** 2)
    elif figura == "trapecio":
        base_mayor, base_menor, altura = datos
        return ((base_mayor + base_menor) * altura) / 2
    elif figura == "rombo":
        diagonal1, diagonal2 = datos
        return (diagonal1 * diagonal2) / 2
    elif figura == "paralelogramo":
        base, altura = datos
        return base * altura
    else:
        return "Figura no válida"


def menu():
    figuras = ["cuadrado", "rectangulo", "triangulo", "circulo",
               "trapecio", "rombo", "paralelogramo"]
    print("Calculadora de áreas")
    print("Selecciona una figura:")
    for numero, nombre in enumerate(figuras, start=1):
        print(str(numero) + ". " + nombre.capitalize())

    opcion = int(input("Opción: "))
    figura = figuras[opcion - 1]

    if figura == "cuadrado":
        datos = [float(input("Lado: "))]
    elif figura == "circulo":
        datos = [float(input("Radio: "))]
    elif figura == "trapecio":
        datos = [float(input("Base mayor: ")),
                 float(input("Base menor: ")),
                 float(input("Altura: "))]
    elif figura == "rombo":
        datos = [float(input("Diagonal mayor: ")),
                 float(input("Diagonal menor: "))]
    else:
        datos = [float(input("Base: ")), float(input("Altura: "))]

    area = calcular_area(figura, *datos)
    print("El área del " + figura + " es: " + str(area))


if __name__ == "__main__":
    menu()
