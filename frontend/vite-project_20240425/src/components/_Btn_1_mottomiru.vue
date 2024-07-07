<template>
  <v-row no-gutters class="my-5">
        <v-col cols="12" class="d-flex my-5 pt-15 my-fit-contents">
          <v-btn
            color="var(--my-color-green)"
            class="mx-auto px-6 py-4 text-center text-h3 my-fit-contents"
            variant="outlined"
            prepend-icon=""
            rounded=""
            append-icon=""
            size="x-large"
            :to="{name: href}"
            >
            {{ text }}

          </v-btn>
        </v-col>
  </v-row>
  <v-skeleton-loader></v-skeleton-loader>

</template>

<script setup lang='ts'>




defineProps({
  text: String,
  href: String
})
</script>
