<template>
  <header class="section">
    <div class="content">
      <div class="title">
        <div>Od idei do pierwszej linijki kodu.</div>
        <div class="lestdothat">
          <span class="highlight">Wygeneruj pomysł</span> na projekt w kilka
          sekund!
        </div>
      </div>
      <p class="subtitle">
        Opisz swoje zainteresowania i technologie, a nasza sztuczna inteligencja
        zaproponuje unikalne projekty programistyczne dopasowane do Ciebie.
      </p>
      <button class="cta-button primary">🚀 Generuj Pomysły!</button>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
/* --- Sekcja Hero --- */
.section {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 4rem 0;
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
  margin-bottom: 1.5rem;
}

.lestdothat {
  font-size: 3rem;
}

.title .highlight {
  color: $gold;
}

.subtitle {
  font-size: 1.25rem;
  max-width: 700px;
  margin: 0 auto 2.5rem;
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
</style>
