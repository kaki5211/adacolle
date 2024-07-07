<template>
  <v-card>  
    <v-container class="px-2 px-md-4">
      <v-card v-if="boolean_card_title" class="text-center elevation-0 py-10">
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">{{ string_card_title_1 }}</strong>{{ string_card_title_2 }}
          </h2>
          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            {{ string_card_title_3 }}
          </div>
        </v-card>

  <div
    class="d-none d-xs-block"
  >
      <v-row
      >

<v-col cols="12">








          <!-- <v-btn
                  @click="resetSearchParams(searchparams, 'all') ;Data = filterVideo(VIDEOS, searchparams)"
                  text="全てクリア"
                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                  color="red"
                  > -->


                  <!-- <div
                  class="ms-auto me-0 my-text-size-40"
                  >
                    全 
                    <a v-if="VIDEOS" class="text-red">{{ filterVideo(VIDEOS, searchparams).length || "0"}}</a>
                    件 表示
                  </div>                     -->

                  <!-- <v-chip-group
                                v-model="searchparams.performers"
                                column
                                multiple
                                color="text-deep-purple-accent-4"

                                @click="Data = filterVideo(VIDEOS, searchparams);UpdateSearchParams(searchparams)"
                              > -->



                              <!-- <div class="d-flex py-3">
                                <v-btn
                                @click="resetSearchParams(searchparams, 'performers') ;Data = filterVideo(VIDEOS, searchparams)"
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
                    <a v-if="filteredData" class="text-red">{{ filteredData.length || "0"}}</a>
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

                <!-- アカウント -->
                <v-row no-gutters>
                  <v-col cols="12">                 
                <v-card md="6" v-if="boolean_filter_account" height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn small outlined tile block class="my-text-color font-weight-medium rounded-b-0 elevation-0" color="primary"
                      height=""><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-1 pb-10">
                              <v-chip-group
                                v-model="searchparams.performers"
                                column
                                multiple
                                color="text-deep-purple-accent-4"

                              >
                                  <v-chip
                                  v-for="item in PERFORMER_LIST"
                                  size="small"
                                  :key="item.id"
                                  label
                                  outline
                                  :value="filter_account_list_name_eng(item)"
                                  color="red"
                                  class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                >
                                  {{ filter_account_list_name(item) }}
                                </v-chip>
                              </v-chip-group>
                          </v-col>
                          
                        </v-row>
                    </v-col>
                  </v-row>
                </v-card>
                </v-col>
                </v-row>

                <!-- タグ -->
                <v-card md="6" v-if="boolean_filter_tag" height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn small outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-b-0 elevation-0" color="primary"
                      height=""><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-1 pb-10">
                              <v-chip-group
                                v-model="searchparams.tags"
                                column
                                multiple
                                v-if="filter_tag_list"
                              >
                                  <v-chip
                                  v-for="(item, index) in filter_tag_list"
                                  size="small"
                                  :key="index"
                                  label
                                  outline
                                  :value="filter_tag_list_name_eng(item)"
                                  color="red"
                                  class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"
                                >
                                  {{ filter_tag_list_name(item) }}
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
                  @click="resetSearchParams(searchparams, 'all') ;Data = filterVideo(VIDEOS, searchparams)"
                  text="全てクリア"          
                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                  color="red"
                  > -->


                  <!-- <div
                  class="ms-auto me-0 my-text-size-40"
                  >
                    全 
                    <a v-if="VIDEOS" class="text-red">{{ filterVideo(VIDEOS, searchparams).length || "0"}}</a>
                    件 表示
                  </div>                     -->

                  <!-- <v-chip-group
                                v-model="searchparams.performers"
                                column
                                multiple
                                color="text-deep-purple-accent-4"

                                @click="Data = filterVideo(VIDEOS, searchparams);UpdateSearchParams(searchparams)"
                              > -->



                              <!-- <div class="d-flex py-3">
                                <v-btn
                                @click="resetSearchParams(searchparams, 'performers') ;Data = filterVideo(VIDEOS, searchparams)"
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
                    <!-- <a v-if="filteredData" class="text-red">{{ filteredData.length || "0"}}</a> -->
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

                <!-- アカウント -->
                <v-card v-if="boolean_filter_account" height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn small outlined tile block class="my-text-color font-weight-medium rounded-b-0 elevation-0" color="primary"
                      height=""><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-1 pb-10">
                              <v-chip-group
                                v-model="searchparams.performers"
                                column
                                multiple
                                color="text-deep-purple-accent-4"
                                
                              >
                                  <v-chip
                                  v-for="item in PERFORMER_LIST"
                                  @clock=" store.commit('SET_SEARCHPARAMS_VIDEO', { value: { tags: [], performers: [searchparams.performers] } })"
                                  size="small"
                                  :key="item.id"
                                  label
                                  outline
                                  :value="filter_account_list_name_eng(item)"
                                  color="red"
                                  class="custom-chip-style mx-0 mb-1 mt-0 elevation-1 px-2"

                                >
                                {{ filter_account_list_name(item) }}
                              </v-chip>
                              </v-chip-group>
                              <!-- {{searchparams.performers}} -->

                              <!-- <div class="d-flex py-3">
                                <v-btn
                                @click="resetSearchParams(searchparams, 'performers')"
                                text="アカウントをクリア"
                                class="ms-auto me-0 my-fit-contents"
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


                <!-- タグ -->
                <v-card v-if="boolean_filter_tag" height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn small outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-b-0 elevation-0" color="primary"
                      height=""><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-1 pb-10">
                              <v-chip-group
                                v-model="searchparams.tags"
                                column
                                multiple
                                v-if="filter_tag_list"
                              >
                                  <v-chip
                                  v-for="(item, index) in filter_tag_list"
                                  size="small"
                                  :key="index"
                                  label
                                  outline
                                  :value="filter_tag_list_name_eng(item)"
                                  color="red"
                                  class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"
                                >
                                  {{ filter_tag_list_name(item) }}
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
  {{ ARTICLE_LIST_FILTERED }}
  {{ searchparams }}
