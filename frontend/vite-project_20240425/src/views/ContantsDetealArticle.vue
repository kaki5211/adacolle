<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted, watch } from 'vue';
import { reactive } from 'vue';


import { VDataTable,
  VDataTableServer,
  VDataTableVirtual, } from 'vuetify/labs/VDataTable'

// ■■■■■■ import > Components ■■■■■■
import Btn_1 from '../components/_Btn_1_mottomiru.vue';
import Btn_2 from '../components/_Btn_2_link.vue';
// import Text_1 from '../components/_Text_1.vue';
// import HelloWorld from './components/HelloWorld.vue'
// import Meta from './components/Meta.vue';
// import ToolBar from './components/ToolBar.vue';
// import Topimage from './components/Topimage.vue';
// import Footer from './components/Footer.vue';
// import Breadcrumbs from './components/Breadcrumbs.vue';
import Con_text from '../components/_Con_text.vue'
import Con_title from '../components/_Con_title.vue'



const route = useRoute();
const store = useStore();



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
const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const ARTICLE_DETEAL = computed(() => { return store.getters.GET_ARTICLE_DETEAL; });




// store.dispatch('FETCH_GET_BREADCRUMBS') 
// const BREADCRUMBS = computed(() => { return store.getters.GET_BREADCRUMBS; })




let SUBCONTENTS = ref(route.path.split("/")[1])

const ARTICLE_CLASS = ref(route.path.split("/").slice(2, 6))

// const ARTICLE_DETEAL = ref([]);
const ARTICLE_DETEAL_TITLE = ref();


// ARTICLE_LIST
// watch(ARTICLE_LIST, (newVal, oldVal) => {
//   if (newVal) {  
//     ARTICLE_DETEAL.value = newVal.filter(item => 
//     item.classmajor === ARTICLE_CLASS.value[0] && 
//     item.classmedium === ARTICLE_CLASS.value[1] && 
//     item.classminor === ARTICLE_CLASS.value[2] &&
//     item.title_number === parseInt(ARTICLE_CLASS.value[3])
//     );
//     ARTICLE_DETEAL_TITLE.value = ARTICLE_DETEAL.value[0].title;
//     BREADCRUMBS.value[5].title = ARTICLE_DETEAL_TITLE.value
//     store.commit('SET_BREADCRUMBS', BREADCRUMBS);

//   }
// });
// if (ARTICLE_LIST.value) {  
//   ARTICLE_DETEAL.value = ARTICLE_LIST.value.filter(item => 
//   item.classmajor === ARTICLE_CLASS.value[0] && 
//   item.classmedium === ARTICLE_CLASS.value[1] && 
//   item.classminor === ARTICLE_CLASS.value[2] &&
//   item.title_number === parseInt(ARTICLE_CLASS.value[3])
//   );
//   ARTICLE_DETEAL_TITLE.value = ARTICLE_DETEAL.value[0].title;
//   BREADCRUMBS.value[5].title = ARTICLE_DETEAL_TITLE.value
//   store.commit('SET_BREADCRUMBS', BREADCRUMBS);
// }


// Virtual Option
// video
// watch(ARTICLE_DETEAL, (newVal, oldVal) => {
//   if (SUBCONTENTS.value === "article" && ARTICLE_CLASS.value[1] === "video") {
//   let ARTICLE_DETEAL_NEW = [...newVal]; // 新しい配列を作成

//   ARTICLE_DETEAL_NEW.forEach((article, index) => {
//     const virtual_option1 = VIDEOS.value.find(item => item.productnumber === article.option1);
//     if (virtual_option1) {
//       ARTICLE_DETEAL_NEW[index].vertual_option1 = virtual_option1;
//     }
//   });
//   newVal = ARTICLE_DETEAL_NEW
// }
// });
// if (SUBCONTENTS.value === "article" && ARTICLE_CLASS.value[1] === "video") {
//   let ARTICLE_DETEAL_NEW = [...ARTICLE_DETEAL.value]; // 新しい配列を作成

//   ARTICLE_DETEAL_NEW.forEach((article, index) => {
//     const virtual_option1 = VIDEOS.value.find(item => item.productnumber === article.option1);
//     if (virtual_option1) {
//       ARTICLE_DETEAL_NEW[index].vertual_option1 = virtual_option1;
//       console.log("virtual_option1.title", virtual_option1.title)
//     } else {
//       ARTICLE_DETEAL_NEW[index].vertual_option1 = {
//         name :"",
//       };

//     }
//   });
//   ARTICLE_DETEAL.value = ARTICLE_DETEAL_NEW
// }


// Virtual Option
// performer
// watch(ARTICLE_DETEAL, (newVal, oldVal) => {
//   if (SUBCONTENTS.value === "article" && ARTICLE_CLASS.value[1] === "performer") {
//   let ARTICLE_DETEAL_NEW = [...newVal]; // 新しい配列を作成

