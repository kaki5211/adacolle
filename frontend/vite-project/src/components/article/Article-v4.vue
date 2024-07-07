<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
// import { beforeRouteUpdate } from 'vuex';

import { computed } from 'vue';
import { ref, onMounted,reactive, watch } from 'vue';


// import VDataTable from '../../node_modules/vuetify/lib/labs/VDataTable/index.mjs';
// import { VDataTable } from '@vuetify/nightly';
import { VDataTable,
  VDataTableServer,
  VDataTableVirtual, } from 'vuetify/labs/VDataTable'


// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'




const route = useRoute();
const store = useStore();

// 必要なら最初に定義する

let VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
const MAKER_LIST = computed(() => { return store.getters.GET_MAKER_LIST; });
const LABEL_LIST = computed(() => { return store.getters.GET_LABEL_LIST; });
const SERIES_LIST = computed(() => { return store.getters.GET_SERIES_LIST; });
const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
const VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });
const URL_PARAM = computed(() => { return store.getters.GET_URL_PARAM; });
const URL_JUDGE_PARAM = computed(() => { return store.getters.GET_URL_JUDGE_PARAM; });
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
const Data = ref()
const SUBCONTENTS_ALL = computed(() => { 
  const item = store.getters.GET_SUBCONTENTS_ALL
  Data.value = item
  return item;
 });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
let SEARCHPARAMS =computed(() => { return store.getters.GET_SEARCHPARAMS; });
let SEARCHPARAMS_ARTICLE =computed(() => { return store.getters.GET_SEARCHPARAMS_ARTICLE; });
const ARTICLE_LIST_DUP =computed(() => { return store.getters.GET_ARTICLE_LIST_DUP; });
const ARTICLE_LIST_PARAMS =computed(() => { return store.getters.GET_ARTICLE_LIST_PARAMS; });


// store.dispatch('FETCH_GET_BREADCRUMBS')



// ■■■ 関数定義 ■■■
// filterVideo
function filterVideo(data, searchparams) {
  let filteredData = data; // オリジナルのデータを変更せずにコピーを作成
  for (let key in searchparams) {
    const filterValue = searchparams[key];
    if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
      if (key === "tags" || key === "performers") {
        if (Array.isArray(filterValue) && filterValue.length !== 0) {
          filteredData = filteredData.filter(item => {
            return item[key].some(item2 => filterValue.includes(item2.name));
          });
        }
      }
    }
  }  return filteredData;
}

// filterArticle
function filterArticle(data, searchparamsarticle) {
  let filteredData = data; // オリジナルのデータを変更せずにコピーを作成
  for (let key in searchparamsarticle) {
    const filterValue = searchparamsarticle[key];
    if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
      if (true) {
        // if (Array.isArray(filterValue) && filterValue.length !== 0) {
        if (Array.isArray(filterValue) && filterValue.length !== 0) {
          filteredData = filteredData.filter(item => {
            return filterValue.includes(item[key]);
          });
        }
      }
    }
  }  return filteredData;
}

// resetSearchParams
function resetSearchParams(searchparams, item) {
    if (item == "all") {
      for (let prop in searchparams) {
        searchparams[prop] = [];
      }
    } else {
      searchparams[item] = [];
    }
  }

// UpdateSearchParams
const UpdateSearchParams = (searchparams) => {
  store.commit('SET_SEARCHPARAMS', searchparams);
}

// resetSearchParams
const PageTransition = (searchparams, item, judge) => {
  for (let prop in searchparams) {
      searchparams[prop] = [];
      if (prop==judge) {
        searchparams[prop] = item;
      }
    }
  console.log(searchparams)
  UpdateSearchParams(searchparams)
}