</template>

<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref, reactive } from 'vue';
import { useRoute } from 'vue-router';



const store = useStore();
const route = useRoute();

const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const ARTICLE_TAG_LIST = computed(() => { return store.getters.GET_ARTICLE_TAG_LIST; });

const VIDEOS_FILTERED = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });
const ARTICLE_LIST_FILTERED = computed(() => { return store.getters.GET_ARTICLE_LIST_FILTERED; });

console.log("VIDEOS_FILTERED", VIDEOS_FILTERED)
console.log("ARTICLE_LIST_FILTERED", ARTICLE_LIST_FILTERED)



const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });



const currentIndex = ref(0)




import { watch, watchEffect } from 'vue'

// const loading = ref(false)

// watch(loading, (val) => {
// if (!val) return

// setTimeout(() => (loading = false), 2000)
// })


const props = defineProps({
  kind: { type: String},
  boolean_card_title: { type: Boolean},
  string_card_title_1: { type: String},
  string_card_title_2: { type: String},
  string_card_title_3: { type: String},
  my_card_list: { type: Object},
  boolean_filter_account: { type: Boolean},
  boolean_filter_tag: { type: Boolean},
  
// const kind = "article"
// const boolean_card_title = true
// const string_card_title_1 = "記事"
// const string_card_title_2 = "（ ブログ ）"
// const string_card_title_3 = ""

  
  // item: { type: Object},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},

});
store.dispatch('FETCH_GET_VIDEOS_FILTERED');




let searchparams=ref({
      "tags":[],
      "performers": []
});
let filteredData=ref([]);
if(props.kind=="video"){
  // searchparams = computed(() => { return store.getters.GET_SEARCHPARAMS_VIDEO; });
  filteredData = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });
}else if(props.kind=="article"){
  // searchparams = computed(() => { return store.getters.GET_SEARCHPARAMS_ARTICLE; });
  filteredData = computed(() => { return store.getters.GET_ARTICLE_LIST_FILTERED; });
}






// const searchparams = ref({
//       "tags":[],
//       "performers": []
//     })

