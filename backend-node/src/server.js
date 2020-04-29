import express from 'express';
const app = express()
import { ConectarDB } from  "./conexion-db"; //importando la funcion para conectar a MongoDB
import { socketMove } from "./socket-io/move-jugadores";
//conectando a MongoDB
ConectarDB()


//creando el servidor
let puerto = process.env.PORT || 5000
const servidor = app.listen(puerto, ()=> console.log(`servidor en el puerto ${puerto}`))
socketMove(servidor)
