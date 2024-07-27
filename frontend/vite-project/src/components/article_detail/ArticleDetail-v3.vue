<template>
    <v-card>
      <v-container class="px-2 px-md-4">
          <v-card class="text-center elevation-0 py-10">
      <!-- <h2 class="text-grey-darken-1 font-weight-regular">
        Introducing new
      </h2> -->
  
          <h2 class="text-h5 text-md-h3 mx-auto mb-4 ">
            <strong class="text-h4 text-md-h2">フィルター</strong><!-- （FANZA 素人 ） -->
          </h2>

          <div class="text-medium-emphasis text-md-h6 text-body-3 pl-2">
            
          </div>

        </v-card>



      <v-row no-gutters >
        <v-col
        :key="key" v-for="(value, key) in article_detail_explain"
        cols="12"
        sm="12"
        md="6"
        lg="4"
        >
      <!-- 素材セクション -->
        <v-card class="mb-4">
          <v-card-title v-if="ARTICLE_DETAIL_OPTIONS_SEARCH_LIST">
            {{ ARTICLE_DETAIL.article_options[key] }}
          </v-card-title>
          <!-- <v-btn @click="updateSearchParams(searchparams, value, key)" :color="searchparams[key].includes(value) ? 'primary' : 'secondary'">
            {{ searchparams[key].includes(value) ? 'ON' : 'OFF' }}a
          </v-btn>           -->
          <v-card-text>
            <v-list dense>
              <v-list-item v-for="(value2, key2) in value" :key="key2">

                <v-chip-group
                                  column
                                  color="text-deep-purple-accent-4"
                                >
                                <v-chip
                                    size="small"
                                    filter-icon="mdi-checkbox-marked"
                                    :value="key2"
                                    color=""
                                    @click="updateSelection(key, key2); updateFilteredOptions();"
                                    class="custom-chip-style"

                                  >
                                    <v-icon v-if="true">
                                      
                                      {{ ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key].includes(key2) ? 'mdi-checkbox-marked' : 'mdi-checkbox-blank-outline' }}
                                    </v-icon>

                                  </v-chip>

                <v-list-item>
                  <div class="d-flex">
                    <v-list-item-title>{{ key2 }}</v-list-item-title>
                    <!-- <v-switch
                    @click="updateSearchParams(searchparams, key2, key)"
                    :color="searchparams[key].includes(key2) ? 'primary' : 'secondary'"
                    :label="searchparams[key].includes(key2) ? 'ON' : 'OFF'"
                    >
                      {{ searchparams[key].includes(value) ? 'ON' : 'OFF' }}
                    </v-switch>  -->




                  <!-- <v-col cols="6">
                    <v-switch
                      :model-value="false"
                      color="primary"
                      label="off"
                    ></v-switch>
                  </v-col>                     -->
                    
                  </div>
                  <v-list-item-subtitle class="pl-5">{{ value2 }}</v-list-item-subtitle>
                </v-list-item>
              </v-chip-group>

              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>



        </v-col>

      </v-row>

    <div
      class=""
    >

        <v-row
        >
        <v-col cols="12">

          <!-- ■■■■■■■■■■■■■■ -->
          <!-- ■■■ Window ■■■-->
          <!-- ■■■■■■■■■■■■■■ -->

        <div>

          <VDataTable
              v-if="ARTICLE_DETAIL_OPTIONS_FILTERED"
              color="var(--my-color-black)"
              :loading="false"
              :items-per-page="-1"
              :headers="headers"
              :items="ARTICLE_DETAIL_OPTIONS_FILTERED.article_childlen"
              item-value="name"
              class="elevation-1 scrollable"
              items-per-page-text=""
              page-text=""
              next-icon=""
              prev-icon=""
              first-icon=""
              last-icon=""
              style="overflow-x: auto; width: 100%; border-collapse: collapse; white-space: nowrap; table-layout: fixed;"
            >
              <!-- ヘッダースロットをカスタマイズして背景色を変更 -->
              <template v-slot:header="{ header }">
                <th style="background-color: #f0f0f0; color: black; padding: 10px;">
                  {{ header.text }}
                </th>
              </template>
                      
              <!-- テーブル行をレンダリングするためのカスタムアイテムスロット -->
              <template v-slot:item="{ item, index }">
                <tr>
                  <template v-for="header in headers">
                    <td v-if="header.key === 'image'">
                      <v-img
                        style="object-fit: cover;"
                        :src="item.article_child_options.image"
                        width="100"
                        height="30"
                        @click="scrollToItem(index)"
                      ></v-img>
                    </td>
                    <td v-else>
                      <span>{{ item.article_child_options[header.value] }}</span>
                    </td>
                  </template>
                </tr>
              </template>
            </VDataTable>
            </div>

          </v-col>

        </v-row>
