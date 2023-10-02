<template>
  <div class="containerbox" v-if="currentRoute === 'cursos'">
    <div v-for="curso in cursos" :key="curso.id" class="item-product">
      <a class="imgCompo">
        <img :src="getCursosImageUrl(curso.name)" alt="imgCurso" />
      </a>
      <h2>{{ curso.name }}</h2>
      <p>
        {{ curso.description }}
      </p>
      <p>Precio del curso: S/.{{ curso.price }}</p>
      <button class="boton">
        <a
          ><router-link to="/transactions" class="link"
            >Compra aqui</router-link
          ></a
        >
      </button>
    </div>
  </div>
  <div class="containerbox" v-else-if="currentRoute === 'asesorias'">
    <div v-for="asesoria in asesorias" :key="asesoria.id" class="item-product">
      <a class="imgCompo">
        <img :src="getAsesoriasImageUrl(asesoria.name)" alt="imgAsesoria" />
      </a>
      <h2>{{ asesoria.name }}</h2>
      <p>{{ asesoria.description }}</p>
      <p>Precio de la asesoría: S/.{{ asesoria.price }}</p>
      <button class="boton">
        <a
          ><router-link to="/transactions" class="link"
            >Compra aqui</router-link
          ></a
        >
      </button>
    </div>
  </div>
  <div class="containerboxprof" v-else-if="currentRoute === 'profesores'">
    <div
      v-for="profesor in profesores"
      :key="profesor.id"
      class="item-profesor"
    >
      <div id="worker_1" class="workers">
        <div class="worker">
          <span class="name">{{ profesor.firstname }}</span
          ><span class="surname">{{ profesor.lastname }}</span>
        </div>
      </div>
      <a class="imgCompo">
        <img
          :src="getProfesoresImageUrl(profesor.lastname)"
          alt="imgProfesor"
        />
      </a>
      <p>Contenido que dicta:</p>
      <div
        v-if="
          getProductByProfesores(profesor.producto_id).length > 0 ||
          getAsesoriaByProfesores(profesor.producto_id).length > 0
        "
      >
        <p
          v-for="curso in getProductByProfesores(profesor.producto_id)"
          :key="curso.id"
          class="cursoProfesor"
        >
          {{ curso.name }}
        </p>
        <p
          v-for="asesoria in getAsesoriaByProfesores(profesor.producto_id)"
          :key="asesoria.id"
          class="cursoProfesor"
        >
          {{ asesoria.name }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { getAllAsesorias } from "@/services/asesorias.api.js";
import { getAllCursos } from "@/services/cursos.api.js";
import { getAllProfesores } from "@/services/profesores.api.js";
export default {
  name: "ContentBoxProduct",
  components: {},
  mounted() {
    this.loadCursos();
    this.loadAsesorias();
    this.loadProfesores();
  },
  data() {
    return {
      cursos: [],
      asesorias: [],
      profesores: [],
    };
  },
  created() {
    this.loadCursos();
    this.loadAsesorias();
    this.loadProfesores();
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
    async loadProfesores() {
      const data = await getAllProfesores();
      if (data.data.success) {
        this.profesores = data.data.profesores;
      }
    },
    getCursosImageUrl(cursoName) {
      if (cursoName == "HTML/CSS") {
        return require(`@/assets/Cursos/HTMLCSS.jpg`);
      } else {
        return require(`@/assets/Cursos/${cursoName}.jpg`);
      }
    },
    getAsesoriasImageUrl(asesoriaName) {
      if (asesoriaName == "HTML/CSS") {
        return require(`@/assets/Asesorias/HTMLCSS.jpg`);
      } else {
        return require(`@/assets/Asesorias/${asesoriaName}.jpg`);
      }
    },
    getProfesoresImageUrl(profesorName) {
      return require(`@/assets/Profesores/${profesorName}.png`);
    },
    getProductByProfesores(profesor_producto_id) {
      return this.cursos.filter((curso) => curso.id === profesor_producto_id);
    },
    getAsesoriaByProfesores(profesor_producto_id) {
      return this.asesorias.filter(
        (asesoria) => asesoria.id === profesor_producto_id
      );
    },
    comprar(id) {
      this.$router.push({ name: "compra", params: { id: id } });
      console.log(id);
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

.containerboxprof {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
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
  justify-content: right;
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

.item-profesor {
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

.boton {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
  background-color: goldenrod;
  color: #fff;
  margin: 0;
}
</style>
