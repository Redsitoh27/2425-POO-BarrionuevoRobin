# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Lista que almacenará las temperaturas de la semana
    temperaturas = []

    # Iteramos por 7 días de la semana
    for i in range(7):
        while True:
            try:
                # Solicitamos la temperatura del día i+1 (para que sea más comprensible para el usuario)
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))

                # Agregamos la temperatura a la lista
                temperaturas.append(temp)
                break  # Salimos del ciclo una vez que la entrada sea válida
            except ValueError:
                # Si se ingresa un valor incorrecto, mostramos un mensaje de error
                print("Por favor, ingrese un valor numérico válido.")

    # Retornamos la lista con todas las temperaturas ingresadas
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Calculamos y retornamos el promedio de las temperaturas
    return sum(temperaturas) / len(temperaturas)


# Programa principal
def main():
    # Mensaje de bienvenida
    print("Programa para calcular el promedio semanal del clima.")

    # Llamamos a la función que obtiene las temperaturas
    temperaturas = ingresar_temperaturas()

    # Llamamos a la función que calcula el promedio
    promedio = calcular_promedio(temperaturas)

    # Mostramos el resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")


# Ejecutar el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para ejecutar el programa