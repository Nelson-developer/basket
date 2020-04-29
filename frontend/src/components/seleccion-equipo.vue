<template>
  <div>
<div class="container-fluid">
  <div class="row">
    <nav class="col-md-3 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky">
          <div class="row">
    <div>
      <h3 class="negrita ml-1">Selecciona y arrastra</h3>
     <draggable class="list-group move" :list="list1" group="people" @change="log">
      
         <div  v-for="(element) in list1"
          :key="element.name">
                <ul class="list-unstyled card mb-2 ml-2 mr-5">
                  <li class="media">
                    <img
                      src="https://www.stickpng.com/assets/images/58419be4a6515b1e0ad75a58.png"
                      class="mr-3"
                      alt="..."
                      height="64"
                      width="64"
                    />
                    <div class="media-body">
                      <h6 class="text-dark mt-3">{{ element.name }}</h6>
                    </div>
                  </li>
                </ul>
              </div>
      </draggable>
    </div>

  </div>
      </div>
    </nav>

    <main role="main" class="col-md-5 ml-sm-auto col-lg-9 px-4">
     
      <h3 class="negrita">Home</h3>
    <div class="card fondo-caja">
  <div class="card-body text-white ">
      <draggable  :list="listVisitante" group="people" @change="log">
        <div
          v-for="(element, index) in listVisitante"
          :key="element.name"
        >
          {{ element.name }} {{ index }}
        </div>
      </draggable>
  </div>
</div>
<br>
      <h3 class="negrita">Visita</h3>
     <div class="card bg-info">
  <div class="card-body text-white fondo-caja">
     <draggable  :list="listCasa" group="people" @change="log">
        <div
          v-for="(element, index) in listCasa"
          :key="element.name"
        >
          {{ element.name }} {{ index }}
        </div>
      </draggable>

  </div>
</div>
<br>
      <h3 class="negrita">Lugar</h3>
     <div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Escribe el lugar donde sera el partido" aria-label="Recipient's username" aria-describedby="button-addon2">
</div>
<br>
<!-- hice este container para tres rejillas y en el centro puse el boton -->
<div class="container">
  <div class="row">
    <div class="col-6 col-md-4"></div>
    <div class="col-6 col-md-4">
      <button type="button" class="btn btn-fondo btn-block fondo-button text-white">Guardar</button>
    </div>
    <div class="col-6 col-md-4"></div>
  </div>


</div>
    </main>
  </div>
</div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
export default {
  name: "two-lists",
  display: "Two Lists",
  order: 1,
  components: {
    draggable
  },
  data() {
    return {
      list1: [
        { name: "Halcones de Sonzacate", id: 1 },
        { name: "Joao", id: 2 },
        { name: "Jean", id: 3 },
        { name: "Gerard", id: 4 }
      ],
      listVisitante: [],
      listCasa: []
    };
  },
  methods: {
    log: function(evt) {
      window.console.log(evt);
    },
    GuardarEquipo(){
     let equipoVisitante = this.listVisitante[0].id
     let equipoCasa = this.listCasa[0].id
     console.log(equipoVisitante, equipoCasa);
     
    }
  }
};
</script>

<style scoped>
.btn-fondo{
  background-color: #3A4677;
}

.fondo-button:hover{
  background-color: #000413;
}
.fondo-caja{
  background-color: #2d51e6;
}
.move{ cursor: move; }
.negrita{
    font-weight: bold
}
.buttons {
  margin-top: 35px;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

    .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      body {
  font-size: .875rem;
}

.feather {
  width: 16px;
  height: 16px;
  vertical-align: text-bottom;
}

/*
 * Sidebar
 */

.sidebar {
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}


@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sidebar-sticky {
    position: -webkit-sticky;
    position: sticky;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #999;
}


/*
 * Content
 */

[role="main"] {
  padding-top: 133px; /* Space for fixed navbar */
}

@media (min-width: 768px) {
  [role="main"] {
    padding-top: 48px; /* Space for fixed navbar */
  }
}

/*
 * Navbar
 */



.form-control-dark {
  color: #fff;
  background-color: rgba(255, 255, 255, .1);
  border-color: rgba(255, 255, 255, .1);
}

.form-control-dark:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, .25);
}
</style>