// ■■■ watch 定義 ■■■
//  filteredData filteredDataArticle
// let filteredData=ref([])
// let filteredDataArticle=ref([])
// watch(SEARCHPARAMS, (newVal, oldVal) => {
//   if (newVal != null) {
//     if (VIDEOS.value) {
//       filteredData.value = filterVideo(VIDEOS.value, newVal)
//     } else {
//       watch(VIDEOS, (newVal2, oldVal2) => {
//         filteredData.value = filterVideo(newVal2, newVal)
//       })
//     }
//   }
// })
// watch(SEARCHPARAMS_ARTICLE, (newVal, oldVal) => {
//   if (newVal != null) {
//     if (ARTICLE_LIST_DUP.value) {
//       filteredDataArticle.value = filterArticle(ARTICLE_LIST_DUP.value, newVal)

//     } else {
//       watch(ARTICLE_LIST_DUP, (newVal2, oldVal) => {
//         filteredDataArticle.value = filterArticle(newVal2, newVal)
//       })
//     }
//     }
//   }
// )



// 2023-10-28 問題箇所　（searchparamsが、コンポーネント間でやり取りできない）
// if (VIDEOS.value && SEARCHPARAMS.value) {
//   filteredData = filterVideo(VIDEOS.value, SEARCHPARAMS.value) 
// }

// if (ARTICLE_LIST_DUP.value && SEARCHPARAMS_ARTICLE.value) {
//   filteredDataArticle = filterArticle(ARTICLE_LIST_DUP.value, SEARCHPARAMS_ARTICLE.value)
// }




// params
let articleparams = ARTICLE_LIST_PARAMS
let searchparamsarticle = SEARCHPARAMS_ARTICLE



// let articleparams = ref({
//     classmajor: [],
//   classmedium: [],
//   classminor: [],
// })
// let searchparamsarticle = ref({
//   classmajor: [],
//   classmedium: [],
//   classminor: [],
// })
// watch(ARTICLE_LIST_PARAMS, (newVal, oldVal) => {
//   if (newVal != null) {
//     if (SEARCHPARAMS_ARTICLE.value) {
//       articleparams.value = ARTICLE_LIST_DUP.value
//       searchparamsarticle.value = SEARCHPARAMS_ARTICLE.value

//     }
//   }
// })







// ■■■　その他定義　■■■
let searchparams = ref()
if (SEARCHPARAMS) { searchparams = SEARCHPARAMS }
let SUBCONTENTS = ref(route.path.split("/")[1])


// let SUBCONTENTS_ALL = ref()
// if (SUBCONTENTS.value === "performer") { SUBCONTENTS_ALL = PERFORMER_LIST }
// else if (SUBCONTENTS.value === "tag") { SUBCONTENTS_ALL = TAG_LIST }
// else if (SUBCONTENTS.value === "video") { SUBCONTENTS_ALL = VIDEOS }
// else if (SUBCONTENTS.value === "article") { SUBCONTENTS_ALL = ARTICLE_LIST_DUP }


let headers_name = ref("");
if (SUBCONTENTS.value === "actor") { headers_name.value = "アクター"; } 
else if (SUBCONTENTS.value === "performer") { headers_name.value = "パフォーマー"; }
else if (SUBCONTENTS.value === "video") { headers_name.value = "動画"; }
else if (SUBCONTENTS.value === "article") { headers_name.value = "記事"; }







const search_view_performer = ref(true)
const search_view_tag = ref(true)
















  

const headers = ref([])
        // sortable: false,

if (SUBCONTENTS.value === "performer") {
  headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
  headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
  headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
}

if (SUBCONTENTS.value === "video") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
  headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
  headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
  headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
  headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });
}

if (SUBCONTENTS.value === "article") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "大分類", align: 'start', key: 'classmajor', value: 'classmajor' });
  headers.value.push({title: "中分類", align: 'start', key: 'classmedium', value: 'classmedium' });
  headers.value.push({title: "小分類", align: 'start', key: 'classminor', value: 'classminor' });
  

  // headers.value.push({title: "項目", align: 'start', key: 'classmedium', value: 'classmedium' });



}


