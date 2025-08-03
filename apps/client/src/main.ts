import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import VueSmoothScroll from 'vue3-smooth-scroll'
import scrollsettings from './config/scroll'
import FontAwesomeIcon from './config/icons'

import router from './router'
const pinia = createPinia()

import './registerServiceWorker'

createApp(App)
  .component('ic', FontAwesomeIcon)
  .use(VueSmoothScroll, scrollsettings)
  .use(pinia)
  .use(router)
  .mount('#app')
