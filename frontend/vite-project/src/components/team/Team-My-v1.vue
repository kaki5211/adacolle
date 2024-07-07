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
          md="5"
          class="d-flex flex-column justify-center align-center pa-5"
        >
          <v-img
            class="rounded elevation-5"
            height="300"
            width="100%"
            gradient="#262626, #262626"
          />
        </v-col>

        <v-col
          cols="12"
          sm="12"
          md="6"
          offset-md="1"
        >
          <v-card-text class="d-flex flex-column justify-center h-100">
            <h3 class="text-lg-h3 text-h5 font-weight-bold mb-4">
            アダルトコレクション
            </h3>

            <span class="text-grey-darken-1"><b>FANZA 素人AV / 18禁カテゴリー まとめブログ</b></span><br>

            <!-- <p class="text-grey-darken-1 mb-4"> -->
              <!-- FANZA 素人AV / 18禁カテゴリー まとめブログ -->
            <!-- </p> -->

            <div>
              <!-- <v-btn
                class="ma-2"
                color="primary"
                icon="mdi-pound"
              /> -->
              <v-btn
                class="ma-2"
                color="grey"
                icon="mdi-twitter"
              />
              <v-btn
                class="ma-2"
                color="grey"
                icon="mdi-instagram"
              />
              <!-- <v-btn
                class="ma-2"
                color="grey"
                icon="mdi-open-in-new"
                text="もっと見る..."
              /> -->
              <v-btn
                append-icon="mdi-open-in-new"
                class="ma-2"
                color="grey"
                text="FANZA 公式"
              >
                <template v-slot:prepend>
                  <!-- <v-icon color="success"></v-icon> -->
                </template>
                <!-- prepend -->

              </v-btn>


            </div>
          </v-card-text>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts" setup>
//
</script>