// クエリパラメータのウォッチ
watch(
  () => route.query,
  (newQuery) => {
      // クエリパラメータが変更されたときにsearchparamsを更新
      searchparams.value.tags = newQuery.tag ? [newQuery.tag] : [];
      searchparams.value.performers = newQuery.performer ? [newQuery.performer] : [];

      if (props.kind=="video") {
        // store.commit('SET_SEARCHPARAMS_VIDEO',{ tags: [newQuery.tag], performers: [newQuery.performer] } );
        store.dispatch('FETCH_GET_SEARCHPARAMS_VIDEO', { tags: searchparams.value.tags, performers: searchparams.value.performers });
      } else if (props.kind=="article") {
        // store.commit('SET_SEARCHPARAMS_ARTICLE',{ tags: [searchparams.value.performers]} );
        store.dispatch('FETCH_GET_SEARCHPARAMS_ARTICLE', { tags: searchparams.value.tags });

      }
  },
  // { immediate: true }
);

watch(
  () => [searchparams.value.tags, searchparams.value.performers],
  (newQuery) => {
      // クエリパラメータが変更されたときにsearchparamsを更新
      // searchparams.value.tags = newQuery.tag ? [newQuery.tag] : [];
      // searchparams.value.performers = newQuery.performer ? [newQuery.performer] : [];

      if (props.kind=="video") {
        // store.commit('SET_SEARCHPARAMS_VIDEO',{ tags: [newQuery.tag], performers: [newQuery.performer] } );
        store.dispatch('FETCH_GET_SEARCHPARAMS_VIDEO', { tags: searchparams.value.tags, performers: searchparams.value.performers });
      } else if (props.kind=="article") {
        // store.commit('SET_SEARCHPARAMS_ARTICLE',{ tags: [searchparams.value.performers]} );
        store.dispatch('FETCH_GET_SEARCHPARAMS_ARTICLE', { tags: searchparams.value.tags });
      }
  },
  // { immediate: true }
);





const key = ref(route.fullPath); // コンポーネントをリロードするためのキー
watch(
  () => route.fullPath,
  (newFullPath) => {
    key.value = newFullPath; // フルパスが変更されたときにキーを更新
  }
);



function updateSearchParams(searchparams, item, kind) {
if (!searchparams[kind]) {
  searchparams[kind] = [];
}
searchparams[kind].push(item);
}

function resetSearchParams(searchparams, kind) {
if (kind === 'all') {
  // for (const key in searchparams) {
  //   if (searchparams.value.hasOwnProperty(key)) {
  //     searchparams[key] = []; // すべてのキーを空の配列にリセット
  //   }
  // }
    // searchparams.value = {
    //   "tags":tags,
    //   "performers": performers
    // };

  if (props.kind=="video") {
    searchparams.tags = [];
    searchparams.performers = [];
    store.dispatch('FETCH_GET_SEARCHPARAMS_VIDEO', searchparams );
  } else if (props.kind=="article") {
    searchparams.tags = [];
    store.dispatch('FETCH_GET_SEARCHPARAMS_ARTICLE', searchparams );
  }
} else {
  console.log("error")
  // searchparams[kind] = []; // 指定されたキーを空の配列にリセット
}
}


const filter_tag_list = computed(() => {
  console.log("props.kind", props.kind)
  if (props.kind === 'video') {
    return TAG_LIST.value
  } else if (props.kind === 'article') {
    return ARTICLE_TAG_LIST.value
  } else {
    return 'error'
  }
})



function filter_tag_list_name_eng(item) {
  console.log(item)
  if (props.kind === 'video') {
    return item.name_eng;
  } else if (props.kind === 'article') {
    return item.article_tag_name_eng;
  } else {
    return 'error';  // デフォルト
  }
}

function filter_tag_list_name(item) {
  if (props.kind === 'video') {
    return item.name;
  } else if (props.kind === 'article') {
    return item.article_tag_name;
  } else {
    return 'error';  // デフォルト
  }
}

function filter_account_list_name_eng(item) {
  if (props.kind === 'video') {
    return item.name_eng;
  } else if (props.kind === 'article') {
    return "error";
  } else {
    return 'error';  // デフォルト
  }
}

function filter_account_list_name(item) {
  if (props.kind === 'video') {
    return item.name;
  } else if (props.kind === 'article') {
    return 'error';
  } else {
    return 'error';  // デフォルト
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
