<template>
    <v-card>
      <v-container class="px-0 px-md-4">

        <v-card v-if="boolean_card_title" class="text-center elevation-0 py-10">
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">{{ string_card_title_1 }}</strong>{{ string_card_title_2 }}
          </h2>
          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            {{ string_card_title_3 }}
          </div>
        </v-card>

        <h2 v-if="boolean_detail" class="text-h7 text-md-h5 mx-auto mb-4 ">
          <strong class="text-h6 text-md-h4">{{ string_detail }}</strong> {{ string_detail_sub }} 
          <!-- {{ detail_performer.name }} -->
        </h2>




        
    <div class="px-md-2">
        <v-row
          :class="{'flex-nowarp': !boolean_detail_one,
            'white-space': !boolean_detail_one,
            'horizontal-scroll':!boolean_detail_one
          }"
        no-gutters>
          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Window ■■■ -->
          <!-- ■■■■■■■■■■■■■■ -->
          
                  <template
                  v-for="(ITEM, index) in my_card_list"
                  :key="index"
                  >

                                      
                    <v-col
                      :cols="boolean_detail ? boolean_detail_one ? 12 : 7 : 6"
                      :sm="boolean_detail ? boolean_detail_one ? 6 : 5 : 4"
                      :md="boolean_detail ? boolean_detail_one ? 6 : 3 : 4"
                      class="pb-0 px-1 px-md-2"
                      :class="{'mx-auto ml-md-0': boolean_detail_one}"
                      style="flex-wrap: nowrap!important;"
                    >
                    <v-row no-gutters>
                      <v-col cols="12"
                      class="rounded elevation-2"
                      >
                        <v-row no-gutters v-if="media[index]==true && kind==='video'" class="rounded-t">
                          <v-col cols="12" class="my-auto aspect-ratio-block mx-auto rounded-t">
                              <video controls class="w-100 my-auto px-0 my-auto rounded-t" playsinline autoplay muted>
                                <source :src="ITEM.video_sumple_video" type="video/mp4">
                                  Your browser does not support the video tag.
                              </video>
                          </v-col>
                        </v-row>
                      <router-link
                        :key="index"
                        style="width: 100%; height: 100%; text-decoration: none; z-index: 1;"
                        :to="url(ITEM)"
                      >
                        <v-img
                          v-if="!media[index]"
                          class="rounded-t aspect-ratio-block mx-auto elevation-0"
                          :src="imageSrc(ITEM)"
                          lazy-src="https://picsum.photos/id/11/100/60"
                          alt="Image"
                          :to="url(ITEM)"
                        >
                        <v-row v-if='kind==="video" && boolean_detail==false && boolean_detail_one==false' no-gutters
                        class="d-none d-xs-block"
                        >
                          <v-col cols="12" class="d-flex rounded-1"
                            v-for="(item2,iiiu) in ITEM.video_performers"
                            :key="iiiu"
                          >
                            <v-btn 
                              rounded="0"
                              class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                              :prepend-icon="'mdi-account-circle'"
                              size="small"
                              exact
                              :to=url_account_video_or_article(item2)
                              >
                              {{item2.name}}
                            </v-btn>
                          </v-col>
                
                          <v-col cols="12" class="d-flex"
                            v-for="(item2,iiiu) in ITEM.video_tags"
                            :key="iiiu"
                          >
                            <v-btn 
                              rounded="0"
                              class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                              :prepend-icon="'mdi-tag-text-outline'"
                              size="small"
                              exact
                              :to=url_tag_video_or_article(item2)
                            >
                              {{item2.name}}
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-img>
                    </router-link>



                      <v-row v-if='kind==="video"' no-gutters class="rounded-b">
                        <v-col cols="6" class="pa-0 my-0 my-fit-contdts d-flex">
                            <v-row no-gutters>
                              <v-btn
                                class="my-fit-contents pa-0 ma-auto text-md-h6"
                                color="primary"
                                lazy-src="https://picsum.photos/id/11/100/60"
                                prepend-icon="mdi-alpha-f"
                                variant="text"
                                block
                                elevation="0"
                                :loading="loading"
                                @click="loading = !loading; handleButtonClick(ITEM.video_productnumber)"
                                target="_blank"
                              >
                                FANZA
                                <template v-slot:loader>
                                  <v-progress-linear indeterminate></v-progress-linear>
                                </template>
                              </v-btn>
                            </v-row>
                          </v-col>

                          <v-divider vertical class=""></v-divider>

                          <v-col cols="6" class="pa-0 my-0 my-fit-contdts d-flex">
                            <v-row no-gutters>
                              <v-btn
                                class="my-fit-contents pa-0 ma-auto text-md-h6"
                                color="primary"
                                lazy-src="https://picsum.photos/id/11/100/60"
                                prepend-icon="mdi-play-box"
                                variant=""
                                block
                                elevation="0"
                                :loading="loading"
                                @click="loading = !loading;toggleMedia(index)"
                              >
                                {{ media[index] ? '閉じる' : '再生' }}
                                <template v-slot:loader>
                                  <v-progress-linear indeterminate></v-progress-linear>
                                </template>
                              </v-btn>
                            </v-row>
                          </v-col>
                        </v-row>
                      </v-col>
                      

                    </v-row>
                    <div class="text-caption text-md-h6"
                    :class="{ 'text-h8': !boolean_detail_one && mdAndUp}"
                    >
                      {{ postday(ITEM) }}
                    </div>
                    <v-btn class="text-sm-h9 text-md-h5"
                    :class="{ 'text-h6': !boolean_detail_one && mdAndUp}"
                    @click="copyText('コピーする文字列')"
                    >
                      {{ title(ITEM) }}
                    </v-btn>

                    <v-col v-if="boolean_detail_one" class="pa-0">

                          <v-btn
                          v-for="(item, index_my_card) in my_card_list[0].video_performers"
                            :key="index_my_card"
                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1 text-md-h6 mx-1 "
                            :prepend-icon="'mdi-account-circle'"
                            size="small"
                            exact
                            :to=url_account_video_or_article(item)
                            >
                            {{ filter_account_list_name(item) }}
                          </v-btn>
                          <v-btn 
                          v-for="(item,index_my_card) in video_or_article_tag_list(my_card_list[0])"
                            :key="index_my_card"
                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1 text-md-h6 mx-1"
                            :prepend-icon="'mdi-tag-text-outline'"
                            size="small"
                            outlined
                            :to=url_tag_video_or_article(item)
                            >
                            
                            {{ filter_tag_list_name(item) }}

                          </v-btn>


                        </v-col>                    


                    </v-col>

                    <v-divider v-if="(index+1) % 3 == 0" class="my-divider d-none d-md-block"></v-divider>
                    <v-divider v-if="(index+1) % 2 == 0" class="my-divider d-md-none"></v-divider>
                    <!-- <v-divider v-if="(index+1) % 3 == 0" class="my-divider"></v-divider> -->
                     

                </template>



                <v-divider vertical v-if="boolean_detail_one && mdAndUp" class="my-divider my-1"></v-divider>
                <v-divider v-if="boolean_detail_one && !mdAndUp" class="my-divider mt-5"></v-divider>

                <!-- images -->
                <template
                v-if="boolean_detail_one && kind === 'video'"
                  class="d-none d-xs-block"
                >

                    <!-- 右半分に画像をN行2列で配置 -->

                    <v-col 
                      :cols="boolean_detail ? boolean_detail_one ? 12 : 12 : 12"
                      :sm="boolean_detail ? boolean_detail_one ? 6 : 6 : 6"
                      :md="boolean_detail ? boolean_detail_one ? 6 : 6 : 6"
                      class="my-5 px-1 px-md-2"
                    >
                      <v-row no-gutters>
                        <v-col
                          v-for="(image, index) in VIDEO_DETAIL_images(VIDEO_DETAIL.video_images)"
                          :key="index"
                          :cols="boolean_detail ? boolean_detail_one ? 6 : 7 : 6"
                          :sm="boolean_detail ? boolean_detail_one ? 4 : 5 : 4"
                          :md="boolean_detail ? boolean_detail_one ? 4 : 3 : 4"
                          class="pa-1 pa-md-2"
                        >
                          <v-img
                            class="rounded-t aspect-ratio-block"
                            :src="image"
                            lazy-src="https://picsum.photos/id/11/100/60"
                            alt="Image"
                          />
                        </v-col>
                      </v-row>
                    </v-col>



                </template>




        </v-row>