const showFilter = ref(true)
const tollgeFilter = () => {
  showFilter.value = !showFilter.value;
}






const ARTICLE_CLASS = ref(route.path.split("/").slice(2))
const ROUTE_PATH_LIST = ref(route.path.split("/"))
console.log("ROUTE_PATH_LIST", ROUTE_PATH_LIST.value.length)


console.log("ARTICLE_CLASSARTICLE_CLASS", ARTICLE_CLASS)


// function calculateAge(birthDate) {
//   const today = new Date();
//   const birthDateParts = birthDate.split('-');
//   const birthYear = Number(birthDateParts[0]);
//   const birthMonth = Number(birthDateParts[1]) - 1;
//   const birthDay = Number(birthDateParts[2]);

//   let age = today.getFullYear() - birthYear;
//   console.log("today.getFullYear()", today.getFullYear())
//   console.log("birthYear", birthYear)
//   console.log("age1", age)

//   if (today.getMonth() < birthMonth || (today.getMonth() === birthMonth && today.getDate() < birthDay)) {
//     age--;
//   }
//   console.log("age2", age)

//   return age;
// }

// for (let i = 0; i < SUBCONTENTS_ALL.value.length; i++) {
//   const item = SUBCONTENTS_ALL.value[i];
//   const age = calculateAge(item.birth);

//   item.age = age;
// }








// ARTICLE_LIST_DUP.value = filterArticle(ARTICLE_LIST_DUP.value, searchparamsarticle)

// 




const ARTICLE_DETEAL_TITLE = ref("")






</script>


<script lang="ts">
import { defineComponent } from 'vue'
import GlobalStyles from '../components/_GlobalStyles.vue';
import { Icon } from '@iconify/vue';
import Text_1 from '../components/_Text_1.vue';



