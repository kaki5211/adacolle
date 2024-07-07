<template>
  <v-card>
    <v-container>
        <v-card class="text-center elevation-0 py-10">
    <!-- <h2 class="text-grey-darken-1 font-weight-regular">
      Introducing new
    </h2> -->

    <h2>
      <b>ランダムピックアップ</b>
    </h2>
  </v-card>
      <v-row>


        <v-col
          cols="12"
          md="4"
          v-for="item in ARTICLE_LIST"
          :key="item"
        >
          <v-img
            class="rounded elevation-5"
            height="200"
            gradient="#262626, #262626"
          />

          <div class="pa-5">
            <div class="text-left">
              <div class="text-h5 mb-2">
                {{item.article_title}}
              </div>

              <div class="text-caption mb-5">
                {{item.article_post_day}}
                <!-- December 4, 2023 -->
              </div>
            </div>
            <div class="text-right">
              <v-btn
                color="black"
                elevation="1"
                variant="outlined"
                rounded
                size="large"
                text="もっと見る..."
                width="128"
                :to="{ name: 'Article_Detail', params: { article_title_eng: item.article_title_eng } }"
              />
            </div>
          </div>
        </v-col>



        <v-col
          cols="12"
          md="4"
          v-for="item in [3,4,5,6]"
          :key="item"
        >
          <v-img
            class="rounded elevation-5"
            height="200"
            gradient="#262626, #262626"
          />

          <div class="pa-5">
            <div class="text-h5 mb-2">
              Optimizing User Interfaces with Vuetify
            </div>

            <div class="text-caption mb-5">
              December 4, 2023
            </div>

            <v-btn
              color="black"
              elevation="1"
              variant="outlined"
              rounded
              size="large"
              text="もっと見る..."
              width="128"
            />

          </div>
        </v-col>


      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });

</script>