</div>


        <div v-if="boolean_detail_one" class=" my-14"></div>

      </v-container>
    </v-card>
  </template>




<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const VIDEOS_FILTERED = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });

import { useRoute } from 'vue-router';
const route = useRoute();
const TableargetvideoProductNumber  = route.params.video_productnumber;
const VIDEO_DETAIL = computed(() => { return VIDEOS.value.find(item => item.video_productnumber === TableargetvideoProductNumber); });

import { useDisplay } from 'vuetify';
const { mdAndUp } = useDisplay();
const mdup = computed(() => mdAndUp.value);



// 
import { watch } from 'vue'

const loading = ref(false)

watch(loading, (val) => {
  if (!val) return

  setTimeout(() => (loading.value = false), 100)
})








const props = defineProps({
  kind: { type: String},
  boolean_card_title: { type: Boolean},
  string_card_title_1: { type: String},
  string_card_title_2: { type: String},
  string_card_title_3: { type: String},
  my_card_list: { type: Object},
  boolean_detail: { type: Boolean},
  string_detail: { type: String},
  string_detail_sub: { type: String},
  boolean_detail_one: { type: Boolean},

  // item: { type: Object},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},
  // item: { type: Object, required: true},

});





// String: 文字列
// Number: 数値
// Boolean: 真偽値
// Array: 配列
// Object: オブジェクト
// Function: 関数
// Symbol: シンボル



