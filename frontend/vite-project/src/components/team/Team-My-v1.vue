<template>
  <v-card>
    <v-container>
      <v-row
        no-gutters
        class="h-100 pa-md-5"
      >
        <v-col
          cols="12"
          sm="12"
          md="6"
          class="d-flex flex-column justify-center align-center pa-2 "
        >
          <v-img
            class="rounded elevation-0"
            height=""
            width="100%"
            src="@/assets/heroheaders/1_planet.jpg"
          />
        </v-col>

        <v-col
          cols="12"
          sm="12"
          md="5"
          offset-md="1"
        >
          <v-card-text class="ml-md-5 d-flex flex-column justify-center h-100 px-3 mx-auto">
            <h3 class="text-lg-h3 text-h5 font-weight-bold mb-4">
              アダコレ
            </h3>
            <span class="text-grey-darken-1"><b>FANZA 素人AV / 18禁カテゴリー まとめブログ</b></span><br>



            <!-- <p class="text-grey-darken-1 mb-4"> -->
              <!-- FANZA 素人AV / 18禁カテゴリー まとめブログ -->
            <!-- </p> -->

            <div>
              <a href="https://twitter.com/adacolle_jp/" target="_blank">
                <v-btn
                  class="ma-2"
                  color="grey"
                  icon="mdi-twitter"
                />
              </a>

              <a href="https://www.instagram.com/adacolle_jp/" target="_blank">
                <v-btn
                  class="ma-2"
                  color="grey"
                  icon="mdi-instagram"
                />
              </a>
              <a href="https://www.dmm.co.jp/digital/" target="_blank">
                <v-btn
                  append-icon="mdi-open-in-new"
                  class="ma-2"
                  color="grey"
                  text="FANZA 公式"
                >
                <!-- https://www.dmm.co.jp/digital/ -->
                  <template v-slot:prepend>
                    <!-- <v-icon color="success"></v-icon> -->
                  </template>
                  <!-- prepend -->

                </v-btn>
              </a>


            </div>
          </v-card-text>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts" setup>
//

const items =  [
"このサイトは以下の企業とプロモーション提携を結んでいます。", 
"・アマゾン　・楽天　・グーグル"
      ]
</script>
