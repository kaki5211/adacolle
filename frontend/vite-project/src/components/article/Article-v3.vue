<template>
    <v-card>  
      <v-container class="px-2 px-md-4">
          <v-card class="text-center elevation-0 py-10">
      <!-- <h2 class="text-grey-darken-1 font-weight-regular">
        Introducing new
      </h2> -->
  
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">フィルター</strong>
          </h2>

          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            <!-- FANZAの素人動画を厳選してピックアップ。 -->
          </div>

        </v-card>


    <div
      class="d-none d-xs-block"
    >
        <v-row
        >
  


<v-col cols="12">








            <!-- <v-btn
                    @click="resetSearchParams(searchparams, 'all') ;Data = filterVideo(ARTICLE_LIST, searchparams)"
                    text="全てクリア"          
                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                    color="red"
                    > -->


                    <!-- <div
                    class="ms-auto me-0 my-text-size-40"
                    >
                      全 
                      <a v-if="ARTICLE_LIST" class="text-red">{{ filterVideo(ARTICLE_LIST, searchparams).length || "0"}}</a>
                      件 表示
                    </div>                     -->

                    <!-- <v-chip-group
                                  v-model="searchparams.performers"
                                  column
                                  multiple
                                  color="text-deep-purple-accent-4"

                                  @click="Data = filterVideo(ARTICLE_LIST, searchparams);UpdateSearchParams(searchparams)"
                                > -->



                                <!-- <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'performers') ;Data = filterVideo(ARTICLE_LIST, searchparams)"
                                  text="アカウントをクリア"          
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  ></v-btn> -->



            <div class="d-flex py-2">
                  <div class="d-flex">
                    <div
                    class="ms-auto me-0"
                    >
                      全 
                      <a v-if="ARTICLE_LIST" class="text-red">{{ filteredData.length || "0"}}</a>
                      件 表示
                    </div>
                  </div>
                  <v-btn
                    @click="resetSearchParams(searchparams, 'all')"
                    text="全てクリア"  
                    class="ms-auto me-0 my-fit-contents text-caption ms-auto px-1 pl-2 d-flex align-center"
                    color="red"
                    size="small"
                    :prepend-icon="'mdi-close'"
                    >
                    <!-- mdi-close-circle-outline -->
                    <!-- mdi-close -->
                      <template v-slot:prepend>
                        <v-icon></v-icon>
                      </template>
                    </v-btn>


                </div>  


                  <!-- タグ -->
                  <v-card height="" class="my-bg-color-white" elevation=0>
                    <v-row no-gutters>
                      <v-col cols="12" class="border">
                        <v-btn small outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                        height="50px" @click="search_view_tag=!search_view_tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                          <v-row no-gutters class="my-auto">
                            <v-col cols="12" class="border px-2 py-5 pb-10">
                                <v-chip-group
                                  v-model="searchparams.tags"
                                  column
                                  multiple

                                >
                                    <v-chip
                                    v-for="item in ARTICLE_TAG_LIST"
                                    size="small"
                                    :key="item.id"
                                    label
                                    outline
                                    :value="item.article_tag_name_eng"
                                    color="red"

                                    
                                    class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                  >
                                    {{ item.article_tag_name }}
                                  </v-chip>
                                </v-chip-group>
                                <!-- {{searchparams.tags}} -->

                                <!-- <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'tags')"
                                  text="タグをクリア"
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  >
                                    <template v-slot:prepend>
                                      <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                    </template>
                                  </v-btn>
                                </div> -->
                            </v-col>
                          </v-row>
                      </v-col>
                    </v-row>
                  </v-card>

      </v-col>
        </v-row>
</div>









          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Mobile ■■■-->
          <!-- ■■■■■■■■■■■■■■ -->
        <v-row
          class="d-xs-none"
        >

  


