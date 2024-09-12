# Clase Libro, con atributos inmutables almacenados en una tupla
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable que almacena título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.info[0]} por {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario, con un ID único y una lista de libros prestados
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}"

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(libro)
        else:
            print(f"{self.nombre} no tiene libros prestados.")

# Clase Biblioteca que gestiona los libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios para asegurar unicidad
        self.historial_prestamos = []

    # Añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido correctamente.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está registrado.")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro_eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro_eliminado.info[0]}' eliminado.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {usuario.user_id} ya está registrado.")

    # Dar de baja un usuario
    def dar_de_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario_id)
            print(f"Usuario con ID {usuario_id} ha sido dado de baja.")
        else:
            print(f"Usuario con ID {usuario_id} no está registrado.")

    # Prestar un libro
    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro_prestado = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro_prestado)
            self.historial_prestamos.append((usuario.user_id, isbn))
            print(f"Libro '{libro_prestado.info[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"El libro con ISBN {isbn} no está disponible.")

    # Devolver un libro
    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print(f"El libro con ISBN {isbn} no estaba prestado a {usuario.nombre}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, termino_busqueda):
        encontrados = []
        for libro in self.libros_disponibles.values():
            if termino_busqueda.lower() in libro.info[0].lower() or \
               termino_busqueda.lower() in libro.info[1].lower() or \
               termino_busqueda.lower() in libro.categoria.lower():
                encontrados.append(libro)
        if encontrados:
            print(f"Libros encontrados para '{termino_busqueda}':")
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros para '{termino_busqueda}'.")

# Pruebas del sistema
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("El Cienfuegos", "Jorge Negrete", "Clásico", "19745")
libro2 = Libro("La Ileada", "Homero", "Distopía", "67890")
libro3 = Libro("Las cruces sobre el agua", "Joaquín Gallegos Lara", "Novela", "54321")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear algunos usuarios
usuario1 = Usuario("Ronnal Montoya", "001")
usuario2 = Usuario("Patricia Barzola", "002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("19745", usuario1)
biblioteca.prestar_libro("67890", usuario2)

# Listar libros prestados
usuario1.listar_libros_prestados()
usuario2.listar_libros_prestados()

# Devolver libros
biblioteca.devolver_libro("19745", usuario1)

# Buscar libros
biblioteca.buscar_libros("Negrete")
biblioteca.buscar_libros("Novela")
