<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed, watchEffect } from 'vue';
import { ref, onMounted, watch } from 'vue';
import { Icon } from '@iconify/vue';

import Text_1 from '../components/_Text_1.vue';


import Breadcrumbs from '../components/Breadcrumbs.vue';


// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'




const route = useRoute();
const store = useStore();

const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
let VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });

const urlPath = window.location.pathname;
const pathList = urlPath.split("/");
const lastpath = pathList[pathList.length - 1];

const VIDEO_DETAIL = computed(() => { return store.getters.GET_VIDEO_DETAIL; });


let SUBCONTENTS = ref(route.path.split("/")[1]+"s")


let SUBCONTENTS_ALL = ref()






if (SUBCONTENTS.value === "performers") {
  SUBCONTENTS_ALL.value = PERFORMER_LIST;
} else if (SUBCONTENTS.value === "tags") {
  SUBCONTENTS_ALL.value = TAG_LIST;
} else if (SUBCONTENTS.value === "videos") {
  SUBCONTENTS_ALL.value = VIDEOS;
}





// const productNumbers = computed(() => {
//   // URL_LISTの値が変更されたときに処理を実行する
//   watchEffect(() => {
//   console.log("URL_LIST222", URL_LIST)

//     const newValue = URL_LIST.value;
//     console.log("URL_LIST", URL_LIST)

//     // ここでnewValueを使用して必要な処理を実行する
//     if (newValue) {
//       const productNumbers = newValue.video.map(video => video.video_productnumber);
//       // ロジックに基づいて何かをする...
//     return productNumbers;

//     }
//   });
// });




// const productNumbers = computed(() => {
//   // URL_LISTの値が変更されたときに処理を実行する
//   const newValue = URL_LIST.value;
//   console.log("URL_LIST222", URL_LIST)

//   // ここでnewValueを使用して必要な処理を実行する
//   const productNumbers = newValue.video.map(video => video.video_productnumber)
  
//   return productNumbers;
// });
// 


// const judgeurl = computed(() => {
//   const newValue = productNumbers.value;
//   const lastpathin = lastpath;

//   // newValueの中にlastpathと一致する要素があるかどうかを判定
//   const hasMatch = newValue.includes(lastpathin);
  
//   return hasMatch;
// });


// const VIDEO_DETAIL = computed(() => {
//   const newValue = judgeurl.value;
//   const newVIDEOS = VIDEOS.value
//   const videoMatch = newVIDEOS.filter((video) => video.video_productnumber === lastpath);
//   console.log("videoMatch", videoMatch)
//   return videoMatch
// });



const iii = ref(0)
</script>


<script lang="ts">
import { defineComponent } from 'vue'
import GlobalStyles from '../components/_GlobalStyles.vue';


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
      media: [false,false,false,false,false,false,false,false,false,false],
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
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
      cards: [
      { title: '【〇〇まとめ】厳選〇〇', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
      { title: '【雑記】〇〇について', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 12 },
      { title: '【〇〇まとめ】厳選〇〇', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 12 },
      { title: '【雑記】〇〇について', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
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
  toggleMedia(index) {
    this.media.splice(index, 1, !this.media[index]); // spliceメソッドを使って要素を置換する
  },
  copyText() {
      const textToCopy = "Hello, world!"; // コピーしたいテキスト
      navigator.clipboard.writeText(textToCopy)
        .then(() => {
          console.log('Text copied to clipboard:', textToCopy);
          // ここでメッセージやフィードバックを表示する場合は、ここにコードを追加
        })
        .catch(err => {
          console.error('Failed to copy text:', err);
          // エラーが発生した場合の処理をここに追加
        });
    },
    copyToClipboard(text) {
      navigator.clipboard.writeText(text)
        .then(() => {
          console.log('Text copied to clipboard');
        })
        .catch((error) => {
          console.error('Failed to copy text: ', error);
        });
    }   
}

});



</script>

