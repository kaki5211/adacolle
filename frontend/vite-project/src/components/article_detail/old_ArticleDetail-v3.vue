<template>
    <v-card>
      <div class="py-2" />


      <v-card class="text-center elevation-0 py-10">
      <!-- <h2 class="text-grey-darken-1 font-weight-regular">
        Introducing new
      </h2> -->
  
          <h2 class="text-h6 text-md-h4 mx-auto mb-4 ">
            <strong class="text-h5 text-md-h3">関連記事</strong>
          </h2>

          <!-- <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            FANZAの素人動画を厳選してピックアップ。
          </div> -->

        </v-card>





      <v-container
        v-for="(detail_tag, index_tag) in ARTICLE_DETAIL.article_tags"
        :key="index_tag"
        class="px-2 px-md-4 pb-16"
      >
      <v-divider v-if="true" class="my-divider py-0 pb-2"></v-divider>


          <h2 class="text-h7 text-md-h5 mx-auto mb-4 ">
            <strong class="text-h6 text-md-h4">{{ detail_tag.article_tag_name }}</strong>（ タグ ）
          </h2>

        <v-row
          class="scrollable"
          style="flex-wrap: nowrap!important;"

        >
          <template
            v-for="item in [3,4,5,6]"
          >
                  <template
                  v-for="(ARTICLE, index) in connection_tags[detail_tag.article_tag_name_eng]"
                  :key="index"
                  >
                  <v-col
                    cols="7"
                    sm="5"
                    md="3"
                    class="pb-0"

                  >
                  <v-row no-gutters>
                    <v-col
                    class="rounded elevation-1"
                    >
                      <v-img
                        class="rounded-t aspect-ratio-block mx-auto"
                        :src="ARTICLE.article_childlen[1].article_child_options.image"
                        lazy-src="https://picsum.photos/id/11/100/60"
                        alt="Image"

                      />
                      <v-row no-gutters>
                        <v-col cols="6" class="pa-0 my-0 my-fit-contdts d-flex">
                          <v-row no-gutters>
                            <v-btn
                              class="my-fit-contents pa-0 ma-auto"
                              color="primary"
                              lazy-src="https://picsum.photos/id/11/100/60"
                              prepend-icon="$vuetify"
                              variant="text"
                              block
                              :loading="loading"
                              @click="loading = !loading"
                              size="small"        

                            >
                              FANZA
                              <template v-slot:loader>
                                <v-progress-linear indeterminate></v-progress-linear>
                              </template>              
                            </v-btn>
                          </v-row>
                        </v-col>

                        <v-divider vertical class="my-divider"></v-divider>

                        <v-col cols="6" class="pa-0 my-0 my-fit-contdts d-flex">
                          <v-row no-gutters>
                            <v-btn
                              class="my-fit-contents pa-0 ma-auto"
                              color="primary"
                              lazy-src="https://picsum.photos/id/11/100/60"
                              prepend-icon="mdi-open-in-new"
                              variant="text"
                              block
                              :loading="loading"
                              @click="loading = !loading"      
                              size="small"        
                            >
                              再生
                              <template v-slot:loader>
                                <v-progress-linear indeterminate></v-progress-linear>
                              </template>              
                            </v-btn>
                          </v-row>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>

                  {{ARTICLE.article_title.split(" - ")[0]}}
                  </v-col>


                </template>
                <!-- {{ connection_performers["kojima-miko"][0].video_productnumber }}
                {{ connection_tags["fera"][0].video_productnumber }} -->
        </template>

        </v-row>

      </v-container>







    </v-card>
  </template>
  


<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });

import { useRoute } from 'vue-router';
const route = useRoute();
const targetarticleinfo  = route.params.article_title_eng;
const ARTICLE_DETAIL = computed(() => { return ARTICLE_LIST.value.find(item => item.article_title_eng === targetarticleinfo); });
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

// const connection_performers = computed(() => {
//   let result = {};
//   for (const video_detail_performer of VIDEO_DETAIL.value.video_performers) {

//     // 初期化
//     result[video_detail_performer.name_eng] = [];

//     // VIDEOS のvideo_performers.nameをリストで取得
//     for (const videos_video of VIDEOS.value) {
//       for (const video_performer of videos_video.video_performers) {
//         if (video_performer.name_eng === video_detail_performer.name_eng) {
//           result[video_detail_performer.name_eng].push(videos_video);
//           break; // パフォーマーが見つかったらループを抜ける
//         }
//       }
//     }
//   }
//   return result;
// });



const connection_tags = computed(() => {
  let result = {};
  for (const article_detail_tag of ARTICLE_DETAIL.value.article_tags) {

    // 初期化
    result[article_detail_tag.article_tag_name_eng] = [];

    // VIDEOS のvideo_tags.nameをリストで取得
    for (const articles_article of ARTICLE_LIST.value) {
      for (const article_tag of articles_article.article_tags) {
        console.log("article_tagarticle_tagarticle_tag", article_tag.article_tag_name)
        if (article_tag.article_tag_name_eng === article_detail_tag.article_tag_name_eng) {
          console.log("■■■■■■■■■■■■■■", article_tag.article_tag_name)

          result[article_detail_tag.article_tag_name_eng].push(articles_article);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});



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





.scroll-x .v-window {
  overflow-x: auto;
  white-space: nowrap;
}
.scroll-x .v-window .v-carousel-item {
  display: inline-block;
  vertical-align: top;
}
.scrollable {
  overflow-x: auto;
  white-space: nowrap;
}

</style>
  