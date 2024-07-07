<template>
  <v-container>
    <h1>Content</h1>

    <p>
      Content is the main part of a website. It usually contains the main message, call to action, and other important elements.
    </p>

    <br>

    <h2>Version 1</h2>

    <ContentVideoV1 />

    <br>

    <h2>Version 2</h2>

    <ContentV2 />

    <br>

    <h2>Version 3</h2>

    <ContentV3 />

    <br>

    <h2>Version 4</h2>

    <ContentV4 />
  </v-container>
</template>

<script lang="ts" setup>
import ContentVideoV1 from '@/components/content/Content-Video-v1.vue'
import ContentV2 from '@/components/content/Content-v2.vue'
import ContentV3 from '@/components/content/Content-v3.vue'
import ContentV4 from '@/components/content/Content-v4.vue'
</script>