export default defineComponent({
  name: 'App',
  components: {
    GlobalStyles,
		Icon,
    Text_1,
    VDataTable,
    VDataTableServer,
    VDataTableVirtual,
    // VideoPlayer,
  },
  data () {
    return {

      itemsPerPage: 5,
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
      sortBy: 'fat',
      sortDesc: false,
      playerOptions: {
        autoplay: false, // 自動再生
        controls: true, // コントロール表示
        sources: [
          {
            src: 'http://www.youtube.com/embed/cvj3-MZO9T', // 動画のURL
            // type: 'video/mp4', // 動画の形式
          },
        ],
      },
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ],
    tab: null,
    }    
  },
  methods: {
  parseJson(value) {
    return JSON.parse(value.replace(/'/g, '"'));
  },
  playVideo() {
      const videoPlayer = this.$refs.videoPlayer;
      videoPlayer.play();
  },

  handleTouchStart(event, i, Index) {
    this.startX = event.touches[0].clientX;
    this.startIndex = this.model[i];
  },
  handleTouchMove(event, i, images) {
    const touch = event.touches[0];
    const distance = touch.clientX - this.startX;
    let changeindex = 0;
    changeindex = parseInt(distance / 100, 10);

    this.model[i] = (this.startIndex + changeindex + (images * 50)) % images
    console.log(this.model[i])
  },

  handleTouchMove2(event) {
      const touch = event.touches[0];
      const distance = touch.clientX - this.startX;

      // スワイプ距離とナビゲーションの座標を比較し、一致する座標を見つける
      const matchIndex = Math.round(distance / NAVIGATION_WIDTH); // ナビゲーションの幅に合わせて調整

      // 一致した座標に対応するインデックスを計算し、表示画像を更新する
      this.model = matchIndex;
    },  
  toggleOrder () {
      this.sortDesc = !this.sortDesc
    },
  nextSort () {
    let index = this.headers.findIndex(h => h.key === this.sortBy)
    index = (index + 1) % this.headers.length
    this.sortBy = this.headers[index].key
  },



},


computed: {
  filteredDesserts() {
    const { sortBy, sortDesc } = this;
    const sortedDesserts = this.desserts.slice().sort((a, b) => {
      const aValue = a[sortBy];
      const bValue = b[sortBy];
      return sortDesc ? bValue - aValue : aValue - bValue;
    });
    return sortedDesserts;
  }
},

});






</script>



<template>
  <v-app id="#my-scroll-target" v-if="VIDEOS_LOADED" class="my-bg-color">

  


    <v-row no-gutters class="my-bg-color-white">
      <p v-if="true">ARTICLE_LIST_DUP: {{ ARTICLE_LIST_DUP }}</p>
      <p v-if="true">ARTICLE_LIST: {{ ARTICLE_LIST }}</p>
      <p v-if="true">TAG_LIST: {{ TAG_LIST }}</p>
      <p v-if="true">TAG_LIST: {{ PERFORMER_LIST }}</p>

      <v-col cols="12" class="my-10 py-10"></v-col>
        <v-col cols="11" class="mx-auto mb-15">
          <h1 class="text-h3">{{ ARTICLE_DETEAL_TITLE || ""}}</h1>
        </v-col>
        <v-col cols="12" class="mx-auto my-15"></v-col>
        <v-col cols="12" class="mx-auto px-10">


<!-- ■■■■video■■■■ -->
          <v-row v-if="SUBCONTENTS == 'video'" dense>
            <v-col
              class="py-3"
            >
            <v-card class="my-15">
              <v-row no-gutters class="px-0">
                <v-toolbar
                  flat
                  dark
                  class="my-bg-color"
                >
                  <v-btn icon @click="tollgeFilter()">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                  <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">フィルター</v-toolbar-title>
                </v-toolbar>
                
                <v-col v-if="showFilter" cols="12" class="mx-auto px-8 pb-15">
                  <div class="d-flex pt-10">
                    <a class="text-h5 ms-auto me-0 text-red">
                      ※項目内では OR検索　/　項目種類では AND検索 <br>
                      　（例１ (performer1 OR performer2) AND (tag1 OR tag2) <br>
                      　（例２ (performer1) AND (maker1) AND (tag1)
                    </a>
                  </div>
                  <div class="d-flex py-10">
                    <v-btn
                    @click="resetSearchParams(searchparams, 'all') ;Data = filterVideo(VIDEOS, searchparams)"
                    text="全てクリア"          
                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                    color="red"
                    >
                    <template v-slot:prepend>
                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                      </template>
                    </v-btn>
                  </div>  
                  <div class="d-flex">
                    <div
                    class="ms-auto me-0 my-text-size-40"
                    >
                      全 
                      <a v-if="VIDEOS" class="text-red">{{ filterVideo(VIDEOS, searchparams).length || "0"}}</a>
                      件 表示
                    </div>
                  </div>

                  <!-- アカウント -->
                  <v-card height="" class="my-bg-color-white" elevation=0>
                    <v-row no-gutters>
                      <v-col cols="12" class="border">
                        <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                        height="50px" @click="search_view_performer=!search_view_performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                          <v-row v-if="search_view_performer" no-gutters class="my-auto">
                            <v-col cols="12" class="border px-2 py-5 pb-10">
                                <v-chip-group
                                  v-model="searchparams.performers"
                                  column
                                  multiple
                                  color="text-deep-purple-accent-4"

                                  @click="Data = filterVideo(VIDEOS, searchparams);UpdateSearchParams(searchparams)"
                                >
                                    <v-chip
                                    v-for="item in PERFORMER_LIST"
                                    :key="item.id"
                                    label
                                    outline
                                    :value="item.name"
                                    color="red"

                                    class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                  >
                                    {{ item.name }}
                                  </v-chip>
                                </v-chip-group>
                                <!-- {{searchparams.performers}} -->

                                <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'performers') ;Data = filterVideo(VIDEOS, searchparams)"
                                  text="アカウントをクリア"          
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  >
                                  <template v-slot:prepend>
                                      <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                    </template>
                                  </v-btn>
                                </div>
                                
                            </v-col>
                            
                          </v-row>
                      </v-col>
                    </v-row>
                  </v-card>



                  <!-- タグ -->
                  <v-card height="" class="my-bg-color-white" elevation=0>
                    <v-row no-gutters>
                      <v-col cols="12" class="border">
                        <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                        height="50px" @click="search_view_tag=!search_view_tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                          <v-row v-if="search_view_tag" no-gutters class="my-auto">
                            <v-col cols="12" class="border px-2 py-5 pb-10">
                                <v-chip-group
                                  v-model="searchparams.tags"
                                  column
                                  multiple
                                  @click="Data = filterVideo(VIDEOS, searchparams)"

                                >
                                    <v-chip
                                    v-for="item in TAG_LIST"
                                    :key="item.id"
                                    label
                                    outline
                                    :value="item.name"
                                    color="red"

                                    
                                    class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                  >
                                    {{ item.name }}
                                  </v-chip>
                                </v-chip-group>
                                <!-- {{searchparams.tags}} -->

                                <div class="d-flex py-3">
                                  <v-btn
                                  @click="resetSearchParams(searchparams, 'tags') ;Data = filterVideo(VIDEOS, searchparams)"
                                  text="タグをクリア"
                                  class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                  color="red"
                                  >
                                    <template v-slot:prepend>
                                      <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                    </template>
                                  </v-btn>
                                </div>
                            </v-col>
                          </v-row>
                      </v-col>
                    </v-row>
                  </v-card>

                  <v-col class="py-5"></v-col>


                </v-col>
                </v-row>

              </v-card>
            </v-col>
          </v-row>





