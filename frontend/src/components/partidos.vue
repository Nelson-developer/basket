<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-10">
          <h4>Partidos</h4>
          <p>Crea partidos anticipados para que los usuarios móviles se enteren</p>
        </div>
        <div class="col-2">
          <router-link :to="/seleccion/ + this.$route.params.categoria ">
            <button
              type="button"
              class="btn btn-outline-primary mt-4 ml-4 fondo-button"
            >Crear partido</button>
          </router-link>
        </div>
      </div>
    </div>

    
    <div class="album bg-light">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="card text-center">
              <div class="card-body">
                <h5 class="card-title">Los Angeles Lakers</h5>
                <h5 class="card-title">VS</h5>
                <h5 class="card-title">Blazers BKB</h5>
                <router-link to="/tablero/1e1e1ee1">
                  <button class="btn btn-outline-primary fondo-button">Iniciar</button>
                </router-link>
              </div>
              <div class="card-footer bg-dark text-white">Sabado 2 de Marzo de 2019</div>
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
export default {};
</script>
<style>
.fondo-button:hover {
  background-color: #000413;
}
</style>