<template>
  <section class="how-it-works">
    <div class="title">Jak to działa? To proste.</div>
    <div class="container">
      <div class="step">
        <div class="step-icon"><ic icon="feather-pointed" /></div>
        <h3>Krok 1: Opisz Koncepcję</h3>
        <p>Wpisz swoje pasje, preferowany język lub poziom trudności.</p>
      </div>
      <div class="step">
        <div class="step-icon"><ic icon="code-branch" /></div>
        <h3>Krok 2: AI Analizuje</h3>
        <p>
          Nasze algorytmy przetwarzają Twoje dane, by znaleźć idealny projekt.
        </p>
      </div>
      <div class="step">
        <div class="step-icon"><ic icon="lightbulb" /></div>
        <h3>Krok 3: Odbierz Pomysły</h3>
        <p>Otrzymaj listę kreatywnych i spersonalizowanych pomysłów.</p>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
.title {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 2rem;
}

.how-it-works {
  padding: 2rem 0;
}

.container {
  display: flex;
  justify-content: space-around;
  gap: 2rem;
  flex-wrap: wrap;
}

.step {
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  flex-basis: 300px;
  border: 1px solid $dark;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  flex-grow: 1;
}

.step:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.step-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.step h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.step p {
  color: var(--secondary-text);
}
</style>