<!-- ■■■■article■■■■ -->
<v-row v-if="SUBCONTENTS == 'article'" dense>
        <v-col
          class="py-3"
        >
          <v-card class="my-15">
            <v-row no-gutters class="px-0">
              <v-toolbar
                flat
                dark
                class="my-bg-color"
              >
                <v-btn icon @click="tollgeFilter()">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">フィルター</v-toolbar-title>
              </v-toolbar>
              
              <v-col v-if="showFilter" cols="12" class="mx-auto px-8 pb-15">
                <div class="d-flex pt-10">
                  <a class="text-h5 ms-auto me-0 text-red">
                  ※項目内では OR検索　/　項目種類では AND検索 <br>
                  　（例１ (performer1 OR performer2) AND (tag1 OR tag2) <br>
                  　（例２ (performer1) AND (maker1) AND (tag1)
                </a>
                </div>

                  <div class="d-flex py-10">
                    <v-btn
                    @click="resetSearchParams(searchparamsarticle, 'all') ;Data = filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)"
                    text="全てクリア"          
                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                    color="red"
                    >
                    <template v-slot:prepend>
                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                      </template>
                    </v-btn>
                  </div>  
                  <div class="d-flex">
                    <div
                    class="ms-auto me-0 my-text-size-40"
                    
                    >
                      全 
                      
                      <!-- <a v-if="ARTICLE_LIST_DUP" class="text-red">{{ filterArticle(ARTICLE_LIST_DUP, searchparamsarticle).length || "0"}}</a> -->
                      <a v-if="Data" class="text-red">{{ SUBCONTENTS_ALL.length || "0"}}</a>

                      件 表示
                    </div>
                  </div>

                    <!-- アカウント -->
                    <v-card height="" class="my-bg-color-white" elevation=0>
                      <v-row no-gutters>
                        <v-col cols="12" class="border">
                          <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                          height="50px" @click="search_view_performer=!search_view_performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                            <v-row v-if="ARTICLE_LIST_PARAMS.classmajor" no-gutters class="my-auto">
                              <v-col cols="12" class="border px-2 py-5 pb-10">
                                  <v-chip-group
                                    v-if="ARTICLE_LIST_PARAMS.classmajor.length > 0"

                                    v-model="searchparamsarticle.classmajor"
                                    column
                                    multiple
                                    color="text-deep-purple-accent-4"

                                    @click="Data = filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)"
                                  >
                                      <v-chip
                                      v-for="item in ARTICLE_LIST_PARAMS.classmajor"
                                      :key="item"
                                      label
                                      outline
                                      :value="item"
                                      color="red"

                                      class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                    >
                                      {{ item }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.performers}} -->

                                  <div class="d-flex py-3">
                                    <v-btn
                                    @click="resetSearchParams(searchparamsarticle, 'classmajor') ;Data = filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)"
                                    text="アカウントをクリア"          
                                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                    color="red"
                                    >
                                    <template v-slot:prepend>
                                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                      </template>
                                    </v-btn>
                                  </div>
                                  
                              </v-col>
                              
                            </v-row>
                        </v-col>
                      </v-row>
                    </v-card>


                    <!-- タグ -->
                    <v-card height="" class="my-bg-color-white" elevation=0>
                      <v-row no-gutters>
                        <v-col cols="12" class="border">
                          <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                          height="50px" @click="search_view_tag=!search_view_tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>

                            <v-row v-if="ARTICLE_LIST_PARAMS.classmedium" no-gutters class="my-auto">
                              <v-col cols="12" class="border px-2 py-5 pb-10">
                                  <v-chip-group
                                  v-if="ARTICLE_LIST_PARAMS.classmedium.length > 0"

                                    v-model="searchparamsarticle.classmedium"
                                    column
                                    multiple
                                    @click="Data = filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)"

                                  >
                                      <v-chip
                                      v-for="item in ARTICLE_LIST_PARAMS.classmedium"
                                      :key="item"
                                      label
                                      outline
                                      :value="item"
                                      color="red"

                                      
                                      class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                    >
                                      {{ item }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.tags}} -->

                                  <div class="d-flex py-3">
                                    <v-btn
                                    @click="resetSearchParams(searchparamsarticle, 'classmedium') ;Data = filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)"
                                    text="タグをクリア"
                                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                    color="red"
                                    >
                                      <template v-slot:prepend>
                                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                      </template>
                                    </v-btn>
                                  </div>
                              </v-col>
                            </v-row>
                        </v-col>
                      </v-row>
                    </v-card>
                    <v-col class="py-5"></v-col>
          </v-col>
        </v-row>
      </v-card>
      </v-col>
    </v-row>



              




    <v-col class="my-10 my-bg-color-white tile"></v-col>
