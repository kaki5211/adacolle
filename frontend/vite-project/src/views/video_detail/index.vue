<template>
  <v-container class="px-2">


    <v-card>  
      <v-container class="px-2 px-md-4">
        <v-card v-if="true" class="text-center elevation-0 py-10">
            <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
              <strong class="text-h4 text-md-h2">動画</strong>（FANZA 素人 ）
            </h2>
            <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
              FANZAの素人動画を厳選してピックアップ。
            </div>
          </v-card>
      </v-container>
    </v-card>

    <div class="py-1" />

    
    <v-divider v-if="(index+1) % 3 == 0" class="my-divider d-none d-md-block"></v-divider>
    <v-divider v-if="(index+1) % 2 == 0" class="my-divider d-md-none"></v-divider>



    <!-- <VideoDetailV1 /> -->

    <div class="py-1" />

      <MyCardV1
        :kind="kind"
        :my_card_list="[VIDEO_DETAIL]"
        :boolean_card_title="0 == 1 ? true : false"
        string_card_title_1=""
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        string_detail = ""
        string_detail_sub = ""
        :boolean_detail_one = true
        
      />

    

    <div class="py-1" />

    <!-- <VideoDetailV2 /> -->

    <!-- <div class="py-1" /> -->

    <template v-for="(item, index) in connection_performers"
     :key="index"
    >
      <MyCardV1
        :kind="kind"
        :my_card_list="[...VIDEOS, ...VIDEOS, ...VIDEOS]"
        :boolean_card_title="index == 0 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0].name"
        string_detail_sub = "(女優)"
      />
    </template>


    <template v-for="(item, index) in connection_tags"
     :key="index"
    >
      <MyCardV1
        :kind="kind"
        :my_card_list="VIDEOS"
        :boolean_card_title="index == -1 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0].name"
        string_detail_sub = "(タグ)"
      />
    </template>
    
    
  </v-container>
</template>

<script lang="ts" setup>
import VideoDetailV1 from '@/components/video_detail/VideoDetail-v1.vue'
import VideoDetailV2 from '@/components/video_detail/VideoDetail-v2.vue'
import MyCardFilterV1 from '@/components/global/my-card-filter-v1.vue'
import MyCardV1 from '@/components/global/my-card-v1.vue'


import { useStore } from 'vuex';
import { computed, ref, watch } from 'vue';

const store = useStore();

const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const VIDEOS_FILTERED = computed(() => { return store.getters.GET_VIDEOS_FILTERED; });
import { useRoute } from 'vue-router';
const route = useRoute();
const videoProductNumber = ref(route.params.video_productnumber);
// 初回ロード時のデータ取得
const VIDEO_DETAIL = computed(() => { return VIDEOS.value.find(item => item.video_productnumber === videoProductNumber.value); });

watch(() => route.params.video_productnumber, (newId) => {
  videoProductNumber.value = newId;
  const VIDEO_DETAIL = computed(() => { return VIDEOS.value.find(item => item.video_productnumber === videoProductNumber.value); });
});


const connection_performers = computed(() => {
  // 初期化
  let result = [];
  for (const video_detail_performer of VIDEO_DETAIL.value.video_performers) {

    // VIDEOS のvideo_performers.nameをリストで取得
    for (const videos_video of VIDEOS.value) {
      for (const video_performer of videos_video.video_performers) {
        if (video_performer.name_eng === video_detail_performer.name_eng) {
          result.push([video_detail_performer, videos_video]);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});


const connection_tags = computed(() => {
  // 初期化
  let result = [];
  for (const video_detail_tag of VIDEO_DETAIL.value.video_tags) {

    // VIDEOS のvideo_tags.nameをリストで取得
    for (const videos_video of VIDEOS.value) {
      for (const video_tag of videos_video.video_tags) {
        if (video_tag.name_eng === video_detail_tag.name_eng) {
          result.push([video_detail_tag, videos_video]);
          break; // パフォーマーが見つかったらループを抜ける
        }
      }
    }
  }
  return result;
});









const kind = "video"
const boolean_card_title = false
const string_card_title_1 = "動画"
const string_card_title_2 = "（FANZA 素人 ）"
const string_card_title_3 = "FANZAの素人動画を厳選してピックアップ。"
const boolean_filter_account = true
const boolean_filter_tag = true

const kind_cat = true

</script>

