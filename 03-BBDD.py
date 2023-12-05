import mysql.connector

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS juegos (
            codigo INT,
            nombre VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            compania INT NOT NULL''')
        self.conn.commit()

    def agregar_juego(self, codigo, nombre, cantidad, precio, imagen, compania):
        self.cursor.execute(f"SELECT * FROM juegos WHERE codigo = {codigo}")
        juego_existe = self.cursor.fetchone()
        if juego_existe:
            return False
        sql = f"INSERT INTO juegos (codigo, nombre, cantidad, precio, imagen_url, compania) VALUES ({codigo}, '{nombre}', {cantidad}, {precio}, '{imagen}', {compania})"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def consultar_juego(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM juegos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def modificar_juego(self, codigo, nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_imagen, nueva_compania):
        sql = f"UPDATE juegos SET nombre = '{nuevo_nombre}', cantidad = {nueva_cantidad}, precio = {nuevo_precio}, imagen_url = '{nueva_imagen}', compania = {nueva_compania} WHERE codigo = {codigo}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_juego(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        juego = self.consultar_juego(codigo)
        if juego:
            print("-" * 40)
            print(f"Código.....: {juego['codigo']}")
            print(f"Nombre: {juego['nombre']}")
            print(f"Cantidad...: {juego['cantidad']}")
            print(f"Precio.....: {juego['precio']}")
            print(f"Imagen.....: {juego['imagen_url']}")
            print(f"Compania..: {juego['compania']}")
            print("-" * 40)
        else:
            print("Juego no encontrado.")


    def listar_juegos(self):
    # Mostramos en pantalla un listado de todos los productos en la tabla
        self.cursor.execute("SELECT * FROM juegos")
        juegos = self.cursor.fetchall()
        print("-" * 40)
        for juego in juegos:
            print(f"Código.....: {juego['codigo']}")
            print(f"Nombre: {juego['nombre']}")
            print(f"Cantidad...: {juego['cantidad']}")
            print(f"Precio.....: {juego['precio']}")
            print(f"Imagen.....: {juego['imagen_url']}")
            print(f"Compania..: {juego['compania']}")
            print("-" * 40)

    def eliminar_juego(self, codigo):
    # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM juegos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

# Programa principal
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
# Agregamos productos a la tabla
catalogo.agregar_juego("1", 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', "101")
catalogo.agregar_juego("2", 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', "102")
catalogo.agregar_juego("3", 'Monitor LED', 5, 25000, 'monitor.jpg', "102")

# Consultamos un producto y lo mostramos
cod_juego = input("Ingrese el código del juego: ")
juego = catalogo.consultar_juego(cod_juego)
if juego:
    print(f"Juego encontrado: {juego['codigo']} - {juego['nombre']}")
else:
    print(f'Juego {cod_juego} no encontrado.')

# Modificamos un producto y lo mostramos
# catalogo.mostrar_producto(1)
# catalogo.modificar_producto(1, 'Teclado mecánico', 20, 34000, 'tecmec.jpg', 106)
# catalogo.mostrar_producto(1)

# Listamos todos los productos
# catalogo.listar_productos()

# Eliminamos un producto
# catalogo.eliminar_producto(2)
# catalogo.listar_productos()


