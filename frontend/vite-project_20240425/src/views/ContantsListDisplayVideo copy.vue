<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted } from 'vue';
import { reactive } from 'vue';


// import { VDataTable } from 'vuetify/labs/VDataTable'



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
const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });

store.dispatch('FETCH_GET_BREADCRUMBS')
const searchparams = reactive({
  performers: [],
  tags: [],
  maker: [],
  label: [],
  series: [],
  duration: [],
  title: [],
  description: [],
  views: [],
  kyounuki_post_day: [],
  active: [],
})





try {
  // const searchrequest = route.query.searchrequest;
  var searchrequest = JSON.parse(route.query.searchrequest);
  console.log("searchparams", searchparams.value)
  console.log("searchrequest", searchrequest)

  if (Array.isArray(searchrequest)) {
    console.log("■point1")
    searchrequest.forEach(item => {
      console.log("■point2")

      for (const key in item) {
        console.log("■point3")

        searchparams[key] = [item[key]];
      }
    });
  }
} catch (error) {
  // エラーが発生した場合は何もしない
}
console.log("route.params.serchrequest", route.query.searchrequest)
console.log("searchparams", searchparams.value)


function toggleTag(tagName, searchparams) {
      console.log("tagName", tagName)
      console.log("searchparams.value.tags", searchparams)
      console.log("searchparams.value.tags", searchparams.tags)
      if (searchparams.tags.includes(tagName)) {
        searchparams.tags = searchparams.tags.filter(tag => tag !== tagName);
      } else {
        searchparams.tags.push(tagName);
      }
    }




// const test = SUBCONTENT  S_ALL.value === searchparams.value.tags

// console.log("SUBCONTENTS_ALL.value.tags", VIDEOS.value[0].tags[0].name)
// console.log("searchparams.value.tags", searchparams.value.tags)
// console.log("■■■■test", test)
// 
function filterVideo(data, searchparams) {
  let filteredData = data; // オリジナルのデータを変更せずにコピーを作成

  for (let key in searchparams) {
    const filterValue = searchparams[key];

    if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
      // console.log("■filterValue■", filterValue)
      // console.log("■filterValue■", key)
      if (key === "tags" || key === "performers") {
        console.log("searchparams", searchparams)

        // if (Array.isArray(filterValue) && filterValue.length !== 0) {
        if (Array.isArray(filterValue) && filterValue.length !== 0) {
          filteredData = filteredData.filter(item => {
            return item[key].some(item2 => filterValue.includes(item2.name));
          });
        }
      }
      //  else {
      //   console.log("key", key)

      //   filteredData = filteredData.filter(item => {
      //     return item[key] && item[key].name === filterValue;
      //   });
      //   console.log("filteredData", filteredData)

      // }
    }
  // console.log("filteredData.length", filteredData.length)
  // console.log("searchparams", searchparams)
  }  return filteredData;
}

