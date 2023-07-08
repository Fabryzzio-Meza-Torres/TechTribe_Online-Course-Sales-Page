<template>
  <div id="app">
    <NavBar />
  </div>
</template>

<script setup>
import NavBar from "./components/Menu.vue";
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

header {
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
