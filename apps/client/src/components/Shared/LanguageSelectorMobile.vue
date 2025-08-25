<template>
  <div class="wrapper" :class="{ open: dropdownOpen }" @click="toggleDropdown">
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
        :key="lang"
        class="option"
        @click.stop="selectLanguage(lang)"
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
      dropdownOpen: false,
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
      this.toggleDropdown()
    },
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen
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
  width: 200px !important;
  font-size: 14px;

  .display {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 10px;
    border: 1px solid $dark_gray;
    cursor: pointer;
    border-radius: 5px;
    user-select: none;
    transition: border-color 0.2s ease;

    .dropdown-icon {
      font-size: 12px;
      transition: transform 0.3s;
    }
  }

  .lang {
    display: flex;
    align-items: center;

    span {
      width: 30px;
      text-align: center;
    }

    img {
      width: 28px;
      height: 18px;
      margin-left: 6px;
      border-radius: 3px;
    }
  }

  .options {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: $dark;
    border-radius: 0 0 5px 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    overflow: hidden;
    max-height: 0;
    opacity: 0;
    transition: all 0.3s ease-in-out;
    z-index: 10;

    .option {
      padding: 8px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: background-color 0.2s;

      &:hover {
        background-color: $dark_gray;
      }

      img {
        width: 28px;
        height: 18px;
        border-radius: 3px;
        margin-left: 6px;
      }
    }
  }

  &.open {
    .dropdown-icon {
      transform: rotate(180deg);
    }

    .options {
      max-height: 500px; // wystarczająco duży żeby pomieścić wszystkie opcje
      opacity: 1;
    }
  }

  @media (max-width: 768px) {
    width: 100%;
    .display {
      font-size: 12px;
      padding: 6px 8px;
    }
    .options .option {
      font-size: 13px;
      padding: 8px 10px;
    }
  }
}
</style>
