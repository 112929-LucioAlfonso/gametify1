#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
#from flask import request

# Instalar con pip install flask-cors


# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time

from flask_cors import CORS
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

class Catalogo:
# Constructor de la clase
    def __init__(self, host, user, password, database):
# Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
# Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS juegos (
            codigo INT,
            nombre VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            compania INT NOT NULL)''')
        self.conn.commit()
# Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
    #----------------------------------------------------------------
    def listar_juegos(self):
        self.cursor.execute("SELECT * FROM juegos")
        juegos = self.cursor.fetchall()
        return juegos
    #----------------------------------------------------------------
    def consultar_juego(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM juegos WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    #----------------------------------------------------------------
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

    def agregar_juego(self, codigo, nombre, cantidad, precio, imagen, compania):
            self.cursor.execute(f"SELECT * FROM juegos WHERE codigo = {codigo}")
            juego_existe = self.cursor.fetchone()
            if juego_existe:
                return False
            sql = "INSERT INTO juegos (codigo, nombre, cantidad, precio, imagen_url, compania) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (codigo, nombre, cantidad, precio, imagen, compania)
            self.cursor.execute(sql,valores)
            self.conn.commit()
            return True
        
    def eliminar_juego(self, codigo):
                # Eliminamos un producto de la tabla a partir de su código
                self.cursor.execute(f"DELETE FROM juegos WHERE codigo = {codigo}")
                self.conn.commit()
                return self.cursor.rowcount > 0
    
    def modificar_juego(self, codigo, nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_imagen, nueva_compania):
                sql = "UPDATE juegos SET nombre = %s, cantidad = %s, precio = %s, imagen_url = %s, compania = %s WHERE codigo = %s"
                valores = (nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_imagen, nueva_compania, codigo)
                self.cursor.execute(sql, valores)
                self.conn.commit()
                return self.cursor.rowcount > 0
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
#catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
catalogo = Catalogo(host='martin927189.mysql.pythonanywhere-services.com', user='martin927189', password='ChA=4)u-_4/X)d#', database='martin927189$miapp')

# Carpeta para guardar las imagenes
#ruta_destino = 'static/img/'
ruta_destino = '/home/martin927189/mysite/static/img/'
        
@app.route("/juegos", methods=["GET"])
def listar_juegos():
    juegos = catalogo.listar_juegos()
    return jsonify(juegos)

@app.route("/juegos/<int:codigo>", methods=["GET"])
def mostrar_juego(codigo):
    catalogo.mostrar_juego(codigo)
    juego = catalogo.consultar_juego(codigo)
    if juego:
        return jsonify(juego)
    else:
        return "Juego no encontrado", 404

@app.route("/juegos", methods=["POST"])
def agregar_juego():
    # Recojo los datos del form
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    compania = request.form['compania']
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)

    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    imagen.save(os.path.join(ruta_destino, nombre_imagen))
    
    if catalogo.agregar_juego(codigo, nombre, cantidad, precio, nombre_imagen, compania):
        return jsonify({"mensaje": "Juego agregado"}), 201
    else:
        return jsonify({"mensaje": "Juego ya existe"}), 400
    

@app.route("/juegos/<int:codigo>", methods=["DELETE"])
def eliminar_juego(codigo):
    # Primero, obtén la información del producto para encontrar la imagen
    juego = catalogo.consultar_juego(codigo)
    if juego:
        # Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, juego['imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
        # Luego, elimina el producto del catálogo
        if catalogo.eliminar_juego(codigo):
            return jsonify({"mensaje": "Juego eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el Juego"}), 500
    else:
        return jsonify({"mensaje": "Juego no encontrado"}), 404

@app.route("/juegos/<int:codigo>", methods=["PUT"])
def modificar_juego(codigo):
    # Recojo los datos del form
    nuevo_nombre = request.form.get("nombre")
    nueva_cantidad = request.form.get("cantidad")
    nuevo_precio = request.form.get("precio")
    nueva_compania = request.form.get("compania")
    # Procesamiento de la imagen
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)
    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    imagen.save(os.path.join(ruta_destino, nombre_imagen))
    # Actualización del producto
    if catalogo.modificar_juego(codigo, nuevo_nombre, nueva_cantidad, nuevo_precio, nombre_imagen, nueva_compania):
        return jsonify({"mensaje": "Juego modificado"}), 200
    else:
        return jsonify({"mensaje": "Juego no encontrado"}), 404
if __name__ == "__main__":
    app.run(debug=True)
























