<template>
  <section id="cursos" v-if="currentRoute === 'cursos'">
    <h1>
      Conoces todos nuestros cursos de <TextMenu class="custom-text-menu" />
    </h1>
    <p>
      Descubre nuestra oferta de cursos de programación y mejora tus
      habilidades.
    </p>
  </section>
</template>

<script>
import TextMenu from "./TextMenu.vue"; // Ruta relativa al archivo del componente TextMenu
export default {
  components: {
    TextMenu, // Registra el componente TextMenu para usarlo en el template
  },
  computed: {
    currentRoute() {
      return this.$route.name;
    },
  },
};
</script>
<style>
section#cursos {
  width: 100%;
  padding-top: 50px;
  padding-right: auto;
  display: inline-block;
}

section#cursos h1 {
  font-size: 36px;
  font-weight: bold;
  padding: 50px;
  width: 100%;
  display: inline;
}

section#cursos p {
  font-size: 18px;
  padding-left: 50px;
  padding-top: 30px;
  margin-bottom: 30px;
}

.custom-text-menu {
  font-size: 36px;
}
</style>