<template>
  <!-- <v-app id="#my-scroll-target" v-if="judgeurl" class="my-bg-color"> -->
    <v-container fluid v-if="VIDEO_DETAIL">
    <v-row justify="space-around" no-gutters>
      <v-col class="py-1" cols="12">


            <v-row no-gutters class="my-bg-color-white">
        <!-- <Text_1 :text_1="text2 || '今日抜き'" /> -->

        
        <v-col cols="12" class="mx-auto px-10">

          <v-card class="my-15 mx-auto "

          >
          <v-toolbar
                flat
                dark
                class="my-bg-color d-flex"
              >
              <v-icon class="my-text-color-white mx-5" size="45" >mdi-file-plus</v-icon>

                <v-toolbar-title class="text-left ms-6 my-text-color-white font-weight-medium text-center my-text-size-40">{{ VIDEO_DETAIL[0].video_issue}}</v-toolbar-title>
              </v-toolbar>
            <!-- <v-card-text tag="h3" class="mt-6 my-underline text-center px-5 my-text-size-40 font-weight-medium">{{ KYOUNUKI.post_day}}</v-card-text> -->

            
              <v-row no-gutters>

                <v-col cols="11" class="mx-auto px-6 py-15 pb-5"
                >

                  <v-carousel
                  class="my-carousel"
                   :show-arrows="false"
                   :cycle="false"
                   v-if="media[1]==false"

                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->
                
                    <v-carousel-item
                      :src="VIDEO_DETAIL[0].video_image"
                      cover
                      aspect-ratio="1.46" alt="Image"
                      
                      
                      
                      
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
                  <v-row no-gutters v-if="media[1]==true">
                    <v-col cols="12" aspect-ratio="1.46" class="mx-auto px-0 my-auto">

                        <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
                          <source :src="VIDEO_DETAIL[0].video_sumple_video" type="video/mp4">
                          Your browser does not support the video tag.
                        </video>
                    </v-col>


                        
                        <v-col cols="12" class="d-flex pb-0 w-100">
                          <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(1)">
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
                  

                  <v-row no-gutters v-if="media[1]==false">
                    <v-col class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(1)">
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

                  <a :to="{ name: 'Video', param: VIDEO_DETAIL[0].video_productnumber}" class="my-text-size-40 font-weight-bold my-10">{{ VIDEO_DETAIL[0].video_title }}</a>


                  <v-row no-gutters>
                    <v-col>
                      <v-btn
                        rounded="0"
                        class="my-fit-contents my-text-size-30  ms-auto me-0"
                        :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                        @click="copyToClipboard(VIDEO_DETAIL[0].video_productnumber)"

                        >
                        {{VIDEO_DETAIL[0].video_productnumber}}
                      </v-btn>
                    </v-col>
                  </v-row>





                  
                  <v-row no-gutters>
                    <v-col>

                  <v-btn 
                    v-for="(item,i) in VIDEO_DETAIL[0].video_performers"
                    :key="i"
                    rounded="0"
                    class="my-fit-contents my-text-size-30  ms-auto me-0"
                    :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
                    >
                    {{item.name}}
                  </v-btn>
                </v-col>
                  </v-row>

                  <v-row no-gutters>
                    <v-col>
                      <v-btn 
                        v-for="(item,i) in VIDEO_DETAIL[0].video_tags"
                        :key="i"
                        rounded="0"
                        class="my-fit-contents my-text-size-30  ms-auto me-0"
                        :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                        >
                        {{item.name}}
                      </v-btn>
                    </v-col>
                  </v-row>

                  <v-row no-gutters>
                    <v-col>
                      <v-btn 
                        rounded="0"
                        class="my-fit-contents my-text-size-30  ms-auto me-0"
                        :prepend-icon="''"
                        >
                        {{VIDEO_DETAIL[0].video_label.name}}
                      </v-btn>
                    </v-col>
                  </v-row>
                  







            



            <v-row no-gutters>
              <v-col class="d-flex">
                <v-btn 
                  v-if="VIDEO_DETAIL[0].video_affiliateurl"
                  class="my-fit-contents py-1 my-1 mx-auto"
                  >
                  <v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
                  <span class="my-text-size-50">外部サイト</span> <!-- テキストのサイズを設定 -->
                </v-btn>
                <v-btn 
                  class="my-fit-contents py-1 my-1 mx-auto"
                  >
                  <v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
                  <span class="my-text-size-50">外部サイト</span> <!-- テキストのサイズを設定 -->
                </v-btn>

                <v-btn 
                  v-if="VIDEO_DETAIL[0].video_affiliateurl"
                  class="my-fit-contents py-1 my-1 mx-auto"
                  >
                  <v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
                  <span class="my-text-size-50">外部サイト</span> <!-- テキストのサイズを設定 -->
                </v-btn>
                <v-btn 
                  class="my-fit-contents py-1 my-1 mx-auto"
                  >
                  <v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
                  <span class="my-text-size-50">{{ VIDEO_DETAIL[0].video_productnumber }}</span> <!-- テキストのサイズを設定 -->
                </v-btn>
              </v-col>
            </v-row>


          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
