// const filteredData = ref(filterVideo(VIDEOS.value, searchparams.value))






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
    // VideoPlayer,
  },
  data () {
    return {
      showCheckboxes: true,
      items_tes: ['foo', 'bar', 'fizz', 'buzz'],
      value_tes: ['foo', 'bar', 'fizz', 'buzz'],
      selectedTags: [],
      amenities: [1, 4],
      neighborhoods: [1],
      search_view_performer: true,
      search_view_tag: true,


      // searchparams: {
      //   performers: null,
      //   tags: ["tag1"],
      //   maker: ["メーカー２"],
      //   label: null,
      //   series: null,
      //   duration: null,
      //   title: null,
      //   description: null,
      //   views: null,
      //   kyounuki_post_day: null,
      //   active: null,
      // },
      filteredData: [],
      media: [false,false,false,false,false,false,false,false,false,false],
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
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
      cards: [
        { title: '【まとめ】〇〇賞についてまとめました！', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: '【個人ブログ】好きな小説家について', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 12 },
        { title: '【考察】今後の本の在り方について', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 12 },
        { title: '【まとめ】〇〇賞についてまとめました！', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
    ],
    tab: null,
    }    
  },
  // watch: {
  //   'searchparams.tags': {
  //     handler: 'updateFilteredData',
  //     deep: true,
  //   },
  // },
  mounted() {
    // ビデオ要素の高さを設定
    this.setVideoHeight();
    // ウィンドウのリサイズ時にビデオの高さを再計算
    window.addEventListener("resize", this.setVideoHeight);
  },


  beforeUnmount() {
    window.removeEventListener("resize", this.setVideoHeight);
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
  setVideoHeight() {
      const video = this.$refs.videoRef;
      const toolbar = this.$el.querySelector(".control-bar");
      if (video && toolbar) {
        const videoHeight = video.getBoundingClientRect().height;
        toolbar.style.height = `${videoHeight}px`;
      }
  },
  handleTagsInput(newSelectedItems) {
    console.log(VIDEOS.value)
    console.log(searchparams.value.tags)
    // this.filteredData = filterVideo(VIDEOS.value, searchparams.value.tags);
    // ここで必要な処理を実行する
  },

  resetSearchParams(searchparams, item) {
    if (item == "all") {
      for (let prop in searchparams) {
        console.log(prop)
        searchparams[prop] = [];
      }
    } else {
      searchparams[item] = [];
    }

    }


  // filterVideo(data, searchparams) {
  //   let filteredData = data
  //   // if SUBCONTENTS_ALL
  //   for (let key in searchparams) {
  //   // 各キーに対する処理を行う（ここではコンソールに表示）

  //     if (searchparams[key] != null) {
  //       if ((key === "tags" || key === "performers") && ((key === "tags" || key === "performers") && filteredData.length !== 0)) {
  //       } else {
  //         filteredData = filteredData.filter(item => {
  //         if (Array.isArray(searchparams[key])) {
  //           return searchparams[key].includes(item[key]?.name);
  //         } else {
  //           return item[key] && item[key].name === searchparams[key];
  //         }
  //       });
  //       }
  //     }
  //   }
  //   return filteredData;
  // },
  // searchparams.tagsが変更されたときに呼ばれるメソッド
  // updateFilteredData() {
  //   // filteredDataを再計算
  //   this.filteredData = this.filterVideo(this.SUBCONTENTS_ALL, this.searchparams);
  // },
  }
});





</script>



<template>
  <v-app id="#my-scroll-target" v-if="VIDEOS_LOADED" class="my-bg-color">


    <div>

