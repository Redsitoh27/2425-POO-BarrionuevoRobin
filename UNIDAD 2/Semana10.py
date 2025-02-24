import os
import json


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            print("No se encontró el archivo de inventario. Creando uno nuevo...")
            return

        try:
            with open(self.ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    self.productos = json.loads(contenido)
                    print("Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al leer el archivo de inventario. Puede estar corrupto.")
        except PermissionError:
            print("Error: No tienes permiso para acceder al archivo de inventario.")

    def guardar_en_archivo(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                json.dump(self.productos, archivo, indent=4)
                print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, name, cantid):
        """Agrega un producto al inventario."""
        if name in self.productos:
            self.productos[name] += cantid
        else:
            self.productos[name] = cantid
        print(f"Producto '{name}' agregado/actualizado con éxito.")
        self.guardar_en_archivo()

    def eliminar_producto(self, name):
        """Elimina un producto del inventario."""
        if name in self.productos:
            del self.productos[name]
            print(f"Producto '{name}' eliminado con éxito.")
            self.guardar_en_archivo()
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra el inventario actual."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto, cantid in self.productos.items():
                print(f"- {producto}: {cantid}")


# Ejecución del sistema
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
