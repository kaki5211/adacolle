<template>

    <v-row no-gutters class="my-5 d-flex">
      <v-col cols="11" class="mx-auto my-fit-contents">
        <div id="" class="my-text-color mx-auto px-0 pt-5 pt-lg-10 pb-3 pb-lg-5 text-left my-w-100">
          <a class="d-inline-block font-weight-black my-text-color text-h5_5 text-md-h4 mb-0 mt-auto pr-2">
            {{text}}
          </a>
      </div>
    </v-col>
  </v-row>

</template>

<script setup lang='ts'>




defineProps({
  text: String,
  // index: Int8Array
  // href: String
})
</script>
