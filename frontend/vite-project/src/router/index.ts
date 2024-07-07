/**
 * router/index.ts
 *
 * This file is used to register all routes
 * Documentation: https://router.vuejs.org/
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router'

// store
import store from '../store';

// vue
import { computed, ref, watch } from 'vue';



const video_productnumbers = computed(() => { return store.getters.GET_VIDEOS.map(item => item.video_productnumber) });

// const isValidProductNumber = VIDEOS.some(item => item.video_productnumber === video_productnumber);


// // ポーリング関数を定義
// const pollForVideos = async (interval = 100, maxRetries = 5000) => {
//   let VIDEOS = null;
//   let retries = 0;
//   while (retries < maxRetries) {
//     VIDEOS = store.getters.GET_VIDEOS;
//     console.log("VIDEOSVIDEOSVIDEOS1111", VIDEOS)
//     if (VIDEOS!=undefined) {
//       console.log("VIDEOSVIDEOSVIDEOS22222222", VIDEOS)

//       return VIDEOS;
//     }
//     await new Promise(resolve => setTimeout(resolve, interval));
//     retries++;
//   }
//   throw new Error('Videos not available');
// };

// console.log("■■checkpoint1")

// let VIDEOS = null;
// // VIDEOSが取得されるまで待つ
// if VIDEOS!=null {
//   VIDEOS = computed(() => { return pollForVideos() });
// }



// sleep
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function wait100ms() {
  console.log("Waiting for 100ms...");
  await sleep(1000);
}








// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ title ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
/* title 例
const site_title = "BOOK I.C. ～本の感想を創造するブログ～";
const site_title1 = "{{breadcrumb.1.title_info}} | BOOK I.C.";
const site_title2 = "【本感想 ブログ】 {{breadcrumb.2.title_info}} | BOOK I.C.";
*/



// ■■■■　webデザイン関係
// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ icon ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <link rel="icon" class="my-icon" href="{% static "static/book-ic_icon.svg" %}" type="image/svg+xml">


// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ テーマカラー　必要？ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <meta name="theme-color" content="#455045">


// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ フォント ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
  // <!-- Noto Sans JP -->
      // <link rel="preconnect" href="https://fonts.googleapis.com">
     // <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
     // <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700&display=swap" rel="stylesheet">

    // <!-- sawarabi gothic -->
    // <link rel="preconnect" href="https://fonts.googleapis.com">
    // <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    // <link href="https://fonts.googleapis.com/css2?family=Sawarabi+Gothic&display=swap" rel="stylesheet">





// ■■■■検索エンジン関係
// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 検索エンジン、キーワード ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
    // <meta name="keywords" content="book-ic,本,本感想,本の感想,感想,書評,書店,小説,文庫,ブログ,個人ブログ,読書,書籍,記録,ネタバレ読書,読書記録">


// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ SEO サムネイル画像 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <meta name="thumbnail" content="{% static "static/book-ic_picture.svg" %}" />


// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 正規化 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <link rel="canonical" href={{ request.build_absolute_uri }} />





// ■■■■外部アプリ関係
// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ meta twitter ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <!-- 1 -->
    // <meta property="og:description" content=" 「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすためにつくりました！。タグ | 小説,文庫,ブログ,本の感想,本感想,読書,書評,書籍,記録,ネタバレ | BOOK I.C."/>
    // <meta property="og:description" content="{{breadcrumb.2.title_info}} | — あらすじ — {{ book_info.contents_synopsis| truncatechars:80 }}"/>
    // <meta property="og:description" content="{{breadcrumb.2.title_info}} | BOOK I.C. ～本の感想を創造するブログ～,{{ other_info.contents_synopsis| truncatechars:80 }}"/>

// <!-- 2 -->
  // <meta charset="utf-8">
  // <meta http-equiv="content-language" content="ja">

// <!-- 3 -->
// {% with breadcrumb|length as el_ %}
// {% if el_ == 1 %}<meta name="robots" content="index">
//     {% elif el_ == 3 %}
//         {% if breadcrumb.1.title_info == "書籍一覧" %}<meta name="robots" content="index">
//         {% elif breadcrumb.1.title_info == "その他 記事" %}<meta name="robots" content="noindex,nofollow">
//         {% endif %}
//     {% endif %}
// {% endwith %}




