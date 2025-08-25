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

  display: flex;
  flex-direction: column;
  gap: 6rem;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 2rem;
}

.final-cta {
  text-align: center;
  padding: 4rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.cta-button.secondary {
  padding: 1rem 2.5rem;
  border-radius: 10000px;
  background-color: $dark;
  color: $light;
  border: 1px solid $violet;
  font-weight: 500;
  font-size: 1rem;
  transition: 0.3s all;
  cursor: pointer;

  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(98, 71, 122, 0.27);
    color: white;
  }
}

/* --- Media Queries dla responsywności --- */
@media (max-width: 1200px) {
  .section-title {
    font-size: 2.25rem;
  }

  .cta-button.secondary {
    padding: 0.9rem 2rem;
    font-size: 0.95rem;
  }
}

@media (max-width: 768px) {
  .home {
    padding: 0 1rem;
    gap: 4rem;
  }

  .section-title {
    font-size: 2rem;
    margin-bottom: 1.5rem;
  }

  .final-cta {
    padding: 3rem 0;
  }

  .cta-button.secondary {
    padding: 0.8rem 1.8rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 1.75rem;
  }

  .cta-button.secondary {
    padding: 0.7rem 1.5rem;
    font-size: 0.85rem;
  }
}
</style>
