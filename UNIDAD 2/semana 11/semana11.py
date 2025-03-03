import json


class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, product_id, product_nombre, product_cantidad, product_precio):
        self.id_producto = product_id
        self.nombre = product_nombre
        self.cantidad = product_cantidad
        self.precio = product_precio

    # Método para actualizar la cantidad del producto
    def actualizar_cantidad(self, nueva_cant):
        self.cantidad = nueva_cant

    # Método para actualizar el precio del producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para obtener la información del producto en formato diccionario
    def obtener_info(self):
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }


class Inventario:
    # Clase que representa el inventario de la tienda
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por su ID
        self.cargar_desde_archivo()  # Cargar inventario desde archivo al iniciar

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    # Método para eliminar un producto del inventario por su ID
    def eliminar_producto(self, product_id):
        if product_id in self.productos:
            del self.productos[product_id]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, product_id, nueva_cant=None, nuevo_precio=None):
        if product_id in self.productos:
            if nueva_cant is not None:
                self.productos[product_id].actualizar_cantidad(nueva_cant)
            if nuevo_precio is not None:
                self.productos[product_id].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    # Método para buscar productos por nombre
    def buscar_producto(self, product_nombre):
        return [producto.obtener_info() for producto in self.productos.values() if
                producto.nombre.lower() == product_nombre.lower()]

    # Método para mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        return [producto.obtener_info() for producto in self.productos.values()]

    # Método para guardar el inventario en un archivo JSON
    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({clave: producto.obtener_info() for clave, producto in self.productos.items()}, archivo, indent=4)

    # Método para cargar el inventario desde un archivo JSON
    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {clave: Producto(clave, p["Nombre"], p["Cantidad"], p["Precio"]) for clave, p in
                                  datos.items()}
        except FileNotFoundError:
            self.productos = {}


# Bloque principal del programa
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicitar datos para agregar un nuevo producto
            prod_id = input("ID del producto: ")
            prod_nombre = input("Nombre: ")
            prod_cantidad = int(input("Cantidad: "))
            prod_precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(prod_id, prod_nombre, prod_cantidad, prod_precio))
        elif opcion == "2":
            # Solicitar ID del producto a eliminar
            prod_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(prod_id)
        elif opcion == "3":
            # Solicitar ID del producto a actualizar y nuevos valores opcionales
            prod_id = input("ID del producto a actualizar: ")
            cantidad_nueva = input("Nueva cantidad (deje vacío si no desea cambiar): ")
            precio_nuevo = input("Nuevo precio (deje vacío si no desea cambiar): ")
            cantidad_nueva = int(cantidad_nueva) if cantidad_nueva else None
            precio_nuevo = float(precio_nuevo) if precio_nuevo else None
            inventario.actualizar_producto(prod_id, cantidad_nueva, precio_nuevo)
        elif opcion == "4":
            # Solicitar nombre del producto a buscar
            prod_nombre = input("Nombre del producto a buscar: ")
            print(inventario.buscar_producto(prod_nombre))
        elif opcion == "5":
            # Mostrar todos los productos del inventario
            print(inventario.mostrar_inventario())
        elif opcion == "6":
            # Salir del programa
            break
        else:
            print("Opción inválida. Intente de nuevo.")
