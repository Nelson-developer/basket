<template>
  <div>
   <jugadores/>
  </div>
</template>
<script>
// @ is an alias to /src
import jugadores from '@/components/jugadores.vue'

export default {
  name: 'home',
  components: {
      jugadores
  }
}
</script>