//   ARTICLE_DETEAL_NEW.forEach((article, index) => {
//     const virtual_option1 = PERFORMER_LIST.value.find(item => item.id === parseInt(article.option1, 10));
//     if (virtual_option1) {
//       ARTICLE_DETEAL_NEW[index].vertual_option1 = virtual_option1;
//     }
//   });
//   newVal = ARTICLE_DETEAL_NEW
// }
// });
// if (SUBCONTENTS.value === "article" && ARTICLE_CLASS.value[1] === "performer") {
//   let ARTICLE_DETEAL_NEW = [...ARTICLE_DETEAL.value]; // 新しい配列を作成

//   ARTICLE_DETEAL_NEW.forEach((article, index) => {
//     const virtual_option1 = PERFORMER_LIST.value.find(item => item.id === article.option1);
//     if (virtual_option1) {
//       ARTICLE_DETEAL_NEW[index].vertual_option1 = virtual_option1;
//     }
//   });
//   ARTICLE_DETEAL.value = ARTICLE_DETEAL_NEW
// }




  



const contents_info = `
    <title>あいうえお
    <subtitle>かきくけこ
    <text>text
    <blockquote>blockquote<bookpage>2
    <title>2
`;

const lines = contents_info.split('\n');
const contents_ = [];
let contents = ref([]);
let current_page = null;
let count = 1;
let count_title = 0;
let count_subtitle = 0;
let count_page = 0;

for (const line of lines) {
    const trimmedLine = line.trim();
    if (!trimmedLine) continue;
    if (trimmedLine === "") continue;

    const [tag, ...contentParts] = trimmedLine.split('>');
    const parsedTag = tag.slice(1).toLowerCase();
    const content = contentParts.join('>').trim();

    if (parsedTag === 'title') {
        count_title++;
    } else if (parsedTag === 'subtitle') {
        count_subtitle++;
    } else if (parsedTag === 'page') {
        if (count_page !== 0) {
            count_page = parseInt(content) - 1;
            contents_.push({ page: count_page, contents });
            contents.value = [];
        }
        continue;
    }

    if (content.includes('<bookpage>')) {
        const [text, page] = content.split('<bookpage>');
        const parsedPage = parseInt(page);
        const obj = {
            tag: parsedTag,
            text,
            count,
            title: count_title,
            subtitle: count_subtitle,
            blockquotepage: parsedPage
        };
        contents.value.push(obj);
    } else {
        const obj = {
            tag: parsedTag,
            text: content,
            count,
            title: count_title,
            subtitle: count_subtitle
        };
        contents.value.push(obj);
    }
    count++;
}



// ここにManyToManyFieldと関連オブジェクトの処理を追加する
// contents_tags_infoなどの変数は適切に設定する必要があります

// 最終的にcontentsを返す
// return contents;


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
  
}
  // headers.value.push({title: "項目", align: 'start', key: 'classmedium', value: 'classmedium' });


















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
    Btn_2,
    VDataTable,
    VDataTableServer,
    VDataTableVirtual,
    // VideoPlayer,
  },
  data () {
    return {
      media: [false,false,false,false,false,false,false,false,false,false],
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
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
  toggleMedia(index) {
    this.media.splice(index, 1, !this.media[index]); // spliceメソッドを使って要素を置換する
  },
}


});



















</script>



