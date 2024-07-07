<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted, watch } from 'vue';
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
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
// const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const ARTICLE_LIST_DUP =computed(() => { return store.getters.GET_ARTICLE_LIST_DUP; });
const ARTICLE_LIST_PARAMS =computed(() => { return store.getters.GET_ARTICLE_LIST_PARAMS; });



// store.dispatch('FETCH_GET_BREADCRUMBS')



let SUBCONTENTS = ref(route.path.split("/")[1])

watch(ARTICLE_LIST_DUP, (newVal, oldVal) => {
  if (newVal) {
    const articletitle = ARTICLE_LIST_DUP.value[0].title
  }
})



  



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

  }
});





</script>



<template>



  <v-row justify="space-around" aria-disabled no-gutters>
    <v-col cols="11" class="mx-auto">
      <v-btn
        variant="text"
        :to="{ name: 'ArticlesList'}"
      >
      リストで見る
      </v-btn>
    </v-col>
  <Text_1 :text_1="text3 || 'ブログ記事'" />
        <v-row class="my-bg-color-white scrollable d-flex" style="flex-wrap: nowrap!important;">
          <v-col
            v-for="card in ARTICLE_LIST_DUP"
            :key="card.title"
            cols="6"
            class="my-bg-color-white my-5 pb-0 my-overflow-initial"
            rounded="xl"
            
          >

          
              <v-card
                v-bind="props"
                :elevation="isHovering ? 16 : 2"
                class="pb-0 mx-4 my-overflow-initial pl-0 my-font-size-20 my-fit-contents my-text-size-30 mt-0 my-bg-color my-text-color-white"
                rounded="xl"
                :to="{ name: 'Article', params: { param: card.classmajor, param2: card.classmedium, param3: card.classminor, param4: card.number} }"
              >

              <template v-slot:loader="{ isActive }">
                <v-progress-linear
                  :active="isActive"
                  color="deep-purple"
                  height="4"
                  indeterminate
                ></v-progress-linear>
              </template>
              
              <v-card-text>
                <p class="my-font-size-20 my-fit-contents my-text-size-30 my-bg-color my-text-color-white">
                  2022-04-02
                </p>
              </v-card-text>

              
              <v-img
                src="https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
                class="align-end rounded-xl"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="450px"
                cover

              >
              
                <!--<v-row v-if="ii==0" no-gutters>  -->
                <v-row no-gutters
>
                  <!-- v-for="(item,i) in VIDEO.performers"  -->
                  <!-- :key="i" -->
                  <v-col cols="12" class="d-flex"
>
                  <!-- :prepend-icon="i === 0 ? 'mdi-account-circle' : ''" -->
                  <div style="position: absolute; top: 0px; right: 0px;">
                    <v-btn 
                      rounded="0"
                      class="my-text-size-30 my-fit-contents"
                      style="position: relative; top: 0px; right: 0px;"
                    >
                      <!-- {{ card.classminor }} -->
                      タグ
                    </v-btn>
                  </div>
                  </v-col>
                </v-row>
                <v-card-title class="text-white text-h3" style="white-space: pre-wrap;" v-text="card.title + aaaa">
                </v-card-title>
                </v-img>
              </v-card>
              
          </v-col>
</v-row>

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
