<template>
  <v-row no-gutters class="my-5">
    <v-col cols="12">
      <div tag="h2" class="text-h4 text-lg-h5 mb-1 py-10 text-center">
        <a class="my-border-color-gray my-border-bottom my-border-2">
        {{ text_2 }}
        </a>

      </div>
    </v-col>
  </v-row>
  <v-skeleton-loader></v-skeleton-loader>

</template>

<script setup lang='ts'>




defineProps({
  text_2: String
})
</script>
