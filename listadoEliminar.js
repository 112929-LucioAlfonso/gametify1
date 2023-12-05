//const URL = "http://127.0.0.1:5000/"
const URL = "https://martin927189.pythonanywhere.com/"
const app = Vue.createApp({
    data() {
        return {
            juegos: []
        }
    },
    methods: {
        obtenerJuegos() {
        // Obtenemos el contenido del inventario
        fetch(URL + 'juegos')
            .then(response => {
                // Parseamos la respuesta JSON
                if (response.ok) { return response.json(); }
            })
            .then(data => {
                // El código Vue itera este elemento para generar la tabla

                this.juegos = data;
            })
            .catch(error => {
                console.log('Error:', error);
                alert('Error al obtener los juegos.');
            });
    },
    eliminarJuego(codigo) {
        if (confirm('¿Estás seguro de que quieres eliminar este juego?')) {
            fetch(URL + `juegos/${codigo}`, { method: 'DELETE' })
                .then(response => {
                    if (response.ok) {
                        this.juegos =
this.juegos.filter(juego => juego.codigo !== codigo);
                        alert('Juego eliminado correctamente.');
                    }
                })
                .catch(error => {
                    alert(error.message);
                });
        }
    }
},
    mounted() {
        //Al cargar la página, obtenemos la lista de productos
        this.obtenerJuegos();
    }
});
app.mount('body');