<template>
  <div class="home">
    <Header />
    <HowWorks />
    <Examples />

    <section class="final-cta">
      <h2 class="section-title">
        {{ $t('home.final.title') }}
      </h2>
      <button class="cta-button secondary">
        🚀 {{ $t('home.final.button') }}
      </button>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Header from '@/components/Home/Header.vue'
import HowWorks from '@/components/Home/HowWorks.vue'
import Examples from '@/components/Home/Examples.vue'

export default defineComponent({
  components: {
    Header,
    HowWorks,
    Examples,
  },
})
</script>

<style lang="scss" scoped>
.home {
  font-family: 'Inter', sans-serif;
  padding: 0 2rem;
  max-width: 1550px;
  margin: auto;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
}

.final-cta {
  text-align: center;
  padding-bottom: 6rem;
}

.cta-button.secondary {
  padding: 1rem 2.5rem;
  border-radius: 10000px;
  background-color: transparent;
  color: $light;
  background: $dark;
  border: 1px solid $violet;
  font-weight: 500;
  font-size: 1rem;
  transition: 0.2s all;
}

.cta-button.secondary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px #62477a44;
  color: white;
}

/* --- Media Queries dla responsywności --- */
@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .home-container {
    padding: 0 1rem;
  }

  .final-cta {
    margin: 3rem -1rem 0;
  }
}
</style>
