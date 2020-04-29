<template>
  <div>
    <!-- Haciendo consulta de graphql -->
    <ApolloQuery :query="require('@/graphql/queries/equipoCategoria.gql')" :variables="{ categoria: idCategoria }">
  
      <template slot-scope="{ result: { data, loading }, isLoading }">
        <!-- Luego de hacer la consulta a graphql pasaremos a pintar los datos -->
        <div v-if="isLoading" class="text-center text-primary mt-4"><!--evento de carga spinner -->
           <div class="spinner-border" role="status">
    <span class="sr-only">Loading...</span>
         </div>
      </div>
        <div class="album py-5 bg-light" v-else>
          <div class="container">
            <div class="row">
              <div
                class="col-md-6"
                v-for="d of data.EquiposPorCategoria"
                :key="d.Id"
              >
                <router-link :to="/jugadores/ + d.Id">
                  <div class="card mb-3" style="max-width: 540px;">
                    <div class="row no-gutters">
                      <div class="col-md-4">
                        <img
                          src="https://i.pinimg.com/originals/2f/2f/f9/2f2ff9f9cc894675d3a4f3d83b42d385.jpg"
                          class="card-img"
                          alt="..."
                        />
                      </div>
                      <div class="col-md-8">
                        <div class="card-body">
                          <h5 class="card-title text-dark">
                            {{d.nombreEquipo}}
                          </h5>
                          <p>Entrenador: {{d.entrenador}}</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </router-link>
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
  data() {
    return {
      idCategoria: this.$route.params.categoria
    };
  }
};
</script>