function imageSrc(item) {
  if (props.kind === 'video') {
    return item.video_image;
  } else if (props.kind === 'article') {
    return item.article_image;
  } else {
    return 'default_image_path.jpg';  // デフォルト
  }
}

function postday(item) {
  if (props.kind === 'video') {
    return item.video_postday;
  } else if (props.kind === 'article') {
    return item.article_post_day;
  } else {
    return 'error';  // デフォルト
  }
}

function title(item) {
  if (props.kind === 'video') {
    return item.video_title.split(" - ")[0];
  } else if (props.kind === 'article') {
    return item.article_title;
  } else {
    return 'error';  // デフォルト
  }
}

function url(item) {
  if (props.kind === 'video') {
    return { name: 'Video_Detail', params: { video_productnumber: item.video_productnumber }};
  } else if (props.kind === 'article') {
    return { name: 'Article_Detail', params: { article_title_eng: item.article_title_eng }};
  } else {
    return { name: 'Error' };  // デフォルトのルート名を指定
  }
}


const media =  ref([false,false,false,false,false,false,false,false,false,false])
const model =  ref([0,0,0,0,0,0,0,0,0,0])

// リアクティブな変数
const startX = ref(0);
const startIndex = ref(null);

// 関数を定義
function handleTouchStart(event, i) {
  startX.value = event.touches[0].clientX;
  startIndex.value = model.value[i];
}

function toggleMedia(index) {
  media.value.splice(index, 1, !media.value[index]); // spliceメソッドを使って要素を置換する
}


function handleButtonClick(item) {
  const url = `https://www.dmm.co.jp/digital/videoc/-/detail/=/cid=${item}/`;
  window.open(url, '_blank');
}




const connection_performers = computed(() => {
  let result = {};
  for (const video_detail_performer of VIDEO_DETAIL.value.video_performers) {

    // 初期化
    result[video_detail_performer.name_eng] = [];

    // VIDEOS のvideo_performers.nameをリストで取得
    for (const videos_video of VIDEOS.value) {
      for (const video_performer of videos_video.video_performers) {
        if (video_performer.name_eng === video_detail_performer.name_eng) {
          result[video_detail_performer.name_eng].push(videos_video);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});



const connection_tags = computed(() => {
  let result = {};
  for (const video_detail_tag of VIDEO_DETAIL.value.video_tags) {

    // 初期化
    result[video_detail_tag.name_eng] = [];

    // VIDEOS のvideo_tags.nameをリストで取得
    for (const videos_video of VIDEOS.value) {
      for (const video_tag of videos_video.video_tags) {
        if (video_tag.name_eng === video_detail_tag.name_eng) {
          result[video_detail_tag.name_eng].push(videos_video);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});


const VIDEO_DETAIL_images = (item) => {
  try {
    // シングルクォートをダブルクォートに置き換える
    const correctedJsonString = item.replace(/'/g, '"');
    // JSON文字列をパースする
    return JSON.parse(correctedJsonString);
  } catch (error) {
    console.error("Invalid JSON string:", error);
    return null;
  }
};

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


function video_or_article_tag_list(item) {
  if (props.kind === 'video') {
    return item.video_tags;
  } else if (props.kind === 'article') {
    return item.article_tags;
  } else {
    return 'error';  // デフォルト
  }
}

function url_tag_video_or_article(item) {
  if (props.kind === 'video') {
    return { name: 'Video', query: { tag: item.name_eng, performer: '' } };
  } else if (props.kind === 'article') {
    return { name: 'Article', query: { tag: item.article_tag_name_eng, performer: '' } };
  } else {
    return 'error';  // デフォルト
  }
}

function url_account_video_or_article(item) {
  if (props.kind === 'video') {
    return { name: 'Video', query: { tag: '', performer: item.name_eng } };
  } else if (props.kind === 'article') {
    return { name: 'Article', query: { tag: '', performer: '' } };
  } else {
    return 'error';  // デフォルト
  }
}

const copyText = (text) => {
  navigator.clipboard.writeText(text).then(() => {
    console.log('Text copied to clipboard');
    // 通知やアラートを表示する場合
    alert('クリップボードにコピーしました！');
  }).catch(err => {
    console.error('Failed to copy text: ', err);
  });
};




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


.horizontal-scroll {
  display: flex;
  overflow-x: scroll;  
}
.flex-nowarp {
  flex-wrap: nowrap;
}

.white-space-nowrap{
  white-space: nowrap;
}

</style>
