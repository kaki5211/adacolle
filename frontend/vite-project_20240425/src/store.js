import { createStore } from 'vuex';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute();

// import createPersistedState from 'vuex-persistedstate'





// URL選択
// const host = "http://127.0.0.1:8000"
// const host_api = "http://127.0.0.1:8000/api"
// const host = "http://172.20.10.5:8000"
// const host_api = "https://localhost:8000/api"
// const host_api = "https://153.122.199.147]:8000/api"
// const host_api = "https://153.122.199.147:8080/api"



  // const host_api = "https://kyounuki.jp:8080/api"
  const host_api = "http://192.168.179.22:8000/api"
// const host_api = "http://172.20.10.4:8000/api"
// const host_api = "http://192.168.179.22:8000/api"



// http://localhost:8000/api/your-endpoint/






// fetchDataAndCommit
async function fetchDataAndCommit({ commit, endpoint, mutationType }) {
  const response = await axios.get(`${host_api}/${endpoint}/`);
  commit(mutationType, response.data);
}

// time.sleep
async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// 配列の要素数の合計を出力する関数
function countTotalElements(searchparams) {
  let total = 0;
  // searchparams オブジェクト内の各プロパティにアクセス
  for (const key in searchparams) {
    if (Array.isArray(searchparams[key])) {
      // プロパティが配列である場合、その配列の要素数を加算
      total += searchparams[key].length;
    }
  }
  return total;
}











