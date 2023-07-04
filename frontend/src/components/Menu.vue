<template>
  <nav class="header">
    <a href="" class="logo">
      <img :src="require('../assets/Logo2.png')" alt="Logo" />
    </a>
    <div class="navbar-container">
      <a><router-link to="/cursos">Cursos</router-link></a>
      <a><router-link to="/asesorias">Asesoria</router-link></a>
      <a><router-link to="/profesores">Profesores</router-link></a>
      <a><router-link to="/sign-in">Iniciar Sesión</router-link></a>
      <a><router-link to="/register">Registrate</router-link></a>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  background-color: #11111f;
}

.navbar-container a:hover {
  background: #080810;
  transition: 0.5s ease;
}

.navbar-container * {
  padding: 28px;
  margin: 1px;
  border-radius: 5px;
  transition: 0.5s ease;
}

.navbar-container {
  z-index: 5;
}

.logo img {
  width: 79%;
}

a.logo {
  width: 92px;
  height: 92px;
  display: flex;
  align-items: center;
  justify-content: center;
}

a {
  color: #fff;
  text-decoration: none;
}
</style>
