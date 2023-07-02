<template>
  <div class="curso">
    <a class="imgCurso">
      <img :src="require('../assets/Cursos/python.jpg')" alt="imgCurso" />
    </a>
    <h2>Python</h2>
    <p>
      Domina Python y crea aplicaciones poderosas con nuestro curso. Sintaxis
      elegante, fácil de leer y recursos accesibles hacen que el aprendizaje sea
      divertido
    </p>
    <a class="BCurso">Ver curso</a>
  </div>
</template>
<script></script>
<style>
.curso {
  background-color: #e0115f;
  display: inline-block;
  width: 275px;
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
  border-radius: 5px;
}
.imgCurso img {
  display: block;
  width: 100%;
  height: 200px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.curso h2 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.curso p {
  font-size: 16px;
  line-height: 1.4;
  margin-bottom: 10px;
}

.BCurso {
  display: inline-block;
  padding: 8px 16px;
  background-color: black;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.BCurso:hover {
  background-color: #e0115f;
}
</style>
