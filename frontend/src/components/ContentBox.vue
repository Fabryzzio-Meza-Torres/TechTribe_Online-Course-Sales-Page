<template>
  <div class="containerbox" v-if="currentRoute === 'cursos'">
    <div v-for="curso in cursos" :key="curso.id" class="item-product">
      <a class="imgCompo">
        <img :src="getCursosImageUrl(curso.id)" alt="imgCurso" />
      </a>
      <h2>{{ curso.name }}</h2>
      <p>
        {{ curso.description }}
      </p>
      <p>Precio del curso: S/.{{ curso.price }}</p>
      <a class="BContainer">Ver curso</a>
    </div>
  </div>
  <div class="containerbox" v-else-if="currentRoute === 'asesorias'">
    <div v-for="asesoria in asesorias" :key="asesoria.id" class="item-product">
      <a class="imgCompo">
        <img :src="getAsesoriasImageUrl(asesoria.id)" alt="imgAsesoria" />
      </a>
      <h2>{{ asesoria.name }}</h2>
      <p>{{ asesoria.description }}</p>
      <p>Precio de la asesoría: S/.{{ asesoria.price }}</p>
      <a class="BContainer">Ver asesoría</a>
    </div>
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
import { getAllAsesorias } from "@/services/asesorias.api.js";
import { getAllCursos } from "@/services/cursos.api.js";
export default {
  name: "ContentBoxProduct",
  components: {},
  mounted() {
    this.loadCursos();
    this.loadAsesorias();
  },
  data() {
    return {
      cursos: [],
      asesorias: [],
    };
  },
  created() {
    this.loadCursos();
    this.loadAsesorias();
    console.log(this.cursos);
  },
  methods: {
    async loadCursos() {
      const data = await getAllCursos();
      if (data.data.success) {
        this.cursos = data.data.cursos;
      }
    },
    async loadAsesorias() {
      const data = await getAllAsesorias();
      if (data.data.success) {
        this.asesorias = data.data.asesorias;
      }
    },
    getCursosImageUrl(cursoName) {
      return require(`@/assets/Cursos/${cursoName}.jpg`);
    },
    getAsesoriasImageUrl(asesoriaName) {
      return require(`@/assets/Asesorias/${asesoriaName}.jpg`);
    },
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
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
}

.item-product {
  background-color: #e0115f;
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
