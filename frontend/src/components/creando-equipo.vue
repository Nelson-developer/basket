<template>
  <div>
      <br>
      <h4 class="text-center">Agregar Nuevo equipo</h4>
    <form class="form-signin" @submit.prevent="GuardarEquipo">
      <div class="form-label-group">
        <input
          type="text"
          id="nombre-equipo"
          class="form-control"
          placeholder="Nombre de Equipo"
          v-model="nombreEquipo"
          required
          autofocus
        />
        <label for="nombre-equipo">Nombre de Equipo</label>
      </div>

      <div class="form-label-group">
        <input
          type="text"
          id="entrenador"
          class="form-control"
          placeholder="Entrenador"
          v-model="entrenador"
          required
        />
        <label for="entrenador">Entrenador</label>
      </div>
       <div class="form-group">
    <label for="exampleFormControlSelect1">Categoria</label>
    <select class="form-control" id="exampleFormControlSelect1" v-model="categoria">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
  </div>
  <input
          type="text"
          id="nombre-equipo"
          class="form-control"
          placeholder="Agregar nueva categoria"
          autofocus
          v-model="categoria"
        />

   <input type="file" name="" ref="boton" @change="processImage($event)">
      <button class="btn btn-lg btn-primary btn-block">
        Guardar
      </button>

    </form>
  </div>
</template>
<script>
import saveEquipo from "@/graphql/mutations/SaveEquipo.gql";
export default {
  data(){
     return{
       nombreEquipo: "",
       entrenador: "",
       categoria: "",
       imagen: "",
      CLOUDINARY_URL: "https://api.cloudinary.com/v1_1/nelson35/image/upload",
      CLOUDINARY_UPLOAD_PRESET: "g0mg1y82",
     }
  },
  methods: {
    processImage(event) {
      this.imagen = event.target.files[0]; // guardamos los metadatos de la imagen
    },
      GuardarEquipo() {
      //gurdando imagen en cloudinary
       let imagenUrl = "";
      const formData = new FormData();
      formData.append("file", this.imagen);
      formData.append("upload_preset", this.CLOUDINARY_UPLOAD_PRESET);
      //funcion para subir a cloudinary la imagen
      fetch(this.CLOUDINARY_URL, { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {imagenUrl = data.url})
        .catch(err => console.log(err));

    this.$apollo.mutate({
      // Query
      mutation: saveEquipo,
      // Parameters
      variables: {
        nombreEquipo: this.nombreEquipo,
        entrenador: this.entrenador,
        categoria: this.categoria,
        logo: imagenUrl,
      }, 
    }).then((data) => {
      this.nombreEquipo = ""
      this.entrenador =  ""
      this.categoria = ""
      console.log(data)
    }).catch((error) => { console.error(error)})
  },
},
}
</script>


<style>
.form-signin {
  width: 100%;
  max-width: 420px;
  padding: 15px;
  margin: auto;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group > input,
.form-label-group > label {
  height: 3.125rem;
  padding: 0.75rem;
}

.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0; /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  pointer-events: none;
  cursor: text; /* Match the input under the label */
  border: 1px solid transparent;
  border-radius: 0.25rem;
  transition: all 0.1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: 1.25rem;
  padding-bottom: 0.25rem;
}

.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  font-size: 12px;
  color: #777;
}

/* Fallback for Edge
-------------------------------------------------- */
@supports (-ms-ime-align: auto) {
  .form-label-group > label {
    display: none;
  }
  .form-label-group input::-ms-input-placeholder {
    color: #777;
  }
}
</style>
