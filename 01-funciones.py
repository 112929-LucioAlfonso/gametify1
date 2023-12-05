juegos = []

def agregar_juego(codigo, nombre, cantidad, precio, imagen, compania):
    if consultar_juego(codigo):
        return False
    nuevo_juego = {
        'codigo': codigo,
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'compania': compania
    }
    juegos.append(nuevo_juego)
    return True

def consultar_juego(codigo):
    for juego in juegos:
        if juego['codigo'] == codigo:
            return juego
    return False

def modificar_juego(codigo, nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_imagen, nueva_compania):
    for juego in juegos:
        if  juego['codigo'] == codigo:
            juego['nombre'] = nuevo_nombre
            juego['cantidad'] = nueva_cantidad
            juego['precio'] = nuevo_precio
            juego['imagen'] = nueva_imagen
            juego['compania'] = nueva_compania
            return True
    return False

def listar_juegos():
    print("-" * 50)
    for juego in juegos:
        print(f"Código.....: {juego['codigo']}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Cantidad...: {juego['cantidad']}")
        print(f"Precio.....: {juego['precio']}")
        print(f"Imagen.....: {juego['imagen']}")
        print(f"Compania..: {juego['compania']}")
        print("-" * 50)

def eliminar_juego(codigo):
    for juego in juegos:
        if  juego['codigo'] == codigo:
            juegos.remove(juego)
            return True
    return False


agregar_juego("1", 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', "101")
agregar_juego("2", 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', "102")
agregar_juego("3", 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', "103")
agregar_juego("4", 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', "104")
agregar_juego("5", 'Pad mouse', 5, 500, 'padmouse.jpg', "105")
agregar_juego("3", 'Parlantes USB', 4, 2500, 'parlantes.jpg', "105") 
# No es posible agregarlo, mismo código que el producto 3.
# Listamos todos los productos en pantalla
listar_juegos()
# Consultar un producto por su código
cod_juego = input("Ingrese el código del juego: ")
juego = consultar_juego(cod_juego)
if juego:
    print(f"Juego encontrado: {juego['codigo']} - {juego['nombre']}")
else:
    print(f'juego {cod_juego} no encontrado.')
# Modificar un producto por su código
modificar_juego("1", 'Teclado mecánico 62 teclas', 20, 34000, 'tecladomecanico.jpg', "106")
# Listamos todos los productos en pantalla
listar_juegos()
# Eliminamos un producto del inventario
eliminar_juego("5")
# Listamos todos los productos en pantalla
listar_juegos()


