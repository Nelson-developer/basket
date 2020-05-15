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
            <button type="button" class="btn btn-outline-primary mt-4 ml-4">Crear Equipo</button>
          </router-link>
        </div>
      </div>
    </div>

    

     <ApolloQuery :query="require('@/graphql/queries/categorias.gql')">
  
      <template slot-scope="{ result: { data, loading }, isLoading }">

        <div v-if="isLoading" class="text-center text-primary mt-4"><!--evento de carga spinner -->
        <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
         </div>
      </div>

      <div class="card">
      <div class="card-body text-dark">Categorias</div>
      <div class="album py-2 bg-light">
        <div class="container">
          <div class="row">
            <div class="col-md-4" v-for="categorias of data.categorias[0].categoria" :key="categorias">
              <div class="card border-primary mb-3" style="max-width: 18rem;">
                <div class="card-body text-dark">
                  <h5 class="card-title text-center">{{ categorias }}</h5>
                  <router-link :to="/equipo/ + categorias">
                    <button type="button" class="btn btn-outline-dark btn-block fondo-button">
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

    </template>  
  </ApolloQuery>

  </div>
</template>

<script>
require("../../public/css/sb-admin-2.min.css");

export default {
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