const store = createStore({
  // plugins: [createPersistedState()],
  state: {
    videos: null,
    video_detail: null,
    performer_list: null,
    tag_list: null,
    maker_list: null,
    label_list: null,
    series_list: null,
    kyounuki_list: null,
    contents_list: null,
    article_detail: null,
    article_list: null,
    article_list_dup: null,
    article_list_params: {
      classmajor: [],
      classmedium: [],
      classminor: [],
    },



    searchparams: {
      performers: [],
      tags: [],
      maker: [],
      label: [],
      series: [],
      duration: [],
      title: [],
      description: [],
      views: [],
      kyounuki_post_day: [],
      active: [],
    },
    searchparams_article: {
      classmajor: [],
      classmedium: [],
      classminor: [],
    },
    set_videos_loaded: null,

    url_list: null,
    url_param: null,
    url_judge_param: null,
    subcontents: null,
    subcontents_all: null,

    topix_list: null,

    debug: null,
    breadcrumbs: null,

    // Contents_list: [], 
    Url_list_loaded: null, // urllist取得完了フラグ
    // Contents_loaded: null, // コンテンツデータ取得完了フラグ
  },
  mutations: {
    SET_VIDEOS(state, data) { state.videos = data; },
    SET_VIDEO_DETAIL(state, data) { state.video_detail = data; },
    SET_PERFORMER_LIST(state, data) { state.performer_list = data; },
    SET_TAG_LIST(state, data) { state.tag_list = data; },

    SET_ARTICLE_DETAIL(state, data) { state.article_detail = data; },
    SET_ARTICLE_LIST(state, data) { state.article_list = data; },
    SET_ARTICLE_LIST_DUP(state, data) { state.article_list_dup = data; },
    SET_ARTICLE_LIST_PARAMS(state, data) { state.article_list_params = data; },


    SET_MAKER_LIST(state, data) { state.maker_list = data; },
    SET_LABEL_LIST(state, data) { state.label_list = data; },
    SET_SERIES_LIST(state, data) { state.series_list = data; },
    SET_KYOUNUKI_LIST(state, data) { state.kyounuki_list = data; },

    SET_VODEOS_LOADED(state, data) { state.set_videos_loaded = data; },

    SET_URL_LIST(state, data) { state.url_list = data; },

    SET_URL_PARAM(state, data) { state.url_param = data; },
    SET_URL_JUDGE_PARAM(state, data) { state.url_judge_param = data; },
    SET_SUBCONTENTS(state, data) { state.subcontents = data; },
    SET_SUBCONTENTS_ALL(state, data) { state.subcontents_all = data; },

    SET_DEBUG(state, data) { state.debug = data; },
    SET_BREADCRUMBS(state, data) { state.breadcrumbs = data; },

    SET_CONTENTS_LIST(state, data) { state.contents_list = data; },

    SET_TOPIX_LIST(state, data) { state.topix_list = data; },


    SET_SEARCHPARAMS(state, data) { state.searchparams = data; },
    SET_SEARCHPARAMS_ARTICLE(state, data) { state.searchparams_article = data; },
    
    // SET_CONTENTS(state, data) { state.Contents_list = [data]; },
    // ADD_CONTENTS(state, data) { state.Contents_list.push(data); },
    // ADD_CONTENTS(state, data) { Vue.set(state.Contents_list, state.Contents_list.length, data); },

  
    
    // SET_URL_LOADED(state, data) { state.Url_list_loaded = data; },
    // SET_CONTENTS_LOADED(state, data) { state.Contents_loaded = data; },
  },

  actions: {
    async FETCH_GET_VIDEOS({ commit }) {
      commit('SET_VODEOS_LOADED', false); // データの取得状態を初期化
      fetchDataAndCommit({ commit, endpoint: 'videos_view', mutationType: 'SET_VIDEOS' });
      commit('SET_VODEOS_LOADED', true); // データの取得状態を更新
      console.log('SET_URL_LOADED: Completed')
      
    },
    async FETCH_GET_PERFORMER_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'performer_list_view', mutationType: 'SET_PERFORMER_LIST' });
    },
    async FETCH_GET_TAG_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'tag_list_view', mutationType: 'SET_TAG_LIST' });
    },
    async FETCH_GET_KYOUNUKI_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'kyounuki_list_view', mutationType: 'SET_KYOUNUKI_LIST' });
    },
    async FETCH_GET_URL_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'url_list_view', mutationType: 'SET_URL_LIST' });
    },
    // async FETCH_GET_MAKER_LIST({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'maker_list_view', mutationType: 'SET_MAKER_LIST' });
    // },
    async FETCH_GET_LABEL_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'label_list_view', mutationType: 'SET_LABEL_LIST' });
    },
    // async FETCH_GET_SERIES_LIST({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'series_list_view', mutationType: 'SET_SERIES_LIST' });
    // },
    async FETCH_GET_ARTICLE_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'article_list_view', mutationType: 'SET_ARTICLE_LIST' });
    },
    // async FETCH_GET_ARTICLE_LIST_DUP({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'article_list_dup_view', mutationType: 'SET_ARTICLE_LIST_DUP' });
    // },
    // async FETCH_GET_ARTICLE_LIST_PARAMS({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'article_list_params_view', mutationType: 'SET_ARTICLE_LIST_PARAMS' });
    // },
    // async FETCH_GET_TOPIX_LIST({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'topix_list_view', mutationType: 'SET_TOPIX_LIST' });
    // },


    async FETCH_GET_DEBUG({ commit }) {
        
      // console.log("urlhost.includes('172.')", urlhost.includes("172."))
      let judge;
      if (this.state.debug == true ) { 
        judge = false
      } else{
        judge=true
      };

      // commit('SET_DEBUG', urlhost.includes("kyounuki"));
      console.log(judge)
      commit('SET_DEBUG', judge);
    },
    async FETCH_GET_BREADCRUMBS({ commit }, newpath) {
      // const { path_ } = payload; // payloadオブジェクトから引数を取り出す
      // URLのパスを取得
      // const urlPath2 = path_
      
      let urlPath;

      if (newpath != null) {
        urlPath = newpath;
        console.log("urlPath", newpath)
      } else {
        urlPath = window.location.pathname;
        console.log("window.location.pathname", window.location.pathname)

      }


      


      
      
      // 事前に定義したパスと表示する文字列の対
      const pathMapping = {
        video: "動画",
        performer: "パフォーマー",
        maker: "メーカー",
        kyounuki: "今日抜き",
        matome: "まとめ",
        article: "雑記"
        
        // ...
      };
      

      
      
      
      // パスを"/"で区切ってリストに変換
      const pathList = urlPath.split("/").filter((path) => path !== "");
      
      // パンくずリストの初期化
      let breadcrumbsList = ""
      breadcrumbsList = [
        {
          title: 'ホーム',
          disabled: false,
          to: '/',
        },
      ];
      console.log("breadcrumbsList", breadcrumbsList)
      
      // パスごとにパンくずリストを作成
      let currentPath = "";
      for (let i = 0; i < pathList.length; i++) {

        const path = pathList[i];
        currentPath += `/${path}`;
        let name = pathMapping[path] || path;
        const disabled = i === (pathList.length - 1); // 最後の要素の場合のみ disabled: true
        // if (4 > i && i > 1 && pathList[0] == "article") {
        //   continue
        // }
        console.log("pathList", pathList)

        let judge_hide_breadcolumbs = false
        if (pathList[0]=="article") {
          judge_hide_breadcolumbs = !judge_hide_breadcolumbs
          if (i == 0) { judge_hide_breadcolumbs = false }
          if (i == 1) { if (pathList.length == 2 && pathList[1]=="list" ) { judge_hide_breadcolumbs = false } }
          if (i == 2) {  }
          if (i == 3) {  }
          if (i == 4) { 
            if (pathList.length == 5) {
              let ARTICLE_DETAIL;
              let ARTICLE_DETAIL_TITLE;
              let ARTICLE_CLASS;
      
              ARTICLE_CLASS = newpath.split("/").slice(2, 6)
      
              for (let sleep_count = 0; sleep_count < 100; sleep_count++) {
                await sleep(1000);
                if (this.state.article_list !== null) {
                  break;
                }
                // 1秒間の一時停止
              }
              
              ARTICLE_DETAIL = this.state.article_list.filter(item => 
              item.classmajor === ARTICLE_CLASS[0] && 
              item.classmedium === ARTICLE_CLASS[1] && 
              item.classminor === ARTICLE_CLASS[2] &&
              item.title_number === parseInt(ARTICLE_CLASS[3])
              );
              ARTICLE_DETAIL_TITLE = ARTICLE_DETAIL[0].title;
              name = ARTICLE_DETAIL_TITLE
              judge_hide_breadcolumbs = false
            }
          }
        }


        if (judge_hide_breadcolumbs == true) { continue }
        breadcrumbsList.push({ title: name, disabled, to: currentPath });
      }
      console.log("breadcrumbsList", breadcrumbsList)
      

      // if (newpath.split("/")[1] == "article" && newpath.split("/").length == 6) {

      //   let ARTICLE_DETAIL;
      //   let ARTICLE_DETAIL_TITLE;
      //   let ARTICLE_CLASS;

      //   ARTICLE_CLASS = newpath.split("/").slice(2, 6)

      //   for (let sleep_count = 0; sleep_count < 100; sleep_count++) {
      //     await sleep(1000);
      //     if (this.state.article_list !== null) {
      //       break;
      //     }
      //     // 1秒間の一時停止
      //   }
        
      //   ARTICLE_DETAIL = this.state.article_list.filter(item => 
      //   item.classmajor === ARTICLE_CLASS[0] && 
      //   item.classmedium === ARTICLE_CLASS[1] && 
      //   item.classminor === ARTICLE_CLASS[2] &&
      //   item.title_number === parseInt(ARTICLE_CLASS[3])
      //   );
      //   ARTICLE_DETAIL_TITLE = ARTICLE_DETAIL[0].title;
      //   // breadcrumbsList[1].title = ARTICLE_DETAIL_TITLE

      // }


      
      // let title =''
      // console.log("pathList.value[1]", pathList.value[1], pathList.value[2], pathList.value[3])


      // if (pathList.includes("article") && !pathList.includes("list")) {  
      //   title = this.article_list.filter(item => 
      //   item.classmajor === pathList.value[1] && 
      //   item.classmedium === pathList.value[2] && 
      //   item.classminor === pathList.value[3] &&
      //   item.title_number === parseInt(pathList.value[4])
      //   );
      // }
      
      // if (title !== '') {
      //   breadcrumbsList[breadcrumbsList.length - 1].title = title;
      // }
      console.log("SET_BREADCRUMBS>breadcrumbsList", breadcrumbsList)
      commit('SET_BREADCRUMBS', breadcrumbsList);
    },
    async FETCH_GET_CONTENTS_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'contents_list', mutationType: 'SET_CONTENTS_LIST' });
    },

    async FETCH_GET_URL_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'url_list_view', mutationType: 'SET_URL_LIST' });
    },


    async FETCH_GET_SUBCONTENTS({ commit }, subcontents) {
      commit('SET_SUBCONTENTS', subcontents);
    },

    async FETCH_GET_VIDEO_DETAIL({ commit }, to) {
      commit('SET_VIDEO_DETAIL', null);

      if (this.state.videos === null) {
        await store.dispatch('FETCH_GET_VIDEOS');
        while(this.state.videos === null) {
          await sleep(50);
        }
      }

      // ビデオリストが取得されているかどうかを確認
        const lastpath = to.path.split("/").pop();
        try {
          const VIDEO_DETAIL = this.state.videos.filter(video => video.video_productnumber === lastpath);
          // 抽出したビデオの詳細をストアにコミットする
          commit('SET_VIDEO_DETAIL', VIDEO_DETAIL);
        } catch (error) {
          // エラーが発生した場合の処理
          console.error('An error occurred while filtering video details:', error);
        }
    },
    async FETCH_GET_SUBCONTENTS_ALL({ commit }, to) {
      let subcontents_all_param = to.path.split("/")[1]
      let subcontents_all;

      for (let sleep_count = 0; sleep_count < 100; sleep_count++) {
        await sleep(1000);
        if (
          this.state.video !== null &&
          this.state.performer_list !== null &&
          this.state.tag_list !== null &&
          this.state.maker_list !== null &&
          this.state.label_list !== null &&
          this.state.series_list !== null &&
          this.state.article_list_dup !== null


        ) {
          break;
        }
      }

      if (subcontents_all_param=="video") {  subcontents_all = this.state.videos }
      else if (subcontents_all_param=="performer") { subcontents_all = this.state.performer_list }
      else if (subcontents_all_param=="tag") { subcontents_all = this.state.tag_list }
      else if (subcontents_all_param=="maker") { subcontents_all = this.state.maker_list }
      else if (subcontents_all_param=="label") { subcontents_all = this.state.label_list }
      else if (subcontents_all_param=="series") { subcontents_all = this.state.series_list }
      // else if (subcontents_all_param=="article") { subcontents_all = this.state.article_list }
      else if (subcontents_all_param=="article") { subcontents_all = this.state.article_list_dup }


      let newPathlength = to.path.split("/").length
      let newPathsplit = to.path.split("/")
      let toParams = to.params
      // let newpath = ""

      // console.log("toParams.param", toParams.param1)
      // console.log("toParams.param2", toParams.param2)
      // console.log("toParams.param3", toParams.param3)
      // console.log("toParams.param4", toParams.param4)

      let searchparams = this.state.searchparams;
      let searchparams_article = this.state.searchparams_article;

      // video
      if (subcontents_all_param=="video" && toParams.param == null) {
        let filteredData = this.state.videos; // オリジナルのデータを変更せずにコピーを作成
        for (let key in searchparams) {
          const filterValue = searchparams[key];
          if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
            if (key === "tags" || key === "performers") {
              if (Array.isArray(filterValue) && filterValue.length !== 0) {
                filteredData = filteredData.filter(item => {
                  return item[key].some(item2 => filterValue.includes(item2.name));
                });
              }
            }
          }
        }
        subcontents_all = filteredData
        
      // article
      } else if (subcontents_all_param=="article" && toParams.param == null) {
        let filteredData = this.state.article_list_dup; // オリジナルのデータを変更せずにコピーを作成
        for (let key in searchparams_article) {
          const filterValue = searchparams_article[key];
          if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
            if (true) {
              // if (Array.isArray(filterValue) && filterValue.length !== 0) {
              if (Array.isArray(filterValue) && filterValue.length !== 0) {
                filteredData = filteredData.filter(item => {
                  return filterValue.includes(item[key]);
                });
              }
              
            }
          }
        }
        subcontents_all = filteredData

      // article > param
      } else if (subcontents_all_param=="article" && toParams.param != null && toParams.param4 == null ) {
        let filteredData = this.state.article_list_dup; // オリジナルのデータを変更せずにコピーを作成
        filteredData = filteredData.filter(item => 
        item.classmajor === toParams.param && 
        (toParams.param2 === undefined || item.classmedium === toParams.param2) &&
        (toParams.param3 === undefined || item.classminor === toParams.param3)

        )
        subcontents_all = filteredData

      // article > param > param4
      } else if (subcontents_all_param=="article" && toParams.param != null && toParams.param4 != null ) {
        let filteredData = this.state.article_list; // オリジナルのデータを変更せずにコピーを作成
        filteredData = filteredData.filter(item => 
        item.classmajor === toParams.param && 
        item.classmedium === toParams.param2 &&
        item.classminor === toParams.param3 &&
        item.title_number === parseInt(toParams.param4)

        )
        commit('SET_ARTICLE_DETAIL', filteredData);

      }








      // filterArticle(ARTICLE_LIST_DUP, searchparamsarticle)



















      // { path: '/', name: 'Home', component: App },
      // { path: '/video',  name: 'Videos',  meta: { subcontents: 'video'}, component: ContantsListDisplayVideo, props: true},
      // { path: '/video/list',  name: 'VideosList',  meta: { subcontents: 'video'}, component: ContantsList, props: true},
      // { path: '/video/:param',  name: 'Video',  meta: { subcontents: 'video'}, component: ContantsDetealVideo, props: true},
      
      // { path: '/kyounuki',  name: 'Kyounuki',  meta: { subcontents: 'kyounuki'}, component: ContantsListKyounuki, props: true},
      // { path: '/performer',  name: 'Performers',  meta: { subcontents: 'performer'}, component: ContantsList, props: true},
      // // { path: '/performer/:param',  name: 'Performer',  meta: { subcontents: 'performer'}, component: About, props: true},
      // { path: '/tag',  name: 'Tags',  meta: { subcontents: 'tag'}, component: ContantsList,  props: true},
      // // { path: '/tag/:param',  name: 'Tag',  meta: { subcontents: 'tag'}, component: About, props: true},
      // { path: '/maker',  name: 'Makers',  meta: { subcontents: 'maker'}, component: ContantsList, props: true},
      // // { path: '/maker/:param',  name: 'Maker',  meta: { subcontents: 'maker'}, component: About, props: true},
      // // { path: '/label',  name: 'Labels',  meta: { subcontents: 'label'}, component: About, props: true},
      // // { path: '/label/:param',  name: 'Label',  meta: { subcontents: 'label'}, component: About, props: true},
      // // { path: '/series',  name: 'Seriess',  meta: { subcontents: 'series'}, component: About, props: true},
      // // { path: '/series/:param',  name: 'Series',  meta: { subcontents: 'series'}, component: About, props: true},
      // { path: '/article',  name: 'Articles',  meta: { subcontents: 'article'}, component: ContantsListDisplayArticle, props: true},
      // { path: '/article/list',  name: 'ArticlesList',  meta: { subcontents: 'article'}, component: ContantsList, props: true},
      // { path: '/article/:param/:param2/:param3/:param4',  name: 'Article',  meta: { subcontents: 'article'}, component: ContantsDetealArticle, props: true},
      // { path: '/article/:param/:param2/:param3',  name: 'ArticleList1',  meta: { subcontents: 'article'}, component: ContantsList, props: true},
      // { path: '/article/:param/:param2',  name: 'ArticleList2',  meta: { subcontents: 'article'}, component: ContantsList, props: true},
      // { path: '/article/:param',  name: 'ArticleList3',  meta: { subcontents: 'article'}, component: ContantsList, props: true},
  




      // commit('SET_SUBCONTENTS_ALL', subcontents_all);
    }
      


  
  
  },  
  
    


  getters: {
    GET_VIDEOS: (state) => state.videos,
    GET_VIDEO_DETAIL: (state) => state.video_detail,
    GET_PERFORMER_LIST: (state) => state.performer_list,
    GET_TAG_LIST: (state) => state.tag_list,

    GET_ARTICLE_DETAIL: (state) => state.article_detail,
    GET_ARTICLE_LIST: (state) => state.article_list,
    GET_ARTICLE_LIST_DUP: (state) => state.article_list_dup,
    GET_ARTICLE_LIST_PARAMS: (state) => state.article_list_params,

    GET_MAKER_LIST: (state) => state.maker_list,
    GET_LABEL_LIST: (state) => state.label_list,
    GET_SERIES_LIST: (state) => state.series_list,
    GET_KYOUNUKI_LIST: (state) => state.kyounuki_list,
    

    GET_SEARCHPARAMS: (state) => state.searchparams,
    GET_SEARCHPARAMS_ARTICLE: (state) => state.searchparams_article,

    GET_VIDEOS_LOADED: (state) => state.set_videos_loaded,


    GET_URL_LIST: (state) => state.url_list,
    GET_URL_PARAM: (state) => state.url_param,
    GET_URL_JUDGE_PARAM: (state) => state.url_judge_param,
    // GET_SUBCONTENTS: (state) => state.subcontents,
    // GET_SUBCONTENTS_ALL: (state) => state.subcontents_all,

    GET_TOPIX_LIST: (state) => state.topix_list,


    GET_DEBUG: (state) => state.debug,
    GET_BREADCRUMBS: (state) => state.breadcrumbs,

    // GET_CONTENTS_LIST: (state) => state.contents_list,


  } 
});


