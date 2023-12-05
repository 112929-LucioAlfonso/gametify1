class Catalogo:
    juegos = []

def agregar_juego(self, codigo, nombre, cantidad, precio, imagen, compania):
    if self.consultar_juego(codigo):
        return False
    nuevo_juego = {
            'codigo': codigo,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'compania': compania
    }
    self.juegos.append(nuevo_juego)
    return True

def consultar_juego(self, codigo):
    for juego in self.juegos:
        if juego['codigo'] == codigo:
            return juego
    return False

def modificar_juego(self, codigo, nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_imagen, nueva_compania):
    for juego in self.juego:
        if  juego['codigo'] == codigo:
            juego['nombre'] = nuevo_nombre
            juego['cantidad'] = nueva_cantidad
            juego['precio'] = nuevo_precio
            juego['imagen'] = nueva_imagen
            juego['compania'] = nueva_compania
            return True
    return False

def listar_juegos(self):
    print("-" * 50)
    for juego in self.juegos:
        print(f"Código.....: {juego['codigo']}")
        print(f"Nombre: {juego['']}")
        print(f"Cantidad...: {juego['cantidad']}")
        print(f"Precio.....: {juego['precio']}")
        print(f"Imagen.....: {juego['imagen']}")
        print(f"Compania..: {juego['compania']}")
        print("-" * 50)

def eliminar_juego(self, codigo):
    for juego in self.juegos:
        if juego['codigo'] == codigo:
            self.juegos.remove(juego)
            return True
    return False

def mostrar_juego(self, codigo):
    juego = self.consultar_juego(codigo)
    if juego:
        print("-" * 50)
        print(f"Código.....: {juego['codigo']}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Cantidad...: {juego['cantidad']}")
        print(f"Precio.....: {juego['precio']}")
        print(f"Imagen.....: {juego['imagen']}")
        print(f"Compania..: {juego['compania']}")
        print("-" * 50)
    else:
        print("Juego no encontrado.")

catalogo = Catalogo()
catalogo.agregar_juego("1", 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', "101")
catalogo.agregar_juego("2", 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', "102")
print()
print("Listado de juegos:")
catalogo.listar_juegos()
print()
print("Datos de un juego:")
catalogo.mostrar_juego("1")
catalogo.eliminar_juego("1")
print()
print("Listado de juegos:")
catalogo.listar_juegos()