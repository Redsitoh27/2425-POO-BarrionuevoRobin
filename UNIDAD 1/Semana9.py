class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def add_producto(self, producto):
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [prod for prod in self.productos if prod.get_id() != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        for prod in self.productos:
            print(prod)


def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.add_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
