<template>
  <v-navigation-drawer>
    <v-list>
      <router-link :to="{ name: 'Home' }">
        <v-img
          src="@/assets/logo_3.png"
          class="ma-auto my-5 mb-10"
          width="180"
        />
      </router-link>


      <v-divider></v-divider>
      <template
        v-for="(item, index) in items"
        :key="index"
      >
        <template v-if="item.subheader">
          <v-list-subheader>{{ item.subheader }}</v-list-subheader>
        </template>

        <template v-else>
          <v-list-item
            :to="item.to"
            :title="item.title"
            exact
            color="primary"
            variant="elevated"
            elevation="0"
            v-bind="item"
          />
        </template>
      </template>
    </v-list>

    <v-container>
    <v-btn @click="toggleTheme">Click me to change color</v-btn>
  </v-container>

  </v-navigation-drawer>
</template>

<script lang="ts" setup>

import { ref, computed } from 'vue'
import { useTheme } from 'vuetify'

// Vuetifyのテーマ管理を利用
const theme = useTheme()

const currentTheme = ref('light')


// const items = [
//   { subheader: 'PAGES' },
//   { title: 'Home', prependIcon: 'mdi-home-variant', to: '/' },
//   { title: 'Sink', prependIcon: 'mdi-faucet', to: '/sink' },
//   { subheader: 'EXAMPLES' },
//   { title: 'Headers', prependIcon: 'mdi-format-header-pound', to: 'headers' },
//   { title: 'Hero Headers', prependIcon: 'mdi-view-dashboard', to: 'heroheaders' },
//   { subheader: 'EXAMPLES' },

//   { title: 'Content', prependIcon: 'mdi-text-box', to: 'content' },
//   { title: 'Features', prependIcon: 'mdi-star-outline', to: 'features' },
//   { title: 'Call To Action', prependIcon: 'mdi-bullhorn-outline', to: 'calltoaction' },
//   { title: 'Gallery', prependIcon: 'mdi-image-multiple', to: 'gallery' },
//   { title: 'Blog', prependIcon: 'mdi-rss', to: 'blog' },
//   { title: 'Testimonial', prependIcon: 'mdi-message-text-outline', to: 'testimonial' },
//   { title: 'E-commerce', prependIcon: 'mdi-cart-outline', to: 'ecommerce' },
//   { title: 'Pricing Table', prependIcon: 'mdi-cash-multiple', to: 'pricing' },
//   { title: 'Team', prependIcon: 'mdi-account-group', to: 'team' },
//   { title: 'Contact', prependIcon: 'mdi-email-outline', to: 'contact' },
//   { title: 'Title', prependIcon: 'mdi-format-title', to: 'title' },
//   { title: 'Footer', prependIcon: 'mdi-page-layout-footer', to: 'footer' }
// ]


const items = [
  { subheader: 'HOME' },
  { title: 'ホーム', prependIcon: 'mdi-home-variant', to: '/' },
  { subheader: 'CONTENTS' },
  // { title: 'V\', prependIcon: 'mdi-home-variant', to: '/' },
  { title: '動画（FANZA 素人）', prependIcon: 'mdi-faucet', to: '/video' },
  { title: '記事  （ブログ） ', prependIcon: 'mdi-text-box', to: '/article' },
  { subheader: 'その他' },
  // { title: '動画（FANZA 素人）', prependIcon: 'mdi-faucet', to: '/video' },
  // { title: '記事  （ブログ） ', prependIcon: 'mdi-text-box', to: '/article' },

]

const toggleTheme = () => {
  currentTheme.value = currentTheme.value === 'light' ? 'dark' : 'light'
  theme.global.name.value = currentTheme.value
}




</script>
