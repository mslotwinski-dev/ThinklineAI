<template>
  <div class="wrapper">
    <div class="display">
      <div class="lang">
        <span v-html="selectedLanguage.label.toUpperCase()" />
        <img :src="`https://flagcdn.com/w40/${selectedLanguage.icon}.png`" />
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
        {{ lang.label.toUpperCase() }}
        <img :src="`https://flagcdn.com/w40/${lang.icon}.png`" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      selectedLanguage: { label: 'en', icon: 'us' },
      languages: [
        { label: 'en', icon: 'us' },
        { label: 'pl', icon: 'pl' },
        { label: 'es', icon: 'es' },
        { label: 'de', icon: 'de' },
      ],
    }
  },
  methods: {
    selectLanguage(lang: { label: string; icon: string }) {
      this.selectedLanguage = lang
      // console.log(`Selected language: ${lang.icon}`)
    },
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
  display: block;
}

.lang {
  display: flex;
  align-items: center;

  span {
    width: 25px;
  }
}

.options {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: $dark;
  border: 1px solid $dark;
  border-top: none;
  border-radius: 0 0 5px 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.option {
  padding: 6px 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: 0.35s all;

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
