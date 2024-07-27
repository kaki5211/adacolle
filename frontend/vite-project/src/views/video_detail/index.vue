<template>
  <v-container class="px-2">


    <MyTitleV1
    :string_card_title_1="'[' + VIDEO_DETAIL.video_productnumber + ']&emsp;' + VIDEO_DETAIL.video_title.split(' - ')[0]"
      string_card_title_2=""
      string_card_title_3=""
    />    

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
        :my_card_list="[item[1]]"
        :boolean_card_title="index == 0 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0].name"
        string_detail_sub = "(女優)"
      />
    </template>
    {{  }}

    <!-- :my_card_list="[...VIDEOS, ...VIDEOS, ...VIDEOS]" -->

    <template v-for="(item, index) in connection_tags"
     :key="index"
    >
      <MyCardV1
        :kind="kind"
        :my_card_list="[item[1]]"
        :boolean_card_title="index == -1 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0].name"
        string_detail_sub = "(タグ)"
      />
    </template>
    
    
    <template v-for="(item, index) in connection_labels"
     :key="index"
    >
      <MyCardV1
        :kind="kind"
        :my_card_list="[item[1]]"
        :boolean_card_title="index == -1 ? true : false"
        string_card_title_1="関連"
        string_card_title_2=""
        string_card_title_3=""
        :boolean_detail = true
        :string_detail = "item[0]"
        string_detail_sub = "(レーベル)"
      />
    </template>


    
  </v-container>
</template>

<script lang="ts" setup>
import MyCardFilterV1 from '@/components/global/my-card-filter-v1.vue'
import MyCardV1 from '@/components/global/my-card-v1.vue'
import MyTitleV1 from '@/components/global/my-title-v1.vue'



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


const connection_labels = computed(() => {
  // 初期化
  let result = [];

    // VIDEOS のvideo_tags.nameをリストで取得
    for (const videos_video of VIDEOS.value) {
      if (videos_video.video_label.name_eng === VIDEO_DETAIL.value.video_label.name_eng) {
        result.push([VIDEO_DETAIL.value.video_label.name, videos_video]);
        break; // パフォーマーが見つかったらループを抜ける
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

