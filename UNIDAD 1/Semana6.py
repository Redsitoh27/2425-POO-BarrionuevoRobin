# Definimos una clase base llamada Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos privados para demostrar encapsulación
        self.__nombre = nombre
        self.__edad = edad

    # Metodo público para acceder al atributo privado __nombre
    def obtener_nombre(self):
        return self.__nombre

    # Metodo público para acceder al atributo privado __edad
    def obtener_edad(self):
        return self.__edad

    # Metodo que puede ser sobrescrito (polimorfismo)
    def descripcion(self):
        return f"{self.__nombre} tiene {self.__edad} años."

# Clase derivada llamada Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.grado = grado  # Nuevo atributo para Estudiante

    # Sobrescribimos el metodo descripcion (polimorfismo)
    def descripcion(self):
        return f"{self.obtener_nombre()} tiene {self.obtener_edad()} años y está en el grado {self.grado}."

# Clase derivada llamada Profesor que hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia  # Nuevo atributo para Profesor

    # Sobrescribimos el metodo descripcion (polimorfismo)
    def descripcion(self):
        return f"{self.obtener_nombre()} tiene {self.obtener_edad()} años y enseña {self.materia}."

# Creamos instancias de las clases
persona = Persona("Carlos", 40)
estudiante = Estudiante("María", 17, "12°")
profesor = Profesor("Luis", 35, "Matemáticas")

# Imprimimos la descripción de cada objeto
print(persona.descripcion())
print(estudiante.descripcion())
print(profesor.descripcion())

# Demostración del uso de encapsulación
print("\nDemostración de encapsulación:")
print(f"Nombre del estudiante: {estudiante.obtener_nombre()}")
print(f"Edad del profesor: {profesor.obtener_edad()}")