</div>




      </v-container>
      </v-card>
  </template>
  
<script lang="ts" setup>
import { useStore } from 'vuex';
import { computed, ref, reactive } from 'vue';
import { useRoute } from 'vue-router';
import cloneDeep from 'lodash/cloneDeep';

const route = useRoute();


const store = useStore();


const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });
const targetarticleinfo  = route.params.article_title_eng;
const ARTICLE_DETAIL = computed(() => { return ARTICLE_LIST.value.find(item => item.article_title_eng === targetarticleinfo); });


const ARTICLE_DETAIL_OPTIONS_SEARCH_LIST = reactive({});
for (const [key, value] of Object.entries(JSON.parse(ARTICLE_DETAIL.value.article_options_explain))) {
  ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key] = [];
}


const updateSelection = (key, key2) => {
  if (!ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key]) {
    ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key] = [];
  }
  const index = ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key].indexOf(key2);
  if (index === -1) {
    ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key].push(key2);
  } else {
    ARTICLE_DETAIL_OPTIONS_SEARCH_LIST[key].splice(index, 1);
  }

  // フィルタリングされたオプションを更新
  updateFilteredOptions();
};

const ARTICLE_DETAIL_OPTIONS_FILTERED = computed(() => {
  let temp = cloneDeep(ARTICLE_DETAIL.value);

  for (const [key, values] of Object.entries(ARTICLE_DETAIL_OPTIONS_SEARCH_LIST)) {
    if (values.length > 0) {
      temp.article_childlen = temp.article_childlen.filter(item => {
        return values.includes(item.article_child_options[key]);
      });
    }
  }

  return temp;
});

const updateFilteredOptions = () => {
  const filteredOptions = ARTICLE_DETAIL_OPTIONS_FILTERED.value;
  store.commit('SET_ARTICLE_DETAIL_OPTIONS_FILTERED', filteredOptions);
};

// 初期化時にフィルタリングされたオプションを設定
updateFilteredOptions();