// <!--　■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　 og 設定 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■　-->
// <!-- １．page type -->
  // <meta property="og:type" content="website" />
  // <meta property="og:type" content="article"/>

  // <!-- ２．title -->
    // <meta property="og:title" content="BOOK I.C. ～本の感想を創造するブログ～"/>
    // <meta property="og:title" content="{{breadcrumb.1.title_info}} | BOOK I.C."/>
    // <meta property="og:title" content="【本感想 ブログ】 {{breadcrumb.2.title_info}} | BOOK I.C."/>

    // <!-- ３．ページ説明文 -->
    // <meta property="og:description" content=" 「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすためにつくりました！。タグ | 小説,文庫,ブログ,本の感想,本感想,読書,書評,書籍,記録,ネタバレ | BOOK I.C."/>
    // <meta property="og:description" content="{{breadcrumb.2.title_info}} | — あらすじ — {{ book_info.contents_synopsis| truncatechars:70 }}"/>
    // <meta property="og:description" content="{{breadcrumb.2.title_info}} | BOOK I.C. ～本の感想を創造するブログ～,{{ other_info.contents_synopsis| truncatechars:70 }}"/>

// <!-- ４．URL -->
  // <meta property="og:url" content="{{ request.build_absolute_uri }}" />
  
// <!-- ５．サイト名 -->
  // <meta property="og:site_name" content="BOOK I.C." />
  
// <!-- ６．その他 -->
  // <meta property="article:publisher" content="(6)FacebookページのURL" />
  
// <!-- ７．表示画像 -->
  // <meta property="og:image" content="{% static "static/book-ic.png" %}" />

// <!-- Twitterカードの設定 -->
  // <meta name="twitter:card" content="summary" />
  // <meta name="twitter:site" content="@BOOK_IC" />






