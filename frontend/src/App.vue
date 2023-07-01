<template>
  <div id="app">
    <NavBar />
  </div>
  <div id="app1">
    <MenuPri />
  </div>
</template>

<script setup>
import NavBar from "./components/Menu.vue";
import MenuPri from "./components/Inicio.vue";
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
body {
  font-family: "montserrat", sans-serif;
  background-color: #11111f;
  color: white;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
