<template>
  <div class="containerbox" v-if="currentRoute === 'cursos'">
    <li v-for="product in products" :key="product.id">
      {{ product.name }} - {{ product.price }}
    <a class="imgCompo">
      <img :src="require('../assets/Cursos/python.jpg')" alt="imgCurso" />
    </a>
    <h2>Python</h2>
    <p>
      Domina Python y crea aplicaciones poderosas con nuestro curso. Sintaxis
      elegante, fácil de leer y recursos accesibles hacen que el aprendizaje sea
      divertido
    </p>
    <p>Precio: ${{ precio }}</p>
    <a class="BContainer">Ver curso</a>
  </li>
  </div>
  <div class="containerbox" v-else-if="currentRoute === 'asesorias'">
    <a class="imgCompo">
      <img
        :src="require('../assets/Asesorias/asesoria.jpg')"
        alt="imgAsesoria"
      />
    </a>
    <h2>Asesoria de Python</h2>
    <p>
      Domina Python con asesoría experta. Código eficiente, soluciones creativas
      y proyectos destacados. Desarrolla tu potencial en programación.
    </p>
    <p>Precio: ${{ precio }}</p>
    <a class="BContainer">Ver Asesoria</a>
  </div>
  <div class="containerprof" v-else-if="currentRoute === 'profesores'">
    <div id="worker_1" class="workers">
      <div class="worker">
        <span class="name">Marvin </span><span class="surname">Abisrror</span>
      </div>
    </div>
    <a class="imgCompo">
      <img
        :src="require('../assets/Profesores/Marvin_Abisrror.png')"
        alt="imgProfesor"
      />
    </a>
    <p>
      Ingeniero de Sistemas con Maestría en Ciencias de la Computación y
      especialidad en Búsquedas Heurísticas.
    </p>
  </div>
</template>

<script>
export default {
  name: "ContentBoxProduct",
  props: {
    products:{
      type: Array,
      required: true,
    }
  },
  computed: {
    currentRoute() {
      return this.$route.name;
    },
  },
};
</script>
<style>
.containerbox {
  background-color: #e0115f;
  display: inline-block;
  width: 275px;
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
  border-radius: 5px;
}

.imgCompo img {
  display: block;
  width: 100%;
  height: 200px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.containerbox h2 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.containerbox p {
  font-size: 16px;
  line-height: 1.4;
  margin-bottom: 10px;
}

.BContainer {
  display: inline-block;
  padding: 8px 16px;
  background-color: black;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.BContainer:hover {
  background-color: #e0115f;
}

.containerprof {
  margin: 25px;
  height: 340px;
  width: 275px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  flex-direction: column;
  padding: 35px;
  border-radius: 8px;
  background: linear-gradient(to bottom, #2c3e50, #1a252f);
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.5;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.worker {
  display: inline-block;
  padding: 20px;
  border-radius: 8px;
  background: linear-gradient(to bottom, #2c3e50, #1a252f);
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.5;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
}

.containerprof img {
  width: 200px;
  height: auto;
  margin-bottom: 10px;
}

.containerprof:hover {
  transform: translateY(-10px);
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}

.containerprof p {
  line-height: 1.5;
  text-align: center;
}
</style>
