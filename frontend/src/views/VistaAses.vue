<template>
  <div class="textinit">
    <TextSec />
  </div>
  <div class="containercurso">
    <ContextBox />
  </div>
</template>

<script setup>
import TextSec from "@/components/TextSec.vue";
import ContextBox from "@/components/ContentBox.vue";
</script>

<style>
.containercurso {
  display: block;
  padding-left: 50px;
}
.textinit {
  padding-left: 50px;
}
</style>
