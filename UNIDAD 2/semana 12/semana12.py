import json


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

    def to_dict(self):
        return {"titulo": self.info[0], "autor": self.info[1], "categoria": self.categoria, "isbn": self.isbn}

    @staticmethod
    def from_dict(data):
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.cargar_libros()

    def guardar_libros(self):
        with open("libros.json", "w") as f:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, f, indent=4)

    def cargar_libros(self):
        try:
            with open("libros.json", "r") as f:
                libros_cargados = json.load(f)
                self.libros = {isbn: Libro.from_dict(datos) for isbn, datos in libros_cargados.items()}
        except FileNotFoundError:
            self.libros = {}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            self.guardar_libros()
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya está en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print("Libro eliminado correctamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Este ID de usuario ya está registrado.")

    def eliminar_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print("Usuario eliminado correctamente.")
        else:
            print("El usuario no existe.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.guardar_libros()
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    self.guardar_libros()
                    print(f"Libro '{libro.info[0]}' devuelto correctamente.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, clave):
        encontrados = [libro for libro in self.libros.values() if
                       clave.lower() in libro.info[0].lower() or clave.lower() in libro.info[
                           1].lower() or clave.lower() in libro.categoria.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID de usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))

        elif opcion == "4":
            user_id = input("ID del usuario a eliminar: ")
            biblioteca.eliminar_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            clave = input("Ingrese título, autor o categoría del libro: ")
            biblioteca.buscar_libro(clave)

        elif opcion == "8":
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
