<template>
  <v-card
    class="pa-2 pa-md-8"
    flat
  >
    <v-container class="px-1">
      <v-row
        align="center"
        justify="space-between"
      >

      <v-col
          cols="12"
          md="5"
          class="d-none d-md-block"
        >
          <h1 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">記事</strong>（ブログ）
          </h1>
          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            あらゆるジャンルを比較調査する実用性ブログ。
          </div>
          <div class="d-flex ga-4 justify-center mt-6 mr-auto ml-0">
            <v-btn
              color="black"
              variant="outlined"
              rounded
              size="large"
              text="もっと見る..."
              width="128"
              :to="{ name: 'Article'}"
              />

            <!-- <v-btn
              color="white"
              elevation="1"
              rounded
              size="large"
              text="Login"
              width="128"
            /> -->
          </div>

        </v-col>





        <v-col
          cols="12"
          md="6"
        >
                  <v-carousel
                    class="aspect-ratio-block h-100 my-img"
                   :show-arrows="false"
                   :cycle="true"
                   v-model="currentIndex"
                   v-if="ARTICLE_LIST"
                  >
                  <router-link
                      v-for="(ARTICLE, index) in ARTICLE_LIST.slice(-5)"
                      :key="index"
                        style="width: 100%; height: 100%; text-decoration: none; z-index: 1;"
                        :to="{ name: 'Article_Detail', params: { article_title_eng: ARTICLE.article_title_eng}}"

                      >

                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->
                  <!-- v-for="(item,ii) in parseJson(VIDEO.video_images)" -->
                    <v-carousel-item
                      :src="ARTICLE.article_childlen[0].article_child_options.image"
                      alt="Image"
                      lazy-src="https://picsum.photos/id/11/100/60"
                      >
                   

                      <v-row no-gutters>
                        <!-- <v-col cols="12" class="d-flex rounded-1"
                          v-for="(item,iii) in ARTICLE.article_tags"
                          :key="iii"
                        >
                          <v-btn 
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                            :prepend-icon="'mdi-account-circle'"
                            >
                            {{item.name}}
                          </v-btn>
                        </v-col>
               -->
                        <v-col cols="12" class="d-flex"
                          v-for="(item,iii) in ARTICLE.article_tags"
                          :key="iii"
                        >
                          <v-btn 
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                            :prepend-icon="'mdi-tag-text'"
                            :to="{ name: 'Article', query: { tag: item.article_tag_name_eng, performer: '' } }"
                          >
                            {{item.article_tag_name}}
                          </v-btn>
                        </v-col>
                 
                      </v-row>

                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                  </v-carousel-item>
                </router-link>
              </v-carousel>
                  <p v-if="currentIndex">{{ ARTICLE_LIST[currentIndex].article_title }}</p>
        </v-col>


























        <v-col
          cols="12"
          md="5"
          class="d-md-none"
        >
          <h1 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">記事</strong>（ブログ）
          </h1>
          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            あらゆるジャンルを比較調査する実用性ブログ。
          </div>
          <div class="d-flex ga-4 justify-center mt-6 mr-auto ml-0">
            <v-btn
              color="black"
              elevation="1"
              variant="outlined"
              rounded
              size="large"
              text="もっと見る..."
              width="128"
            />

            <!-- <v-btn
              color="white"
              elevation="1"
              rounded
              size="large"
              text="Login"
              width="128"
            /> -->
          </div>

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

const currentIndex = ref(0)

</script>
<style scoped>
.aspect-ratio-block {
  background: 
#ccc;
  aspect-ratio: 16 / 9;
}

.v-img__img {
  left:-10%!important;
}

.my-fit-contents {
  height: fit-content!important;
}
</style>