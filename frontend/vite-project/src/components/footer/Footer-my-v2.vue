<template>
  <v-card>
    <v-container class="text-center py-12">
      <div class="d-inline-block">
        <v-img
        src="@/assets/logo_3.png"
        class="ma-auto"
        width="300"
      />
      </div>

      <div class="my-3">
        <v-btn
          v-for="(item, index) in links"
          :key="index"
          :text="item.name"
          variant="text"
          class="mx-2 text-grey-darken-1"
          rounded
          :to="{ name: item.to }"
        />
      </div>

      <div
        class="text-center mt-10 text-grey-darken-1"
        cols="12"
      >
        All rights are reserved &copy;
        {{ new Date().getFullYear() }}, Vuetify, LLC
      </div>
    </v-container>
  </v-card>
</template>

<script lang="ts" setup>


interface Link {
  name: string;
  to: string;
}

const links: Link[] = [
  { name: "ホーム", to: "Home" },
  { name: "動画", to: "Video" },
  { name: "記事", to: "Article" },
];


</script>
