<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-6 ">
          <h5 class="text-dark negrita mt-2">AGREGAR UN JUGADOR</h5>
          <p>Tu puedes agregar datos personales de cada jugador</p>
          <button
            type="button"
            class="btn btn-outline-primary fondo-button"
            @click="FormularioJugador = false"
            v-if="FormularioJugador"
          >
            Cancelar
          </button>
          <button
            type="button"
            class="btn btn-outline-primary fondo-button"
            @click="FormularioJugador = true"
            v-else
          >
            Agregar
          </button>
          <br /><br />
          <form v-show="FormularioJugador" @submit.prevent="GuardarJugador">
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                placeholder="Nombre"
                required
                v-model="nombre"
              />
            </div>
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                placeholder="Posición"
                required
                v-model="posicion"
              />
            </div>
            <div class="form-group">
              <input class="form-control" type="number" v-model.number="edad" />
            </div>
            <div class="form-group">
              <input
                class="form-control"
                type="number"
                v-model.number="altura"
              />
            </div>
            <div class="form-group">
              <input
                type="file"
                class="form-control-file"
                id="exampleFormControlFile1"
                @change="processImage($event)"
              />
            </div>
            <button type="submit" class="btn btn-primary btn-block">
              Guardar
            </button>
          </form>
          <br /><br />

          <h4 class="text-center">Jugadores</h4>
          <div class="card" v-for="jugador of jugadores" :key="jugador._id">
            <div class="card-body fondo-hover">
              {{jugador.nombre}}
            </div>
          </div>
        </div>

        <div class="col-6">
          <div class="card mt-2">
            <div class="card-body">
              <h5 class="text-center negrita">PERFIL</h5>
              <p class="text-center">
                Selecciona un jugador para ver su perfil
              </p>
            </div>
            
            <div class="card mb-3">
              <img
                src="https://www.elindependiente.com/wp-content/uploads/2018/07/LeBron-James-1440x808.jpg"
                class="card-img-top"
              />
              <div class="card-body">
                <h5 class="card-title">Nombre: Lebron James</h5>
                <h5 class="card-text">Posicion: Escolta</h5>
                <h5 class="card-text">Edad: Escolta</h5>
                <h5 class="card-text">Altura: 205 cm</h5>
                <button
                  class="btn edit-color btn-block fondo-button-hover text-white"
                >
                  Editar<i class="ml-2 fas fa-bell fa-pen"></i>
                </button>
              </div>
            </div>
          </div>
          <br /><br /><br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
require("../../public/css/sb-admin-2.min.css");
require("../../public/vendor/fontawesome-free/css/all.min.css");
import SaveJugador from "@/graphql/mutations/SaveJugador.gql";
import gql from "graphql-tag";
export default {
  data() {
    return {
      FormularioJugador: false,
      idEquipo: this.$route.params.idEquipo,
      nombre: "",
      posicion: "",
      edad: 0,
      altura: 0,
      imagen: "",
      CLOUDINARY_URL: "https://api.cloudinary.com/v1_1/nelson35/image/upload",
      CLOUDINARY_UPLOAD_PRESET: "o1zbsjpg",
      jugadores: []
    };
  },
  // Apollo-specific options
  apollo: {
    // Advanced query with parameters
    EquipoJugadores: {
      query: gql`
        query EquipoJugadores($Id: ID) {
          EquipoJugadores(Id: $Id) {
            jugadores {
              Id
              nombre
            }
          }
        }
      `,
      variables () {
      // Use vue reactive properties here
      return {
          Id: this.idEquipo,
      }
    },
      // obtenemos los resultados de la query con parametrps
      result({ data }) {
         this.jugadores = data.EquipoJugadores[0].jugadores
      },
      // Error handling
      error(error) {
        console.error("We've got an error!", error);
      }
    }
  },
  methods: {
    MostrarNoticacion() {
      this.$toast.open({
        message: "Se guardo correctamente",
        type: "success",
        duration: 3000,
        dismissible: true
      });
    },
    processImage(event) {
      this.imagen = event.target.files[0]; // guardamos los metadatos de la imagen
    },
    async GuardarJugador() {
      let imagenUrl = "";
      const formData = new FormData();
      formData.append("file", this.imagen);
      formData.append("upload_preset", this.CLOUDINARY_UPLOAD_PRESET);
      //funcion para subir a cloudinary la imagen
      await fetch(this.CLOUDINARY_URL, { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => (imagenUrl = data.url))
        .catch(err => console.log(err));

      //hacemos la mutacion en apollo
      this.$apollo
        .mutate({
          // Query
          mutation: SaveJugador,
          // Parameters
          variables: {
            id: this.idEquipo,
            nombreJugador: this.nombre,
            posicion: this.posicion,
            imagen: imagenUrl,
            edad: this.edad,
            altura: this.altura
          } //promises
        })
        .then(() => {
          this.nombre = "";
          this.posicion = "";
          this.imagen = "";
          this.altura = 0;
          this.edad = 0;
          this.MostrarNoticacion();
          this.$apollo.queries.EquipoJugadores.refetch(); //lo que hace este metodo es refrescar la consulta EquipoJugadores cuando se genera un cambio
        })
        .catch(error => console.error(error));
    }
  }
};
</script>

<style>
.negrita {
  font-weight: bold;
}
.fondo-hover:hover {
  background-color: rgba(6, 65, 133, 0.918);
  color: white;
}
.edit-color {
  background-color: rgba(12, 116, 236, 0.918);
}

.fondo-button-hover:hover {
  background-color: #000413;
}
</style>
