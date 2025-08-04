<template>
  <nav>
    <div class="logo">
      <img src="@/assets/logo_violet.svg" />
      <div>Thinkline</div>
      <div class="ai">AI</div>
    </div>
    <div class="actions">
      <div>
        <router-link to="/">{{ $t('navbar.generate') }}</router-link>
      </div>
      <div>
        <router-link to="/about">{{ $t('navbar.projects') }}</router-link>
      </div>
      <LanguageSelector />
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import LanguageSelector from '@/components/Shared/LanguageSelector.vue'

export default defineComponent({
  components: {
    LanguageSelector,
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
  padding: 10px;
  justify-content: space-evenly;

  user-select: none;
}

.logo {
  display: flex;
  align-items: center;

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

.actions {
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 18px;

  a {
    text-decoration: none;
    color: $light;
    transition: color 0.15s;

    &:hover {
      color: $violet;
    }
  }
}
</style>
