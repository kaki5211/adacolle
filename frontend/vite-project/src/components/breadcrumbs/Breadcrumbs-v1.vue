<template>
    <v-card class="py-1">
      <v-container class="px-1 px-md-3 py-0">
          <v-card class="text-center elevation-0 py-0 text-h4">




          <div class="pl-1 py-0">
            <v-breadcrumbs
              v-if="breadcrumbsList"
              :items="breadcrumbsList"
              color="var(--my-color-white)"
              bg-color="var(--my-color)"
              class="custom-breadcrumbs py-1"
              style="white-space: nowrap; overflow-x: auto"
              :to="breadcrumbsList"
            >
                <template v-slot:divider>
                  <v-icon
                    color="var(--my-color-white)"
                    icon="mdi-chevron-right"
                    size="30"
                    class=""
                  ></v-icon>
                </template>
                <template v-slot:prepend>
                  <v-icon
                    color="var(--my-color-white)"
                    size="30"
                    icon="mdi-home"
                    class="pr-3"
                  ></v-icon>
                </template>
              </v-breadcrumbs>
              
            </div>

        </v-card>

      </v-container>
    </v-card>
  </template>
  


<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });

const currentIndex = ref(0)

import { watch } from 'vue'

const loading = ref(false)

watch(loading, (val) => {
  if (!val) return
  setTimeout(() => (loading.value = false), 2000)
})

const breadcrumbsList = computed(() => { return store.getters.GET_BREADCRUMBS; })


</script>






<style scoped>
.aspect-ratio-block {
  background: #ccc;
  aspect-ratio: 3 / 2;
  /* aspect-ratio: 1; */
}

.my-fit-contents {
  width: fit-content;
  height: fit-content;
  }

  .text-h6 {
  font-size: 1.25rem !important;
  font-weight: 500;
  line-height: 2rem;
  letter-spacing: 0.0125em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

  .text-h7 {
  font-size: 1.125rem !important;
  font-weight: 500;
  line-height: 1.75rem;
  letter-spacing: 0.0107142857em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

.text-h8 {
  font-size: 1rem !important;
  font-weight: 500;
  line-height: 1.5rem;
  letter-spacing: 0.01em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

.text-h9 {
  font-size: 0.875rem !important;
  font-weight: 400;
  line-height: 1.25rem;
  letter-spacing: 0.0085em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}







</style>
  

<style>


.v-breadcrumbs a{
  font-size: 1.125rem !important;
  font-weight: 500;
  line-height: 1.75rem;
  letter-spacing: 0.0107142857em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}



.custom-breadcrumbs .v-breadcrumbs__item {
    font-size: 20px; /* フォントサイズを設定 */
    white-space: pre-wrap; /* 折り返しを有効に */
  }
  .custom-breadcrumbs {
    display: flex;
    flex-wrap: wrap; /* 項目が自然に折り返されるように */
  }

.v-breadcrumbs-divider{
  display: inline-block;
  padding: 0 0px;
  vertical-align: middle;

}
</style>
