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
          md="6"
        >
                  <v-carousel
                    class="aspect-ratio-block h-100 my-img"
                   :show-arrows="false"
                   :cycle="true"
                   v-model="currentIndex"
                   v-if="VIDEOS"
                   
                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->
                  <!-- v-for="(item,ii) in parseJson(VIDEO.video_images)" -->
                      <router-link
                        v-for="(VIDEO, index) in VIDEOS.slice(-5)"
                        :key="index"
                        :to="{ name: 'Video_Detail', params: { video_productnumber: VIDEO.video_productnumber}}"
                        style="width: 100%; height: 100%; text-decoration: none; z-index: 1;"
                      >

                      <v-carousel-item

                        :src="VIDEO.video_image"
                        alt="Image"
                        lazy-src="https://picsum.photos/id/11/100/60"

                      >

                      <!-- <router-link
                        :to="{ name: 'Video', params: { param: VIDEO.video_productnumber}}"
                        style="display: block; width: 100%; height: 100%;"
                        class="d-flex"
                      >
                      </router-link> -->

                      <v-row no-gutters> 
                        <v-col cols="12" class="d-flex rounded-1"
                          v-for="(item,iii) in VIDEO.video_performers"
                          :key="iii"

                        >
                          <v-btn 
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                            :prepend-icon="'mdi-account-circle'"
                            style="z-index: 10;"
                            :to="{ name: 'Video', query: { tag: '', performer: item.name_eng } }"
                            >
                            {{item.name}}
                          </v-btn>
                        </v-col>
              
                        <v-col cols="12" class="d-flex"
                          v-for="(item,iii) in VIDEO.video_tags"
                          :key="iii"
                        >
                          <v-btn 
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2 "
                            :prepend-icon="'mdi-tag-text-outline'"
                            style="z-index: 10;"
                            :to="{ name: 'Video', query: { tag: item.name_eng, performer: '' } }"

                            >
                            {{item.name}}
                          </v-btn>
                        </v-col>
                        <v-col cols="12" class="d-flex rounded-1"
                          v-for="(item,iii) in [VIDEO.video_label]"
                          :key="iii"

                        >
                          <v-btn 
                            rounded="0"
                            class="my-fit-contents text-caption ms-auto me-0 px-1 pl-2"
                            :prepend-icon="'mdi-label-outline'"
                            style="z-index: 10;"
                            :to="{ name: 'Video', query: { tag: '',performer: '', label: item.name_eng } }"
                            >
                            {{item.name}}
                          </v-btn>
                        </v-col>                        
                      </v-row>


                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                  </v-carousel-item>
                  </router-link>
                  </v-carousel>
                  <p>{{ VIDEOS[currentIndex].video_title }}</p>

        </v-col>

        <v-col
          cols="12"
          md="5"
        >
          <h1 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">動画</strong>（FANZA 素人 ）
          </h1>

          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            FANZAの素人動画を厳選してピックアップ。
          </div>
          <div class="d-flex ga-4 justify-center mt-6">
            <v-btn
              color="black"
              elevation="1"
              variant="outlined"
              rounded
              size="large"
              text="もっと見る..."
              width="128"
              :to="{ name: 'Video'}"
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


const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });

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