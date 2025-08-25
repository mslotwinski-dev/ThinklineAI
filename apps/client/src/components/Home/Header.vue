<template>
  <header class="section">
    <div class="content">
      <div class="title">
        <div>
          {{ $t('home.header.title') }}
        </div>
        <div class="lestdothat">
          <span class="highlight">{{ $t('home.header.highlight') }}</span>
          {{ $t('home.header.letsdothat') }}
        </div>
      </div>
      <p class="subtitle">
        {{ $t('home.header.subtitle') }}
      </p>
      <button class="cta-button primary">
        🚀 {{ $t('home.header.button') }}
      </button>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
.section {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 4rem 2rem;
  margin: 2rem 0;

  background-image: url('@/assets/hero.png');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
}

.title {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.lestdothat {
  font-size: 3rem;
  line-height: 1.1;
  display: block;
}

.title .highlight {
  color: $gold;
}

.subtitle {
  font-size: 1.25rem;
  max-width: 700px;
  margin: 1rem auto 2rem;
  line-height: 1.5;
  color: $light;
}

.cta-button {
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 50px;
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cta-button.primary {
  background-color: $dark;
  color: white;
}

.cta-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px #62477a44;
}

/* --- Media Queries dla responsywności --- */
@media (max-width: 1200px) {
  .title {
    font-size: 2.25rem;
  }
  .lestdothat {
    font-size: 2.5rem;
  }
  .subtitle {
    font-size: 1.1rem;
  }
}

@media (max-width: 768px) {
  .section {
    padding: 3rem 0.5rem;
    min-height: 50vh;
  }
  .title {
    font-size: 2rem;
  }
  .lestdothat {
    font-size: 2.2rem;
  }
  .subtitle {
    font-size: 1rem;
  }
  .cta-button {
    padding: 0.9rem 2rem;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .title {
    font-size: 1.75rem;
  }
  .lestdothat {
    font-size: 1.9rem;
  }
  .subtitle {
    font-size: 0.95rem;
    max-width: 100%;
  }
  .cta-button {
    padding: 0.8rem 1.5rem;
    font-size: 0.95rem;
  }
}
</style>
