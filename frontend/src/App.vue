<template>
  <div id="app">
    <div id="wrapper">

    <!-- Sidebar -->
    <ul class="navbar-nav color-fondo sidebar sidebar-dark accordion" id="accordionSidebar">

      <!-- Sidebar - Brand -->
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
        <div class="sidebar-brand-icon rotate-n-15">
          <i class="fas fa-basketball-ball"></i>
        </div>
        <div class="sidebar-brand-text mx-3">Basket</div>
      </a>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">

      <!-- Nav Item - Dashboard -->
      <router-link to="/"><li class="nav-item active">
        <a class="nav-link" >
          <i class="fas fa-home"></i>
          <span>Inicio</span></a>
      </li></router-link>

      <router-link to="/crear-equipo"><li class="nav-item ">
        <a class="nav-link" >
          <i class="fas fa-users"></i>
        <span>Crear Equiṕo</span></a>
      </li></router-link>

      <!-- Nav Item - Utilities Collapse Menu -->
     <router-link to="/estadistica-categoria"> <li class="nav-item ">
        <a class="nav-link" >
          <i class="fas fa-chart-bar"></i>
          <span>Estadisticas</span></a>
      </li></router-link>

      <li class="nav-item ">
        <a class="nav-link" >
          <i class="fas fa-address-card"></i>
        <span>Acerca de</span></a>
      </li>
      <li class="nav-item ">
        <a class="nav-link">
          <i class="fas fa-cog"></i>
          <span>Configuración</span></a>
      </li>

    </ul>
       <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">      
    <router-view/>
  </div>
  </div>
    </div>
    </div>
</template>

<style>
.color-fondo{
  background: rgb(4,29,133);
}
</style>
