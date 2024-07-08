<template>
  <v-container class="px-2">

    <MyCardFilterV1
      :kind="kind"
      :my_card_list="VIDEOS_FILTERED"
      :string_card_title_1="string_card_title_1"
      :string_card_title_2="string_card_title_2"
      :string_card_title_3="string_card_title_3"
      :boolean_filter_account="boolean_filter_account"
      :boolean_filter_tag="boolean_filter_tag"
      :boolean_detail = false
    />

    <!-- <VideoV3 /> -->

    <!-- <div class="py-1" /> -->

    <!-- <VideoV1 /> -->

    <div class="py-1" />

    <MyCardV1
      :kind="kind"
      :my_card_list="VIDEOS_FILTERED"
      :boolean_card_title="boolean_card_title"
      :string_card_title_1="string_card_title_1"
      :string_card_title_2="string_card_title_2"
      :string_card_title_3="string_card_title_3"
      :boolean_detail = false
    />

    

  </v-container>
</template>

<script lang="ts" setup>
// import VideoV3 from '@/components/video/Video-v3.vue'
// import VideoV1 from '@/components/video/Video-v1.vue'
import MyCardV1 from '@/components/global/my-card-v1.vue'
import MyCardFilterV1 from '@/components/global/my-card-filter-v1.vue'

import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();

// const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const VIDEOS_FILTERED = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });

console.log(VIDEOS_FILTERED)

const kind = "video"
const boolean_card_title = false
const string_card_title_1 = "動画"
const string_card_title_2 = "（FANZA 素人 ）"
const string_card_title_3 = "FANZAの素人動画を厳選してピックアップ。"
const boolean_filter_account = true
const boolean_filter_tag = true

const kind_cat = true

store.dispatch('FETCH_GET_VIDEOS_FILTERED');

// store.commit('SET_SEARCHPARAMS_VIDEO', { value: { tags: [newQuery.tag], performers: [newQuery.performer] } });
// store.commit('SET_SEARCHPARAMS_ARTICLE', { value: { performers: [newQuery.performer] } });




// const ARTICLE_LIST_FILTERED = computed(() => {
//   const tags = searchparams.value.tags;

//   // 両方の条件が空の場合はすべてのビデオを返す
//   if (tags.length === 0) {
//     store.dispatch('FETCH_GET_ARTICLE_LIST_FILTERED', ARTICLE_LIST.value);
//     return ARTICLE_LIST.value;
//   }

//   // タグでフィルタリング
//   let temp = ARTICLE_LIST.value.filter(article => {
//       const article_tags_list = article.article_tags.map(item => item.article_tag_name_eng);
//       return tags.length === 0 || tags.every(tag => article_tags_list.includes(tag));
//   });
  
//   // storeに登録
//   // store.commit("", temp)
//   store.dispatch('FETCH_GET_ARTICLE_LIST_FILTERED', temp);

//   return temp
// });



</script>