<a>DataDataDataData
{{ Data }}
</a>
<!-- ■■■■TABLE■■■■ -->

  <div>
    <VDataTable
    v-if="SUBCONTENTS_ALL && SUBCONTENTS"
    color="var(--my-color-black)"
    :loading="false"
    :items-per-page="-1"
    :headers="headers"
    :items="Data"
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

  <template v-if="SUBCONTENTS === 'article' && this.$route.path.split('/').length === 5" v-slot:item.title="{ item }">
    <!-- <router-link :to="{ name: 'Article', params: { param: item.classmajor, param2: item.classmedium, param3: item.classminor, param4: item.number} }"> -->
      {{ item.title }}aa
    <!-- </router-link> -->
  </template>
    
  <template v-if="SUBCONTENTS === 'video'" v-slot:item.title="{ item }">
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
  </template>

  </VDataTable>
  </div>





















  <div>
</div>



</v-col>
</v-row>




  </v-app>
  <div v-else>
      データを読み込んでいます...
  </div>
</template>




<style>


/* .v-table {
    --v-table-header-height: 20px;
    border-radius: inherit;
    line-height: 1.2;
    max-width: 100%;
} */

/* 
.v-data-table__tr>td{
    height: calc(var(--v-table-row-height, 52px) + 10px)!important;
} */
:root {
  --v-table-row-height: 30px;
}
.v-img__img--cover {
    object-fit: cover;
    object-position: right;
}



</style>
