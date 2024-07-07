import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'

import router from './router'
import store from './store';
import { createMetaManager } from 'vue-meta'
const metaManager = createMetaManager()



// import VueMeta from 'vue-meta'


// Vuetify
import 'vuetify/styles'
import 'vuetify/dist/vuetify.css' // VuetifyのCSSをインポート
import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.min.css'
// import { aliases, mdi } from 'vuetify/iconsets/mdi-svg';
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
const vuetify = createVuetify({
  components,
  directives,
})

// const vuetify = createVuetify({
//     components,
//     directives,
//  });

// const vuetify = createVuetify()



createApp(App)
.use(store)
.use(router)
// .use(createMetaManager())
.use(metaManager)
.use(vuetify)
.mount('#app')