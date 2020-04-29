<template>
  <div class="row">
    <div class="col-6">
      <br />
      <table class="table table-striped">
        <thead class="thead-dark">
          <tr>
            <th scope="col">N°</th>
            <th scope="col">Nombre</th>
            <th scope="col">Puntos</th>
            <th scope="col">Asistencias</th>
            <th scope="col">Tapas</th>
            <th scope="col">Robos</th>
            <th scope="col">Puntaje</th>
          </tr>
        </thead>
        <draggable v-model="list" tag="tbody">
          <tr v-for="item in list" :key="item.name">
            <td scope="row">{{ item.id }}</td>
            <td class="move">{{ item.name }}</td>
            <td>{{ item.sport }}</td>
          </tr>
        </draggable>
      </table>
    </div>

    <div class="col-6">
      <br />
      <table class="table table-striped ">
        <thead class="thead-dark">
          <tr>
            <th scope="col">N°</th>
            <th scope="col">Nombre</th>
            <th scope="col">Puntos</th>
            <th scope="col">Asistencias</th>
            <th scope="col">Tapas</th>
            <th scope="col">Robos</th>
            <th scope="col">Puntaje</th>
          </tr>
        </thead>
        <draggable v-model="list" tag="tbody" @change="log">
          <tr v-for="(item,index) in list" :key="item.name">
           <td scope="row" class="move bg-success text-white" v-if="index <= 4">{{item.id }}</td>
            <td scope="row" class="move" v-else>{{item.id }}</td>
            <td scope="row" class="move bg-success text-white" v-if="index <= 4">{{ item.name }}</td>
            <td scope="row" class="move" v-else>{{ item.name }}</td>
            <td scope="row" class="move bg-success text-white" v-if="index <= 4">{{ item.puntos }}</td>
            <td scope="row" class="move" v-else>{{ item.puntos }}</td>
          </tr>
        </draggable>
      </table>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import io from "socket.io-client";
export default {
  name: "table-example",
  display: "Table",
  order: 8,
  components: {
    draggable,
  },
  created() {
    this.conectadoSocket();
  },
  data() {
    return {
      list: [
        { id: 1, name: "Abby", puntos: 35 },
        { id: 2, name: "Brooke", puntos: 35 },
        { id: 3, name: "Courtenay", puntos: 35 },
        { id: 4, name: "David", puntos: 35 },
        { id: 5, name: "Nelson",puntos: 35 },
        { id: 6, name: "Karina", puntos: 35 },
        { id: 7, name: "Josue", puntos: 35 },
        { id: 7, name: "Adonis", puntos: 35 },
        { id: 8, name: "Roberto", puntos: 35 },
        { id: 9, name: "Pablo", puntos: 35 },
      ],
      dragging: false,
      color: true,
      socket: "",
    };
  },
  methods: {
    conectadoSocket() {
      this.socket = io("ws://localhost:5000");

      if (this.socket) {
        console.log("conectado desde el cliente");
      }
    },
    log: function(evt) {
      window.console.log(evt);
      //si el usuario que entra a la cancha tiene su propiedad oldIndex mayor a 4 entro a la cancha
      if (evt.moved.newIndex <= 4 && evt.moved.oldIndex > 4) {
      this.socket.emit("mimensaje", { jugador: evt.moved.element.name, mensaje: "Entro a la cancha"});
      } else if (evt.moved.newIndex > 4 && evt.moved.oldIndex < 4) {
      this.socket.emit("mimensaje", { jugador: evt.moved.element.name, mensaje: "Salio de la cancha"});
      }
      window.console.log(evt.moved.element.name);
    },
  },
};
</script>

<style>
.move {
  cursor: move;
}
</style>
