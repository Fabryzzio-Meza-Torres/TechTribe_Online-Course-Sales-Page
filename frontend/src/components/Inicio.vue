<template>
  <div>
    <main>
      <div class="principal-header" id="textdefault">
        <h1>
          Desarrolla tu <TextMenu /> y tu <strong>creatividad</strong>
          con nuestra educación tecnológica de vanguardia
        </h1>
      </div>

      <div class="button-container" id="botonmenuin">
        <button class="button">
          <a class="text-b" href="/register">Inscríbete ahora</a>
        </button>
      </div>
    </main>
    <footer>
      <p>&copy; TechTribe 2023</p>
    </footer>
  </div>
  <div class="area">
    <ul class="circles">
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>
</template>

<script>
import TextMenu from "./TextMenu.vue"; // Ruta relativa al archivo del componente TextMenu

export default {
  name: "MenuPri",
  components: {
    TextMenu, // Registra el componente TextMenu para usarlo en el template
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poppins&family=Roboto+Mono:wght@200&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Wix+Madefor+Text&display=swap");

/* Estilos para el body */
body {
  font-family: "Poppins", sans-serif;
  margin: 0;
  padding: 0;
  background-color: #11111f;
  color: white;
  background-repeat: no-repeat;
  background-size: cover;
}

.principal-header {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
  font-size: 30px;
}

main {
  padding: 64px;
  background: linear-gradient(186deg, #11111f, #0e0e24);
  min-height: 54vh;
}

h1 {
  display: block;
  font-size: 45px;
  margin-block-start: 0.67em;
  margin-block-end: 0.67em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
  width: 50%;
  text-align: center;
}

h1 strong {
  color: #4cbfdc;
}

strong {
  font-weight: bold;
}

.container {
  width: 100%;
  max-width: 100%;
  margin: 0;
}

.hcontainer {
  display: flex;
  background-image: linear-gradient(45deg, black, transparent);
  background-position: center center;
  background-color: #29293e;
  background-size: auto;
  background-size: cover;
  background-repeat: no-repeat;
  font-size: 50px;
  padding: 20px;
  min-height: 10rem;
  flex-direction: column;
}

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
}

.button {
  background-color: #23234400;
  font-family: "Wix Madefor Text", sans-serif;
  border-radius: 17px;
  color: white;
  border: none;
  cursor: pointer;
  border: 1px solid white;
  font-size: 1.2rem;
  padding: 1rem 2rem;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #1f1f2f;
}

.text-b {
  color: white;
  text-decoration: none;
}
footer {
  background: linear-gradient(186deg, #11111f, #0e0e24);
  color: #fff;
  text-align: center;
  padding: 20px;
}
* {
  margin: 0px;
  padding: 0px;
}

.context {
  width: 100%;
  position: absolute;
  top: 50vh;
}

.context h1 {
  text-align: center;
  color: #fff;
  font-size: 50px;
}

.area {
  background: #11111f;
  background: -webkit-linear-gradient(to left, #8f94fb, #4e54c8);
  width: 100%;
}

.circles {
  position: relative;
  bottom: -100px;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.circles li {
  position: absolute;
  display: block;
  list-style: none;
  width: 20px;
  height: 20px;
  background: rgba(255, 255, 255, 0.2);
  animation: animate 25s linear infinite;
  bottom: -150px;
}

.circles li:nth-child(1) {
  left: 25%;
  width: 80px;
  height: 80px;
  animation-delay: 0s;
}

.circles li:nth-child(2) {
  left: 10%;
  width: 20px;
  height: 20px;
  animation-delay: 2s;
  animation-duration: 12s;
}

.circles li:nth-child(3) {
  left: 70%;
  width: 20px;
  height: 20px;
  animation-delay: 4s;
}

.circles li:nth-child(4) {
  left: 40%;
  width: 60px;
  height: 60px;
  animation-delay: 0s;
  animation-duration: 18s;
}

.circles li:nth-child(5) {
  left: 65%;
  width: 20px;
  height: 20px;
  animation-delay: 0s;
}

.circles li:nth-child(6) {
  left: 75%;
  width: 110px;
  height: 110px;
  animation-delay: 3s;
}

.circles li:nth-child(7) {
  left: 35%;
  width: 150px;
  height: 150px;
  animation-delay: 7s;
}

.circles li:nth-child(8) {
  left: 50%;
  width: 25px;
  height: 25px;
  animation-delay: 15s;
  animation-duration: 45s;
}

.circles li:nth-child(9) {
  left: 20%;
  width: 15px;
  height: 15px;
  animation-delay: 2s;
  animation-duration: 35s;
}

.circles li:nth-child(10) {
  left: 85%;
  width: 150px;
  height: 150px;
  animation-delay: 0s;
  animation-duration: 11s;
}

@keyframes animate {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
    border-radius: 0;
  }

  100% {
    transform: translateY(-1000px) rotate(720deg);
    opacity: 0;
    border-radius: 50%;
  }
}
</style>
