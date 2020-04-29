import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/crear-equipo',
    name: 'crear',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/crearEquipo.vue')
  },
  {
    path: '/form-crear-equipo',
    name: 'form-crear-equipo',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/creando-equipo.vue')
  },
  {
    path: '/equipo/:categoria',
    name: 'equipo',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/equiposCategoria.vue')
  },
  {
    path: '/jugadores/:idEquipo',
    name: 'jugador',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/RutaJugador.vue')
  },
  {
    path: '/estadistica-categoria',
    name: 'estadisticas',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/estadisticas-categoria.vue')
  },
  {
    path: '/estadisticas-equipo/:categoria',
    name: 'estadisticas-equipo',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/estadisticas-equipo.vue')
  },
  {
    path: '/partidos/:categoria',
    name: 'partidos',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/partidos.vue')
  },
  {
    path: '/tablero/:idpartido',
    name: 'tablero',
    // route level co1de-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/tablero-ruta.vue')
  },
  {
    path: '/seleccion',
    name: 'seleccion',
    // route level co1de-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/seleccion-equipo.vue')
  }


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
