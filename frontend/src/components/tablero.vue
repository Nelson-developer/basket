<template>
  <div class="container">
    <div class="row">
      <div class="col-sm">
        <div class="card w-75 ml-4 card border-dark">
          <div class="card-body text-center">
            <h3 class="text-center">Home</h3>
            <h1 class="card-title ml-4 big text-dark">25</h1>
            <h4 class="card-title ml-4 text-dark">Halcones de Sonzacate</h4>
          </div>
        </div>
      </div>
      <div class="col-sm">
        <br />
        <div class="card border-primary mb-3" style="max-width: 18rem;">
          <div class="card-body text-primary">
            <!-- audio chicharra-->
            <h2 class="text-center">Tiempo</h2>
            <h1 class="card-title text-center big-time">
              {{ minutes }}:{{ seconds }}
            </h1>
            <h1
              class="card-title text-center big-time"
              :class="{ 'text-danger': TiempoAgotado }"
            >
              {{ posesion }}
            </h1>
            <h4 class="text-center">Primer Cuarto</h4>
            <div class="d-flex justify-content-center">
              <i
                class="fas fa-bell fa-question"
                data-toggle="popover"
                title="Presiona SPACE para avanzar"
              ></i>
            </div>
          </div>
        </div>
        <div class="controls">
          <button
            class="btn btn-dark"
            v-if="!timer"
            @click="startTimer"
            @keyup.enter="startTimer"
          >
            Iniciar tiempo
          </button>
          <button
            class="btn btn-danger"
            v-if="timer"
            @click="stopTimer"
            @keyup.enter="stopTimer"
          >
            Stop
          </button>
          <button class="btn btn-dark" v-if="resetButton" @click="resetTimer">
            Reset
          </button>
        </div>
        <div>
          <button class="btn btn-dark" @click="reiniciarPosesion()">
            Restablecer Posesion
          </button>
        </div>
      </div>
      <div class="col-sm">
        <div class="card w-75 ml-4 card border-dark">
          <div class="card-body text-center">
            <h3 class="text-center">Guest</h3>
            <h1 class="card-title ml-4 big text-dark">28</h1>
            <h4 class="card-title ml-4">Brujos de Izalco BKB</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import io from "socket.io-client";
export default {
  mounted(){
    this.conectadoSocket()
  },
  data() {
    return {
      timer: null,
      totalTime: 10 * 60,
      resetButton: false,
      edit: false,
      userTime: 10,
      posesion: 24,
      TiempoAgotado: false,
      detenerposesion: null,
      socket: "",
    };
  },
  methods: {
    startTimer: function() {
      //inicia el tiempo
      this.timer = setInterval(() => this.countdown(), 1000); //1000ms = 1 segundo
      this.TiempoPosesion(); // ejecuto la funcion para la cuenta regresiva de la posesion
      this.resetButton = true;
      this.edit = false;
    },
    stopTimer: function() {
      clearInterval(this.timer); //funcion que detiene el tiempo del periodo
      this.DetenerPosesion(); //la ejecutamos para detener la posesion al mismo tiempo que el tiempo de periodo
      this.timer = null;
      this.resetButton = true;
    },
    resetTimer: function() {
      //reinicia el tiempo por default
      this.totalTime = this.userTime * 60;
      clearInterval(this.timer);
      this.timer = null;
      this.resetButton = false;
    },
    padTime: function(time) {
      // si es menor a 10 el numero se le coloca un 0 por ejemplo 09
      return (time < 10 ? "0" : "") + time;
    },
    countdown: function() {
      //ejecuta la cuenta regresiva
      this.totalTime--;
      this.infoTablero()//mando al socket cada vez que le resta al contador
    },
    TiempoPosesion() {
      // tiempo de posesion que son 24 segundos
      const self = this;
      this.detenerposesion = setInterval(() => {
        if (self.posesion == 10) {
          self.TiempoAgotado = true; //coloca de diferente color el numero
        }
        if (self.posesion == 0) {
          //cuando los segundos lleguen a cero sonara la chicharra y se restablecera el tiempo
          setTimeout(self.ChicharraSonido(), 3000);
          self.TiempoAgotado = false;
          self.posesion = 24;
        } else {
          //resta la posesion
          self.posesion--;
        }
      }, 1000);
    },
    ChicharraSonido() {
      //funcion que ejecuta el sonido de la chicharra
      var audio = new Audio(require("./chicharra-basket.mp3"));
      audio.play();
    },
    DetenerPosesion: function() {
      //funcion que detiene la posesion
      clearInterval(this.detenerposesion);
    },
    reiniciarPosesion() {
      //restablezco el valor default que es 24 segundos
      this.posesion = 24;
    },
    conectadoSocket() {
      this.socket = io("ws://localhost:5000");

      if (this.socket) {
        console.log("conectado");
      this.socket.emit("tablero", { minuto: 1, segundo: 2 });
      }
    },
    infoTablero(){
      this.socket.emit("tablero", { minuto: this.minutes, segundo: this.seconds });
    }
  },
  computed: {
    minutes: function() {
      //obtenemos los minutos
      const minutes = Math.floor(this.totalTime / 60);
      //console.log(minutes);
      return this.padTime(minutes);
    },
    seconds: function() {
      //obtenemos los segundos
      const seconds = this.totalTime - this.minutes * 60;
      return this.padTime(seconds);
    },
  },
};
</script>

<style>
.big {
  font-size: 800%;
}
.big-time {
  font-size: 450%;
}
</style>
