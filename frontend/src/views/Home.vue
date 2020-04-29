<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-10">
          <h4>Partidos</h4>
          <p>
            Crea partidos anticipados para que los usuarios móviles se enteren
          </p>
        </div>
        <div class="col-2">
          <router-link to="/seleccion">
            <button
              type="button"
              class="btn btn-outline-primary mt-4 ml-4 fondo-button"
            >
              Crear partido
            </button>
          </router-link>
        </div>
      </div>
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
                  <router-link :to="/partidos/ + datos.categoria">
                    <button
                      type="button"
                      class="btn btn-outline-dark btn-block fondo-button"
                    >
                      Ver Partidos
                    </button>
                  </router-link>
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
require("../../public/vendor/fontawesome-free/css/all.min.css");
import gql from "graphql-tag";
export default {
  mounted() {
    this.QuitarDuplicados();
  },
  data() {
    return {
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
    QuitarDuplicados() {
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
</style>