const headers = computed(() => {
  let headers = [] // 配列をリアクティブにするために ref を使用して初期化
  // シングルクォートをダブルクォートに置き換え
  let inputStr = ARTICLE_DETAIL.value.article_options_order.replace(/'/g, '"');
  // JSON.parseを使って文字列を配列に変換
  let outputArray = JSON.parse(inputStr);
  // JSON.parseを使って文字列をオブジェクトに変換
  // let outputObjDict = JSON.parse(ARTICLE_DETAIL.value.article_options);
  let outputObjDict = ARTICLE_DETAIL.value.article_options;

  for (let item of outputArray) {
    let itemValue = outputObjDict[item];
    headers.push({ title: itemValue, align: 'start', key: item, value: item });
  }
  return headers; // headers.value ではなく headers を返す
});

// const headers = [
//         { text: 'Image', value: 'image' },
//         { text: 'Name', value: 'name' },
//         { text: 'Price', value: 'price' },
//         { text: 'Thickness', value: 'thickness' },
//         { text: 'Material', value: 'material' }
//       ]





// console.log("ARTICLE_DETAIL.article_options_order", ARTICLE_DETAIL.value.article_options.name)
// for (let item of ARTICLE_DETAIL.value.article_options) {
//   if (ARTICLE_DETAIL.value.article_options_order.hasOwnProperty(key)) {
//     let value = ARTICLE_DETAIL.value.article_options_order[key];
//     console.log("key:", key);
//     console.log("value:", value);
//   }
//   console.log(item)
// }


  // headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  // headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
  // headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
  // headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });



// const headers = ref([])
//   headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
//   headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
//   headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
//   headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
//   headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
//   headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });



// if (SUBCONTENTS.value === "performer") {
//   headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
//   headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
//   headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
// }

// if (SUBCONTENTS.value === "video") {
  // headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  // headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
  // headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
  // headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
  // headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
  // headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });
// }

// if (SUBCONTENTS.value === "article") {
//   headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
//   headers.value.push({title: "大分類", align: 'start', key: 'classmajor', value: 'classmajor' });
//   headers.value.push({title: "中分類", align: 'start', key: 'classmedium', value: 'classmedium' });
//   headers.value.push({title: "小分類", align: 'start', key: 'classminor', value: 'classminor' });
  
// }















const article_detail_explain = computed(() => {return JSON.parse(ARTICLE_DETAIL.value.article_options_explain)})

// filter
// searchparamsのcomputedプロパティ
// const searchparams = computed(() => {
//   let result = {};
//   for (const [key, value] of Object.entries(JSON.parse(ARTICLE_DETAIL.value.article_options_explain))) {
//     result[key] = [];  // 初期値として空の配列をセット
//   }
//   return result;
// });

const searchparams_allitem = computed(() => {
  const result = {};
  const parsedOptions = JSON.parse(ARTICLE_DETAIL.value.article_options_explain);
    
  for (const [key, value] of Object.entries(parsedOptions)) {
      result[key] = [];
    for (const [key2, value2] of Object.entries(value)) {
      result[key].push(key2); // item.key の部分は適切なキー名に置き換える必要があります
    }
  }


  console.log(parsedOptions.key)
  return result;
});

// filteredDat
// const filteredData = computed(() => {
//   let temp = ARTICLE_DETAIL;

//   // searchparams.valueが定義されるまで待つ
//   for (const [key, values] of Object.entries(searchparams.value)) {
//     if (values.length > 0) {
//       temp = temp.value.article_childlen.filter(item => {
//         return values.includes(item.article_child_options[key]);
//       });
//     }
//   }

//   return temp;
// });


function updateSearchParams(searchparams, item, kind) {
  if (!searchparams[kind]) {
    searchparams[kind] = [];
  }
  searchparams[kind].push(item);
}

function resetSearchParams(searchparams, kind) {
  if (kind === 'all') {
    for (const key in searchparams) {
      if (searchparams.hasOwnProperty(key)) {
        searchparams[key] = []; // すべてのキーを空の配列にリセット
      }
    }
  } else {
    searchparams[kind] = []; // 指定されたキーを空の配列にリセット
  }
}





const scrollToItem = (index) => {
  const element = document.getElementById(`#item_${index}`);
  if (element) {
    const topPosition = element.getBoundingClientRect().top + window.scrollY - 100;
    window.scrollTo({
      top: topPosition,
      behavior: 'smooth'
    });
  }
};



</script>


<style scoped>
.aspect-ratio-block {
  background: #ccc;
  aspect-ratio: 3 / 2;
  /* aspect-ratio: 1; */
}

.my-fit-contents {
  width: fit-content;
  height: fit-content;
  }

  .text-h6 {
  font-size: 1.25rem !important;
  font-weight: 500;
  line-height: 2rem;
  letter-spacing: 0.0125em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

  .text-h7 {
  font-size: 1.125rem !important;
  font-weight: 500;
  line-height: 1.75rem;
  letter-spacing: 0.0107142857em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

.text-h8 {
  font-size: 1rem !important;
  font-weight: 500;
  line-height: 1.5rem;
  letter-spacing: 0.01em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}

.text-h9 {
  font-size: 0.875rem !important;
  font-weight: 400;
  line-height: 1.25rem;
  letter-spacing: 0.0085em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: none !important;
}


@media (min-width: 480px) {
  .d-xs-none {
    display: none !important;
  }
  .d-xs-block {
    display: block;
  }
}

@media (min-width: 479.98px) {
  .d-xs-block {
    display: block !important;
  }
}

.my-underline {
  text-decoration: underline;
}

.scrollable {
  overflow-x: auto;
  white-space: nowrap;
}


</style>
  

<style>




.v-data-table-footer {
  display: none;
}

</style>