</div>
      <v-row no-gutters class="my-bg-color-white">
        <!-- {{ filteredData }} -->
        <v-col cols="12" class="mx-auto px-10">
          <v-card class="my-15 pb-15">
              <v-row no-gutters class="px-0">
                <!-- <v-checkbox
                  cols="3"
                  v-for="item in TAG_LIST"
                  :key="item.name"
                  v-model="searchparams.tags"
                  :label="item.name"
                  :value="item.name"
                  @change="filteredData = filterVideo(VIDEOS, searchparams)"

                ></v-checkbox> -->


              <v-toolbar
                flat
                dark
                class="my-bg-color"
              >
                <!-- <v-btn icon> -->
                  <!-- <v-icon>mdi-close</v-icon> -->
                <!-- </v-btn> -->
                <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">フィルター</v-toolbar-title>
              </v-toolbar>

              <v-col cols="12" class="mx-auto px-8">

                <div class="d-flex pt-10">
                  <a class="text-h5 ms-auto me-0 text-red">
                  ※項目内では OR検索　/　項目種類では AND検索 <br>
                  　（例１ (performer1 OR performer2) AND (tag1 OR tag2) <br>
                  　（例２ (performer1) AND (maker1) AND (tag1)
                </a>
                </div>

                <!-- <v-card height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg" height="50px" href="/performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-5 pb-10">
                            <v-btn
                              v-for="(item,i) in PERFORMER_LIST"
                              :key="i"
                              class="my-fit-contents my-text-size-30  ms-auto me-0"

                              >
                              {{item.name}}
                            </v-btn>
                          </v-col>
                        </v-row>
                    </v-col>
                  </v-row>
                </v-card>

                <v-card height="" class="my-bg-color-white mt-15" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg" height="50px" href="/tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-5 pb-10">
                            <v-btn
                            v-for="(item,i) in TAG_LIST"
                            :key="i"
                            class="my-fit-contents my-text-size-30  ms-auto me-0"

                            v-model="searchparams.performers"
                            column
                            multiple
                            @click="filteredData = filterVideo(VIDEOS, searchparams)"
                            
                            >
                            {{item.name}}
                          </v-btn>
                          </v-col>
                        </v-row>
                        {{ searchparams.tags }}

                    </v-col>
                  </v-row>
                </v-card> -->








                  <div class="d-flex py-10">
                    <v-btn
                    @click="resetSearchParams(searchparams, 'all') ;filteredData = filterVideo(VIDEOS, searchparams)"
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

                                    @click="filteredData = filterVideo(VIDEOS, searchparams)"
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
                                    @click="resetSearchParams(searchparams, 'performers') ;filteredData = filterVideo(VIDEOS, searchparams)"
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
                                    @click="filteredData = filterVideo(VIDEOS, searchparams)"

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
                                    @click="resetSearchParams(searchparams, 'tags') ;filteredData = filterVideo(VIDEOS, searchparams)"
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







                  </v-col>
              </v-row>

          </v-card>

          <v-col cols="12" class="py-10"></v-col>




            


















          <!-- 動画 -->
          <v-card class="my-15">
            <v-toolbar
                flat
                dark
                class="my-bg-color"
              >
                <!-- <v-btn icon> -->
                  <!-- <v-icon>mdi-close</v-icon> -->
                <!-- </v-btn> -->
                <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">動画</v-toolbar-title>
              </v-toolbar>
              <v-row no-gutters>

                <v-col cols="6" class="mx-auto px-6 py-15 pb-5"
                  v-for="(VIDEO,i) in filterVideo(VIDEOS, searchparams)"
                  :key="i"
                  :src="VIDEO"
                >


                  <v-carousel
                  class="my-carousel"
                  v-if="media[i]==false"
                   :show-arrows="false"
                   :cycle="false"
                   v-model="model[i]"
                    @touchstart="handleTouchStart($event, i, model[i])"



                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->

                    <v-carousel-item
                      v-for="(item,ii) in parseJson(VIDEO.images)"
                      :key="ii"
                      cover
                      aspect-ratio="" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"
                      class="d-flex justify-end"
                      
                      
                    >
                    <v-row v-if="ii==0" no-gutters>
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
                    </v-row>
                    <v-row v-if="ii==1" no-gutters>
                      <v-col cols="12" class="d-flex"
                      v-for="(item,i) in VIDEO.tags"
                          :key="i"
                      >
                        <v-btn 
                          rounded="0"
                          class="my-fit-contents my-text-size-30  ms-auto me-0"
                          :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                          >
                          {{item.name}}
                        </v-btn>
                      </v-col>
                    </v-row>

                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                  </v-carousel-item>
                  </v-carousel>
                  <v-row no-gutters v-if="media[i]==true">
                    <v-col cols="12" aspect-ratio="0.73" class="mx-auto px-0 my-auto">

                        <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
                          <source src="https://liginc.co.jp/wp-content/uploads/2020/05/D0002060347_00000_V_000.mp4?_=1" type="video/mp4">
                          Your browser does not support the video tag.
                        </video>
                    </v-col>


                        
                        <v-col cols="12" class="d-flex pb-0 w-100">
                          <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(i)">
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
                  

                  <v-row no-gutters v-if="media[i]==false">
                    <v-col class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(i)">
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

                  <p class="my-text-size-50 font-weight-midium pt-2">{{VIDEO.title}}</p>

                  <!-- <v-row no-gutters>
                    <v-col class="d-flex">
                      <v-btn 
                        v-for="(item,i) in VIDEO.tags"
                        :key="i"
                        class="my-fit-contents my-text-size-30 py-1 my-1"
                        :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                        >
                        {{item.name}}
                      </v-btn>
                    </v-col>
                  </v-row> -->

                </v-col>
              </v-row>
            </v-card>












        <Btn_1 text="もっとみる"/>


      </v-col>
    </v-row>














  </v-app>
  <div v-else>
      データを読み込んでいます...
    </div>
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
