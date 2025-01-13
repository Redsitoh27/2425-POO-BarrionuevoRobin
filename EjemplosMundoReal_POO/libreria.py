# Clase Producto
class Producto:
    """
    Clase que representa un producto (en este caso, un libro).
    Atributos:
        - nombre: El nombre del producto.
        - precio: El precio del producto.
    Métodos:
        - mostrar_info: Muestra la información del producto (nombre y precio).
    """
    def __init__(self, nombre, precio):
        """
        Inicializa un producto con su nombre y precio.
        """
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        """
        Devuelve la información del producto en un formato legible.
        """
        return f"Producto: {self.nombre}, Precio: ${self.precio}"


# Clase Cliente
class Cliente:
    """
    Clase que representa a un cliente de la tienda.
    Atributos:
        - nombre: El nombre del cliente.
        - correo: El correo del cliente.
        - reservas: Una lista que contiene los productos reservados por el cliente.
    Métodos:
        - realizar_reserva: Permite al cliente realizar una reserva de un producto.
        - mostrar_reservas: Muestra los productos reservados por el cliente.
    """
    def __init__(self, nombre, correo):
        """
        Inicializa un cliente con su nombre, correo y una lista vacía de reservas.
        """
        self.nombre = nombre
        self.correo = correo
        self.reservas = []

    def realizar_reserva(self, producto):
        """
        Permite que el cliente realice una reserva de un producto.
        El producto se agrega a la lista de reservas del cliente.
        """
        self.reservas.append(producto)
        print(f"{self.nombre} ha reservado el libro: {producto.nombre}")

    def mostrar_reservas(self):
        """
        Muestra todos los productos que el cliente ha reservado.
        Si no hay reservas, muestra un mensaje indicando que no tiene reservas.
        """
        if self.reservas:
            print(f"Reservas de {self.nombre}:")
            for reserva in self.reservas:
                print(f"- {reserva.nombre} (${reserva.precio})")
        else:
            print(f"{self.nombre} no tiene reservas.")


# Clase Tienda
class Tienda:
    """
    Clase que representa una tienda con productos disponibles para ser reservados.
    Atributos:
        - productos: Lista de productos disponibles en la tienda.
    Métodos:
        - agregar_producto: Permite agregar un nuevo producto a la tienda.
        - mostrar_productos: Muestra todos los productos disponibles en la tienda.
        - realizar_reserva: Permite que un cliente realice una reserva de un producto.
    """
    def __init__(self):
        """
        Inicializa la tienda con una lista vacía de productos.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto a la tienda.
        """
        self.productos.append(producto)
        print(f"Producto agregado: {producto.nombre}")

    def mostrar_productos(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        print("Productos disponibles en la tienda:")
        for producto in self.productos:
            print(producto.mostrar_info())

    def realizar_reserva(self, cliente, producto_nombre):
        """
        Permite que un cliente realice una reserva de un producto específico.
        Busca el producto por nombre y si lo encuentra, realiza la reserva.
        Si el producto no está disponible, muestra un mensaje de error.
        """
        for producto in self.productos:
            if producto.nombre == producto_nombre:
                cliente.realizar_reserva(producto)
                return
        print(f"El producto {producto_nombre} no está disponible.")


# Crear instancias de la tienda, productos y clientes

# Crear una tienda
tienda = Tienda()

# Crear algunos productos (libros)
libro1 = Producto("Cien Años de Soledad", 25.00)
libro2 = Producto("El Quijote", 18.50)

# Agregar productos a la tienda
tienda.agregar_producto(libro1)
tienda.agregar_producto(libro2)

# Crear algunos clientes
cliente1 = Cliente("Juan Pérez", "juan@email.com")
cliente2 = Cliente("Ana Gómez", "ana@email.com")

# Mostrar los productos disponibles en la tienda
tienda.mostrar_productos()

# Realizar algunas reservas
tienda.realizar_reserva(cliente1, "Cien Años de Soledad")
tienda.realizar_reserva(cliente2, "El Quijote")

# Mostrar las reservas de los clientes
cliente1.mostrar_reservas()
cliente2.mostrar_reservas()