(async () => {
  try {
    // await store.dispatch('fetchUrlListData');
    // await store.dispatch('fetchData');
    await store.dispatch('FETCH_GET_VIDEOS');
    await store.dispatch('FETCH_GET_PERFORMER_LIST');
    await store.dispatch('FETCH_GET_TAG_LIST');
    // await store.dispatch('FETCH_GET_KYOUNUKI_LIST');
    await store.dispatch('FETCH_GET_URL_LIST');
    // await store.dispatch('FETCH_GET_MAKER_LIST');
    await store.dispatch('FETCH_GET_LABEL_LIST');
    // await store.dispatch('FETCH_GET_SERIES_LIST');
    await store.dispatch('FETCH_GET_DEBUG');
    // await store.dispatch('FETCH_GET_BREADCRUMBS', { path_: "success!" })
    await store.dispatch('FETCH_GET_BREADCRUMBS')
    // await store.dispatch('FETCH_GET_CONTENTS_LIST');
    await store.dispatch('FETCH_GET_ARTICLE_LIST');
    // await store.dispatch('FETCH_GET_ARTICLE_LIST_DUP');
    // await store.dispatch('FETCH_GET_ARTICLE_LIST_PARAMS');

    // await store.dispatch('FETCH_GET_VIDEO_DETAIL');

    
    // await store.dispatch('FETCH_GET_URL_LIST');

    console.log('Data fetched successfully');
    
  } catch (error) {
    console.log('Error fetching data:', error);
  }
})();

export default store;
