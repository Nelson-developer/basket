<template >
<div>
<div class="container">
  <div class="row">
    <div class="col-10">
            <h4>Estadisticas</h4>
        <p>Mira las estadisticas de cada categoria para estar enterado de los jugadores tendencia</p>
    </div>
  </div>
</div>
<div class="album py-5 bg-light">
    <div class="container">
      <div class="row">
        <div class="col-md-4" v-for="d of datos" :key="d.edad" >
    <div class="card border-primary mb-3" style="max-width: 18rem;" >
  <div class="card-body text-dark" >
    <h5 class="card-title text-center">Masculino U17</h5>
   <router-link to="/estadisticas-equipo/Masculino U17">
      <button type="button" class="btn btn-outline-dark btn-block fondo-button">Ver Estadisticas</button>
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
export default {
  data(){
    return{
       datos:[
        {
          nombre: "Nelson",
          edad: 1
        },
         {
          nombre: "Nelson",
          edad: 2
        },
         {
          nombre: "Nelson",
          edad: 3
        },
        {
          nombre: "Nelson",
          edad: 4
        },
       ]
    }
  }
}
</script>

<style>
.fondo-button:hover{
  background-color: #000413;
}
</style>