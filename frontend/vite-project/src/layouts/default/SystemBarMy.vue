<template>
  <v-system-bar
    color="#262626"
    height="56"
  >
    <div class="d-flex align-center">
      <!-- <v-img
        src="https://cdn.vuetifyjs.com/docs/images/logos/vuetify-logo-v3-slim-text-dark.svg"
        class="ms-2"
        width="128"
      /> -->
      <router-link :to="{ name: 'Home' }" class="ms-2">
        <v-img
          src="@/assets/logo_1.png"
          class="ms-2"
          width="110"
        />
      </router-link>


      <!-- <div class="text-body-2 font-weight-black ms-2 d-none d-md-block">
        THEMES
      </div> -->
      <v-img

        :to="{ name: 'Home' }"

      />
      <router-link :to="{ name: 'Home' }" class="ms-2">
        <v-img
          src="@/assets/logo_2.png"
          class="ms-2 d-none d-md-block"
          width="256"
        />
      </router-link>

    </div>

    <v-spacer />
    

        <!-- <v-toolbar-items v-if="mdAndUp">
            <v-btn text="Home" />

            <v-btn text="Portfolio" />

            <v-btn text="Contact" />
          </v-toolbar-items> -->

            <template v-if="mdAndUp">
              
              <v-divider vertical class=""></v-divider>

              <div style="display: flex; align-items: center;">
                <a href="https://twitter.com/adacolle_jp/" target="_blank">
                  <v-btn
                    class="ma-2"
                    color="white"
                    icon="mdi-twitter"
                    variant="text"
                  />
                </a>

                <v-divider vertical class=""></v-divider>

                <a href="https://www.instagram.com/adacolle_jp/" target="_blank">
                  <v-btn
                    class="ma-2"
                    color="white"
                    icon="mdi-instagram"
                    variant="text"
                  />
                </a>

                <v-divider vertical class=""></v-divider>

                <a href="https://www.dmm.co.jp/digital/" target="_blank" class="px-2">
                  <v-btn
                    append-icon="mdi-open-in-new"
                    class="ma-2"
                    color="white"
                    variant="text"
                  >
                  FANZA 公式
                  <!-- https://www.dmm.co.jp/digital/ -->
                  <template v-slot:prepend>
                    <!-- <v-icon color="success"></v-icon> -->
                  </template>
                  <!-- prepend -->
                </v-btn>
              </a>
            </div>

            <!-- <v-btn
              class="ms-6 me-2"
              color="primary"
              size="large"
              text="Signup"
              variant="elevated"
              width="128"
            /> -->

            </template>


    <!-- <v-btn
      append-icon="mdi-open-in-new"
      color="primary"
      href="https://store.vuetifyjs.com/products/nebula-ui-kit/"
      rel="noopener"
      target="_blank"
      text="Buy now"
      variant="flat"
    /> -->

    <v-app-bar-nav-icon
      v-if="!mdAndUp"
      class="d-inline-block"
      @click="emit('click:toggle')"
    />

  </v-system-bar>
</template>

<script setup>
const emit = defineEmits(['click:toggle'])

import { useDisplay } from 'vuetify'

const { mdAndUp } = useDisplay()


import MyLogo from '@/assets/mylogo.png'

</script>
