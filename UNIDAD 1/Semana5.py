import math


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado dado su lado.

    Parámetros:
    lado (float): El tamaño de un lado del cuadrado.

    Retorna:
    float: El área del cuadrado.
    """
    return lado ** 2


# Función para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return (base * altura) / 2


# Función principal que ejecuta el programa
def main():
    # Variables para los datos de entrada
    figura = input("¿Qué figura deseas calcular el área (cuadrado, círculo, triángulo)? ").lower()

    # Variable booleana para verificar si la entrada es válida
    entrada_valida = False
    area = 0.0  # Inicializa el área a 0

    if figura == "cuadrado":
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        entrada_valida = True
    elif figura == "círculo":
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        entrada_valida = True
    elif figura == "triángulo":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        entrada_valida = True
    else:
        print("Figura no válida, por favor elige entre cuadrado, círculo o triángulo.")

    # Si la entrada es válida, muestra el resultado
    if entrada_valida:
        print(f"El área del {figura} es: {area:.2f} unidades cuadradas.")
    else:
        print("No se pudo calcular el área debido a una entrada inválida.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