const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: {



        },

      },
      {
        path: 'video',
        name: 'Video',
        component: () => import('@/views/video/index.vue')
      },
      {
        path: 'video/:video_productnumber',
        name: 'Video_Detail',
        component: () => import('@/views/video_detail/index.vue'),
        beforeEnter: async (to, from, next, commit, state) => {

          // storeからvideosを取得
          const videos = computed(() => store.getters.GET_VIDEOS);

          // videos が取得されるまで待機
          let videoProductNumbers_count = 1;
          while (!videos.value) {
            videoProductNumbers_count += 1;
            await sleep(500);
            if (videoProductNumbers_count > 1000 || videos.value) {
              console.log("success!", videos.value)
              break;
            }
          }
          
          const productNumber = to.params.video_productnumber;
          const videoProductNumbers = videos.value.map(item => item.video_productnumber)

          const VIDEO_DETAIL = videos.value.filter(video => video.video_productnumber === productNumber);

          // 取得したvideo product numbersにproductNumberが含まれているか確認
          if (videoProductNumbers.includes(productNumber)) {
            store.commit('SET_VIDEO_DETAIL', VIDEO_DETAIL);
            next();
          } else {  
            next();
          }
        }
      },


      {
        path: 'article',
        name: 'Article',
        component: () => import('@/views/article/index.vue')
      },
      {
        path: 'article/:article_title_eng',
        name: 'Article_Detail',
        component: () => import('@/views/article_detail/index.vue'),
        beforeEnter: async (to, from, next) => {

          // storeからvideosを取得
          const articles = computed(() => store.getters.GET_ARTICLE_LIST);

          // articles が取得されるまで待機
          let videoProductNumbers_count = 1;
          while (!articles.value) {
            videoProductNumbers_count += 1;
            await sleep(500);
            if (videoProductNumbers_count > 1000 || articles.value) {
              console.log("success!", articles.value)
              break;
            }
          }
          
          // videos が取得されるまで待機
          const productNumber = to.params.article_title_eng;
          console.log("productNumber", productNumber)
          const videoProductNumbers = articles.value.map(item => item.article_title_eng)

          // videos が取得されるまで待機
          if (videoProductNumbers.includes(productNumber)) {
            next()
          } else {
            next()
          }
        }
      },


      /*

      プライバシーポリシー
      自己紹介
      インスタ、X、ブロック
      リスト


      */











      {
        path: '/sink',
        name: 'Sink',
        component: () => import('@/views/Sink.vue')
      },
      {
        path: 'headers',
        name: 'Headers',
        component: () => import('@/views/headers/index.vue')
      },
      {
        path: 'heroheaders',
        name: 'Heroheaders',
        component: () => import('@/views/hero-headers/index.vue')
      },
      {
        path: 'content',
        name: 'Content',
        component: () => import('@/views/content/index.vue')
      },
      {
        path: 'features',
        name: 'Features',
        component: () => import('@/views/features/index.vue')
      },
      {
        path: 'calltoaction',
        name: 'Call to Action',
        component: () => import('@/views/call-to-action/index.vue')
      },
      {
        path: 'gallery',
        name: 'Gallery',
        component: () => import('@/views/gallery/index.vue')
      },
      {
        path: 'blog',
        name: 'Blog',
        component: () => import('@/views/blog/index.vue')
      },
      {
        path: 'testimonial',
        name: 'Testimonial',
        component: () => import('@/views/testimonial/index.vue')
      },
      {
        path: 'ecommerce',
        name: 'Ecommerce',
        component: () => import('@/views/ecommerce/index.vue')
      },
      {
        path: 'pricing',
        name: 'Pricing',
        component: () => import('@/views/pricing/index.vue')
      },
      {
        path: 'team',
        name: 'Team',
        component: () => import('@/views/team/index.vue')
      },
      {
        path: 'contact',
        name: 'Contact',
        component: () => import('@/views/contact/index.vue')
      },
      {
        path: 'title',
        name: 'Title',
        component: () => import('@/views/title/index.vue')
      },
      {
        path: 'footer',
        name: 'Footer',
        component: () => import('@/views/footer/index.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,

  // 追加↓　2024/0517
  scrollBehavior(to, from, savedPosition) {
    // if (to.path === from.path) {
    //   const hash = to.hash;
    //   if (hash) {
    //     return new Promise((resolve) => {
    //       const targetElement = document.querySelector(hash);
    //       if (targetElement) {
    //         const topOffset = targetElement.offsetTop;
    //         window.scrollTo({
    //           top: topOffset,
    //           behavior: 'smooth'
    //         });

    //         // setTimeoutを使用して一定時間後にPromiseを解決
    //         setTimeout(() => {
    //           resolve();
    //         }, 500); // 500ミリ秒後に解決する例
    //       }
    //     });
    //   }
    // }

    // if (savedPosition) {
    //   return savedPosition;
    // }


      // if (to.hash) {
      //   return {
      //     el: to.hash - 100,
      //     behavior: 'smooth',
      //   }
      // } 
      
      if (to.hash) {
      return new Promise((resolve) => {
        const targetElement = document.querySelector(to.hash);
        console.log("targetElement", targetElement)
        if (targetElement) {
          const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY;
          console.log("targetPosition", targetPosition)

          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
          // スクロールが完了したら解決する
          window.addEventListener('scroll', function handler() {
            window.removeEventListener('scroll', handler, true);
            resolve();
          }, true);
        }
      });
    } else {
      return new Promise((resolve) => {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
        // スクロールが完了したら解決する
        window.addEventListener('scroll', function handler() {
          window.removeEventListener('scroll', handler, true);
          resolve();
        }, true);
        setTimeout(() => {
          resolve({ left: 0, top: 0 })
        }, 500)
      });

    }




  },

  // ルートのトレーリングスラッシュを削除
  strict: true,
  // 末尾のスラッシュを削除するためのリダイレクトを有効化
  // trailingSlash: true


})










