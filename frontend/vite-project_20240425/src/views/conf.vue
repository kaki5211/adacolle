



<v-row v-if="ARTICLE_CLASS.value[1] === 'video'" no-gutters>

  <v-col  cols="11" class="mx-auto px-6 py-15 pb-5">

  <v-carousel
    class="my-carousel"
    v-if="media[1]==false"
    :show-arrows="false"
    :cycle="false"
    v-model="model[1]"
    @touchstart="handleTouchStart($event, 1, model[1])"
  >
    <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->

  <v-carousel-item
    v-for="(item,ii) in parseJson(item.images)"
    :key="ii"
    cover
    aspect-ratio="1.46" :src="item" alt="Image" @click="model[(i)+iii*4] = (model[(i)+iii*4] + 1 ) % parseJson(VIDEO.images).length"
  >
  
<!-- <v-row v-if="ii==0" no-gutters>
  <v-col cols="12" class="d-flex"
  v-for="(item,i) in VIDEO.performers"
      :key="i"
  >
    <v-btn 
      rounded="0"
      class="my-fit-contents my-text-size-30  ms-auto me-0"
      :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
      >
      {{item.name}}
    </v-btn>
  </v-col>
</v-row> -->
<!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

</v-carousel-item>
</v-carousel>
<v-row no-gutters v-if="media[(i)+iii*4]==true">
<v-col cols="12" aspect-ratio="1.46" class="mx-auto px-0 my-auto">

    <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
      <source src="https://liginc.co.jp/wp-content/uploads/2020/05/D0002060347_00000_V_000.mp4?_=1" type="video/mp4">
      Your browser does not support the video tag.
    </video>
</v-col>


    
    <v-col cols="12" class="d-flex pb-0 w-100">
      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia((i)+iii*4)">
        閉じる
      </v-btn> 
    </v-col>

</v-row>


<!--
<div v-if="media[i]==true" class="video-container">
<video ref="videoRef" class="video-player" controls playsinline autoplay muted>
  <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<v-toolbar class="control-bar" absolute bottom>
  コントロールバーのコンポーネントをここに追加
  <v-btn icon>
    <v-icon>mdi-play-pause</v-icon>
  </v-btn>
  <v-slider thumb-label="always"></v-slider>
  追加のコントロールボタンやスライダーなどを配置
</v-toolbar>
</div>
-->


<!-- <div v-if="media[i]==true" aspect-ratio="0.73" class="mx-auto px-0 my-auto d-flex">
<div class="video-wrapper">
<video ref="videoPlayer" :class="['video-player', { 'small': isSmall }]" playsinline autoplay muted>
  <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<div class="custom-controls">
  <div class="progress-bar" @mousedown="startDrag">
    <div class="progress" :style="{ width: progressWidth }"></div>
  </div>
</div>
</div>
</div> -->


<!-- videoSrc -->


<v-row no-gutters v-if="media[(i)+iii*4]==false">
<v-col class="d-flex pb-0 w-100">
  <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia((i)+iii*4)">
    再生
  </v-btn> 
</v-col>
</v-row>

<!-- <v-row no-gutters>
<v-col class="d-flex mt-1 w-100">
  <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-open-in-new">
    続きを見る
  </v-btn> 
</v-col>
</v-row> -->

<a :to="{ name: 'Video', param: VIDEO.productnumber}" class="custom-link my-text-size-50 font-weight-medium pt-2">{{ VIDEO.title }}</a>


<v-row no-gutters>
<v-col class="d-flex">
  <v-btn 
    v-for="(item,i) in VIDEO.performers"
    :key="i"
    class="my-fit-contents my-text-size-30 py-1 my-1"
    :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
    >
    {{item.name}}
  </v-btn>
</v-col>
</v-row>

<v-row no-gutters>
<v-col class="d-flex">
  <v-btn 
    v-for="(item,i) in VIDEO.tags"
    :key="i"
    class="my-fit-contents my-text-size-30 py-1 my-1"
    :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
    >
    {{item.name}}
  </v-btn>
</v-col>
</v-row>









<!-- <v-card-title class="py-5 text-h3 font-weight-bold my-text-color-black my-letter-spacing-initial" tag="h3">
コンビニ人間            
</v-card-title> -->






<v-row v-if="true" no-gutters>
<v-col cols="8" class="mx-auto mt-15 mb-10">
<List_1 />
</v-col>
</v-row>




<Text_2 text_2="あらすじ" />


<v-card-text class="psy-3 my-text-color">
<a class="text-h5 font-weight-medium my-text-contents">
{{contents_synopsis}}
</a>
</v-card-text>

<v-row no-gutters>
<v-col class="d-flex">
<v-btn 
v-for="(item,i) in VIDEO.performers"
:key="i"
class="my-fit-contents py-1 my-1 mx-auto"
>
<v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
<span class="my-text-size-50">外部サイト</span> <!-- テキストのサイズを設定 -->                </v-btn>
</v-col>
</v-row>

</v-col>
</v-row>



</v-row>
</v-card>







</v-col>
</v-row>





