<template>
  <div>
   <tablero/>
   <tablaJugadores/>
  </div>
</template>
<script>
// @ is an alias to /src
import tablero from '@/components/tablero.vue'
import tablaJugadores from '@/components/tabla-jugadores.vue'

export default {
  name: 'home',
  components: {
    tablero,
    tablaJugadores 
  }
}
</script>