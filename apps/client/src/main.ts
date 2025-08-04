import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'

import App from './App.vue'

import VueSmoothScroll from 'vue3-smooth-scroll'
import scrollsettings from './config/scroll'
import FontAwesomeIcon from './config/icons'

import router from './router'
const pinia = createPinia()

const savedLocale = localStorage.getItem('locale') || 'pl'

import en from './locales/en.json'
import pl from './locales/pl.json'

const i18n = createI18n({
  locale: savedLocale,
  fallbackLocale: 'en',
  messages: { en, pl },
})

import './config/registerServiceWorker'

createApp(App)
  .component('ic', FontAwesomeIcon)
  .use(VueSmoothScroll, scrollsettings)
  .use(i18n)
  .use(pinia)
  .use(router)
  .mount('#app')
