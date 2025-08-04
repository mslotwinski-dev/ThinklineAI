<template>
  <section class="example">
    <div class="title">
      {{ $t('home.examples.title') }}
    </div>
    <div class="grid">
      <div class="card">
        <h4>
          {{ $t('home.examples.card.head.A') }}
        </h4>
        <p>
          {{ $t('home.examples.card.p.A') }}
        </p>
        <div class="tags">
          <span class="tag">JavaScript</span>
          <span class="tag">React</span>
          <span class="tag">NodeJS</span>
          <span class="tag beginner">{{ $t('levels.beginner') }}</span>
        </div>
      </div>
      <div class="card">
        <h4>{{ $t('home.examples.card.head.B') }}</h4>
        <p>
          {{ $t('home.examples.card.p.B') }}
        </p>
        <div class="tags">
          <span class="tag">Python</span>
          <span class="tag">TensorFlow</span>
          <span class="tag advanced">
            {{ $t('levels.advanced') }}
          </span>
        </div>
      </div>
      <div class="card">
        <h4>{{ $t('home.examples.card.head.C') }}</h4>
        <p>
          {{ $t('home.examples.card.p.C') }}
        </p>
        <div class="tags">
          <span class="tag">Vue.js</span>
          <span class="tag">Node.js</span>
          <span class="tag">MongoDB</span>
          <span class="tag intermediate">
            {{ $t('levels.intermediate') }}
          </span>
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