<v-col cols="12">








            <!-- <v-btn
                    @click="resetSearchParams(searchparams, 'all') ;Data = filterVideo(ARTICLE_LIST, searchparams)"
                    text="全てクリア"          
                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                    color="red"
                    > -->


                    <!-- <div
                    class="ms-auto me-0 my-text-size-40"
                    >
                      全 
                      <a v-if="ARTICLE_LIST" class="text-red">{{ filterVideo(ARTICLE_LIST, searchparams).length || "0"}}</a>
                      件 表示
                    </div>                     -->

                    <!-- <v-chip-group
                                  v-model="searchparams.performers"
                                  column
                                  multiple
                                  color="text-deep-purple-accent-4"

                                  @click="Data = filterVideo(ARTICLE_LIST, searchparams);UpdateSearchParams(searchparams)"
                                > -->



                                <!-- <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'performers') ;Data = filterVideo(ARTICLE_LIST, searchparams)"
                                  text="アカウントをクリア"          
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  ></v-btn> -->



            <div class="d-flex py-2">
                  <div class="d-flex">
                    <div
                    class="ms-auto me-0"
                    >
                      全 
                      <a v-if="ARTICLE_LIST" class="text-red">{{ filteredData.length || "0"}}</a>
                      件 表示
                    </div>
                  </div>
                  <v-btn
                    @click="resetSearchParams(searchparams, 'all')"
                    text="全てクリア"  
                    class="ms-auto me-0 my-fit-contents text-caption ms-auto px-1 pl-2 d-flex align-center"
                    color="red"
                    size="small"
                    :prepend-icon="'mdi-close'"
                    >
                    <!-- mdi-close-circle-outline -->
                    <!-- mdi-close -->
                      <template v-slot:prepend>
                        <v-icon></v-icon>
                      </template>
                    </v-btn>


                </div>  

                  <!-- タグ -->
                  <v-card height="" class="my-bg-color-white" elevation=0>
                    <v-row no-gutters>
                      <v-col cols="12" class="border">
                        <v-btn small outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                        height="50px" @click="search_view_tag=!search_view_tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                          <v-row no-gutters class="my-auto">
                            <v-col cols="12" class="border px-2 py-5 pb-10">
                                <v-chip-group
                                  v-model="searchparams.tags"
                                  column
                                  multiple

                                >
                                    <v-chip
                                    v-for="item in ARTICLE_TAG_LIST"
                                    size="small"
                                    :key="item.id"
                                    label
                                    outline
                                    :value="item.article_tag_name_eng"
                                    color="red"

                                    
                                    class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                  >
                                    {{ item.article_tag_name }}
                                  </v-chip>
                                </v-chip-group>
                                <!-- {{searchparams.tags}} -->

                                <!-- <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'tags')"
                                  text="タグをクリア"
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  >
                                    <template v-slot:prepend>
                                      <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                    </template>
                                  </v-btn>
                                </div> -->
                            </v-col>
                          </v-row>
                      </v-col>
                    </v-row>
                  </v-card>

      </v-col>


  
        </v-row>
      </v-container>
    </v-card>
  </template>
  
<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
// const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
const ARTICLE_TAG_LIST = computed(() => { return store.getters.GET_ARTICLE_TAG_LIST; });

const currentIndex = ref(0)





import { watch } from 'vue'

const loading = ref(false)

watch(loading, (val) => {
  if (!val) return

  setTimeout(() => (loading.value = false), 2000)
})





// filter
const searchparams = ref({
  "tags":[],
  })

// filteredData
const filteredData = computed(() => {
  const tags = searchparams.value.tags;

  // 両方の条件が空の場合はすべてのビデオを返す
  if (tags.length === 0) {
    store.dispatch('FETCH_GET_ARTICLE_LIST_FILTERED', ARTICLE_LIST.value);
    return ARTICLE_LIST.value;
  }

  // タグでフィルタリング
  let temp = ARTICLE_LIST.value.filter(article => {
      const article_tags_list = article.article_tags.map(item => item.article_tag_name_eng);
      return tags.length === 0 || tags.every(tag => article_tags_list.includes(tag));
  });
  
  // storeに登録
  // store.commit("", temp)
  store.dispatch('FETCH_GET_ARTICLE_LIST_FILTERED', temp);

  return temp
});


function updateSearchParams(searchparams, item, kind) {
  if (!searchparams[kind]) {
    searchparams[kind] = [];
  }
  searchparams[kind].push(item);
}

function resetSearchParams(searchparams, kind) {
  if (kind === 'all') {
    for (const key in searchparams) {
      if (searchparams.hasOwnProperty(key)) {
        searchparams[key] = []; // すべてのキーを空の配列にリセット
      }
    }
  } else {
    searchparams[kind] = []; // 指定されたキーを空の配列にリセット
  }
}













  

const headers = ref([])
        // sortable: false,

// if (SUBCONTENTS.value === "performer") {
//   headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
//   headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
//   headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
// }

// if (SUBCONTENTS.value === "video") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
  headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
  headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
  headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
  headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });
// }

// if (SUBCONTENTS.value === "article") {
//   headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
//   headers.value.push({title: "大分類", align: 'start', key: 'classmajor', value: 'classmajor' });
//   headers.value.push({title: "中分類", align: 'start', key: 'classmedium', value: 'classmedium' });
//   headers.value.push({title: "小分類", align: 'start', key: 'classminor', value: 'classminor' });
  
// }












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
  