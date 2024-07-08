<template>
  <v-main>
    <v-container class="px-2 pb-0">
      <Breadcrumbs />
    </v-container>

    <router-view />

    <v-container class="px-2 pt-0">
      <FooterMyV2 />
    </v-container>    
  </v-main>
</template>

<script setup>
import Breadcrumbs from '@/components/breadcrumbs/Breadcrumbs-v1.vue'
import FooterMyV2 from '@/components/footer/Footer-my-v2.vue'



</script>

<style>

@media (min-width: 1600px) {
    .v-container {
      max-width: 1500px;
    }
  }

</style>