router.beforeEach((to, from, next) => {
  // すべてのルートに対して実行したいコードをここに記述
  // 例えば、変更後のパスを取得することができます

  // BREADCRUMBS
  const toPath = to.path;
  const toParams = to.params;
  store.dispatch('FETCH_GET_BREADCRUMBS', toPath)




  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  const site_name = "サイト名";
  const site_name_sub = "- サイト簡単に説明文 -";

  const site_title = "ホーム";

  
  const site_title1 = "page_title | site_name";
  const site_title2 = "page_title | site_name";


  const defaultMeta = {






    title: site_name + site_name_sub ,
    metaTags: [
  //固定
      { charset: 'utf-8' },
      // { http-equiv: 'content-language', content: 'ja' },
      { name: 'theme-color', content: '#455045' },  //  テーマカラー

  //og 固定
      { property: 'og:site_name', content: site_name },  //  og info
      { name: 'twitter:card', content: 'summary' },  //  ツイッターinfo
      { name: 'twitter:site', content: '@' + site_name },  //  ツイッターinfo


  //検索エンジン 固定
      { name: 'keywords', content: 'ビデオ, 詳細, Vue' },  //  検索キーワード


  //検索エンジン
      { name: 'thumbnail', content: 'https://example.com/thumbnail.png' },  //  サムネイル
      { name: 'description', content: 'ページの説明文| truncatechars:70' },  //  検索エンジン説明文


  //// og 動的
      { property: 'og:title', content: site_name },  //  ツイッターinfo
      { property: 'og:description', content: '　ページ説明文　| truncatechars:70' },  //  og 検索エンジン説明文
      { property: 'og:url', content: '{{ request.build_absolute_uri }}"' },  //  わかんない
      { property: 'og:image', content: '{% static "static/book-ic.png" %}' },  //  og image

  //その他
      { name: 'robots', content: 'index' },  //  検索エンジンにクロールさせる
      { name: 'robots', content: 'noindex,nofollow' },  //  検索エンジンにクロールさせ無い
      { property: 'article:publisher', content: '(6)FacebookページのURL' },  //  facebook 不要？

    ],

    link: [
      // { rel: 'icon', class, 'my-icon, 'href: 'static/book-ic_icon.svg', type: 'image/svg+xml'},  //icon
      { rel: 'preconnect', href: 'https://fonts.googleapis.com' },  //  フォント必要
      // { rel: 'preconnect', href: 'https://fonts.gstatic.com' crossorigin},  //  フォント不要？
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700&display=swap' },  //  Noto+Sans+JP
      //{ rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Sawarabi+Gothic&display=swap' },  //  Sawarabi+Gothic
      
      { rel: 'canonical', href: 'request.build_absolute_uri' },  //  正規化 url 不要？

    ],


    script: [
      { src: 'https://example.com/default.js' },
      // 他のデフォルトスクリプト
    ]

    
          // store: myStore,
          // requiresAuth: true,
          // breadcrumb: 'ホーム > ビデオ > 詳細',
          // layout: 'main-layout'          

  };


  const meta = nearestWithMeta ? {
    title: nearestWithMeta.meta.title || defaultMeta.title,
    metaTags: (nearestWithMeta.meta.metaTags || []).concat(defaultMeta.metaTags),
    link: (nearestWithMeta.meta.link || []).concat(defaultMeta.link),
    script: (nearestWithMeta.meta.script || []).concat(defaultMeta.script),
  } : defaultMeta;

  document.title = meta.title;

  // 古いメタタグを削除
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // 新しいメタタグを追加
  meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  }).forEach(tag => document.head.appendChild(tag));

  // 新しいリンクタグを追加
  meta.link.map(linkDef => {
    const link = document.createElement('link');

    Object.keys(linkDef).forEach(key => {
      link.setAttribute(key, linkDef[key]);
    });

    link.setAttribute('data-vue-router-controlled', '');

    return link;
  }).forEach(link => document.head.appendChild(link));

  // 新しいスクリプトタグを追加
  meta.script.map(scriptDef => {
    const script = document.createElement('script');

    Object.keys(scriptDef).forEach(key => {
      script.setAttribute(key, scriptDef[key]);
    });

    script.setAttribute('data-vue-router-controlled', '');

    return script;
  }).forEach(script => document.head.appendChild(script));





  // デバッグ用のディスパッチ
  store.dispatch('FETCH_GET_DEBUG');

  next();
});




  











  






  














export default router
