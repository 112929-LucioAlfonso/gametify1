//const URL = "http://127.0.0.1:5000/"
const URL = "https://martin927189.pythonanywhere.com/"
// Realizamos la solicitud GET al servidor para obtener todos los productos
fetch(URL + 'juegos')
    .then(function (response) {
        if (response.ok) {
            return response.json();
    }   else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al obtener los juegos.');
        }
})
    .then(function (data) {
        let tablaJuegos = document.getElementById('tablaJuegos');
        // Iteramos sobre los productos y agregamos filas a la tabla
        for (let juego of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + juego.codigo + '</td>' +
                '<td>' + juego.nombre + '</td>' +
                '<td align="right">' + juego.cantidad + '</td>' +
                '<td align="right">' + juego.precio + '</td>' +
                // Mostrar miniatura de la imagen
                //'<td><img src=static/img/' + producto.imagen_url +'alt="Imagen del producto" style="width: 100px;"></td>' +'<td align="right">' + producto.proveedor + '</td>';
                '<td><img src=https://www.pythonanywhere.com/user/martin927189/files/home/martin927189/mysite/static/img/' + juego.imagen_url +' width="100%" height="100%" ></td>' +'<td align="right">' + juego.compania + '</td>';
//Una vez que se crea la fila con el contenido del producto, se agrega a la tabla utilizando el método appendChild del elemento tablaProductos.

            tablaJuegos.appendChild(fila);
        }
    })
    .catch(function (error) {
        // En caso de error
        alert('Error al agregar el juego.');
        console.error('Error:', error);
    })