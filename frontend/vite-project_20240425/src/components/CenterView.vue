


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
  <v-row no-gutters>
      <v-col cols="6" rounded="0">
        <v-btn
          rounded="0"
          class="w-100 my-text-size-30 my-fit-contents my-bg-color"
          elevation="0"
          :to="{ name: 'Videos'}"
        >
          aiueo
        </v-btn>
    </v-col>

    <v-col cols="6" rounded="0">
        <v-btn
          rounded="0"
          class="w-100 my-text-size-30 my-fit-contents my-bg-color"
          elevation="0"
          :to="{ name: 'Articles'}"
        >
          aiueo
        </v-btn>
    </v-col>
  </v-row>



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
