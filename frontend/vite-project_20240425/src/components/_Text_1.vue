<template>
  <v-row no-gutters class="mb-10">
    <v-col cols="12" class="pt-16">
      <div tag="h2" class="text-h2 text-lg-h4 mb-1 py-15 text-center font-weight-bold">
        ―&emsp;{{ text_1 }}&emsp;―
      </div>
    </v-col>
  </v-row>
</template>

<script setup lang='ts'>




defineProps({
  text_1: String
})
</script>
