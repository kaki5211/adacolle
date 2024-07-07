<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" class="image-container">
        <v-img
          src='/src/assets/book-ic_picture.svg'
          contain
          class="blur-image"
        ></v-img>
        <div class="text-container">
          <span class="my-text-title my-text-size-50 my-text-color-black">BOOK</span>
          <br>
          <br>
          
          <span class="my-text-subtitle my-text-size-30 my-text-color-gray">～ブログ～</span>

        </div>
      </v-col>
    </v-row>
  </v-container>
</template>


<style scoped>
.image-container {
  position: relative;
}

.blur-image {
  filter: blur(2px);
}

.text-container {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 100%;
}

</style>