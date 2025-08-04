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

import cn from './locales/cn.json'
import de from './locales/de.json'
import en from './locales/en.json'
import es from './locales/es.json'
import fr from './locales/fr.json'
import it from './locales/it.json'
import jp from './locales/jp.json'
import pl from './locales/pl.json'
import ru from './locales/ru.json'

const i18n = createI18n({
  locale: savedLocale,
  fallbackLocale: 'en',
  messages: { cn, de, en, es, fr, it, jp, pl, ru },
})

import './config/registerServiceWorker'

createApp(App)
  .component('ic', FontAwesomeIcon)
  .use(VueSmoothScroll, scrollsettings)
  .use(i18n)
  .use(pinia)
  .use(router)
  .mount('#app')
