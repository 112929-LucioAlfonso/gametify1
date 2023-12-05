//const URL = "http://127.0.0.1:5000/"
const URL = "https://martin927189.pythonanywhere.com/"


const app = Vue.createApp({
  data() {
        return {
            codigo: '',
            nombre: '',
            cantidad: '',
            precio: '',
            compania: '',
            imagen_url: '',
            imagenUrlTemp: null,
            mostrarDatosJuego: false,
        };
    },

  methods: {
    obtenerJuego() {
            fetch(URL + 'juegos/' + this.codigo)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
//Si la respuesta es un error, lanzamos una excepción para ser "catcheada" más adelante en el catch.

                        throw new Error('Error al obtener los datos del juego.')
                    }
                })
                .then(data => {
                    this.nombre = data.nombre;
                    this.cantidad = data.cantidad;
                    this.precio = data.precio;
                    this.compania = data.compania;
                    this.imagen_url = data.imagen_url;
                    this.mostrarDatosJuego = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Código no encontrado.');
                })
    },
    seleccionarImagen(event) {
            const file = event.target.files[0];
            this.imagenSeleccionada = file;
            this.imagenUrlTemp = URL.createObjectURL(file); // Crea una URL temporal para la vista previa
        },
    guardarCambios() {
            const formData = new FormData();
            formData.append('codigo', this.codigo);
            formData.append('nombre', this.nombre);
            formData.append('cantidad', this.cantidad);
            formData.append('compania', this.compania);
            formData.append('precio', this.precio);

        if (this.imagenSeleccionada) {
                formData.append('imagen', this.imagenSeleccionada, this.imagenSeleccionada.name);
            }
            //Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
            
        fetch(URL + 'juegos/' + this.codigo, {
                method: 'PUT',
                body: formData,
            })
        .then(response => {
            //Si la respuesta es exitosa, utilizamos response.json() para parsear la respuesta en formato JSON.
                if (response.ok) {
                    return response.json()
                } else {
            //Si la respuesta es un error, lanzamos una excepción.
                    throw new Error('Error al guardar los cambios del juego.')
            }
            })
        .then(data => {
                alert('Juego actualizado correctamente.');
                this.limpiarFormulario();
            })
        .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el juego.');
        });
    },
    limpiarFormulario() {
                this.codigo = '';
                this.nombre = '';
                this.cantidad = '';
                this.precio = '';
                this.imagen_url = '';
                this.imagenSeleccionada = null;
                this.imagenUrlTemp = null;
                this.mostrarDatosJuego = false;
        }
    }
});

app.mount('#app');