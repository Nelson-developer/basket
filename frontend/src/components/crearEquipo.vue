<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-10">
          <br />
          <h4>Crea tus Equipos</h4>
          <p>Crea tus equipos para luego crear partidos en tiempo real</p>
        </div>
        <div class="col-2">
          <router-link to="/form-crear-equipo">
            <button type="button" class="btn btn-outline-primary mt-4 ml-4">
              Crear Equipo
            </button>
          </router-link>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-body text-dark">
        Categorias
      </div>

      <div class="album py-2 bg-light">
        <div class="container">
          <div class="row">
            <div
              class="col-md-4"
              v-for="datos of categoriaUnica"
              :key="datos.categoria"
            >
              <div class="card border-primary mb-3" style="max-width: 18rem;">
                <div class="card-body text-dark">
                  <h5 class="card-title text-center">{{ datos.categoria }}</h5>
                  <router-link :to="/equipo/ + datos.categoria">
                    <button
                      type="button"
                      class="btn btn-outline-dark btn-block fondo-button"
                    >
                      Ver Estadisticas
                    </button>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
require("../../public/css/sb-admin-2.min.css");
import SaveEquipo from "@/graphql/mutations/SaveEquipo.gql";
import gql from "graphql-tag";

export default {
  mounted() {
    this.filtrarData();
  },
  data() {
    return {
      nombreEquipo: "",
      entrenador: "Nelson",
      logo: "",
      categoria: "",
      equipos: [],
      categoriaUnica: []
    };
  },
  apollo: {
    equipos: gql`
      query {
        equipos {
          categoria
        }
      }
    `
  },
  methods: {
    GuardarEquipo() {
      this.$apollo
        .mutate({
          // Query
          mutation: SaveEquipo,
          // Parameters
          variables: {
            nombreEquipo: this.nombreEquipo,
            entrenador: this.entrenador,
            categoria: this.categoria,
            logo: "aqui ira el logo"
          } //promises
        })
        .then(data => {
          console.log(data);
          this.$apollo.queries.equipos.refetch(); //lo que hace este metodo es refrescar la consulta equipos cuando se genera un cambio
        })
        .catch(error => console.error(error));
    },
    filtrarData() {
      //esta funcion me permite filtrar las categorias no repetidas de el objeto equipos
      this.categoriaUnica = Object.values(
        this.equipos.reduce(
          (prev, next) => Object.assign(prev, { [next.categoria]: next }),
          {}
        )
      );
    }
  }
};
</script>
<style>
.fondo-button:hover {
  background-color: #000413;
}
.color-boton {
  background-color: rgba(6, 25, 131, 0.966);
}
</style>
