<template>
  <div>
      <ApolloQuery :query="require('@/graphql/queries/categorias.gql')">
  
      <template slot-scope="{ result: { data, loading }, isLoading }">

        <div v-if="isLoading" class="text-center text-primary mt-4"><!--evento de carga spinner -->
        <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
         </div>
      </div>
      
  <div class="album py-2 bg-light" v-else>
      <div class="container">
        <div class="row">
          <div class="col-md-4" v-for="categorias of data.categorias[0].categoria" :key="categorias">
            <div class="card border-primary mb-3" style="max-width: 18rem;">
              <div class="card-body text-dark">
                <h5 class="card-title text-center">{{ categorias }}</h5>
                <router-link :to="/partidos/ + categorias">
                  <button type="button" class="btn btn-outline-dark btn-block fondo-button">
                    Ver Partidos
                  </button>
                </router-link>
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
require("../../public/vendor/fontawesome-free/css/all.min.css");
export default {
  
};
</script>

<style>
.fondo-button:hover {
  background-color: #000413;
}
</style>


