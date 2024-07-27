<template>
  <v-container class="px-2">
    <!-- <h1>Home</h1> -->

    <!-- <Breadcrumbs /> -->

    <!-- <div class="py-1" /> -->

    <HeroHeaderMyV1 />

    <div class="py-1" />

    <ContentMyV1 />

    <div class="py-1" />

    <ContentMyV2 />

    <div class="py-1" />

    <!-- <FeaturesV1 /> -->

    <!-- <div class="py-1" /> -->

    <!-- <CalltoActionV1 /> -->

    <!-- <div class="py-1" /> -->

    <!-- <TitleMyV5 /> -->

    <!-- <div class="py-1" /> -->

    <MyCardV1
      kind="article"
      :my_card_list="ARTICLE_LIST"
      :boolean_card_title="true"
      string_card_title_1="ランダムピックアップ"
      string_card_title_2=""
      string_card_title_3="&nbsp;"
      :boolean_detail = false

    />
    <div class="py-1" />

    <!-- <TestimonialV2 /> -->

    <!-- <div class="py-1" /> -->

    <!-- <PricingTableV1 /> -->

    <!-- <div class="py-1" /> -->

    <TeamMy1 />

    <!-- <div class="py-1" /> -->

    <!-- <FooterMyV2 /> -->

  </v-container>
</template>

<script lang="ts" setup>
// import Breadcrumbs from '@/components/breadcrumbs/breadcrumbs-v1.vue'
import CalltoActionV1 from '@/components/call-to-action/CalltoAction-v1.vue'
import ContentMyV1 from '@/components/content/Content-my-v1.vue'
import ContentMyV2 from '@/components/content/Content-my-v2.vue'
import ContentV2 from '@/components/content/Content-v2.vue'
import FeaturesV1 from '@/components/features/Features-v1.vue'
import BlogMyV1 from '@/components/blog/Blog-my-v1.vue'
// import FooterMyV2 from '@/components/footer/Footer-my-v2.vue'
import GalleryV1 from '@/components/gallery/Gallery-v1.vue'
import HeroHeaderV1 from '@/components/hero-headers/HeroHeaders-v1.vue'
import HeroHeaderMyV1 from '@/components/hero-headers/HeroHeaders-my-v1.vue'
import PricingTableV1 from '@/components/pricing/PricingTable-v1.vue'
import TeamMy1 from '@/components/team/Team-My-v1.vue'
import TestimonialV2 from '@/components/testimonial/Testimonial-v2.vue'

import TitleMyV2 from '@/components/title/Title-My-v2.vue'
import TitleMyV5 from '@/components/title/Title-My-v5.vue'

import MyCardV1 from '@/components/global/my-card-v1.vue'


import { useStore } from 'vuex';
import { computed, ref } from 'vue';

const store = useStore();

const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
</script>