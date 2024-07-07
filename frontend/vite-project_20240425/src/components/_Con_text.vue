<template>

    <v-row no-gutters class="my-5 d-flex">
      <v-col cols="11" class="mx-auto my-fit-contents">
        <div class="px-0 py-7 py-lg-10 text-left" style="word-break: break-all;">
          <a class="text-my-text-color text-h5 text-md-h4 mb-0">
              {{text}}
          </a>
      </div>
    </v-col>
  </v-row>

</template>

<script setup lang='ts'>




defineProps({
  text: String,
  // href: String
})
</script>
