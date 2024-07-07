<script setup>
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted } from 'vue';

import { defineProps } from 'vue';
const props = defineProps({
  contents: {
    type: Array,
    required: true
  }
});



// const page_max = props.contents.page_max
// let page_now = ref(parseInt(router.params.params2, 10));
// const host = router.params.options;


</script>










<script>
import { mdiNumeric1,
  mdiNumeric2,
  mdiNumeric3,
  mdiNumeric4,
  mdiNumeric5,
  mdiNumeric6,
  mdiNumeric7,
  mdiNumeric8,
  mdiNumeric9,
  // mdiNumeric1,
  mdiMinus,
  mdiFormatListNumbered,
} from '@mdi/js';


export default {
  data() {
    return {
      files: [
        {
          color: 'blue',
          icon: 'mdi-clipboard-text',
          subtitle: 'Jan 20, 2014',
          title: 'Vacation itinerary',
        },
        {
          color: 'amber',
          icon: 'mdi-gesture-tap-button',
          subtitle: 'Jan 10, 2014',
          title: 'Kitchen remodel',
        },
      ],
      folders: [
        {
          title: 'Photos',
        },
        {
          title: 'Recipes',
        },
        {
          title: 'Work',
        },
      ],
    }
  }
}
</script>



<template>
  <v-row no-gutters
  id="mokuji"

  >
    <v-col cols="11" class="mx-auto">

    <div class="d-flex my-bg-color-white">
      <v-btn variant="text" class="ms-auto me-0">
        目次を全て表示
      </v-btn>
    </div>


    <v-card
      class="mx-auto"
    >
      <v-toolbar class="my-bg-color">
        <v-toolbar-title class="text-center my-text-color-white">ー 目次 ー</v-toolbar-title>
      </v-toolbar>



      <v-list lines="two">
        <div class="d-flex my-4 mb-8">
          <a class="mx-auto text--lighten-1 my-text-size-20 font-weight-bold my-5">
            <!-- <v-icon class="">mdi-numeric-1</v-icon> -->
            コンビニ人間</a>
        </div>

        <v-list-item  
          v-for="(folder, index)  in folders"
          :key="folder.title"
          :subtitle="folder.subtitle"
          class="py-0"
          min-height="40"
        >


        <template v-slot:prepend>
          <v-card-title class="py-0">
            <v-icon color="black" class="mx-auto">mdi-numeric-1</v-icon>
            <v-icon :color="index === 0 ? 'white' : 'black'" class="mx-auto">mdi-minus</v-icon>
            <v-icon :color="index === 0 ? 'white' : 'black'" class="mx-auto">mdi-numeric-1</v-icon>
          </v-card-title>

          <v-list-item-title :class="index === 0 ? 'font-weight-black' : ''" v-if="index === 0">
            {{ folder.title }}
          </v-list-item-title>
          <v-list-item-title v-else>
            {{ folder.title }}
          </v-list-item-title>
          
        </template>
      </v-list-item>  
        
      <v-divider class="my-4"></v-divider>
      </v-list>
    </v-card>
  </v-col>
</v-row>

</template>