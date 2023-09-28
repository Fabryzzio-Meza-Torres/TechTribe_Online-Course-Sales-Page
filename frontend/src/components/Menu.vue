<template>
  <nav class="header">
    <a href="" class="logo">
      <img :src="require('../assets/Logo2.png')" alt="Logo" />
    </a>
    <div class="navbar-container">
      <a><router-link to="/cursos" class="link">Cursos</router-link></a>
      <a><router-link to="/asesorias" class="link">Asesoria</router-link></a>
      <a><router-link to="/profesores" class="link">Profesores</router-link></a>
      <a class="logreg"
        ><router-link to="/sign-in" class="link">Iniciar Sesión</router-link></a
      >
      <a class="logreg"
        ><router-link to="/register" class="link">Registrate</router-link></a
      >
      <a href="#" style="display: none" id="closeSession">Cerrar sesión</a>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};

window.onload = function () {
  if (document.cookie) {
    document.getElementById("closeSession").style.display = "inline-block";
    document.getElementsByClassName("logreg")[0].style.display = "none";
    document.getElementsByClassName("logreg")[1].style.display = "none";
    document.getElementById("closeSession").addEventListener("click", () => {
      //borrar cookie
      document.cookie =
        "session=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      window.location.href = "/";
    });
  } else {
    document.getElementById("closeSession").style.display = "none";
  }
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

.link,
a {
  color: white;
  text-decoration: none;
}
</style>
