<template>
  <v-container class="px-2">

    <MyCardFilterV1
      :kind="kind"
      :my_card_list="ARTICLE_LIST_FILTERED"
      :string_card_title_1="string_card_title_1"
      :string_card_title_2="string_card_title_2"
      :string_card_title_3="string_card_title_3"
      :boolean_filter_account="boolean_filter_account"
      :boolean_filter_tag="boolean_filter_tag"

      


    />

    <!-- <ArticleV3 /> -->

    <!-- <div class="py-1" /> -->

    <!-- <ArticleV1 /> -->

    <div class="py-1" />

    <MyCardV1
      :kind="kind"
      :my_card_list="ARTICLE_LIST_FILTERED"
      :boolean_card_title="boolean_card_title"
      :string_card_title_1="string_card_title_1"
      :string_card_title_2="string_card_title_2"
      :string_card_title_3="string_card_title_3"

    />




  </v-container>
</template>

<script lang="ts" setup>
import ArticleV1 from '@/components/article/Article-v1.vue'
import ArticleV3 from '@/components/article/Article-v3.vue'
import MyCardV1 from '@/components/global/my-card-v1.vue'
import MyCardFilterV1 from '@/components/global/my-card-filter-v1.vue'

import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();

const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const ARTICLE_LIST_FILTERED = computed(() => { return store.getters.GET_ARTICLE_LIST_FILTERED; });
// const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
// const VIDEOS_FILTERED = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });

const kind = "article"
const boolean_card_title = false
const string_card_title_1 = "記事"
const string_card_title_2 = "（ ブログ ）"
const string_card_title_3 = ""
const boolean_filter_account = false
const boolean_filter_tag = true


store.dispatch('FETCH_GET_ARTICLE_LIST_FILTERED');




</script>
