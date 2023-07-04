<template>
  <section id="cursos" v-if="currentRoute === 'cursos'">
    <h1>
      Conoce todos nuestros cursos de <TextMenu class="custom-text-menu" />
    </h1>
    <p>
      Descubre nuestra oferta de cursos de programación y mejora tus
      habilidades.
    </p>
  </section>
  <section id="asesorias" v-else-if="currentRoute === 'asesorias'">
    <h1>Asesorate con los <TextMenu class="custom-text-menu" /></h1>
    <p>
      ¿Necesitas ayuda con un proyecto o una tarea de programación? Contáctanos
      y te asesoramos.
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
section {
  width: 100%;
  padding-top: 50px;
  padding-right: auto;
  display: inline-block;
}

section h1 {
  font-size: 36px;
  /* padding-left: 50px; */
  font-weight: bold;
  width: 100%;
  display: inline;
}

section p {
  font-size: 18px;
  padding-top: 30px;
  margin-bottom: 30px;
}

.custom-text-menu {
  font-size: 36px;
}
</style>