<template>



      <v-row no-gutters class="my-bg-color-white">
        <v-col cols="12" class="my-10 py-10"></v-col>
        <v-col cols="11" class="mx-auto mb-15">
          <h1 class="text-h3">{{ ARTICLE_DETEAL_TITLE || ""}}</h1>
        </v-col>
        <v-col cols="12" class="mx-auto my-15"></v-col>

        <v-col cols="12" class="mx-auto px-6">

        <v-container fluid>

          
      <v-row v-if="ARTICLE_DETEAL" dense>
        <v-col
          class="py-3"

        >
        ARTICLE_DETEAL: {{ ARTICLE_DETEAL }}

        <v-card class="">
        <p class="pl-5 my-font-size-20 my-fit-contents my-text-size-40 mt-0 my-bg-color my-text-color-white">一覧表</p>


        <div>
          <VDataTable
          v-if="ARTICLE_DETEAL.length > 0"
          color="var(--my-color-black)"
          :loading="false"
          :items-per-page="-1"
          :headers="headers"
          :items="ARTICLE_DETEAL"
          item-value="name"
          class="elevation-1 custom-table text-h3 my-font-size-20"
          :items-per-page-options="[ {value: -1, title: 'All'} ]"
          items-per-page-text=""
          page-text=""
          next-icon=""
          prev-icon=""
          first-icon=""
          last-icon=""
          style="overflow-x: scroll; width: 100%; border-collapse: collapse; white-space: nowrap;"
          disable-pagination
        >

        <template v-slot:item.name="{ item, index }">
          <a :href="'#article_' + index" class="my-text-size-40">{{ item.name }}</a>
        </template>

        <template v-slot:item.vertual_option1.name="{ item, index }">
          <a v-if="item.vertual_option1 && item.vertual_option1.name" :href="'#article_' + index" class="text-decoration-none text-h3 my-font-size-20">{{ item.vertual_option1.name || ""}}</a>
        </template>

        <template v-slot:item.option1="{ item, index }">
          <a :href="'#article_' + index" class="text-decoration-none text-h3 my-font-size-20">{{ item.option1 }}</a>
        </template>

        



        </VDataTable>
        </div>





        </v-card>

        </v-col>
      </v-row>




      <v-row v-if="ARTICLE_DETEAL" dense>
        <v-col
          v-for="(item, index) in ARTICLE_DETEAL"
          :key="index"
          cols="12"
          class="py-3"
        >
        <v-card class="">

        <p class="pl-5 my-font-size-20 my-fit-contents my-text-size-40 mt-0 my-bg-color my-text-color-white"><v-icon class="my-3 mr-3" contain size="60px"><Icon icon="icon-park:update-rotation" /></v-icon>{{ item.post_day }}</p>







            <v-row v-if="ARTICLE_CLASS[1] == 'video'" no-gutters>

                <v-col cols="11" class="mx-auto px-6 py-15 pb-5">

                  <v-carousel
                    class="my-carousel"
                    v-if="media[index]==false"
                    :show-arrows="false"
                    :cycle="false"
                    v-model="model[index]"
                    @touchstart="handleTouchStart($event, index, model[index])"
                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->

                    <v-carousel-item
                      v-for="(item2,ii) in parseJson(item.vertual_option1.images)"
                      :key="ii"
                      cover
                      aspect-ratio="1.46" :src="item2" alt="Image" @click="model[index] = (model[index] + 1 ) % parseJson(item.vertual_option1.images).length"
                    >
                    <!-- <v-row v-if="ii==0" no-gutters>
                      <v-col cols="12" class="d-flex"
                      v-for="(item,i) in VIDEO.performers"
                          :key="i"
                      >
                        <v-btn 
                          rounded="0"
                          class="my-fit-contents my-text-size-30  ms-auto me-0"
                          :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
                          >
                          {{item.name}}
                        </v-btn>
                      </v-col>
                    </v-row> -->
                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                    </v-carousel-item>
                  </v-carousel>
                  <v-row no-gutters v-if="media[index]==true">
                    <v-col cols="12" aspect-ratio="1.46" class="mx-auto px-0 my-auto">

                        <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
                          <source src="https://liginc.co.jp/wp-content/uploads/2020/05/D0002060347_00000_V_000.mp4?_=1" type="video/mp4">
                          Your browser does not support the video tag.
                        </video>
                    </v-col>


                        
                    <v-col cols="12" class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(index)">
                        閉じる
                      </v-btn> 
                    </v-col>
                  </v-row>


                  <!--
                  <div v-if="media[i]==true" class="video-container">
                    <video ref="videoRef" class="video-player" controls playsinline autoplay muted>
                      <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
                      Your browser does not support the video tag.
                    </video>

                    <v-toolbar class="control-bar" absolute bottom>
                      コントロールバーのコンポーネントをここに追加
                      <v-btn icon>
                        <v-icon>mdi-play-pause</v-icon>
                      </v-btn>
                      <v-slider thumb-label="always"></v-slider>
                      追加のコントロールボタンやスライダーなどを配置
                    </v-toolbar>
                  </div>
                  -->


                <!-- <div v-if="media[i]==true" aspect-ratio="0.73" class="mx-auto px-0 my-auto d-flex">
                  <div class="video-wrapper">
                    <video ref="videoPlayer" :class="['video-player', { 'small': isSmall }]" playsinline autoplay muted>
                      <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
                      Your browser does not support the video tag.
                    </video>
                    <div class="custom-controls">
                      <div class="progress-bar" @mousedown="startDrag">
                        <div class="progress" :style="{ width: progressWidth }"></div>
                      </div>
                    </div>
                  </div>
                  </div> -->


                  <!-- videoSrc -->
                  

                  <v-row no-gutters v-if="media[(index)]==false">
                    <v-col class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia((index))">
                        再生
                      </v-btn> 
                    </v-col>
                  </v-row>

                    <!-- <v-row no-gutters>
                    <v-col class="d-flex mt-1 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-open-in-new">
                        続きを見る
                      </v-btn> 
                    </v-col>
                  </v-row> -->

                  <!-- <a :to="{ name: 'Video', param: item.productnumber}" class="custom-link my-text-size-50 font-weight-medium pt-2">{{ item.title }}</a> -->


                  <v-row no-gutters>
                    <v-col class="d-flex">
                      <v-btn 
                        v-for="(item2,i) in item.vertual_option1.performers"
                        :key="i"
                        class="my-fit-contents my-text-size-30 py-1 my-1 mr-5 pr-5"
                        :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
                        >
                        {{item2.name}}
                      </v-btn>
                      <v-btn 
                        v-for="(item2,i) in item.vertual_option1.tags"
                        :key="i"
                        class="my-fit-contents my-text-size-30 py-1 my-1 mr-5 pr-5"
                        :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                        >
                        {{item2.name}}
                      </v-btn>
                    </v-col>
                  </v-row>





                  
