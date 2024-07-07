<script setup>
// import { VList, VListItem, VListItemContent } from 'vuetify/lib'; // 正しいインポートパスを指定


import { computed } from 'vue';
import { useStore } from 'vuex';
// import { ref, onMounted } from 'vue';
import { ref } from 'vue';
import { Icon } from '@iconify/vue';
// import { useMeta } from 'vue-meta';


const drawer = ref(false);
const props = ref(true);
const isActive = ref(true);

const store = useStore();
const myData = computed(() => {
  return store.getters.getMyData;
});

// myData.book_list[0].id



// const title = computed(() => myData.value.book_list[0]?.title || '')
// const icon = "/src/assets/book-ic_icon.svg";
// const count = ref(0);
// const increaseCount = () => {
//   count.value++;
// };
</script>


<script>
import { defineComponent } from 'vue'


export default defineComponent({
	components: {
		Icon,
	},
});
</script>






<template>
  <div>

  <v-row no-gutters class="py-1 my-bg-color-black"></v-row>
  <v-footer class="my-bg-color px-0">
    <v-row justify="center" no-gutters class="mt-10">


      <v-col cols="6">
        <v-row justify="center" no-gutters style="height: 100%">
          <v-col cols="11" align-self="center"

          >
          <v-list id="drwer-list" density="compact" nav class="pl-8 my-bg-color my-text-color-white">

            <v-list-item class="text-h3 my-text-size-40" title="ホーム" value="home"
            :to="{ name: 'Home'}"
            >
              <template v-slot:prepend>
                <v-icon><Icon icon="solar:home-bold-duotone" /></v-icon>
              </template>
            </v-list-item>

            <!-- <v-list-item class="text-h3 my-text-size-40" title="今日抜き" value="kyounuki"
            :to="{ name: 'Kyounuki'}"
            >
              <template v-slot:prepend>
                <v-icon><Icon icon="icon-park:soccer-one" /></v-icon>
              </template>
            </v-list-item> -->
            
            <v-list-item class="text-h3 my-text-size-40" title="ブログ記事" value="video"
              :to="{ name: 'Articles'}"
              >
                <template v-slot:prepend>
                  <v-icon>mdi-post-outline</v-icon>
                </template>
              </v-list-item>


            <v-list-item class="text-h3 my-text-size-40" title="動画" value="video"
            :to="{ name: 'Videos'}"
            >
              <template v-slot:prepend>
                <v-icon><Icon icon="icon-park:video-two" /></v-icon>
              </template>
            </v-list-item>          


            <v-list-item class="my-text-size-40" disabled title="ランキング(準備中...)" value="ranking">
              <template v-slot:prepend>
                <v-icon><Icon icon="icon-park:ranking-list" /></v-icon>
              </template>
            </v-list-item>

            </v-list>

            </v-col>
        </v-row>
      </v-col>



 

      <v-col cols="6">
        <v-row justify="center" no-gutters style="height: 100%">
          <v-col cols="11" align-self="center"

          >
          <v-list id="drwer-list" density="compact" nav class="pl-8 my-bg-color my-text-color-white">

          <v-list-item class="my-text-size-40" disabled title="ブログ記事(準備中...)" value="ranking">
            <template v-slot:prepend>
              <v-icon><Icon icon="fluent:content-view-28-filled" /></v-icon>
            </template>
          </v-list-item>

          </v-list>
            <!-- <v-btn

              :ripple="true"
              color="white my-fit-contents"
              variant="text"
              class="mx-2 text-h3 py-4"
              rounded="xl"
            >
              {{ link }}
            </v-btn> -->
          </v-col>

          <v-col cols="11" class="py-10 d-flex mt-auto mb-0" >
              



                <v-btn :ripple="false" size="100" icon color="var(--my-color)" class="mx-auto">
                  <v-icon size="100" color="#1DA1F2">mdi-twitter</v-icon>
                </v-btn>


                <v-btn :ripple="false" size="100" icon color="var(--my-color)" class="mx-auto">
                  <v-icon size="100"><Icon icon="skill-icons:instagram" /></v-icon>
                </v-btn>






          </v-col> 
        </v-row>
      </v-col>
      


      <v-row no-gutters class="py-3 my-bg-color-black"></v-row>

      <v-col class="text-center text-h3 mt-10 my-text-color-white" cols="12">
            {{ new Date().getFullYear() }} — <strong>Kyounuki</strong>
      </v-col>
    </v-row>
  </v-footer>
  <v-row no-gutters class="py-2 my-bg-color-black"></v-row>
</div>
  </template>




<style>
.v-list-item__content {
    align-self: center;
    grid-area: content;
    overflow: inherit;
}

</style>