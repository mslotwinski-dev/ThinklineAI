<template>
  <nav>
    <div class="logo" @click="$router.push('/')">
      <img src="@/assets/logo_violet.svg" />
      <div>Thinkline</div>
      <div class="ai">AI</div>
    </div>

    <div class="desktop-actions">
      <router-link to="/generate">{{ $t('navbar.generate') }}</router-link>
      <router-link to="/projects">{{ $t('navbar.projects') }}</router-link>
      <LanguageSelector />
    </div>

    <!-- Hamburger menu for mobile -->
    <div
      class="mobile-menu-icon"
      :class="{ open: menuOpen }"
      @click="toggleMenu"
    >
      <span></span>
      <span></span>
      <span></span>
    </div>

    <div class="mobile-actions" :class="{ open: menuOpen }">
      <router-link to="/generate" @click="toggleMenu">{{
        $t('navbar.generate')
      }}</router-link>
      <router-link to="/projects" @click="toggleMenu">{{
        $t('navbar.projects')
      }}</router-link>
      <LanguageSelectorMobile />
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import LanguageSelector from './LanguageSelector.vue'
import LanguageSelectorMobile from './LanguageSelectorMobile.vue'

export default defineComponent({
  components: {
    LanguageSelector,
    LanguageSelectorMobile,
  },
  setup() {
    const menuOpen = ref(false)
    const toggleMenu = () => {
      menuOpen.value = !menuOpen.value
    }
    return { menuOpen, toggleMenu }
  },
})
</script>

<style lang="scss" scoped>
nav {
  color: $light;
  background-color: #232b2f;
  border-radius: 10px;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  padding: 10px 20px;
  position: relative;
  user-select: none;
}

.logo {
  display: flex;
  align-items: center;
  cursor: pointer;

  img {
    width: 50px;
    height: 50px;
    margin-right: 10px;
  }
}

.ai {
  color: $violet;
  font-weight: 700;
  margin-left: 5px;
  font-size: 24px;
}

.desktop-actions {
  display: flex;
  align-items: center;
  gap: 20px;

  a {
    text-decoration: none;
    color: $light;
    transition: color 0.15s;

    &:hover {
      color: $violet;
    }
  }

  @media (max-width: 768px) {
    display: none;
  }
}

.mobile-menu-icon {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 25px;
  height: 20px;
  cursor: pointer;
  z-index: 1100;

  span {
    display: block;
    height: 3px;
    background-color: $light;
    border-radius: 2px;
    transition: all 0.3s ease;
  }

  &.open span:nth-child(1) {
    transform: rotate(45deg) translateY(12px);
  }
  &.open span:nth-child(2) {
    opacity: 0;
  }
  &.open span:nth-child(3) {
    transform: rotate(-45deg) translateY(-12px);
  }

  @media (max-width: 768px) {
    display: flex;
  }
}

.mobile-actions {
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  width: 100%;
  background-color: #232b2f;
  padding-top: 100px;
  align-items: center;
  gap: 30px;
  transition: transform 0.3s ease, opacity 0.3s ease;
  transform: translateX(100%);
  opacity: 0;
  z-index: 1000;

  &.open {
    transform: translateX(0);
    opacity: 1;
  }

  a {
    text-decoration: none;
    color: $light;
    font-size: 22px;
    font-weight: 500;
    transition: color 0.2s;

    &:hover {
      color: $violet;
    }
  }
}
</style>
