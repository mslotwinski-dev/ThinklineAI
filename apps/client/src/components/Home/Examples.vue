<template>
  <section class="example">
    <div class="title">Zobacz, co możesz stworzyć</div>
    <div class="grid">
      <div class="card">
        <h4>Aplikacja do śledzenia książek</h4>
        <p>
          Aplikacja webowa zintegrowana z API do monitorowania postępów w
          czytaniu.
        </p>
        <div class="tags">
          <span class="tag">JavaScript</span>
          <span class="tag">React</span>
          <span class="tag">NodeJS</span>
          <span class="tag beginner">Początkujący</span>
        </div>
      </div>
      <div class="card">
        <h4>Prognozowanie cen akcji</h4>
        <p>
          Model uczenia maszynowego przewidujący ceny akcji na podstawie analizy
          sentymentu z newsów.
        </p>
        <div class="tags">
          <span class="tag">Python</span>
          <span class="tag">TensorFlow</span>
          <span class="tag advanced">Zaawansowany</span>
        </div>
      </div>
      <div class="card">
        <h4>Platforma dla roślin</h4>
        <p>
          Lokalna platforma społecznościowa, gdzie użytkownicy mogą wymieniać
          się wiedzą o domowych roślinach.
        </p>
        <div class="tags">
          <span class="tag">Vue.js</span>
          <span class="tag">Node.js</span>
          <span class="tag">MongoDB</span>
          <span class="tag intermediate">Średniozaaw.</span>
        </div>
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

.example {
  padding: 3rem 0;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.card {
  padding: 1rem 2rem;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}

.card h4 {
  font-size: 1.4rem;
  margin-bottom: 0.75rem;
}

.card p {
  flex-grow: 1;
  margin-bottom: 1.5rem;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background-color: #444;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.tag.beginner {
  background-color: #27ae60;
}
.tag.intermediate {
  background-color: #f39c12;
}
.tag.advanced {
  background-color: #c0392b;
}
</style>
