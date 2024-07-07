

<style scoped>
div {
  font-family: 'Sawarabi Gothic', sans-serif;
}
</style>



<script setup>
import { useMeta } from 'vue-meta';


const { metaInfo } = useMeta({
  title: "",
  meta: [
    { charset: 'utf-8' },
    { name: 'theme-color', content: '#455045' },
    { name: 'langueage', content: '日本語' },
    { name: 'author', content: 'BOOK I.C.'},
    { name: 'robots', content: 'text/html', charset: 'UTF-8'},
    //{ name: 'robots', content: 'index' },
    { "http-equiv": 'Content-Language', content: 'ja' },
    { "http-equiv": 'Expires', content: '86400' },
    { "http-equiv": 'Content-Type', content: 'text/html', charset: 'UTF-8'},



    //■基本設定
    //{ name: 'description', content: '「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすための本感想ブログです！。今後、本に関する様々な情報を掲載予定です！'},
    { name: 'keywords', content: 'book-ic,本,本感想,本の感想,感想,書評,書店,小説,文庫,ブログ,個人ブログ,読書,書籍,記録,ネタバレ読書,読書記録' },
    { name: 'thumbnail', content: '/src/assets/book-ic_picture.svg' },


    // og 設定
    // １．page type
    //{ property: 'og:type', content: 'website' }, //content: article 
    // ２．title
    //{ property: 'og:title', content: 'BOOK I.C. ～本の感想を創造するブログ～' }, 
    // ３．ページ説明文
    //{ property: 'og:description', content: ' 「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすための本感想ブログです！。タグ | 小説,文庫,ブログ,本の感想,本感想,読書,書評,書籍,記録,ネタバレ | BOOK I.C.' }, 
    // ４．URL
    //{ property: 'og:url', content: 'absolute_url' }, 
    // ５．サイト名
    { property: 'og:site_name', content: 'BOOK I.C.' }, 
    // ６．その他
    //{ property: 'article:publisher', content: '(6)FacebookページのURL' }, 
    // ７．表示画像
    { property: 'og:image', content: '/src/assets/book-ic.png' }, 

    // Twitterカードの設定 
    //{ name: 'twitter:title', content: 'summary' }, 
    { name: 'twitter:card', content: 'summary' }, 
    { name: 'twitter:site', content: '@BOOK_IC' },

  ],

  link: [
    { rel: 'icon', href: '/src/assets/book-ic_icon.svg', type: 'image/x-icon' },
    // { rel: 'stylesheet', href: 'styles.css' },
    { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Sawarabi+Gothic&display=swap',},
    //{ rel: 'canonical', href: 'url',}, 正規化
    //{ rel: 'prev', href: '前のページのURL',}, 
    //{ rel: 'next', href: '次のページのURL',},

  ],

  /*
  script: [
    // Google ADSense
    { async: true, src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1203419703310974", crossorigin: "anonymous"},
    // Google tag (gtag.js)
    { async: true, src: "https://www.googletagmanager.com/gtag/js?id=G-BS7M4Z8XRZ", crossorigin: "anonymous"},
    {
      innerHTML: `
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-BS7M4Z8XRZ');
        gtag('config', 'UA-244839165-1');
      `,
      type: "text/javascript",
    },
    {
      innerHTML: `
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-KKTTVX3');
      `,
      type: "text/javascript",
    },
    { async: true, type: "application/javascript", src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1203419703310974", crossorigin: "anonymous"},

  ],
*/
  
})




// const title = computed(() => myData.value.book_list[0]?.title || '')
// const icon = "/src/assets/book-ic_icon.svg";
// const count = ref(0);
// const increaseCount = () => {
//   count.value++;
// };
</script>








<template>
<!-- <!DOCTYPE html> -->
  <metainfo>
    <!-- <template v-slot:title="{ content }">{{ content ? `${content} | SITE_NAME` : `SITE_NAME` }}</template> -->
    <template v-slot:title="{ content }">{{ content ? `${content} | SITE_NAME` : `SITE_NAME` }}</template>
  </metainfo>
</template>








