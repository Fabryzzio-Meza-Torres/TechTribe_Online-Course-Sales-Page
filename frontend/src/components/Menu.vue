<template>
  <nav class="header">
    <a href="" class="logo">
      <img :src="require('../assets/Logo2.png')" alt="Logo" />
    </a>
    <div class="navbar-container">
      <router-link to="/cursos" class="Mienlace">Cursos</router-link>
      <router-link to="/asesorias" class="Mienlace">Asesoria</router-link>
      <router-link to="/profesores" class="Mienlace">Profesores</router-link>
      <router-link to="/sign-in" class="Mienlace">Iniciar Sesión</router-link>
      <router-link to="/register" class="Mienlace">Registrate</router-link>
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

a {
  color: white;
  text-decoration: none;
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

.Mienlace {
  color: white;
  text-decoration: none;
  transition: color 0.3s;
}

.Mienlace:hover {
  color: gold;
}

.Mienlace:visited {
  color: white;
}
</style>
