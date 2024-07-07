


<script setup>

import { ref , computed} from 'vue';
import { useStore } from 'vuex';
const store = useStore();



// // 事前に定義したパスと表示する文字列の対
// const pathMapping = {
//   video: "コンテンツ",
//   performer: "パフォーマー",
//   maker: "メーカー",
//   kyounuki: "今日抜き",
//   // ...
// };

// // URLのパスを取得
// const urlPath = window.location.pathname;


// // パスを"/"で区切ってリストに変換
// const pathList = urlPath.split("/").filter((path) => path !== "");
// console.log("pathList", pathList)

// // パンくずリストの初期化
// const breadcrumbsList = ref([
//   {
//     title: 'ホーム',
//     disabled: false,
//     href: '/',

//   },
// ]);
// console.log("breadcrumbsList", breadcrumbsList)

// // パスごとにパンくずリストを作成
// let currentPath = "";
// for (let i = 0; i < pathList.length; i++) {
//   const path = pathList[i];
//   currentPath += `/${path}`;
//   const name = pathMapping[path] || path;
//   const disabled = i === pathList.length - 1; // 最後の要素の場合のみ disabled: true
//   breadcrumbsList.value.push({ title: name, disabled, href: currentPath });
// }


// store.dispatch('FETCH_GET_BREADCRUMBS')
// const breadcrumbsList = ref(computed(() => { return store.getters.GET_BREADCRUMBS; }))
const breadcrumbsList = computed(() => { return store.getters.GET_BREADCRUMBS; })




</script>


<script >

</script>





<template>
 <div>
    
    <v-breadcrumbs
      v-if = "breadcrumbsList"
      :items="breadcrumbsList"
      color="var(--my-color-white)"
      bg-color="var(--my-color)"
      class=""
      style="white-space: nowrap; overflow-x: auto"
      :to="breadcrumbsList"


    >
      <template v-slot:divider>
        <v-icon
          color="var(--my-color-white)"
          icon="mdi-chevron-right"
          size="40"
        ></v-icon>
      </template>
      <template v-slot:prepend>
        <v-icon
          color="var(--my-color-white)"
          size="40"
          icon="mdi-home"
        ></v-icon>
      </template>
    </v-breadcrumbs>
  </div>
</template>



<style>
.v-breadcrumbs a{
  font-size: 35px;

}
</style>

