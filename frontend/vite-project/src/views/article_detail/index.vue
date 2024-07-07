<template>
  <v-container class="px-2">


    
    <h1>Testimonials</h1>



    <ArticleDetailV1 />

    <div class="py-1" />

    <ArticleDetailV3 />
    
    <div class="py-1" />

    <!-- <ArticleDetailV2 /> -->

    <template v-for="(item, index) in connection_tags"
     :key="index"
    >
      <MyCardV1
        :kind="kind"
        :my_card_list="ARTICLE_LIST"
        :boolean_card_title="index == -1 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0].name"
        string_detail_sub = "タグ"
      />
    </template>


  </v-container>
</template>

<script lang="ts" setup>
import ArticleDetailV1 from '@/components/article_detail/ArticleDetail-v1.vue'
import ArticleDetailV2 from '@/components/article_detail/ArticleDetail-v2.vue'
import ArticleDetailV3 from '@/components/article_detail/ArticleDetail-v3.vue'

import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
const store = useStore();
const route = useRoute();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const Tableargetarticlenameeng  = route.params.article_title_eng;
const ARTICLE_DETAIL = computed(() => { return ARTICLE_LIST.value.find(item => item.article_title_eng === Tableargetarticlenameeng); });


import { computed, ref } from 'vue';



const kind = "article"

const connection_tags = computed(() => {
  let result = [];
  for (const article_detail_tag of ARTICLE_DETAIL.value.article_tags) {

     // VIDEOS のvideo_tags.nameをリストで取得
    for (const articles_article of ARTICLE_LIST.value) {
      for (const article_tag of articles_article.article_tags) {
        if (article_tag.article_tag_name_eng === article_detail_tag.article_tag_name_eng) {

          result.push([article_detail_tag, articles_article]);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});

</script>

