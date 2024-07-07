<template>
      <v-container class="px-2 px-md-4">
          <v-card class="text-center elevation-0 py-10">
      <!-- <h2 class="text-grey-darken-1 font-weight-regular">
        Introducing new
      </h2> -->
  
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">動画</strong>（FANZA 素人 ）
          </h2>

          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            FANZAの素人動画を厳選してピックアップ。
          </div>

        </v-card>
    <div
      class="d-none d-xs-block"
    >
        <v-row
        >
  


          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Window ■■■-->
          <!-- ■■■■■■■■■■■■■■ -->

        <div>

          <VDataTable
              v-if="ARTICLE_LIST"
              color="var(--my-color-black)"
              :loading="false"
              :items-per-page="-1"
              :headers="headers"
              :items="ARTICLE_LIST"
              item-value="name"
              class="elevation-1 custom-table"
              :items-per-page-options="[ {value: -1, title: 'All'} ]"
              items-per-page-text=""
              page-text=""
              next-icon=""
              prev-icon=""
              first-icon=""
              last-icon=""
              style="overflow-x: scroll; width: 100%; border-collapse: collapse; white-space: nowrap;"
            >
          <!-- 
            <template v-if="SUBCONTENTS === 'article' && ROUTE_PATH_LIST.length == 4" v-slot:item.title="{ item }">
              <router-link :to="{ name: 'ArticleList1', params: { param: item.classmajor, param2: item.classmedium, param3: item.classminor, param4: item.number} }">
                {{ item.title }}
              </router-link>
            </template> -->

            <!-- <template> -->
              <!-- <router-link :to="{ name: 'Article', params: { param: item.classmajor, param2: item.classmedium, param3: item.classminor, param4: item.number} }"> -->
                <!-- {{ item.title }} -->
              <!-- </router-link> -->
            <!-- </template> -->
              
            <!-- <template v-if="SUBCONTENTS === 'video'" v-slot:item.title="{ item }">
              <router-link :to="{ name: 'Video', params: { 'param': item.productnumber}}">
                  {{ item.title }}
                </router-link>
            </template>
            <template v-if="SUBCONTENTS === 'video'" v-slot:item.tags="{ item }">
              <a v-for="(item2, index) in item.tags" :key="item2.name" style="white-space: nowrap; overflow-x: auto">
                <a>{{ index > 0 && item.tags.length > 0 ? ', ' : '' }}</a>
                <router-link @click="PageTransition(searchparams, item2.name, 'tags')" :to="{ name: 'Videos', params: { 'param': item.name}}">
                  {{ item2.name }}
                </router-link>
              </a>
            </template>
            <template v-if="SUBCONTENTS === 'video'" v-slot:item.performers="{ item }">
              <a v-for="(item2, index) in item.performers" :key="item2.name" style="white-space: nowrap; overflow-x: auto">
                <a>{{ index > 0 && item.tags.length > 0 ? ', ' : '' }}</a>
                <router-link :to="{ name: 'Videos', params: { 'param': item.name}}">
                  {{ item2.name }}
                </router-link>
              </a>
            </template>
            <template v-if="SUBCONTENTS === 'video'" v-slot:item.maker="{ item }">
                  {{ item.maker != '' ? item.maker : '' }}
            </template> -->

            </VDataTable>
            </div>
  
        
        </v-row>
</div>









          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Mobile ■■■-->
          <!-- ■■■■■■■■■■■■■■ -->
        <v-row
          class="d-xs-none"
        >



        <div>

        </div>
  
  
        </v-row>
      </v-container>
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


@media (min-width: 480px) {
  .d-xs-none {
    display: none !important;
  }
  .d-xs-block {
    display: block;
  }
}

@media (min-width: 479.98px) {
  .d-xs-block {
    display: block !important;
  }
}

.my-underline {
  text-decoration: underline;
}
</style>
  