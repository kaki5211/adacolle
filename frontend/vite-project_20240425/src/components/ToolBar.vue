


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
  <header>
    <v-app-bar  
      rounded
      color="var(--my-color)"
      height="150"
      prominenttitle
      scroll-behavior="elevate fade-image"
      scroll-target="#my-scroll-target"
      :scroll-threshold="200"
      id="#toolbar"
        >
        
      <v-toolbar-title @click="$router.push({ name: 'Home' })" class="my-text-title my-text-size-50 my-text-color-white">BOOK</v-toolbar-title>

      <v-spacer></v-spacer>
        <v-btn class="mx-11 d-flex" icon>
          <v-icon class="align-center" size="80" color="#1DA1F2">mdi-twitter</v-icon>
        </v-btn>


        <v-btn class="mx-11 d-flex" icon>
          <v-icon class="align-center" size="80"><Icon icon="skill-icons:instagram" /></v-icon>
        </v-btn>
        <v-app-bar-nav-icon class="mx-11 d-flex"  @click.stop="drawer = !drawer">
          <v-icon class="align-center my-text-color-white" size="80">mdi-backburger</v-icon>
        </v-app-bar-nav-icon>

        
    </v-app-bar>






      <v-navigation-drawer
        temporary
        location="right"
        v-model="drawer"
        style="width: 70%"
      >



      <template v-slot:prepend>
        <v-list-item
          lines="two"
          style=""
          class="my-text-size-50 d-flex"
          
        >
          <template v-slot:prepend>
            <v-avatar size="10" style="height: auto; width: 100%;">
              <img style="height: 350px; width: 350px;" src="/src/assets/avatar.jpg" alt="Avatar">
            </v-avatar>
          </template>

        </v-list-item>

      </template>
      <v-list-item
          lines="two"
          style=""
          class="my-text-size-50 d-flex text-center mx-auto d-flex w-100"
          center
          
        >
        <v-list-item-content class="mx-auto w-100">
            <v-list-item-title class="my-text-size-40 my-fit-contents font-weight-bold my-text-margin-05 pb-10">Jane Smith(仮)（管理人）</v-list-item-title>
            <!-- <v-list-item-subtitle class="my-text-size-30 my-fit-contents my-text-margin">Logged in</v-list-item-subtitle> -->
        </v-list-item-content>

        </v-list-item>



        <v-divider></v-divider>




        
        <v-list id="drwer-list" density="compact" nav class="pl-8">

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
      <v-icon><Icon icon="icon-park:video-two" /></v-icon>
    </template>
  </v-list-item>

  <v-list-item class="text-h3 my-text-size-40" title="動画" value="video"
  :to="{ name: 'Videos'}"
  >
    <template v-slot:prepend>
      <v-icon><Icon icon="icon-park:video-two" /></v-icon>
    </template>
  </v-list-item>

  <!--
  <v-list-item class="my-text-size-40" disabled title="ランキング(準備中...)" value="ranking">
    <template v-slot:prepend>
      <v-icon><Icon icon="icon-park:ranking-list" /></v-icon>
    </template>
  </v-list-item>

  <v-list-item class="my-text-size-40" disabled title="ブログ記事(準備中...)" value="ranking">
  <template v-slot:prepend>
    <v-icon><Icon icon="fluent:content-view-28-filled" /></v-icon>
  </template>
</v-list-item>
-->

</v-list>



</v-navigation-drawer>
<!-- <v-main style="height: 500px"></v-main> -->


    
</header>
</template>





<style>

.v-toolbar-title__placeholder {
  height: auto;
  overflow: visible!important;;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.v-navigation-drawer__prepend {
  margin-left: auto!important;
  margin-right: auto!important;
}



.v-list-item__content{
  align-self: center;
    grid-area: content;
    overflow: hidden;
    width: 100%;
}

#drwer-list .v-list-item-title {
  font-size: 50px;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}



</style>














<!-- 

<v-dialog
transition="dialog-bottom-transition"
width="auto"
>
<template v-slot:activator="{ props }">
  <v-btn
    icon
    color=var(--my-color-white)
    v-bind="props"
  ><v-icon>mdi-export</v-icon></v-btn>
</template>

<template v-slot:default="{ isActive }">
  <v-card class="rounded-xl">
    <v-list-item class="py-2 my-bg-color" href="{% url 'book:top' %}">
      <v-list-item-content class="my-bg-color">
        <v-list-item-title class="my-text-title my-text-size-50 my-text-color-white text-center py-2">
        </v-list-item-title>
        <v-list-item-subtitle class="text-center my-text-size-30 my-text-color-white">
          ～本の感想を創造するブログ～
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-card-text class="my-bg-color-gray">
      <v-responsive :aspect-ratio="16/9">
        <div>SITE MAP</div>
      </v-responsive>
    </v-card-text>
    <v-card-text>
      <v-responsive :aspect-ratio="16/9">
        <div class="text-h2 pa-12">Hello world!</div>
      </v-responsive>
    </v-card-text>

    
    <v-card-actions class="justify-end">
      <v-btn
        variant="text"
        @click="isActive.value = false"
      >Close</v-btn>
    </v-card-actions>
  </v-card>
</template>
</v-dialog>
 -->