<!-- 関連記事 -->


  <v-row no-gutters class="my-bg-color-white">
        <!-- <Text_1 :text_1="text2 || '今日抜き'" /> -->

        
        <v-col cols="12" class="mx-auto px-10">

          <v-card class="my-15 mx-auto "

          >
          <v-toolbar
                flat
                dark
                class="my-bg-color"
                v-if="VIDEOS"
              >
              <!-- <v-icon class="my-text-color-white mx-5" size="45" >mdi-file-plus</v-icon> -->

                <v-toolbar-title class="text-left ms-6 my-text-color-white font-weight-medium text-center my-text-size-40">関連記事</v-toolbar-title>
              </v-toolbar>
            <!-- <v-card-text tag="h3" class="mt-6 my-underline text-center px-5 my-text-size-40 font-weight-medium">{{ KYOUNUKI.post_day}}</v-card-text> -->





              <v-row no-gutters
                class="mx-5 mb-10"
                style="flex-wrap: nowrap!important; overflow-x: auto;"
                v-for="(performer,p_index) in VIDEO_DETAIL[0].video_performers"
                :key="p_index"

              >
              <p class="my-text-size-40 font-weight-bold my-10">{{ performer.name }}</p>

              <template
                v-for="(VIDEO,i) in VIDEOS"
                :key="i"
                >
                <v-col cols="6" class="mx-auto px-6 py-15 pb-5"
                  v-if="VIDEO.video_performers.map(performer => performer.name).includes(performer.name)"
                >

                            <router-link
                                  :to="{ name: 'Video', params: { param: VIDEO.video_productnumber}, meta: { subcontents: searchparams }}"
                                  @click="handleClick"
                                  class="my-text-decoration-none"

                                >

                              <v-carousel
                              class="my-carousel"
                              :show-arrows="false"
                              :cycle="false"
                              >
                              <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->
                              <!-- v-for="(item,ii) in parseJson(VIDEO.video_images)" -->
                                <v-carousel-item
                                  cover
                                  aspect-ratio="16:9" :src="VIDEO.video_image" alt="Image" 
                                  class="my-custom-img"
                                  >

                                <v-row no-gutters>
                                  <!-- v-for="(item,i) in VIDEO.video_performers" -->

                                  <v-col cols="12" class="d-flex"
                                    v-for="(item,ii) in VIDEO.video_performers"
                                    :key="ii"
                                  >
                                    <v-btn 
                                      rounded="0"
                                      class="my-fit-contents my-text-size-30  ms-auto me-0"
                                      :prepend-icon="ii === 0 ? 'mdi-account-circle' : ''"
                                      
                                      >
                                      {{item.name}}
                                    </v-btn>
                                  </v-col>
                                </v-row>
                                
                                <!-- <v-row no-gutters>
                                  <v-col cols="12" class="d-flex"
                                    v-for="(item,ii) in VIDEO.video_tags"
                                    :key="ii"
                                  >
                                    <v-btn 
                                      rounded="0"
                                      class="my-fit-contents my-text-size-30  ms-auto me-0"
                                      :prepend-icon="ii === 0 ? 'mdi-tag-text-outline' : ''"
                                      >
                                      {{item.name}}
                                    </v-btn>
                                  </v-col>
                                </v-row> -->

                                <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                              </v-carousel-item>
                                
                              </v-carousel>

                            </router-link>
                            <v-row no-gutters>
                                  <!-- v-for="(item,i) in VIDEO.video_performers" -->

                                  <v-col cols="12" class="d-flex"
                                  >
                                    <v-btn 
                                      rounded="0"
                                      class="my-fit-contents my-text-size-30  ms-auto me-0"
                                      :prepend-icon="ii === 0 ? 'mdi-account-circle' : ''"
                                      
                                      >
                                      aaaaaaaaaaaa
                                    </v-btn>
                                  </v-col>
                                </v-row>


          </v-col>
          
        </template>
        </v-row>
      </v-card>
    </v-col>
  </v-row>










<!-- 終わり -->





          </v-col>




    </v-row>
  </v-container>
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
</style>
