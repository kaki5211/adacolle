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
    

        <v-toolbar-items v-if="mdAndUp">
            <v-btn text="Home" />

            <v-btn text="Portfolio" />

            <v-btn text="Contact" />
          </v-toolbar-items>

          <template #append>
            <template v-if="mdAndUp">
              <v-icon
                icon="mdi-twitter"
                color="disabled"
                class="me-2"
              />

              <v-icon
                icon="mdi-facebook"
                color="disabled"
                class="me-2"
              />

              <v-icon
                icon="mdi-linkedin"
                color="disabled"
                class="me-2"
              />

            <!-- <v-btn
              class="ms-6 me-2"
              color="primary"
              size="large"
              text="Signup"
              variant="elevated"
              width="128"
            /> -->

            <v-app-bar-nav-icon
              class="d-inline-block"
              @click="emit('click:toggle')"
            />
            </template>

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
