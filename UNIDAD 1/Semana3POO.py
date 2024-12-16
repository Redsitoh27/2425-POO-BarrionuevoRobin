class Clima:
    def __init__(self):
        # Atributo que guarda las temperaturas ingresadas por el usuario
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        # Bucle para ingresar las temperaturas de cada día de la semana
        for i in range(7):
            while True:
                try:
                    # Solicitamos la temperatura del día i+1 (más comprensible para el usuario)
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))

                    # Almacenamos la temperatura en la lista de temperaturas
                    self.temperaturas.append(temp)
                    break  # Salimos del ciclo si la temperatura es válida
                except ValueError:
                    # Si se ingresa un valor no numérico, mostramos un mensaje de error
                    print("Por favor, ingrese un valor numérico válido.")

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        # Calculamos el promedio de las temperaturas almacenadas en la lista
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
def main():
    # Mensaje de bienvenida
    print("Programa para calcular el promedio semanal del clima utilizando POO.")

    # Creamos una instancia de la clase Clima
    clima = Clima()

    # Llamamos al método de la clase para ingresar las temperaturas
    clima.ingresar_temperaturas()

    # Llamamos al método de la clase para calcular el promedio
    promedio = clima.calcular_promedio()

    # Mostramos el resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")


# Ejecutar el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para ejecutar el programa