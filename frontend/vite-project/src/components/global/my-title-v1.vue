<template>
  <v-card >  
    <v-container class="px-2 px-md-4">
      <v-card class="text-center elevation-0 py-4 pb-3 py-md-8 pb-md-8">
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">{{ string_card_title_1 }}</strong>{{ string_card_title_2 }}
          </h2>
          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            {{ string_card_title_3 }}
          </div>
        </v-card>
    </v-container>
  </v-card>
</template>


<script lang="ts" setup>
// import { useStore } from 'vuex';
// import { computed, ref, reactive } from 'vue';
// import { useRoute } from 'vue-router';



// const store = useStore();
// const route = useRoute();








const props = defineProps({
  string_card_title_1: { type: String},
  string_card_title_2: { type: String},
  string_card_title_3: { type: String},
})








</script>


<style scoped>





</style>
