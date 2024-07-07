<template>
    <v-card>
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

                  <template
                  v-for="(ARTICLE, index) in [ARTICLE_LIST[1]]"
                  :key="index"
                  >
                  <v-col
                    class="mx-auto "
                    cols="8"
                    md="6"
                  >
                    <v-row no-gutters>
                      <v-col
                        class="rounded elevation-1"
                        cols="12"
                      >
                      <!-- <v-divider v-if="(index+1) % 3 == 0" class="my-divider d-none d-md-block"></v-divider> -->
                      

                      
                        <v-img
                          class="rounded-t aspect-ratio-block mx-auto"
                          :src="ARTICLE.article_childlen[0].article_child_options.image"
                          lazy-src="https://picsum.photos/id/11/100/60"
                          alt="Image"
                        >
                      </v-img>

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
                              >
                                FANZA
                                <template v-slot:loader>
                                  <v-progress-linear indeterminate></v-progress-linear>
                                </template>              
                              </v-btn>
                            </v-row>
                          </v-col>

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


                    <div class="pa-0">
                      <div class="text-left">
                        <div class="text-caption">
                          {{ARTICLE.article_postday}}
                        </div>
                        <div class="text-h9">
                          {{ARTICLE.article_title.split(" - ")[0]}}
                        </div>
          
                        
                        <v-col cols="" class="pa-0">
                          <!-- <v-btn 
                          v-for="(item,iii) in ARTICLE.article_performers"
                                    :key="iii"

                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1"
                            :prepend-icon="'mdi-account-circle'"
                            size="small"
                            >
                            {{item.name}}
                          </v-btn> -->

                          <v-btn 
                          v-for="(item,iii) in ARTICLE.article_tags"
                            :key="iii"
                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1"
                            :prepend-icon="'mdi-tag-text-outline'"
                            size="small"
                            >
                            {{item.article_tag_name}}
                          </v-btn>


                        </v-col>


                      </div>
                    </div>
                  </v-col>


                </template>
        
        </v-row>
</div>









          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Mobile ■■■-->
          <!-- ■■■■■■■■■■■■■■ -->
        <v-row
          class="d-xs-none"
        >
                  <template
                  v-for="(ARTICLE, index) in [ARTICLE_LIST[1]]"
                  :key="index"
                  >
                  <v-col
                    cols="11"
                    xs="11"
                    class="mx-auto"
                  >
                  <v-row no-gutters>
                    <v-col
                    class="rounded elevation-1"
                    >
                      <v-img
                        class="rounded-t aspect-ratio-block mx-auto"
                        :src="ARTICLE_LIST.article_image"
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



                  </v-col>


                  <v-col
                    cols="12"
                    md="12"
                    class="px-3 pr-2"
                  >
                    <div class="pa-0">
                      <div class="text-left">
                        <div class="text-body-2">
                          {{ARTICLE.article_postday}}
                        </div>
                        <div class="text-h7">
                          {{ARTICLE.article_title.split(" - ")[0]}}
                        </div>
          
                        
                        <v-col cols="" class="pa-0">
                          <!-- <v-btn 
                          v-for="(item,iii) in ARTICLE.article_performers"
                            :key="iii"
                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1"
                            :prepend-icon="'mdi-account-circle'"
                            size="small"
                            >
                            {{item.name}}
                          </v-btn> -->

                          <v-btn 
                          v-for="(item,iii) in ARTICLE.article_tags"
                            :key="iii"
                            elevation="1"
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto px-1"
                            :prepend-icon="'mdi-tag-text-outline'"
                            size="small"
                            >
                            {{item.article_tag_name}}
                          </v-btn>


                        </v-col>


                      </div>
                    </div>


                  </v-col>
                </template>
        </v-row>


        <v-divider class="my-divider my-14"></v-divider>



        <!-- images -->
        <!-- <div
          class="d-none d-xs-block"
        >
          <v-row
          >
            <v-col
            v-for="(image,iiii) in [ARTICLE_DETAIL.article_childlen[0].article_child_options.image]"
                :key="iiii"
              class="mx-auto "
              cols="4"
              md="3"
            >
              <v-img
                class="rounded-t aspect-ratio-block mx-auto"
                :src=image
                lazy-src="https://picsum.photos/id/11/100/60"
                alt="Image"
              >
              </v-img>

            </v-col>
          </v-row>
        </div> -->


        <!-- Mobile -->
        <!-- <v-row
          class="d-xs-none px-3"
        >
          <v-col
            v-for="(image,iiii) in [ARTICLE_DETAIL.article_childlen[0].article_child_options.image]"
              :key="iiii"

          class="mx-auto px-2"
          cols="6"
          md="6"
          >
              <v-img
                class="rounded-t aspect-ratio-block mx-auto"
                :src=image
                lazy-src="https://picsum.photos/id/11/100/60"
                alt="Image"
              >
              </v-img>
            </v-col>
          </v-row> -->
        <!-- images end -->

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
const ARTICLE_DETAIL_images = (item) => {
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
  