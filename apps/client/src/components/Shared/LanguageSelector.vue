<template>
  <div class="wrapper">
    <div class="display">
      <div class="lang">
        <span v-html="selectedLanguage.toUpperCase()" />
        <img :src="getLanguageIcon(selectedLanguage)" />
      </div>
      <span class="dropdown-icon">▼</span>
    </div>
    <div class="options">
      <div
        v-for="lang in languages"
        :key="lang.value"
        class="option"
        @click="selectLanguage(lang)"
      >
        {{ lang.toUpperCase() }}
        <img :src="getLanguageIcon(lang)" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

const LOCALE_STORAGE_KEY = 'locale'

export default defineComponent({
  data() {
    return {
      languages: [
        'en',
        'es',
        'fr',
        'pl',
        'de',
        'it',
        'ru',
        'jp',
        'cn',
        // 'in',
        // 'no',
        // 'nl',
      ],
      selectedLanguage: 'en',
    }
  },

  methods: {
    getLanguageIcon(lang: string): string {
      // Free Russia
      if (lang === 'ru') {
        return 'https://upload.wikimedia.org/wikipedia/commons/6/6f/White-blue-white_flag.svg'
      }

      // Variations
      if (lang === 'en') lang = 'us'

      return `https://flagcdn.com/w40/${lang}.png`
    },
    selectLanguage(lang: string) {
      this.selectedLanguage = lang
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      ;(this as any).$i18n.locale = lang
      localStorage.setItem(LOCALE_STORAGE_KEY, lang)
    },
  },

  mounted() {
    const savedLocale = localStorage.getItem(LOCALE_STORAGE_KEY)
    const initialLang = savedLocale || 'en'
    this.selectLanguage(initialLang)
  },
})
</script>

<style lang="scss" scoped>
.wrapper {
  position: relative;
  width: 100px;
}

.display {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 10px;
  border: 1px solid $dark_gray;
  cursor: pointer;
  border-radius: 5px;
  user-select: none;

  .dropdown-icon {
    font-size: 10px;
    transition: transform 0.3s;
  }
}

.wrapper:hover .options {
  height: 103px;
  border: 1px solid $dark;
}

.lang {
  display: flex;
  align-items: center;

  span {
    width: 25px;
  }
}

.options {
  display: flex;
  height: 0px;
  overflow: hidden;
  position: absolute;
  flex-wrap: wrap;
  top: 100%;
  left: 0;
  width: 305px;
  background-color: $dark;
  border-top: none;
  border-radius: 0 0 5px 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  z-index: 10;
  transition: all 0.2s ease-in-out;
}

.option {
  width: 100px;
  padding: 6px 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: 0.35s all;
  flex-grow: 1;

  &:hover {
    background-color: $dark_gray;
  }
}

img {
  width: 28px;
  height: 18px;
  margin-left: 10px;
  border-radius: 3px;
}
</style>