<!-- contents end -->

                </v-col>
                </v-row>







              <!-- video 以外 -->
              <v-col v-else cols="11" style="max-height: 500px;" class="mx-auto px-0 my-auto pt-15 pb-5 mt-0 d-flex">
                <!-- <img class="center text-center mx-auto" src="https://picsum.photos/600/300"> -->
                <!-- gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" -->

                <v-img
                src="https://picsum.photos/500/500"
                class=""
                gradient=""
                alt="Image"
                aspect-ratio=""
                >
                </v-img>
              </v-col>




















            <!-- <v-col cols="11" class="mx-auto px-0 my-auto d-flex">
              <h3  class="v-card-title text-h3"></h3>
            </v-col> -->
            <v-card-title v-if="item.vertual_option1 && item.vertual_option1.name" :id="'article_' + index" class="py-5 text-h3 font-weight-bold my-text-color-black my-letter-spacing-initial" tag="h3">
              {{ item.vertual_option1.name || item.name }}            
            </v-card-title>

            
            <!-- <v-col cols="11" class="mx-auto px-0 my-auto d-flex"> -->
              <!-- <a class="my-text-size-50">{{ item.content }}</a> -->
            <!-- </v-col> -->
            <!-- contents -->
            <div>
                <div v-for="(contents_, index) in contents" :key="index">
                  <!-- <div v-if="contents_.tag !== 'title' && contents_.tag !== 'subtitle' && contents_.tag !== 'blockquote'" class="px-1"> -->
                  <!-- </div> -->
                  <!-- <div v-if="contents_.tag === 'title'"> -->
                    <!-- contents_title {{ contents_.text }} -->
                    <!-- <contents-title :text="contents_.text" :ty="index" :tyTitle="contents_[2]" /> -->

                    <!-- <div v-if="contentsPage > 1"> -->
                        <!-- <img :src="'/media/media/' + postDay + '/' + contentsPage + '.jpg'" /> -->
                    <!-- </div> -->
                  <!-- </div> -->
                  <!-- <div v-else-if="contents_.tag === 'subtitle'"> -->
                    <!-- <v-divider class="pb-0 mb-0" v-if="index > 2" /> -->
                      <!-- <contents-subtitle :text="contents_.text" :ty="index" /> -->
                    
                    <!-- <v-row no-gutters style="min-width: 250px; max-width:100%;" class="pt-10 pb-8"> -->
                      <!-- <v-col cols="12" align-self="center" style="min-width: 250px;" class="mx-auto my-auto"> -->
                        <!-- <google-adsense-display /> -->
                      <!-- </v-col> -->
                    <!-- </v-row> -->
                  <!-- </div> -->
                  <div v-if="contents_.tag === 'text'">
                    <!-- <contents-text :text="contents_.text" /> -->
                    <Con_text :text=contents_.text />
                  </div>
                  <!-- <div v-else-if="contents_.tag === 'blockquote'"> -->
                    <!-- <contents-blockquote :text="contents_.text" :page="contents_[2]" /> -->
                    <!-- contents_blockquote {{ contents_.text }} -->
                  <!-- </div> -->
                  <!-- <div v-if="contents_.tag !== 'title' && contents_.tag !== 'subtitle' && contents_.tag !== 'blockquote'" class="px-1"> -->
                  <!-- </div> -->
                </div>
              </div>


















            <v-col cols="11" class="mx-auto px-0 my-auto d-flex">
              <Btn_2 text="商品リンク" href="a" appendicon="mdi-open-in-new"/>
            </v-col>
































        </v-card>

        </v-col>
      </v-row>




    </v-container>





    <a id="aiueo">aiueo</a>
















      </v-col>



    </v-row>


























































    





</template>




<style scoped>

.video-container {
  position: relative;
  width: 100%;
}
.video-player {
  width: 100%;
}
.control-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
}

.custom-chip-style {
  /* ここに独自のスタイルを追加 */
  /* font-size: 40px; */
  /* 他のスタイルプロパティを追加 */
  height: fit-content!important;
  font-size: 30px!important;


  
}
</style>



